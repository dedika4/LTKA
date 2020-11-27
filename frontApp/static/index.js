
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     // document.getElementById("jarak").innerHTML = this.responseText;
    alert("Berhasil");
    }
  };
  xhttp.open("GET", 'http://localhost:5000/api/positions', true);
  xhttp.send();
