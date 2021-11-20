// Initialize and add the map
function initMap() {
  // The location of Uluru
  //var latitude = document.getElementById("latitude");
  //var longitude = div.textContent;
  //var latitude = document.getElementById("longitude");
  //var longitude = div.textContent;
  const uluru = { lat: 0.00, lng: 0.00 };
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
