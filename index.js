// Initialize and add the map
function initMap() {
  // The location of Uluru
  var latitude = 00314.1097
  var longitude = 5556.1356
  const uluru = { lat: latitude, lng: latitude };
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
initMap();
