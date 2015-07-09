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
    function RegionProjectsCtrl($scope, RegionProjects, filterFilter){
    $scope.group= [];
    $scope.regions = [];
    $scope.regionalprojects = {};
    $scope.groupregionalprojects = {};
    $scope.uniquegroupregionalprojects = {};


    // RegionProjects.query(function(response){
    //         $scope.regionalprojects = JSON.stringify(response);
    // });

    RegionProjects.query(function(response){
            $scope.regionalprojects = response;
            //get unique project regions
            $scope.uniquegroupregionalprojects = _.chain($scope.regionalprojects).map(function(projects){return projects.project_region;}).uniq().value();
            // // group by projects - use _.groupBy underscore method
            // $scope.groupregionalprojects = _.groupBy($scope.regionalprojects,'project_region');
    });

    // $scope.regionalprojects = $(function(){
    // $.getJSON('/api/projects1/', function(data) {
    //     return (JSON.stringify(data));
    // });
    // });



    // $scope.regionalprojects = jQuery.ajax({
    //         url: "/api/projects1/",
    //         type: "GET",

    //         contentType: 'application/json; charset=utf-8',
    //         success: function(resultData) {
    //             console.log(resultData);
    //             return resultData;
    //         },
    //         error : function(jqXHR, textStatus, errorThrown) {
    //         },

    //         timeout: 120000,
    //     });


    // $scope.regionalprojects = [{"project_release_name":"FCIS6.5.0.0.0$HSBCHK_R61","project_region":"EUR"},{"project_release_name":"FCUBS11.1.0.1.0$NMIBTZ_R3","project_region":"EUR"},{"project_release_name":"FLEXCUBE@VJR3.4.0.0.0$JBUNJP","project_region":"JAP"},{"project_release_name":" FCIS6.5.0.0.0$HSBCHK_R61","project_region":"EUR"},{"project_release_name":"FCUBS_10.5.0.0.0$BNTBUS_R19","project_region":"AME"},{"project_release_name":"FCUBS_12.0.2.0.0$EGPNBE_R1","project_region":"EUR"},{"project_release_name":"FCUBS_3.3.0.0.0$CITIBK_R716","project_region":"JAP"},{"project_release_name":"FCUBS_7.1.0.0.0$EFGBRS_R19","project_region":"EUR"},{"project_release_name":"FCUBS_12.0.2.0.0$ABNGNG_R4","project_region":"EUR"},{"project_release_name":"FCIS_7.0.0.0.0$PERMMY_R20","project_region":"EUR"},{"project_release_name":"FCUBS11.1.0.1.0$NMIBTZ_R5","project_region":"EUR"},{"project_release_name":"FCUBS11.1.0.1.0$NMIBTZ_R4","project_region":"EUR"},{"project_release_name":"FCUBS11.1.0.1.0$NMIBTZ_R6","project_region":"AME"},{"project_release_name":"FCUBS11.1.0.1.0$NMIBTZ_R7","project_region":"JAP"},{"project_release_name":"FCUBS11.1.0.1.0$NMIBTZ_R8","project_region":"EUR"}];

    $scope.filterRegions = function() {

        return function(p) {
            for (var i in $scope.regions){
                console.log($scope.group);
                if (p.project_region == $scope.group[i] && $scope.regions[i]) {
                    console.log("i am here");
                    return true;
                }
            }
        };

    };

});
