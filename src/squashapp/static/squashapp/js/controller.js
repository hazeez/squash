var squashControllers = angular.module('squashappng.controller', []);

squashControllers.controller('ProjectListCtrl', function ProjectListCtrl($scope, Projects){
    $scope.projects = {};

    Projects.query(function(response){
        $scope.projects = response;
    });
});

squashControllers.controller('MyProjectsCtrl', function MyProjectsCtrl($scope, Projects, User, AuthUser){
    $scope.projects = {};
    name = AuthUser.name;
    User.get({
        name: name
    }, function(response){
        $scope.user = response;
        $scope.projects = response.projects;
    });
});
