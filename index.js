// Initialize and add the map
function initMap() {
  // The location of Uluru
  latitude = document.currentScript.getAttribute('latitude');
  longitude = document.currentScript.getAttribute('longitude');

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
