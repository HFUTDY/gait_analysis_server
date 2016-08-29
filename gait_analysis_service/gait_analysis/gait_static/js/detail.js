window.onload=function(){
    w_summary(result.w_summary);
    track(result.track);
    graph(result.graph);
};

function w_summary(req){
    $(".item").remove();
    var list = {};
    list['步数'] = [req.steps, '步'];
    list['速度'] = [req.v, '米/秒'];
    list['最大速度'] = [req.max_v, '米/秒'];
    list['行走距离'] = [req.s, '米'];
    list['左步长'] = [req.sl, '米'];
    list['右步长'] = [req.sr, '米'];
    list['支撑期时间'] = [req.stance_time, '秒'];
    list['摆动期时间'] = [req.swing_time, '秒'];
    list['步频'] = [req.cadence, '步/分钟'];
    list['加速次数'] = [req.a_time, ''];
    list['减速次数'] = [req.d_time, ''];
    list['双腿支撑时间'] = [req.d_s_time, '秒'];
    list['能量消耗'] = [req.calorie, '卡'];

    var $wrapper = $('.w_summary');
    for(var tmp in list){
        var test = '<div class="item g">' +
                        '<div class="inner">' +
                            '<div class="ico">' +
                                '<b class="icon icon_smy_time"></b>' +
                            '</div>' +
                            '<div class="name">' +
                                tmp +
                            '</div>' +
                            '<div class="all">' +
                                list[tmp][0] +
                                '<span class="unit">' +
                                list[tmp][1] +
                                '</span>' +
                            '</div>' +
                        '</div>' +
                    '</div>';
        $wrapper.append(test);
    };
};


function track(req){
    var xAxis = {
        labels:{
            enable: false
        },
        lineWidth: 0,
        categories: req.x,
        tickWidth: 0
    };
    var series = [{
        itemStyle : {
            normal : {
                lineStyle:{
                    color:'black'
                }
            }
        },
        data: req.y
    }];
    var chart = {
        type: 'line',
        height: 200
    };
    var title = {
        text: '轨迹'
    };

    var yAxis = {
        gridLineColor: '#FFFFFF',
        title: {
            text: 'value'
        },
        plotLines:[{
            color: '#EEEE00',
            dashStyle: 'solid',
            value: 0,
            width: 2
        }]
    };
    var credits = {
        enabled: false
    };
    var plotOptions = {
        series: {
            marker: {
                enabled: false
            },
            events: {
                legendItemClick: function (event) {
                    return false;
                }
            }
        }
    };


    var json = {};

    json.chart = chart;
    json.title = title;
    json.credits = credits;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.plotOptions = plotOptions;
    json.series = series;

    $('#track').highcharts(json);
};


function graph(req){
    var choice = [
        ['Left Foot Pressure', 'l_pressure', ['a', 'b', 'c', 'd'], '#l_pressure_graph'],
        ['Right Foot Pressure', 'r_pressure', ['a', 'b', 'c', 'd'], '#r_pressure_graph'],
        ['Left Foot Acceleration', 'l_acceleration', ['x', 'y', 'z'], '#l_acceleration_graph'],
        ['Right Foot Acceleration', 'r_acceleration', ['x', 'y', 'z'], '#r_acceleration_graph'],
        ['Left Foot Gyroscope', 'l_gyroscope', ['x', 'y', 'z'], '#l_gyroscope_graph'],
        ['Right Foot Gyroscope', 'r_gyroscope', ['x', 'y', 'z'], '#r_gyroscope_graph'],

    ];
    for(var i=0;i<6;i++){
        var series = [];
        for(var j=0;j<choice[i][2].length;j++){
            var str = {'name': choice[i][2][j], 'data': req[choice[i][1]][choice[i][2][j]]};
            series.push(str);
        };
        var chart = {
            type: 'line',
            zoomType: 'xy',
            height: 400
        };

        var title = {
            'text': choice[i][0]
        };

        var xAxis = {
            scrollbar: {
                enabled: true
            },
            categories: req.categories,
            tickmarkPlacement: 'on',
            plotLines:[]
        };
        for(var z=0;z<req.plotLines.length;z++){
            xAxis.plotLines.push({
                color: 'red',
                dashStyle: 'dot',
                value: req.plotLines[z],
                width: 1
            });
        };
        var yAxis = {
            title: {
                text: 'value'
            }
        };
        var credits = {
            enabled: false
        };
        var plotOptions = {
            series: {
                marker: {
                    radius: 3
                },
                events: {
                    click: function(event) {
                        if(this.chart.title.textStr[0] == 'L'){
                            var insole = 'l_pressure';
                        }
                        else{
                            var insole = 'r_pressure';
                        };
                        var position = [
                            ["#l_a", "#l_b", "#l_c", "#l_d"],
                            ["#r_a", "#r_b", "#r_c", "#r_d"]
                        ];

                        for(var i=0;i<2;i++){
                            for(var j=0;j<4;j++){
                                if(req[insole][choice[i][2][j]][event.point.x]>3){
                                    P_display(position[i][j]);
                                };
                            };
                        };
                    },
                    mouseOut: function(){
                        $('.footprint .active').removeClass('active');
                    },
                    legendItemClick: function (event) {
                        return false;
                    }
                }
            }
        };

        var json = {};

        json.chart = chart;
        json.title = title;
        json.credits = credits;
        json.xAxis = xAxis;
        json.yAxis = yAxis;
        json.plotOptions = plotOptions;
        json.series = series;
        $(choice[i][3]).highcharts(json);
    };
};


function P_display(position){
    $(position).addClass('active');
};