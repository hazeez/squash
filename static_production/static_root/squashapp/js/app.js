angular.module('squashapp-ng', ['ui-router',
    'ui-state',
    'ngResource',
    'squashapp-ng.services',
    'squashapp-ng.controller'
])

.config(['', function($interpolateProvider, $httpProvider,
        $resourceProvider, $stateProvider, $urlRouterProvider) {

        // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');


    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    $urlRouterProvider.otherwise('/');

    $stateProvider
    .state('projects', {
        url: '/projects',
        templateUrl : 'home.html',
        controller: 'ProjectListCtrl',
    });
}]);
