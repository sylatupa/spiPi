dojo.require("esri.map");
dojo.require("dijit.Menu");
//dojo.require("dijit.layout.BorderContainer");
//dojo.require("dijit.layout.ContentPane");
//dojo.require("dijit.TitlePane"); //basemap widget
dojo.require("dijit.dijit"); // optimize: load dijit layer  from basemap widget
/*dojo.require("dijit.layout.BorderContainer");
  dojo.require("esri.toolbars.draw");
  dojo.require("dijit.layout.ContentPane");
  dojo.require("dijit.TitlePane");	//basemap widget
  */
//dojo.require("esri.dijit.Legend");
dojo.require("esri/InfoTemplate");
dojo.require("esri.dijit.BasemapGallery"); //basemap widget
dojo.require("esri.dijit.Popup"); //identify function
dojo.require("esri.dijit.InfoWindow");
dojo.require("esri.dijit.Scalebar");
dojo.require("esri.tasks.locator");
dojo.require("esri.arcgis.utils");  // module that does REST requests

var scalebar;
var locator;
var map, routeTask, routeParams;
var stopSymbol, routeSymbol, lastStop;
var map;
var identifyParams, idResult;
var legend, layerInfo = [];                 //used for legend
var mouseXY;
var mouseText;
var mouseX, mouseY;
//var font = new esri.symbol.Font("12pt", esri.symbol.Font.WEIGHT_BOLD, "Courier");

/* ************************:::INIT:::***************************** */
//function init(x, y, z, view) {

function init() {
  //    initIdentify();
  //    initLayerObject();
  //
  //    
  //Create geocoder  
  locator = new esri.tasks.Locator("http://tasks.arcgis.com/ArcGIS/rest/services/WorldLocator/GeocodeServer");
  routeTask = new esri.tasks.RouteTask("http://tasks.arcgisonline.com/ArcGIS/rest/services/NetworkAnalysis/ESRI_Route_NA/NAServer/Route");
  var initExtent = new esri.geometry.Extent({ "xmin": -12862164.02, "ymin": 3638477.99, "xmax": -12059880.97, "ymax": 4416301.19, "spatialReference": { "wkid": 102100} });
  var popup = new esri.dijit.InfoWindow({ fillSymbol: new esri.symbol.SimpleFillSymbol(esri.symbol.SimpleFillSymbol.STYLE_SOLID, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([255, 0, 0]), 2), new dojo.Color([255, 255, 0, 0.25])) }, dojo.create("div"));
  map = new esri.Map("myMap", { extent: initExtent, wrapAround180: true });
  var basemap = new esri.layers.ArcGISTiledMapServiceLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer");

  map.addLayer(basemap);
  dojo.connect(map, 'onLoad', function (map) {
      dojo.connect(dijit.byId("myMap"), 'resize', map, map.resize);
      scalebar = new esri.dijit.Scalebar({ map: map, attachTo: "top-right" });
      dojo.connect(map, "onMouseDown", MouseHandler);
      dojo.connect(map, "onMouseMove", HoverHandler);
      dojo.connect(map, "onMouseDrag", MouseHandler);
      //dojo.connect(map, "onClick", executeIdentifyTask);
      //setLayObjInfos();
      //setTimeout("buildLayerList();", 1500);
      setTimeout("initAddressLocater();", 3500);
      createToolbar(map);
      createBasemapGallery();
      //addPin();
      //        addData();
      //

      //latitude and longitude set in app.js
      locationTimeout = setTimeout( function(){
	if(longitude!=null) { 
	zoomTo(longitude -.1, latitude -.3, longitude +.1, latitude +.3);
	}
	else{ console.log("do no zooming");}
	} , 5000 );
      if (typeof(coordinate) != 'undefined') {            // If coordinate is not defined--then the user is looking for a specific feature to zoom to.
//	setCoordinate();
      }
  });
};

