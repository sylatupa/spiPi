//Perform the geocode. This function runs when the "Locate" button is pushed.  
function locate() {
  var address = {
    'SingleLine': dojo.byId("address").value
  };
  var options = {
address:address,
	outFields:["*"]
  };
  //optionally return the out fields if you need to calculate the extent of the geocoded point
  locator.addressToLocations(options);
}
function initAddressLocater() {
  //Draw and zoom to the result when the geocoding is complete                
  dojo.connect(locator, "onAddressToLocationsComplete", function(geocodeResults) {
      map.graphics.clear();
      dojo.forEach(geocodeResults, function(geocodeResult, index) {
	//create a random color for the text and marker symbol
	var r = Math.floor(Math.random() * 250);
	var g = Math.floor(Math.random() * 100);
	var b = Math.floor(Math.random() * 100);

	var symbol = new esri.symbol.SimpleMarkerSymbol(esri.symbol.SimpleMarkerSymbol.STYLE_CIRCLE, 20, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([r, g, b, 0.5]), 10), new dojo.Color([r, g, b, 0.9]));
	var pointMeters = esri.geometry.geographicToWebMercator(geocodeResult.location);
	var locationGraphic = new esri.Graphic(pointMeters, symbol);

	var font = new esri.symbol.Font().setSize("12pt").setWeight(esri.symbol.Font.WEIGHT_BOLD);
	var textSymbol = new esri.symbol.TextSymbol((index + 1) + ".) " + geocodeResult.address, font, new dojo.Color([r, g, b, 0.8])).setOffset(5, 15);
	//add the location graphic and text with the address to the map
	map.graphics.add(locationGraphic);
	map.graphics.add(new esri.Graphic(pointMeters, textSymbol));
	});
      var ptAttr = geocodeResults[0].attributes;

      zoomTo (ptAttr.West_Lon, ptAttr.South_Lat, ptAttr.East_Lon, ptAttr.North_Lat);

      showResults(geocodeResults);

  });
}

function zoomTo(West_Lon, South_Lat, East_Lon, North_Lat) {
  console.log('west_lon: ' +West_Lon + ', south_lat: ' + South_Lat + ', East_Lon: ' + East_Lon + ', North_Lat: ' + North_Lat);
  var esriExtent = new esri.geometry.Extent(West_Lon, South_Lat, East_Lon, North_Lat, new esri.SpatialReference({wkid: 4326}));
   map.setExtent(esri.geometry.geographicToWebMercator(esriExtent));
}
function showResults(results) {
  var rdiv = dojo.byId("resultsdiv");
  var centerPanel = dojo.byId("centerPanel");
  centerPanel.style.height = '865px';
  rdiv.style.display = 'block'
    rdiv.innerHTML = "<p><b>Results : " + results.length + "</b></p>";

  var content = [];
  dojo.forEach(results, function(result, index) {            
     console.log(result); 
      content.push("<fieldset>");
      content.push("<legend>&nbsp;<b>" + (index + 1) + ". " + result.address +"</b>");
      content.push("&nbsp;&nbsp;|&nbsp;&nbsp; <input style='float:right' type='button' value='Center At Address' onclick='zoomTo("+result.attributes.West_Lon +","+ result.attributes.South_Lat +","+ result.attributes.East_Lon + ","+ result.attributes.North_Lat +")'/>");      
      content.push("</b></legend>");
      content.push("<b><i>Score: </i></b> " + result.score + "<b><i> | Method: </i></b>" + result.attributes.MatchLevel + " | ");
     // content.push("<br/>");	  
      content.push("<b><i>Longitude (x)</i></b> : " + result.location.x  + " | <b><i>Latitude (y)</i></b>: " + result.location.y  );
      // content.push("<b>GeoRSS-Simple</b>&lt;georss:point&gt;" + result.location.y + " " + result.location.x + "&lt;/georss:point&gt;");
      //          content.push("<b>GeoRSS-GML</b> &lt;georss:where&gt;&lt;gml:Point&gt;&lt;gml:pos&gt;" + result.location.y + " " + result.location.x + "&lt;/gml:pos&gt;&lt;gml:Point&gt;&lt;/georss:where&gt;");
      content.push("<br/>");
      content.push("<b><i>JSON:</i></b> " + dojo.toJson(result.location.toJson()));
      //          content.push('<b>Geo JSON</b>  "geometry": {"type": "Point", "coordinates": [' + result.location.y + ',' + result.location.x + ']}');
      //content.push("<br/>");
      //content.push('<b>GeoRSS-GML</b>&lt;Point xmlns="http://www.opengis.net/gml" &gt;&lt;pos&gt;' + result.location.y + " " + result.location.x + "&lt;/pos&gt;&lt;Point&gt;");
      //	  <Point xmlns="http://www.opengis.net/gml"><pos>33.394398711029645 -111.95809052697564</pos></Point>
      content.push("</fieldset>");
      });
  rdiv.innerHTML += content.join("");

}

