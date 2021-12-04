let map;

//Initialise the Map.
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    //Set Default Zoom and Location
    zoom: 10,
    center: new google.maps.LatLng(55.953346, -3.188375),
  });

  //Use the Coords.geojson file (output from the scripts)
  map.data.loadGeoJson(
    "./coords.geojson"
  );
  //The size of the PPM Popups
  var infowindow = new google.maps.InfoWindow({
  pixelOffset: new google.maps.Size(0, -40)
});
  //Pop up the PPM when pointers are clicked
  map.data.addListener('click', function(evt) {
  infowindow.setContent(evt.feature.getProperty('PPM'));
  infowindow.setPosition(evt.feature.getGeometry().get());
  infowindow.open(map);
});


}
