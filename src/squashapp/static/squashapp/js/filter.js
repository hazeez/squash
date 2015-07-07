var uniqueRegions = function(data, key) {
    var result = new Array();
    for (var i = 0; i < data.length; i++) {
        var value = data[i][key];

        if (result.indexOf(value) == -1) {
            result.push(value);
        }
    }
    return result;
};

angular.module('squashappng.filter', []).filter('groupBy',
    function() {
        return function(collection, key) {
            if (collection === null) return;
            return uniqueRegions(collection, key);
        };
    });
