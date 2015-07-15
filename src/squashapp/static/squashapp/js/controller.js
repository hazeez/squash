var squashControllers = angular.module('squashappng.controller', []);

squashControllers.controller('ProjectListCtrl', function ProjectListCtrl($scope, Projects, getReleaseName) {
    $scope.projects = {};

    Projects.query(function(response) {
        $scope.projects = response;
    });

    // get project name from the view - from the td element
    // $scope.editProject = {};
    $scope.release_name = {};
    $scope.EditRow = function(project) {

        $scope.releasename = project.project_release_name;
        //passing the scope release name to the service
        // because in angularjs you dont get to share variables between controllers
        getReleaseName.releasename = $scope.releasename;
    };
});

squashControllers.controller('MyProjectsCtrl', function MyProjectsCtrl($scope, MyProjects, AuthUser) {
    $scope.sqaprojects = {};
    sqaname = AuthUser.sqaname;
    MyProjects.query({
        name1: sqaname
    }, function(response) {
        $scope.sqaprojects = response;

    });

});

squashControllers.controller('RegionProjectsCtrl',
    function RegionProjectsCtrl($scope, RegionProjects) {

        $scope.regions = [];
        $scope.regionalprojects = {};
        $scope.groupregionalprojects = {};
        $scope.uniquegroupregionalprojects = {};

        $scope.filterRegions = function() {
            return function(p) {
                for (var i in $scope.regions) {
                    if (p.project_subregion == $scope.uniquegroups[i] &&
                        $scope.regions[i]) {
                        return true;
                    }
                }
            };
        };

        RegionProjects.query(function(response) {
            $scope.regionalprojects = response;
            //get unique project re
            $scope.uniquegroups = _.chain($scope.regionalprojects).map(function(projects) {
                return projects.project_subregion;
            }).uniq().value();
            return $scope.uniquegroups;
            // // group by projects - use _.groupBy underscore method
            // $scope.groupregionalprojects = _.groupBy($scope.regionalprojects,'project_region');
        });

    });


squashControllers.controller('ProjectDetailsCtrl',
    function ProjectDetailsCtrl($scope, ProjectDetails, getReleaseName) {
        $scope.releasedetail = {};
        ProjectDetails.query({
            //getting the releasename from the getReleasename service
            releasename: getReleaseName.releasename
        }, function(response) {
            $scope.releasedetail = response;
        });

    });
