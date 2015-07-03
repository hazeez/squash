// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('squashappng.services', ['ngResource'])
.factory('Projects', function($resource){
    return $resource('/api/projects/');
});

