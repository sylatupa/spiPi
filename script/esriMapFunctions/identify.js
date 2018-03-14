var identifyWidget;

function initIdentify() {
	identifyWidget = document.getElementById("identify");
}
var defObj;

function executeIdentifyTask(evt) {
    var computedStyle = getComputedStyle(identifyWidget); //getting the style of the identify widget
    if (computedStyle.display != "none") {		  //if its not visible--do not do the identify task
        identifyWidget.innerHTML = "<table class='myWidgetTable'><tr class='myWidgetTable'><td style='color:blue;'><center>Identify</center></td></tr>"
					+ "<tr class='myWidgetTable'><td class='myWidgetTable'>"
				  	+ "</td></tr></table>";
	//iterate through the array of layers 
	//get the list of visible layers, if there are visible layers then execute identify task.
        for (i = 0; i < layerObjArray.length; i++) {		
            var visibleLayers = layerObjArray[i].layerObj.visibleLayers;
            if (visibleLayers[0] != -1) {
                layerObjArray[i].identifyParams.layerIds = visibleLayers;
                layerObjArray[i].identifyParams.geometry = evt.mapPoint;
                layerObjArray[i].identifyParams.mapExtent = map.extent;
                var deferred = layerObjArray[i].identifyTask.execute(layerObjArray[i].identifyParams);
                deferred.addCallback(function (response) { // response is an array of identify result objects. Let's return an array of features.
			console.log("response length",response.length);
			console.log("visible layers ", visibleLayers);
			console.log("visible layers ", response[0].layerName);
			for (j = 0; j < response.length; j++) {
			var feature = response[0].feature;
                        var template = new esri.InfoTemplate("Attributes", "${*}");
                        feature.setInfoTemplate(template);
                        identifyWidget.innerHTML += "<table class='myWidgetTable'><tr class='myWidgetTable'><td class='myWidgetTable' style='color:blue;'><center>"
                                                        + response[0].layerName
                                                        + "</center></td></tr><tr class='myWidgetTable'><td class='myWidgetTable'>"
                                                        + feature.getContent()
                                                        + "</td></tr></table>";
                   	}  //end of for loop response
                });  //end of deferred.addCallback

            } // end of if statement
	    else {
		// no visible sublayers in this layer.
	    }
            //	map.infoWindow.setContent("HERE HERE");
            //	map.infoWindow.setTitle("Title");
        } // end of for loop on array of objects
    } // end of if statment, checking if the identify widget is visisble.
}
