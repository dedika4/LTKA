function displayData(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var pos = JSON.parse(this.responseText);
      document.getElementById("jarak").innerHTML ="Jarak anda adalah "+pos.distance+" dengan sudut "+pos.direction;
      ang = Math.ceil(pos.direction/30) + 1;
      data = [0,0,0,0,0,0,0,0,0,0,0,0];
      data[ang]=pos.distance;
      labels =  ["0","30", "60", "90", "120", "150", "180","210","240","270","300","330"];
      renderChart(data, labels);
    }else{
     console.log('error')
    }
  };
  xhttp.open("GET", 'http://localhost:5000/api/positions', true);
  xhttp.send();
}

function renderChart(data, labels) {
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                data: data,
		backgroundColor: 'rgba(255,255,255)',
		borderColor : 'rgba(255,255,255)',
		pointBackgroundColor : 'rgba(0,0,0)',
		pointRadius: '5'
            }]
        },
        options: {
    	     animation: {
        	duration: 0
    	     },
	     scale: {
                angleLines: {
                  display: false
             },
             ticks: {
               suggestedMin: 0,
               suggestedMax: 20
             }
         }
	}
    });
}

setInterval(displayData, 1000);
