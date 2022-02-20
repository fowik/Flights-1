document.getElementById("showHide").onclick = function() {
    var theDiv = document.getElementById("popUpInfo");
    if(theDiv.style.display == 'none') {
        theDiv.style.display = 'block';
    } 
    else {
        theDiv.style.display = 'none';
    }
}

$('#findtext').click(function() {
    window.location.href = '/some/new/page';
    return false;
});

function est() {
  document.getElementById("popUp").style.display = "block";
}

function net() {
  document.getElementById("popUp").style.display = "none";
}

function rege() {
  document.getElementById("loge").style.left = "-400px";
  document.getElementById("rege").style.left = "50px";
  document.getElementById("btnn").style.left = "100px";
}

function loge() {
  document.getElementById("loge").style.left = "50px";
  document.getElementById("rege").style.left = "450px";
  document.getElementById("btnn").style.left = "0px";
}

