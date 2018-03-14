
// make a html table from a javascript object
function makeTableFromObject (jsonObject) {
  var dashString = '<div class="layout_tabs"><p></div><div class="layout_content">'
    dashString += '<table class="table" >' 
    var first = true
    for (var element in jsonObject) {
      if (first == true) {
     markCol = '<th>'
       markEndCol = '</th>'
       first = false;
      }
      else {
     markCol = '<td>'
       markEndCol = '</td>'
      }
      dashString += markRow
     dashString += markCol
     dashString += element
     dashString += markEndCol + markCol;
      dashString += jsonObject[element]
     dashString += markEndCol
     dashString += markEndRow
    }
  dashString += '</table>'
    dashString += '</div></div>'
    return dashString
};
// make a html table from a javascript object and apply it directly to the id #test
var makeTestTableFromObject = function (jsonObject) {
  var dashString = '<div class="layout_tabs"><p></div><div class="layout_content">'
    dashString += '<table class="table" >' 
    var first = true
    for (var element in jsonObject) {
      if (first == true) {
     markCol = '<th>'
       markEndCol = '</th>'
       first = false;
      }
      else {
     markCol = '<td>'
       markEndCol = '</td>'
      }
      dashString += markRow
     dashString += markCol
     dashString += element
     dashString += markEndCol + markCol;
      dashString += jsonObject[element]
     dashString += markEndCol
     dashString += markEndRow
    }
  dashString += '</table>'
    dashString += '</div></div>'
    $('#test').append(dashString);
};
//"{"0":{"id":"0","name":"EMPLID","data":["1000252472"]},"1":{"id":"1","name":"EFFSEQ","data":["1"]}
// make a table from a json object in the format above. simiular to the json object used in dojo.js
// basically transoposes the data
var makeColumnTableFromObject = function (jsonObject) {
  var first = true
    //th = table_titlerow
    var dashString = '<div class="layout_tabs"><p></div><div class="layout_content">'
    dashString += '<table class="table" >'  
    dashString += markRow
    for (var element in jsonObject) {
      first = true
     dashString += markCol
     dashString += jsonObject[element]['id']                                        // grab the id of the column element
     dashString += markEndCol
     dashString += markCol
     dashString += jsonObject[element]['name']                                   // grab the name of the column element
     dashString += markEndCol
     for(var i = 0; i < jsonObject[element]['data'].length ; i++) {          // iterate across data of the column element   
       dashString += markCol
         dashString += jsonObject[element]['data'][i]
         dashString += markEndCol
     }
      dashString += markEndRow
    }
  dashString += '</table>'
    dashString += '</div>'
    return dashString;
};
var markRow = '<tr>'
var markCol = '<td>'
var markEndRow = '<tr>'
var markEndCol = '</td>'

