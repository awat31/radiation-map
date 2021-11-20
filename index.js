// Initialize and add the map
function initMap(data) {
  // The location of Uluru
  //var latitude = document.getElementById("latitude");
  //var longitude = div.textContent;
  //var latitude = document.getElementById("longitude");
  //var longitude = div.textContent;
  //var latitude = data.latitude
  //var longitude = data.longitude
  const uluru = { lat: data.latitude, lng: data.longitude };
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
