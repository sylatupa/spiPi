var layerListInLayerWidget;

function initLayerObject() {
	layerListInLayerListWidget = document.getElementById("layer_list");
}

var urlArray = [
];

function layerObjFunc(index, url) {
    this.url = url;
    this.layerObj = new esri.layers.ArcGISDynamicMapServiceLayer(url);
    var layer = this.layerObj;
    this.index = index;
    this.layerInfo = [];
    this.subLayers = [];
    this.identifyTask = new esri.tasks.IdentifyTask(url);
    this.identifyParams = new esri.tasks.IdentifyParameters();
    this.identifyParams.tolerance = 3;
    this.identifyParams.returnGeometry = true;
    this.identifyParams.layerIds = [];
    this.identifyParams.layerOption = esri.tasks.IdentifyParameters.LAYER_OPTION_VISIBLE;
    this.identifyParams.width  = 333;
    this.identifyParams.height =444;
};
function subLayerObjFunc() {
    this.url = [];
    this.defaultVisibility = [];
    this.id = [];
    this.name = [];
    this.RESThandle = [];
    this.fields = [];
};
layerObjFunc.prototype.toString = function() {
    return  "<span style='color:yellow'>" + "Index: " + this.index + "<br />LayerInfo: "+this.layerInfo + "</span><br />";
}
subLayerObjFunc.prototype.toString = function() {
    return  "<span style='color:yellow'>" + "ID: " + this.id + "<br />LayerName: "+this.name + "<br />Fields: " + this.fields+"</span><br />";
}
var layerObjArray = [];
for (k = 0; k < urlArray.length; k++) {
	var urlList = urlArray[k].split("/");
	var listLength = urlList.length;
	var layerId = urlList[listLength-2];
	layerObjArray.push(new layerObjFunc(layerId, urlArray[k]));
}
function setLayObjInfos(map) {
    for (i = 0 ; i < layerObjArray.length; i++) {
	    layerObjArray[i].layerInfo = layerObjArray[i].layerObj.layerInfos;
	    for (j = 0 ; j < layerObjArray[i].layerInfo.length; j++) {
		    layerObjArray[i].subLayers[j] = new subLayerObjFunc();
	    	    layerObjArray[i].subLayers[j].defaultVisibility = false; // usually all true so I dont use: layerObjArray[i].layerInfo[j].defaultVisibility;
		    layerObjArray[i].subLayers[j].id = layerObjArray[i].layerInfo[j].id;
		    layerObjArray[i].subLayers[j].name = layerObjArray[i].layerInfo[j].name;

   	            //layerObjArray[i].identifyParams.layerIds.push(layerObjArray[i].layerInfo[j].id);
//		    response = esri.request({
//			       "url": layerObjArray[i].url + "/" + layerObjArray[i].subLayers[j].id,
//			       "content": {"f": "json" },"callbackParamName": "callback",
//			});
		    //console.log("layer OBJ: ",dojo.toJson(response));
		    //response.then(requestSucceeded, requestFailed);  //original code
//    		    response.then(requestSucceeded, requestFailed);
	    }//done loading subLayer from layerInfo
     } // done loading all layers with subLayers
}


//Go through the array of all the layer and sublayer objects and create a check box for each sublayer object
function buildLayerList() {
    	var visible = [];
    	var items = [];
    	for (i = 0; i < layerObjArray.length; i++) {            
	   	items = []; 
	   	visible = [];

	    	for (j =0; j < layerObjArray[i].subLayers.length ; j++) {           //making the checkbox for each sublayer
	            	if ( layerObjArray[i].subLayers[j].defaultVisibility) {         //checking its defaultVisibility
       		        	visible.push(layerObjArray[i].subLayers[j].id);             //the visible array holds the number id of the sublayer
                    	}
	            	var IdNameCombo = layerObjArray[i].index + "||"                 //IdNameCombo links back to sublayer visibility
                	+  layerObjArray[i].subLayers[j].name 
	                + "||" +  layerObjArray[i].subLayers[j].id;
            	    	items.push(" <table class='myWidgetTable'><tr class='myWidgetTable'><td class='myWidgetTable' style='color:blue;'>"
	                +"<input type='checkbox' class='list_item'"           //make the check box
       		        + ( layerObjArray[i].subLayers[j].defaultVisibility ? "checked=checked" : "")
                	+ "' id='" + IdNameCombo
	       	    	+ "' onclick='updateLayerVisibility(this);' />"
        	    	+ " <label for='" + IdNameCombo + "'>" + layerObjArray[i].subLayers[j].name + "</label><br />"
                	+"</td></tr><tr class='myWidgetTable'><td class='myWidgetTable'></td></tr></table>");
	     	} // End of sublayer for loop
		var newSpan = document.createElement("span");
        	newSpan.id = "layer_list" + layerObjArray[i].index;
		layerListInLayerListWidget.innerHTML += "<h4>" + layerObjArray[i].index + "</h4>";
	    	layerListInLayerListWidget.appendChild(newSpan);
	    	dojo.byId(newSpan).innerHTML += items.join(' ') + "<br />";
		if (visible.length > 0) {
	        	layerObjArray[i].layerObj.setVisibleLayers(visible);
		} //end of if, setting visible layers
		else{
		 	layerObjArray[i].layerObj.setVisibleLayers([-1]);
		} //end of else, setting visible layers
        	map.addLayer(layerObjArray[i].layerObj);
    	} // end of for loop, building layer list of all layer objects in layerObjArray
}

function buildLegendList() {	
	for(i=0;i <layerObjArray.length;i++) {
		layerInfo.push({layer:layerObjArray[i].layerObj, title:layerObjArray[i].subLayers[0].name});        
	}
          legend = new esri.dijit.Legend({map:map,layerInfos:layerInfo},"mapLegend");
          legend.startup();
}
function updateLayerVisibility(control) {
	var layerInfo =[];
	var elementInLayerArray = control.id.split("||");
	for (var k = 0; k < layerObjArray.length; k++) {
		if (layerObjArray[k].index == elementInLayerArray[0]) {
			layer = layerObjArray[k].layerObj;
			layerInfo.push({layer:layerObjArray[k].layerObj, title:layerObjArray[k].name})
			break;
		}
	}
    	visible = [];
    	var inputs = dojo.query("#"+control.parentElement.id+">"), input;
	dojo.forEach(inputs, function (input) {
        	if (input.checked) {
			input = input.id.split("||");
			input = input[2];
            		visible.push(input);
	        } });
	if (visible.length === 0) {
		visible.push(-1);
	}

	layer.setVisibleLayers(visible);
	legend.refresh();	
}

function requestSucceeded(response,io) {
	var fieldInfo, pad, layerInfo;
	var layerName =	response.name;
	var layerID = response.id;
	if ( response.hasOwnProperty("fields") ) { fieldInfo = dojo.map(response.fields, function(f) { return f.name; }); //also f.alias, f.type, f.id
	setFieldInfo(layerName, layerID, fieldInfo);		//Goes and finds the subLayer, by layerName, and sets the field names
        } else {
        console.log("Failed: ", "No field info found. Please double-check the URL.");
        }
}
function requestFailed(error, io) {
    console.log("Failed: ", error);
    dojo.addClass(dojo.byId("debug"), "failure");

    dojo.toJsonIndentStr = "  ";
    dojo.byId("debug").value = dojo.toJson(error, true);
}
function setFieldInfo(layerName, layerID, fieldInfo) {
	var Names = [];
	for (i = 0 ; i < layerObjArray.length; i++) {
	    for (j = 0 ; j < layerObjArray[i].subLayers.length; j++) {
		Names += layerObjArray[i].subLayers[j].name + "  ";
		if (layerName===layerObjArray[i].subLayers[j].name) {
			layerObjArray[i].subLayers[j].fields = fieldInfo;
			//console.log("Index of Layer and subLayer is: ", (i + " " +j));
			break;	
		}
	    }
	}
}
