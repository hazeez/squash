// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('squashapp-ng.services', ['ngResource'])
.factory('Projects', function($resource){
    console.log("i am here");
    return $resource('/api/projects/');
    });

