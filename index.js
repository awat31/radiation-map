// Initialize and add the map
function initMap(latitude, longitude) {

  // The location of Uluru
  //var div = document.getElementById("latitude");
  //var latitude = div.textContent;
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
initMap(latitude, longitude);
