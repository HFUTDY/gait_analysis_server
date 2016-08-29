(function() {
    $('#starttime').datepicker({
        onSelect: function(date) {
            $('#starttime').parent().find('.value').text(date);
        },
        dateFormat: 'yy-mm-dd'
    });

    $('#endtime').datepicker({
        onSelect: function(date) {
            $('#endtime').parent().find('.value').text(date);
        },
        dateFormat: 'yy-mm-dd'
    });
})();

(function() {
    var chart = document.getElementById('chart');
    var line = new Chart(chart, {
        type: 'line',
        data: {
            labels: [
                '16.07.19',
                '16.07.20',
                '16.07.21',
                '16.07.22',
                '16.07.23',
                '16.07.24',
                '16.07.25',
                '16.07.26',
                '16.07.27'
            ],
            datasets: [{
                data: [
                    18,
                    14,
                    13,
                    19,
                    15,
                    17,
                    26,
                    20,
                    24
                ],
                backgroundColor: '#bcefec',
                borderColor: '#22cbc1',
                borderWidth: 2
            }]
        },
        options: {
            maintainAspectRatio: false,
            legend: {
                display: false
            },
            gridLines: {
                offsetGridLines: false
            },
            scales: {
                yAxes: [{
                    display: false
                }],
                xAxes: [{
                    gridLines: {
                        // drawBorder: false,
                        // offsetGridLines: true,
                        drawTicks: false,
                        tickMarkLength: 2
                    },
                    ticks: {
                        maxRotation: 10,
                        // mirror: true
                        // padding: 100
                        callback: function(value, key, list) {
                            if(key == 0) {
                                return '';
                            } else if(key == (list.length - 1)){
                                return '';
                            } else {
                                return value;
                            }
                        }
                    },
                    scaleLabel: {
                        display: false
                    }
                }]
            },
            hover: {
                mode: 'label'
            }
        }
    });
})();