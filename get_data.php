<?php
  // The global $_POST variable allows you to access the data sent with the POST method by name
  // To access the data sent with the GET method, you can use $_GET
$data = htmlspecialchars($_POST['data']);
$latitude = htmlspecialchars($_POST['latitude']);
$longitude = htmlspecialchars($_POST['longitude']);

echo htmlspecialchars($latitude);
echo htmlspecialchars($longitude);

?>
