var squashControllers = angular.module('squashappng.controller', []);

squashControllers.controller('ProjectListCtrl', function ProjectListCtrl($scope, Projects){
    $scope.projects = {};

    Projects.query(function(response){
        $scope.projects = response;
    });
});

squashControllers.controller('MyProjectsCtrl', function MyProjectsCtrl($scope, Projects, MyProjects, AuthUser){
    $scope.sqaprojects = {};
    sqaname = AuthUser.sqaname;
    MyProjects.query({name1:sqaname}, function(response){
        $scope.sqaprojects = response;
    });

});
