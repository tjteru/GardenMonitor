<?php

DEFINE('ROOT', '../');

$http_origin = $_SERVER['HTTP_ORIGIN'];

// Allow access from several domains
if ($http_origin == "http://tribeawesome.com" || $http_origin == "http://awesomeiswhatwetotallyare.com") {
    header('Access-Control-Allow-Origin: ' . $http_origin);
}

header("Content-type: text/javascript");

// Set these to your username and password
$con = mysql_connect("localhost", "username", "password");

// and set this to your database
mysql_select_db("Database");

if (!$con) {
    log_error("Mysql Error: " . mysql_error());
    die();
}

$status = array();

$status['status'] = 'successful';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $startTime = mysql_real_escape_string($_POST['startTime']);
    $dataSet = mysql_real_escape_string($_POST['dataSet']);
} else {
    $startTime = mysql_real_escape_string($_GET['startTime']);
    $dataSet = mysql_real_escape_string($_GET['dataSet']);
}


$query = "SELECT UNIX_TIMESTAMP(time), s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12 FROM aerodata WHERE created > FROM_UNIXTIME(" . $startTime . ")";

$result = mysql_query($query);
if (!$result) {
    //echo mysql_error(); //log_error("Mysql Error: " . mysql_error());
    $status['status'] = 'error ' . $query;
}

$status['data'] = Array();
if (mysql_num_rows($result)) {
    $row = mysql_fetch_assoc($result);
    while ($row = mysql_fetch_row($result)) {
        //  cast results to specific data types
        foreach ($row as &$value) {
            $value = floatval($value);
        }
        $test_data[] = [$row[0], $row[$dataSet + 1]];
    }
    $status['data'] = $test_data;
}

echo json_encode($status);
?>
