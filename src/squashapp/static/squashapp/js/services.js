// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('squashappng.services', ['ngResource'])
.factory('Projects', function($resource){
    return $resource('/api/projects/');
})
.factory('MyProjects', function ($resource) {
    // body...
    return $resource('/api/projects/:name1/');
})
.factory('RegionProjects', function($resource){
    return $resource('/api/projects1/');
});


