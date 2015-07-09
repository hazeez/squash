var squashControllers = angular.module('squashappng.controller', []);

squashControllers.controller('ProjectListCtrl', function ProjectListCtrl($scope, Projects){
    $scope.projects = {};

    Projects.query(function(response){
        $scope.projects = response;
    });
});

squashControllers.controller('MyProjectsCtrl', function MyProjectsCtrl($scope, MyProjects, AuthUser){
    $scope.sqaprojects = {};
    sqaname = AuthUser.sqaname;
    MyProjects.query({name1:sqaname}, function(response){
        $scope.sqaprojects = response;
    });

});

squashControllers.controller('RegionProjectsCtrl',
    function RegionProjectsCtrl($scope, RegionProjects){
    $scope.regions = [];
    $scope.regionalprojects = {};
    var jsonstr = "";

    RegionProjects.query(function(response){
            // $scope.regionalprojects = JSON.stringify(response);
            $scope.regionalprojects = JSON.parse(JSON.stringify(response));
            // $scope.regionalprojects = response;
            console.log($scope.regionalprojects);
            console.log(typeof $scope.regionalprojects);
            // return $scope.regionalprojects;

    });


    $scope.filterRegions = function() {
        return function(p) {
            for (var i in $scope.regions){
                if (p.project_region == $scope.group[i] && $scope.regions[i]) {
                    return true;
                }
            }
        };

    };

});
