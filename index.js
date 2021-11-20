// Initialize and add the map
function initMap(longitude, latitude) {

  // The location of Uluru
  //var latitude = document.getElementById("latitude");
  //var longitude = div.textContent;
  //var latitude = document.getElementById("longitude");
  //var longitude = div.textContent;
  var latitude = 0.00
  var longitude = 0.00 
  const uluru = { lat: latitude, lng: longitude };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: uluru,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}

setInterval(initMap, 60000);
initMap(longitude, latitude);
