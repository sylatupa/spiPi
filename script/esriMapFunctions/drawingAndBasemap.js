var geom;
var mpGeographic;
var coordinates;
var geometry;


function createToolbar(themap) {
  toolbar = new esri.toolbars.Draw(themap);       
  dojo.connect(toolbar, "onDrawEnd", addToMap);
}

function addToMap(geometry) {
  geographic = esri.geometry.webMercatorToGeographic(geometry);
  switch (geometry.type) {
    case "point":
      var symbol = new esri.symbol.SimpleMarkerSymbol(esri.symbol.SimpleMarkerSymbol.STYLE_SQUARE, 10, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([255, 0, 0]), 1), new dojo.Color([0, 255, 0, 0.25]));
    coordinates = '<Point xmlns="http://www.opengis.net/gml">';
    coordinates += "<pos>";
    coordinates += geographic.y + " " + geographic.x;
    coordinates += "</pos></Point>";
    console.log(geographic);
    coordinates = "Point: " + dojo.toJson(geographic.toJson());
    break;
    case "polyline":
      var symbol = new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_DASH, new dojo.Color([255, 0, 0]), 1);
    coordinates = '<MultiCurve xmlns="http://www.opengis.net/gml">';
    coordinates += "<curveMembers>";
    var paths = geographic.paths[0];
    var startCoord;
    for (k = 0; k < paths.length; k++) {
      if (k ==0 ) {
      }
      else {
	var start = paths[k-1];
	var end = paths[k];
	coordinates += "<LineString><posList>" + start[0] + " " +start[1]  + " " + end[0] + " " +end[1] + "</posList></LineString>";
      }
    }
    coordinates += "</curveMembers></MultiCurve>";
    coordinates = "MultiCurve: " + dojo.toJson(geographic.toJson());
    break;
    case "polygon":
      var symbol = new esri.symbol.SimpleFillSymbol(esri.symbol.SimpleFillSymbol.STYLE_SOLID, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_DASHDOT, new dojo.Color([255, 0, 0]), 2), new dojo.Color([255, 255, 0, 0.25]));
    coordinates = '<Polygon xmlns="http://www.opengis.net/gml">';
    coordinates += "<exterior><LinearRing><posList>";
    dojo.forEach(geographic.rings[0], function (PolyPointResult, index) {
	coordinates += PolyPointResult[0] + " " + PolyPointResult[1] + " ";
	});
    coordinates += "</posList></LinearRing></exterior></Polygon>";
    coordinates = "Polygon: " + dojo.toJson(geographic.toJson())
      break;
    case "multipoint":
      var symbol = new esri.symbol.SimpleMarkerSymbol(esri.symbol.SimpleMarkerSymbol.STYLE_DIAMOND, 20, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([0, 0, 0]), 1), new dojo.Color([255, 255, 0, 0.5]));
    coordinates = geographic.points;
    coordinates = '<MultiPoint xmlns="http://www.opengis.net/gml">';
    coordinates += "<pointMembers>";
    console.log("points", geographic);
    var points = geographic.points;
    for (k = 0; k < points.length; k++) {
      var point = points[k];
      console.log("points", points);
      coordinates += "<Point><pos>" + point[0] + " " + point[1]  + "</pos></Point>";
    }
    coordinates += "</pointMembers></MultiPoint>";
    coordinates = "MultiPoint: " + dojo.toJson(geographic.toJson());
    break;
  }
  var graphic = new esri.Graphic(geometry, symbol);
  var textBoxGeometry = dojo.byId("textBoxGeometry");
  textBoxGeometry.value = coordinates;
  var textBoxWeebly = dojo.byId("input-574171923733714464")
    var textGoogle = dojo.byId("entry_1043123993")
    if(textBoxWeebly)
    {
      textBoxWeebly.value = coordinates;
    }
  if(textGoogle)
  {
    textGoogle.value = coordinates;
  }
  map.graphics.add(graphic);
  map.showZoomSlider();
  //toolbar.deactivate();
}

var geographic;
var geom;
function addLineToMap(geometry) {
  geometry;
  //var symbol = new esri.symbol.SimpleMarkerSymbol(esri.symbol.SimpleMarkerSymbol.STYLE_SQUARE, 10, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([255, 0, 0]), 1), new dojo.Color([0, 0, 255, .88]));
  var symbol = new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([22, 100, 255]), 5);
  for (i = 0; i < geometry.features.length; i++) {
    var template = new esri.InfoTemplate();
    var line = new esri.geometry.Polyline(geometry.features[i].geometry.paths, geometry);
      graphic = new esri.Graphic(line, symbol);
      template.setTitle(geometry.features[i].attributes["NAME"]);
   //template.setTitle("<b>"+title+" 	</b>");
     template.setContent("Length: " + geometry.features[i].attributes["LENGTH"] );


    graphic.setInfoTemplate(template);
    //  map.graphics.add(geographic);

//    map.graphics.add(new esri.Graphic(line, symbol));
    map.graphics.add(graphic);

    
  }
  map.showZoomSlider();
  //toolbar.deactivate();
}
var graphic
function addPin() {
  var symbol = new esri.symbol.SimpleMarkerSymbol(esri.symbol.SimpleMarkerSymbol.STYLE_SQUARE, 10, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([255, 0, 0]), 1), new dojo.Color([0, 255, 0, 0.25]));
  var point = new esri.geometry.Point(-112.70, 34.15, new esri.SpatialReference({ wkid: 102100 }))
    point = esri.geometry.geographicToWebMercator(point);
  graphic = new esri.Graphic(point, symbol);
  map.graphics.clear()
}
function addData(element) {

  if (document.getElementById(element.id).checked) {
    console.log("Adding Map Layers");
    console.log(element);

    Sound_Scape.forEach(function(entry){
	setPoint(entry);
	}
	);

    living_classroom.forEach(function(entry){
	setPoint2(entry);
	}
	);
    // major_arizona_rivers.features.forEach(function(entry){
    addLineToMap(major_arizona_rivers);
    //	}
    //	);
  } else {
    map.graphics.clear()
  }

}
function setPoint2(entry) {
  var xCoord = entry['y'];
  var yCoord = entry['x'];
  var title = entry['Living Classroom Description'] 
    var description = [
    entry["Living Classroom Water Body"],
    ", ",
    entry["Living classroom State"],
    "<br>",    
    "<a href='"  ,
    entry["GeoHack"],
    "'>",
    entry['Living Classroom Description'] ,
    "</a>",
    "<br>",    
    entry["Demographics"]
      ].join('\n');

  var symbol = new esri.symbol.SimpleMarkerSymbol(esri.symbol.SimpleMarkerSymbol.STYLE_SQUARE, 10, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([255, 0, 0]), 1), new dojo.Color([0, 0, 255, .88]));
  var point = new esri.geometry.Point(xCoord, yCoord, new esri.SpatialReference({ wkid: 102100 }))
    point = esri.geometry.geographicToWebMercator(point);
  graphic = new esri.Graphic(point, symbol);

  var template = new esri.InfoTemplate();
  //  template.setTitle("<b>${name}</b>");
  template.setTitle("<b>"+title+" 	</b>");
  template.setContent(description );
  graphic.setInfoTemplate(template);
  map.graphics.add(graphic);
}

function setPoint(entry) {
  var xCoord = entry.data.y;
  var yCoord = entry.data.x;
  var title = entry.data.Title 
    var description = entry.data.location_name + "</br>" + entry.data.Country;
  description += "<br>Sound Cloud Url: <a href='"+entry.data.url+"'>" + entry.data.Title + "</a>"

    var symbol = new esri.symbol.SimpleMarkerSymbol(esri.symbol.SimpleMarkerSymbol.STYLE_SQUARE, 10, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([255, 0, 0]), 1), new dojo.Color([0, 255, 0, .88]));
  var point = new esri.geometry.Point(xCoord, yCoord, new esri.SpatialReference({ wkid: 102100 }))
    point = esri.geometry.geographicToWebMercator(point);
  graphic = new esri.Graphic(point, symbol);

  var template = new esri.InfoTemplate();
  //  template.setTitle("<b>${name}</b>");
  template.setTitle("<b>"+title+" 	</b>");
  template.setContent(description );
  graphic.setInfoTemplate(template);
  map.graphics.add(graphic);
}

function createBasemapGallery() {
  var basemapGallery = new esri.dijit.BasemapGallery({
showArcGISBasemaps: true,
map: map
}, "basemapGallery");
basemapGallery.startup();
dojo.connect(basemapGallery, "onError", function(msg) {console.log(msg)});
}

