var Type;
var Url;
var Data;
var ContentType;
var DataType;
var ProcessData;
var resultObject;

var wsUrl = "http://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php#";
var wsUrl = "http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php";
var xhr = new XMLHttpRequest({mozSystem: true});
$.support.cors = true;



function serviceGetWeather() {$.ajax({
//"permissions": { "systemXHR" : {}, }
crossDomain:true,
type: "GET",               
url: "http://api.openweathermap.org/data/2.5/weather",                 
url: "http://api.openweathermap.org/data/2.5/forecast/daily",                 
data: "lat=33.403961&lon=-111.929474&mode=json&cnt=7&units=imperial",                 

//        contentType: ContentType,   
dataType: "html",
processdata: true ,   
success: function (msg) {//alert(msg);
},
//error: alert($readyS)
});
}

// Function to call WCF  Service       
function CallService() {
    $.ajax({
        type: Type,                 //GET or POST or PUT or DELETE verb
        url: Url,                   // Location of the service
//        data: Data,                 //Data sent to server
//        contentType: ContentType,   // content type sent to server
        dataType: DataType,         //Expected data format from server
//        processdata: ProcessData,   //True or False
        success: function (msg) {   //On Successfull service call
            ServiceSucceeded(msg);
        },
        error: ServiceFailed        // When Service call fails
    });
}

function ServiceGetWeather() {
    //public string SetComment(int DevId, string Comment, string CreatedBy) {
    Type = "GET";
    Url = "http://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php";
        Url = "http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?whichClient=NDFDgen&lat=39.7&lon=-104.75&product=time-series"
//    Data = '{}';
    ContentType = "application/xml; charset=utf-8";
    DataType = "xml";
   // ProcessData = true;
    CallService();
}


function ServiceGetAllDevelopmentWater() {
    //public string SetComment(int DevId, string Comment, string CreatedBy) {
    Type = "POST";
    Url = "http://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php";
    Data = '{}';
    ContentType = "application/xml; charset=utf-8";
    DataType = "xml";
    ProcessData = true;
    CallService();
}

function setCheckBoxAllHPCPolylines(incoming) {
    var symbol = new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.SOLID, new dojo.Color([255, 0, 0]), 1);
    var attr;
    if (incoming.checked) {
        for (i = 0; i < xmlItemListHPCAllPolylines.length; i++) {
            var PointArray = [];
            try {
                var coords = xmlItemListHPCAllPolylines[i].getElementsByTagName("Gml")[0].childNodes[0].nodeValue
                var pointLink = xmlItemListHPCAllPolylines[i].getElementsByTagName("HPCProjectNumber")[0].childNodes[0].nodeValue;
                if (coords.substring(0, 10) == "LINESTRING") {
                    allCoords = coords.substring(11, coords.length - 1);
                    allCoords = allCoords.replace("(", "");
                    allCoords = allCoords.replace(")", "");
                    allCoords = allCoords.split(",");
                    for (j = 0; j < allCoords.length; j++) {
                        coords = allCoords[j].trim();
                        coords = coords.split(" ");
                        var x = coords[0];
                        var y = coords[1];
                        var newPoint = new esri.geometry.Point(x, y, map.spatialReference);
                        PointArray.push(newPoint);
                    }
                    attr = { "Xcoord": x, "Ycoord": y, "URL": pointLink };
                    var infoTemplate = new esri.InfoTemplate("HPC Project Location",
                        "HPC Project Number: ${URL} <br/>" +
                        "Latitude: ${Ycoord} <br/> Longitude: ${Xcoord}" +
                        "<br/> <a href='http://phx-gis-dev-ags/Dashboard/HPC.aspx?HPCId=${URL}' title='Goto Record View' target='_blank'><img id='Image1' style='height:33%;' src='http://phx-gis-dev-ags/Images/appImages/DevelopmentDashboard/Document2.png'></a>" +
                        "<a href='http://phx-gis-dev-ags/Dashboard/Map.aspx?HPCId=${URL}' title='Goto Catchment View' target='_blank'><img id='Image2' style='height:33%;' src='http://phx-gis-dev-ags/Images/appImages/DevelopmentDashboard/world.png'/></a><br />");
                    var polyline = new esri.geometry.Polyline(new esri.SpatialReference({ wkid: 4326 }));
                    polyline.addPath(PointArray);
                    var polyline = esri.geometry.geographicToWebMercator(polyline);
                    var graphic = new esri.Graphic(polyline, symbol, attr, infoTemplate);
                    map.graphics.add(graphic);
                }

            } //end of try
            catch (err) {
                console.log("Unable to Put Point: ", XMLAllHPCLatLongs[i]);
                console.log("Error: ", err);
            } //end of catch
        } //end of for
    } //end of if
    else {
        map.graphics.clear();
    } //end of else
}
function setCheckBoxAllHPCPoints(incoming) {
    var attr;
    if (incoming.checked) {
        for (i = 0; i < xmlItemListHPCAllLatLongs.length; i++) {
            try {
                var coords = xmlItemListHPCAllLatLongs[i].getElementsByTagName("Gml")[0].childNodes[0].nodeValue
                var pointLink = xmlItemListHPCAllLatLongs[i].getElementsByTagName("HPCProjectNumber")[0].childNodes[0].nodeValue;
                if (coords.substring(0, 5) == "POINT") {
                    coords = coords.split(" ");
                    var x = coords[1].replace("(", "");
                    var y = coords[2].replace(")", "");
                    var newPoint = new esri.geometry.Point(x, y, map.spatialReference);
                    //attr = { "Xcoord": x, "Ycoord": y, "Title": pointTitle, "URL": pointLink };
                    attr = { "Xcoord": x, "Ycoord": y, "URL": pointLink };
                    var infoTemplate = new esri.InfoTemplate("HPC Project Location",
                    "HPC Project Number: ${URL} <br/>" +
                    "Latitude:${Xcoord}  <br/> Longitude: ${Ycoord}" +
                    "<br/> <a href='http://phx-gis-dev-ags/Dashboard/HPC.aspx?HPCId=${URL}' title='Goto Record View' target='_blank'><img id='Image1' style='height:33%;' src='http://phx-gis-dev-ags/Images/appImages/DevelopmentDashboard/Document2.png'></a>" +
                    "<a href='http://phx-gis-dev-ags/Dashboard/Map.aspx?HPCId=${URL}' title='Goto Catchment View' target='_blank'><img id='Image2' style='height:33%;' src='http://phx-gis-dev-ags/Images/appImages/DevelopmentDashboard/world.png'/></a><br />");
                    var r = 255;
                    var g = 5;
                    var b = 5;
                    var symbol = new esri.symbol.SimpleMarkerSymbol(esri.symbol.SimpleMarkerSymbol.STYLE_CIRCLE, 5, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([r, g, b, 0.5]), 10), new dojo.Color([r, g, b, 0.9]));
                    var pointMeters = esri.geometry.geographicToWebMercator(newPoint);
                    var graphic = new esri.Graphic(pointMeters, symbol, attr, infoTemplate);
                    map.graphics.add(graphic);
                }
                //var esriExtent = new esri.geometry.Extent(ptAttr.West_Lon, ptAttr.South_Lat, ptAttr.East_Lon, ptAttr.North_Lat, new esri.SpatialReference({ wkid: 4326 }));
                //map.setExtent(esri.geometry.geographicToWebMercator(esriExtent));
            } //end of try
            catch (err) {
                console.log("Unable to Put Point: ", XMLAllHPCLatLongs[i]);
                console.log("Error: ", err);
            } //end of catch
        } //end of for
    } //end of if
    else {
        map.graphics.clear();
    } //end of else
}

function setCheckBoxAllHPCPolygons(incoming) {
    var symbol = new esri.symbol.SimpleFillSymbol(esri.symbol.SimpleFillSymbol.SOLID, new dojo.Color([255, 0, 0]), 1);
    var attr;
    if (incoming.checked) {
        for (i = 0; i < xmlItemListHPCAllPolygons.length; i++) {
            var PointArray = [];
            //try {
                var coords = xmlItemListHPCAllPolygons[i].getElementsByTagName("Gml")[0].childNodes[0].nodeValue
                //var pointTitle = xmlItemListHPCAllPolygons[i].getElementsByTagName("Name")[0].childNodes[0].nodeValue;
                var pointLink = xmlItemListHPCAllPolygons[i].getElementsByTagName("HPCProjectNumber")[0].childNodes[0].nodeValue;
                if (coords.substring(0, 7) == "POLYGON") {
                    
                    allCoords = coords.substring(9, coords.length - 1);
                    allCoords = allCoords.replace("(", "");
                    allCoords = allCoords.replace(")", "");
                    allCoords = allCoords.split(",");
                    for (j = 0; j < allCoords.length; j++) {
                        coords = allCoords[j].trim();
                        coords = coords.split(" ");
                        var x = coords[0];
                        var y = coords[1];
                        var newPoint = new esri.geometry.Point(x, y, map.spatialReference);
                        console.log(coords)
                        PointArray.push(newPoint);
                    }
                    attr = { "Xcoord": x, "Ycoord": y, "URL": pointLink };
                    var infoTemplate = new esri.InfoTemplate("HPC Project Location",
                        "HPC Project Number: ${URL} <br/>" +
                        "Latitude: ${Ycoord} <br/> Longitude: ${Xcoord}" +
                        "<br/> <a href='http://phx-gis-dev-ags/Dashboard/HPC.aspx?HPCId=${URL}' title='Goto Record View' target='_blank'><img id='Image1' style='height:33%;' src='http://phx-gis-dev-ags/Images/appImages/DevelopmentDashboard/Document2.png'></a>" +
                        "<a href='http://phx-gis-dev-ags/Dashboard/Map.aspx?HPCId=${URL}' title='Goto Catchment View' target='_blank'><img id='Image2' style='height:33%;' src='http://phx-gis-dev-ags/Images/appImages/DevelopmentDashboard/world.png'/></a><br />");
                    var polygon = new esri.geometry.Polygon(new esri.SpatialReference({ wkid: 4326 }));
                    polygon.addRing(PointArray);
                    var polygon = esri.geometry.geographicToWebMercator(polygon);
                    var graphic = new esri.Graphic(polygon, symbol, attr, infoTemplate);
                    console.log(graphic);
                    map.graphics.add(graphic);
                }

            //} //end of try
            //catch (err) {
            //    console.log("Unable to Put Point: ", XMLAllHPCLatLongs[i]);
            //    console.log("Error: ", err);
           // } //end of catch
        } //end of for
    } //end of if
    else {
        map.graphics.clear();
    } //end of else
}

//$.ajax({
//    type: "POST",
//    url: wsUrl,
//    contentType: "text/xml",
//    dataType: "xml",
//    data: soapRequest,
//    success: ServiceSucceeded,
//    error: ServiceFailed
//});
//var ajaxOut;
//data = {"lat": '38.99', "lon":'-77.01', "product":'time-series', "begin":'2004-01-01T00:00:00',"end":'2013-04-20T00:00:00',"maxt":'maxt',"mint":'mint'};
//function ServiceGetWeather() {
//    Data = data;
//    Url = wsUrl;
//    getXmlDoc($.ajax({
//        type: "GET",
//        url: wsUrl,
//        data: Data,
//        contentType: "json",
//        dataType: "xml",
//        //jsonp: "jsoncallback",
//        processData: true,
//        complete: function (msg) { console.log("complete",msg); }
//        //success: function (msg) { ServiceSucceeded(msg); },
//        //error: ServiceFailed
//    }));
//}


function ServiceFailed(result) {
    alert('Service call failed: ' + result.responseText + "\n " +
            "TYPE: " + Type + "\n " +
            "Url: " + Url + "\n " +
            "Data: " + Data + "\n " +
            "Content Type: " + ContentType + "\n " +
            "DATA TYPE: " + DataType + "\n" +
            "Process Data: " + ProcessData + "\n ");

    Type = null;
    Url = null;
    Data = null;
    ContentType = null;
    DataType = null;
    ProcessData = null;
}
function ServiceSucceeded(result) {
    alert(result);
    //            if (DataType == "json") {
    //                var resultObject = result.GetUserResult;
    //
    //                for (i = 0; i < resultObject.length; i++) {
    //                    alert(resultObject[i]);
    //                }
    //            }
}

