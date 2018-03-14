
var app = angular.module("app", ['ngRoute'])
app.controller("main", function($scope,$sce, $http, $route,$routeParams) {
  $scope.report = WorkNotes;

$scope.renderHtml = function(html_code, element)
{
  if(element == 'h1') {
    return $sce.trustAsHtml(html_code);
  }
  else if (html_code && html_code.length > 350) {
    //html_code = html_code.substring(0,201) + "[...]"
    return $sce.trustAsHtml(html_code);
  }
  else {
    return $sce.trustAsHtml(html_code);
  }
};

$scope.myFunc = function(id) {
  $('#editor').html(id)
}
});


app.controller("detail_controller", function($scope, $routeParams, $http, $route, $sce, $filter) {
  //$scope.param1 = $routeParams.param1;
  $scope.post_id = $routeParams.post;
  $scope.report = WorkNotes;

$scope.renderHtml = function(html_code, element)
{
  if(element == 'h1') {
    return $sce.trustAsHtml(html_code);
  }
  else if (html_code && html_code.length > 350) {
    //html_code = html_code.substring(0,201) + "[...]"
    return $sce.trustAsHtml(html_code);
  }
  else {
    return $sce.trustAsHtml(html_code);
  }
};

}); 

//  $scope.stop_words = stop_words;
//  console.log(stop_words);

app.filter('firstWord', function() {

  return function(data) {
    if(!data) return data;
    data = data.split(' '); 
    for (var wrd in data){
      the_word = ''
      for (var word in stop_words){
	if(data[wrd].trim().toLowerCase() == stop_words[word]){
	  break;
	}
	else {
	  the_word = data[wrd].trim()

	}

	  
	}
      
      }
    return the_word;
    }
  
});


/*
angular.module('FilterInControllerModule', []).controller('FilterController', ['filterFilter', function FilterController(filterFilter) {
  this.filteredArray = filterFilter(WorkNotes, 'Done');
}]);
*/
app.config(function($routeProvider) {
  $routeProvider.when('/detail?post', {
    templateUrl: './views/detail.html',
    controller: 'detail_controller'
  })
    $routeProvider.when('/detail', {
    templateUrl: './views/detail.html',
    controller: 'detail_controller'
  })

 $routeProvider.otherwise({ redirectTo: '/home' }); //can be login too!!!!!
});

app.filter('unique', function() {
  return function(collection, keyname) {
    var output = [], 
      keys = [];

    angular.forEach(collection, function(item) {
      var key = item[keyname];
      if(keys.indexOf(key) === -1) {
	keys.push(key); 
	output.push(item);
      }
    });
    return output;
  };
});



