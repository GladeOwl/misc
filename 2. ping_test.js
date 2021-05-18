const ping = require('ping');

function checkConnection() {
	var hosts = ['192.168.1.1', 'google.com'];
	var allGood = true;
	hosts.forEach(function(host) {
		ping.sys.probe(host, function(isAlive) {
			if (!isAlive) allGood = false; 
		});
	});

	if (allGood) {
		console.log('Good')
	}
	else {
		console.log('Bad')
	}
}
var pingCheck = setInterval(checkConnection, 3000);
