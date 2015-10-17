var bookworm = angular.module('bookworm', []);

bookworm.controller('bookController', function ($scope, $http) {
  $http.get('js/books.json')
        .then(function(response){
          $scope.books = response.data;
        });
  $scope.orderProp = 'number';
});

bookworm.controller('dateUpdater', function ($scope, $http) {
  $http.get('js/updated_date.json')
        .then(function(response){
          $scope.dates = response.data;
        });
});
