let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10,
    center: new google.maps.LatLng(55.953346, -3.188375),
    mapTypeId: "terrain",
  });

  map.data.loadGeoJson(
    "./coords.geojson"
  );

  map.data.addListener('mouseover', function(evt) {
  infowindow.setContent(evt.feature.getProperty('PPM'));
  infowindow.setPosition(evt.feature.getGeometry().get());
  infowindow.open(map);
});

}
