var squashControllers = angular.module('squashapp-ng.controller', []);

squashControllers.controller('ProjectListCtrl', function(){
    $scope.projects = {};

    Projects.query(function(){
        $scope.projects = response;
    });
});
