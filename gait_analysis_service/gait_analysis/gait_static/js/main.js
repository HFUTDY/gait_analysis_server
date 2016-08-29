$(document).ready(function() {
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

    var result;
    change_time(0);

});


function w_summary(req){
    var list = {};
    list['运动时间'] = [req.duration, '分', 'g', 'Duration'];
    list['能量消耗'] = [req.calorie, '卡', 'o', 'Energy'];
    list['步数'] = [req.steps, '步', 'b', 'Steps'];

    var $wrapper = $('.w_summary');
    $("#g").remove();
    $("#o").remove();
    $("#b").remove();
    for(var tmp in list){
        var value = '<div class="item '+list[tmp][2]+'" id="'+list[tmp][2]+'">' +
                        '<div class="inner">' +
                            '<div class="ico">' +
                                '<b class="icon icon_smy_time"></b>' +
                            '</div>' +
                            '<div class="name">' +
                                tmp +
                                '<div class="s">' +
                                list[tmp][3] +
                            '</div></div>' +
                            '<div class="all">' +
                                list[tmp][0] +
                                '<span class="unit">' +
                                list[tmp][1] +
                                '</span>' +
                            '</div>' +
                        '</div>' +
                    '</div>';
        $wrapper.append(value);
    };
};


function graph(req, i){
    var li = ['#s_li', '#e_li', '#d_li'];
    for(var j=0;j<3;j++){
        if(j==i){
            $(li[j]).addClass("active");
        }
        else{
            $(li[j]).removeClass("active");
        }
    }
    var choice = [
        ['Steps', req.stepsList, '步'],
        ['Energy', req.calorieList, '卡'],
        ['Duration', req.durationList, '分']
    ];
    var chart = {
        type: 'column'
    };

    var title = {
        text: choice[i][0]
    };

    var xAxis = {
        categories: req.categoriesList
    };
    var yAxis = {
        min: 0,
        title: {
            text: choice[i][2],
            rotation: 0,
        }
    };
    var plotOptions = {
        series: {
            events: {
                click: function(event) {
                    var date= event.point.category;
                    var myForm = document.createElement("form");
                    myForm.action = "/analysis/detail/";
                    myForm.method = "POST";
                    var dateInput = document.createElement("input");
                    dateInput.setAttribute("name", "date");
                    dateInput.setAttribute("value", date);
                    myForm.appendChild(dateInput);
                    document.body.appendChild(myForm);
                    myForm.submit();
                    document.body.removeChild(myForm);
                },
                legendItemClick: function(event) {
                    return false;
                }

            }
        }
    };
    var tooltip = {
        shared: true,
        useHTML: true,
        headerFormat: '<b>开始时间:{point.key}<br>结束时间:{point.key}</b><table>',
        pointFormat: '<tr><td><b>{series.name}: <b></td><td><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        valueDecimals: 2
    };
    var series =  [{
        name: 'steps',
        data: choice[i][1]
    }];

    var json = {};

    json.chart = chart;
    json.title = title;
    json.tooltip = tooltip;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.plotOptions = plotOptions;
    json.series = series;

    $('#graph_step').highcharts(json);
};


function change_li(i){
    graph(result.graph, i);
};


function time_query(){
    var $st = $("#starttime").val();
    var $et = $("#endtime").val();
    if(!$st){
        alert('选择开始时间');}
    else if(!$et){
        alert('选择结束时间');}
    else{
        var start_time = Date.parse(new Date($st));
        var end_time = Date.parse(new Date($et));
        $.getJSON('/analysis/main_query/',
            {'start_time': start_time, 'end_time': end_time},
            function(data){
                result = data;
                w_summary(data.w_summary);
                graph(data.graph, 0);
        });
    }
};


function change_time(i){
    var time = ['#time0', '#time1', '#time2', '#time3'];
    for(var j=0;j<4;j++){
        if(j==i){
            $(time[j]).addClass("active");
        }
        else{
            $(time[j]).removeClass("active");
        }
    }
    var myDate=new Date();
    switch(i)
    {
    case 0:
        var start_time = new Date(myDate.getFullYear(), myDate.getMonth(), myDate.getDate()-7).getTime();
        break;
    case 1:
        var start_time = new Date(myDate.getFullYear(), myDate.getMonth()-1, myDate.getDate()).getTime();
        break;
    case 2:
        var start_time = new Date(myDate.getFullYear(), myDate.getMonth()-3, myDate.getDate()).getTime();
        break;
    case 3:
        var start_time = new Date(myDate.getFullYear(), myDate.getMonth()-6, myDate.getDate()).getTime();
        break;
    default:
        alert("非法的时间选择")
    }
    $.getJSON('/analysis/main_query/',
        {start_time: start_time, end_time: myDate.getTime()},
        function(data){
            result = data;
            w_summary(data.w_summary);
            graph(data.graph, 0);
    });
};