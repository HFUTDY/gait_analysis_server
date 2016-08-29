$(document).ready(function() {
    (function() {
        $('#starttime').datepicker({
            onSelect: function(date) {
                $('#starttime').parent().find('.value').text(date);
                $('#timeform').submit();
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
    init_record();

});

function add_record(result){
    var month = "";
    for(var i=0;i<result.length;i++){
        var start_time = result[i].start_time;
        var newDate = new Date(start_time);
        var this_month = newDate.getMonth()+1;
        if(this_month != month){
            var $p_record = $("#p_record");
            var p_record = document.getElementById("p_record");
            var w_navi =  '<div class="w_navi">' +
                              '<b class="flag"></b>' +
                              '<div class="ico">' +
                                  '<b class="icon icon_calendar"></b>' +
                              '</div>' +
                              '<div class="date">' +
                                  newDate.getFullYear()+"年"+(newDate.getMonth()+1)+"月" +
                              '</div>' +
                          '</div>';
            $p_record.append(w_navi);
            var ul = document.createElement("ul");
            ul.className = "list";
            month = this_month;
        }
        var li = document.createElement("li");
        if(i%2==0){
            li.className = "odd";
        }

        var t_div = document.createElement("div");
        t_div.className = "time";
        t_div.appendChild(document.createTextNode(newDate.toLocaleString().replace("/", "年").replace("/", "月").replace(" ", "日 ")));
        var date = start_time;
        t_div.onclick=function(){
            var myForm = document.createElement("form");
            myForm.action = "/analysis/detail/";
            myForm.method = "POST";
            var dateInput = document.createElement("input");
            dateInput.setAttribute("name", "date");
            dateInput.setAttribute("value", date);
            myForm.appendChild(dateInput);
            document.body.appendChild(myForm);
            myForm.submit();
        }
        li.appendChild(t_div);

        var s_div = document.createElement("div");
        s_div.className = "summary";

        var grid = [["grid g", "icon icon_time",
        [[parseInt(result[i].duration/3600), "H"], [parseInt(result[i].duration/60-parseInt(result[i].duration/3600)*60), "M"]]],
        ["grid o", "icon icon_grd", [[result[i].calorie, "Cal"]]], ["grid b", "icon icon_step", [[result[i].steps, "S"]]]];
        for(var j=0;j<3;j++){
            var grid_div = document.createElement("div");
            grid_div.className = grid[j][0];

            var ico_div = document.createElement("div");
            ico_div.className = "ico";

            var ico_b = document.createElement("b");
            ico_b.className = grid[j][1];
            ico_div.appendChild(ico_b);

            grid_div.appendChild(ico_div);
            for(var z=0;z<grid[j][2].length;z++){
                var all_span = document.createElement("span");
                all_span.className = "all";
                all_span.appendChild(document.createTextNode(grid[j][2][z][0]));
                grid_div.appendChild(all_span);
                grid_div.appendChild(document.createTextNode(grid[j][2][z][1]));
            };

            s_div.appendChild(grid_div);
        }

        li.appendChild(s_div);
        ul.appendChild(li);
    p_record.appendChild(ul);
    }
};


function choice(){
    $(".w_navi").remove();
    $(".list").remove();
    var $st = $("#starttime").val();
    var $et = $("#endtime").val();
    if(!$st){
        alert('选择开始时间');}
    else if(!$et){
        alert('选择结束时间');}
    else{
        var start_time = Date.parse(new Date($st));
        var end_time = Date.parse(new Date($et));
        $.getJSON('/analysis/record_query/',
            {'start_time': start_time, 'end_time': end_time},
            function(data){
                add_record(data);
        });
    }
};


function init_record(){
    $(".w_navi").remove();
    $(".list").remove();
    var myDate = new Date();
    var s_time = Date.parse(new Date(myDate.getFullYear(), myDate.getMonth()-2, 1));
    var e_time = Date.parse(new Date(myDate.getFullYear(), myDate.getMonth()+1, 1));
    $.getJSON('/analysis/record_query/',
        {'start_time': s_time, 'end_time': e_time},
        function(data){
            add_record(data);
    });
};

