
Server Script_JSON
// Class Object gets the methos .size
// gives the javascript Object the property of .size
// when called with an object as the peramiter then returns the amount of properties of the passed object
     Object.size = function(obj) {
    var size = 0, key;
    console.writeln(obj);
    for (key in obj) {
        if (obj.hasOwnProperty(key)) {        
                  size++;
          }
          else {     size++;     }
    }
    return size;
};
function getJSONFromDatafunnel (df) {
  return makeJSONString(getTableFromDatafunnel(df));
}
function getTableFromDatafunnel (getDfunnel)
{
     if (request.verbose) {    
  console.writeln("DataFunnel Passed: " + getDfunnel);
  }
  var dfunnel = datafunnel.get(getDfunnel);
  var dfTable = new Object();
  dfTable.headers = new Array();
  dfTable.tableCols = new Array();
  var i;
  var j;
  for (i = 0 ; i < dfunnel.numCols() ; i++) {
    j = 0 ;
    dfTable.tableCols[i] = new Array();
    for (j = 0 ; j < dfunnel.numRows() ; j++)
    {
      dfTable.tableCols[i].push(dfunnel.cell(j+1,i+1)); //push a value in the second dimension array
    }
  }
  return dfTable;
}
function makeJSONString(table) {
  var jsonString = "{";                              //{                              Begin JSON obj
  columnRowData = "";
  colNameandColon = "";
  for (var i = 0; i < table.tableCols.length ; i++)
  {    
    for (var j = 0; j < table.tableCols[i].length ; j++)
    {
      if (j == 0) {         
     colNameAndColon = i+":{id:'"+i+"',name:'"+table.tableCols[i][j] + "',data:[";         // "Apple": [    Top of the Column          Inner Obj Head              
     continue;
      }
      if ( j < table.tableCols[i].length-1) {         
     columnRowData += '"'+table.tableCols[i][j]+'",';          // "Data","Data2","Data3",     Rows Cont.
      }
      else
      {              
     columnRowData += '"'+table.tableCols[i][j]+'"';          // "Data4"     Row Stop               End JSON obj
      }
    }    
    if ( i < table.tableCols.length-1 ) {
      jsonString +=  colNameAndColon + columnRowData + "]},";                              //{"Apple": [ "Data","Data2","Data3","Data4"],
    }
    else
    {
      jsonString +=  colNameAndColon + columnRowData + "]}";                               //{"Apple": [ "Data","Data2","Data3","Data4"]
    }
    columnRowData = "";
    }
    jsonString += "}";
    return jsonString
    }
    function getRowsFromTableColObject (columnObj) {
      var RowArray = new Array();
      for (var i = 0; i < columnObj.length ; i++)
      {    
     RowArray.push(columnObj[i]);
      }
      return RowArray;
    }
    //------------------------------------------------------------------------------------------------
    function getRowJSONFromDatafunnel (df) {
      return makeJSONStringFromRowTable(getDataInRowsFromTableFromDatafunnel());
    }
    function getDataInRowsFromTableFromDatafunnel (getDfunnel)
    {
      var dfunnel = datafunnel.get(getDfunnel);
      var dfTable = new Object();
      dfTable.headers = new Array();
      dfTable.rows = new Array();
      var i;
      var j;
      for (i = 0 ; i < dfunnel.numRows() ; i++) {
     j = 0 ;
     dfTable.rows[i] = new Array();
     for (j = 0 ; j < dfunnel.numCols() ; j++)
     {
       dfTable.rows[i].push(dfunnel.cell(i+1,j+1)); //push a value in the second dimension array
     }
      }
      return dfTable;
    }
    function makeJSONStringFromRowTable(table) {
      var jsonString = "{";                             
      jsonString += 'tableProperty: {columnCount: "'+table.rows[0].length + '", rowCount:"'+ table.rows.length+'"},';
      var rowData = "";
      for (var i = 0; i < table.rows.length ; i++)                               //go down all rows
      {    
     rowData = i+":{";
     for (var j = 0; j < table.rows[i].length ; j++)                            //get all the columns in row
     {
       if (j < table.rows[i].length) {                                       
         rowData += 'col'+j+':"'+table.rows[i][j] + '",';
       }
       else {
         rowData += '{col"'+j+':"'+table.rows[i][j] + '"}';
       }
     }     //end get all columns for row element
     if ( i < table.rows.length-1 ) {
       jsonString +=  rowData + "},";                              //{"Apple": [ "Data","Data2","Data3","Data4"],
     }
     else
     {
       jsonString +=  rowData + "}";                               //{"Apple": [ "Data","Data2","Data3","Data4"]
     }
     }
     jsonString += "}";
     return jsonString
     }
//returns json of name value pairs for the dashboard variables and their values
function getDashboardVariables () {
  var i = 0;
  var dashboardNameValuesPairs = '{';                                                                                          // {         
  dashboardNameValuesPairs += '"Dashboard_Variables":"These Variables are used to set the snapshots.",';          // just the header for the json object
  for (var property in dashboard) {                                                                           // for each attrubute of the variable dashboard, put it into the final string
    if (property.substring(0,7) == "format_" && dashboard[property]) {         
      //if (i < dashboard.size ) {         
      dashboardNameValuesPairs += '"'+property.substring(7,property.length)+'"'+':"'+dashboard[property].replace(/['"]/g,'') +'",';
      //     }
      //else {         
      //     dashboardNameValuesPairs += property.substring(7,property.length)+":'"+dashboard[property].replace(/['"]/g,'') +"'";
      //}
    }
    else
    {         
    }
    i++;
  }
  // the .size method is a custom method of the Object Class--and requires the instanstation from the previous script section
  dashboardNameValuesPairs += '"length":"'+Object.size(dashboard) +'"';                                                        // ,name:'value' , put all the extra attrubutes of the json object here, in the form of name:'value'
  dashboardNameValuesPairs += '}';                                                                                                    // }
  return dashboardNameValuesPairs;
}
//------------------------------------------------------------------------------------------------    
function getCommaSQLFromJSArray (JSArray) {
  return makeCommaStringFromRowTable(getDataInRowsFromTableFromJSObject(JSArray));
}
function getDataInRowsFromTableFromJSObject (jsObject) {
  var newJSObject = new Array();
  for (var i = 0; i < jsObject.length; i++) {
    var year = jsObject[i].substring(0,1) + jsObject[i].substring(2,4);                                        // '212' , year in the form of 212
    var yearBefore = parseInt(year)-1;                                                                                               // the year before
    var yearBeforeToTermString  = yearBefore +'7'
      newJSObject.push("'"+yearBeforeToTermString.toString()+"'");                                                            // the fall semester with a comma
  }              
  return newJSObject
}
function makeCommaStringFromRowTable(table) {
  var sqlString = "";                             
  for (var i = 0; i < table.length ; i++)                              
  {         
    if ( i < table.length-1 ) {
      sqlString +=  table[i] + ",";                             
    }
    else
    {
      sqlString +=  table[i];                              
    }
  }
  return sqlString
}
//------------------------------------------------------------------------------------------------
// takes 2014 aid year and converts it to 2137 term
// would like to keep the same structure as dojo table but will wait till later
getFallTermCommaSQLFromJSArray = function (jsObject) {
  var newString = "";
  for (var i = 0; i < jsObject.length; i++) {
    console.writeln("here: " + jsObject[i]);    
           if (jsObject[i] != '%' && jsObject[i].toString()) {    
                 var year = jsObject[i].substring(0,1) + jsObject[i].substring(2,4);                                        // '212' , year in the form of 212
                 var yearBefore = parseInt(year)-1;                                                                                               // the year before
                    var yearBeforeToTermString  = yearBefore +'7'
                    if (i < jsObject.length -1 ) {         
                           newString += "'"+yearBeforeToTermString.toString()+"',";                                                            // the fall semester with a comma
                    }
                    else {         
                           newString += "'"+yearBeforeToTermString.toString()+"'";                                                            // the fall semester
                    }
              }
  }              
  return newString;
}
//------------------------------------------------------------------------------------------------
// takes 2014 aid year and converts it to '2137','2141','2144' term
// would like to keep the same structure as dojo table but will wait till later
getTermCommaSQLFromAidYearJSArray = function (aidYearArray) {
  var newString = "";
  for (var i = 0; i < aidYearArray.length; i++) {
    if(aidYearArray[i] != '%' && aidYearArray[i]) {    
      var yearPrefix = aidYearArray[i].substring(0,1) + aidYearArray[i].substring(2,4);
      newString += "'"+ (parseInt(yearPrefix)-1).toString() + "7',";
      newString += "'"+ yearPrefix + "1',";
      newString += "'"+ yearPrefix + "4'";
      if ( i < aidYearArray.length-1) {    
     newString += ',';
      }
      else {    
      }
    }
    console.writeln(newString);
  }
  return newString;
}

