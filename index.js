// Initialize and add the map
function initMap() {
  // The location of Uluru
  //var div = document.getElementById("latitude");
  //var latitude = div.textContent;
  const uluru = { lat: -12.543, lng: 131.036 };
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
