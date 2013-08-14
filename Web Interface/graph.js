
var updateInterval = 10;
var numSensors = 2;

var seriesOptions = [{
        name: 'Ebb and Flow Water Level',
        data: (function() {
            // generate an array of random data
            var data = [];
            var startTime = ((new Date()).getTime()) / 1000 - (60 * 60 * 24 * 7);


            newData = getNewData(startTime, 0); // get data from 5 sec ago to current time

            for (var i = 0; i < newData.length; i++) {
                data.push([
                    newData[i][0] * 1000,
                    newData[i][1]
                ]);
            }
            return data;
        })()
    }, {
        name: 'Aeroponics Moisture',
        data: (function() {
            // generate an array of random data
            var data = [];
            var startTime = ((new Date()).getTime()) / 1000 - (60 * 60 * 24 * 7);


            newData = getNewData(startTime, 1); // get data from 5 sec ago to current time

            for (var i = 0; i < newData.length; i++) {
                data.push([
                    newData[i][0] * 1000,
                    newData[i][1]
                ]);
            }
            return data;
        })()
    }, ];



function getNewData(time, sensor) {

    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    }
    else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.open("POST", "http://casacraft.homeip.net:8080/aero/getdata.php", false);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("startTime=" + time + "&dataSet=" + sensor);

    if (xmlhttp.status == 200) {
        try {

            response = JSON.parse(xmlhttp.responseText);
            if (response['status'] == 'successful' && response['data'] != null) {
                if (response['data'].length > 0) {
                    var data = response['data'];
                    var chartData = [];
                    for (var i = 0; i < data.length; i++) {
                        chartData.push([parseFloat(data[i][0]), parseFloat(data[i][1])]);
                    }
                }
                return chartData;

            }

            if (response['debug']) {
                alert("Debug: " + response['debug']);
            }

            if (response['error']) {
                alert("Error: " + response['error']);
            }
        }


        catch (error) {
            alert("An error occured: " + error);
            log_error(error);
        }
    }


    return [];
}

$(function() {

    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    // Create the chart
    $('#container').highcharts('StockChart', {
        chart: {
            type: 'spline',
            events: {
                load: function() {

                    // set up the updating of the chart each second
                    series = this.series;
                    setInterval(function() {
                        var time = ((new Date()).getTime()) / 1000 - updateInterval;
                        var data;

                        data = getNewData(time, 0); // get data from 5 sec ago to current time
                        for (var i = 0; i < data.length; i++) {
                            series[0].addPoint([data[i][0] * 1000, data[i][1]], true, false, true);
                        }

                        data = getNewData(time, 1); // get data from 5 sec ago to current time
                        for (var i = 0; i < data.length; i++) {
                            series[1].addPoint([data[i][0] * 1000, data[i][1]], true, false, true);
                        }

                    }, updateInterval * 1000);
                }
            }
        },
        rangeSelector: {
            buttons: [{
                    count: 5,
                    type: 'minute',
                    text: '5M'
                }, {
                    count: 30,
                    type: 'minute',
                    text: '30M'
                }, {
                    count: 6,
                    type: 'hour',
                    text: '6H'
                }, {
                    count: 1,
                    type: 'day',
                    text: '1D'
                }, {
                    type: 'all',
                    text: 'All'
                }],
            inputEnabled: false,
            selected: 1
        },
        title: {
            text: 'Live Data'
        },
        exporting: {
            enabled: true
        },
        series: seriesOptions,
        yAxis: [{min: 0, max: 5.01}]
    });

});

