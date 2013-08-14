<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Garden Data</title>

        <script type="text/javascript" src="js/jquery.min.js"></script>
        <script type="text/javascript" src="graph.js"></script>
    </head>
    <body>
        <script src="js/highstock.js"></script>
        <script src="js/modules/exporting.js"></script>

        <div id="container" style="<?php 
        
        echo htmlspecialchars(
                isset($_GET['height']) ? "height: " . ($_GET['height']-17) . "px; " : "height: 500px;"
            );
        
        echo htmlspecialchars(
                isset($_GET['width']) ? "width: " . $_GET['width'] . "px; " : "min-width: 500px;"
            );
        
        
        ?>"></div>
    </body>
</html>

