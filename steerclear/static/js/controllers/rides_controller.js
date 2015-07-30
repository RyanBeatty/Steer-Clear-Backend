app.controller('RidesController', ['$scope', 'RidesService', function($scope, RidesService){

	var ride = {
        "num_passengers": 4,
        "start_latitude": 37.273485,
        "start_longitude": -76.719628,
        "end_latitude": 37.280893,
        "end_longitude": -76.719691
    };

    RidesService.createRide(ride)

	RidesService.getRides().then(function(data){
		$scope.rides = data.rides
        console.log (data.rides)
	})

}]);