angular.module('squashappng', [
    'ui.router',
    'ngResource',
    'squashappng.services',
    'squashappng.controller'
])

.config(function($interpolateProvider, $httpProvider,
        $resourceProvider, $stateProvider, $urlRouterProvider) {

        // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('{$$');
    $interpolateProvider.endSymbol('$$}');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    $urlRouterProvider.otherwise('/');

    $stateProvider
    // .state('projectdetails',{
    //     url:'/projectdetails',
    //     templateUrl : '/static/squashapp/partials/project-details.html',
    // })
    .state('regionprojects', {
        // url: '/:name',
        url:'/regionprojects',
        templateUrl : '/static/squashapp/partials/region-projects.html',
        controller: 'RegionProjectsCtrl',
    })
    .state('myprojects', {
        // url: '/:name',
        url:'/:name1',
        templateUrl : '/static/squashapp/partials/sqa-list.html',
        controller: 'MyProjectsCtrl',
    })
    .state('projectslist', {
        url: '/',
        templateUrl : '/static/squashapp/partials/project-list.html',
        controller: 'ProjectListCtrl',
    });

});


