param


$.ajax({
    type: "POST",
    contentType: 'application/json',
    url: "/data/acceleration/query/pages",
    cache : false,  //禁用缓存
    data: JSON.stringify(param),    //传入已封装的参数
    dataType: "json",
    success: function(result) {
            //异常判断与处理
            if ( !result || !result.successful ) {
                alert('获取数据失败');
                return;
            }
            else{
            //封装返回数据，这里仅演示了修改属性名
            returnData.draw = data.draw;//这里直接自行返回了draw计数器,应该由后台返回
            returnData.recordsTotal = total;
            returnData.recordsFiltered = total;//后台不实现过滤功能，每次查询均视作全部结果
            returnData.data = result.data.accelerations;
            //关闭遮罩
            $wrapper.spinModal(false);
            //调用DataTables提供的callback方法，代表数据已封装完成并传回DataTables进行渲染
            //此时的数据需确保正确无误，异常判断应在执行此回调前自行处理完毕
            callback(returnData);
        }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
        alert("查询失败");
        //$wrapper.spinModal(false);
    }
});