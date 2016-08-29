
window.onload=function(){
    var date = new Date();

    for(var i=1980; i<date.getFullYear()+1; i++){
        document.getElementById("year").options.add(new Option(i, i));
    };

    for(var i=1;i<13;i++){
        document.getElementById("month").options.add(new Option(i, i));
    };
    document.getElementById("year")[year].selected = true;
    document.getElementById("month")[month].selected = true;
};

function checkUsername(){
    $.getJSON('/homepage/checkusername', {user_name:$('#user_name').val()}, function(data){
    if (data.result==1){$("#error").attr("class", "icon icon_pass");}
    else{ $("#error").attr("class", "icon icon_warning");}
    })
};

function checkPWD(){
    var pwd0=document.getElementById("oldpwd");
    var pwd1=document.getElementById("newpwd1");
    var pwd2=document.getElementById("newpwd2");

    if(!pwd0.value){
        $("#pwd_error1").attr("class", "icon icon_warning");
        return false;
    }
    else{
        $("#pwd_error1").attr("class", "");
    }
    if(pwd2.value && pwd1.value==pwd2.value){
        $("#pwd_error2").attr("class", "icon icon_pass");
        if(pwd1.value.length<5){
            alert('密码长度不能小于5');
            document.getElementById("newpwd1").value='';
            document.getElementById("newpwd2").value='';
            document.getElementById("newpwd1").focus();
            return false;
        }
        return true;
    }
    else{
        $("#pwd_error2").attr("class", "icon icon_warning");
        return false;
    }

};

function modify_check(){
    var nickname=document.getElementById("user_nickname");
    var weight=document.getElementById("user_weight");
    var height=document.getElementById("user_height");
    var email=document.getElementById("user_email");

    var re= /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/; //email validation
    /* /^(1[0-9]{10})$/ */
    var patt=new RegExp(re);

    if(nickname.value.trim()=='' || nickname.value==null){
        alert('昵称不能为空');
        document.getElementById("user_nickname").focus();
        return false;
    };

    if(nickname.value.length > 30){
        alert('昵称长度不能超过30');
        document.getElementById("user_nickname").focus();
        return false;
    };

    if(!patt.test(email.value)){
        alert('请输入正确的邮箱名');
        document.getElementById("user_email").value='';
        document.getElementById("user_email").focus();
        return false;
    };

    var re_weight = /^[1-9]\d{0,2}(\.[0-9])?$/;
    var patt_weight = new RegExp(re_weight)

    var re_height = /^[1-9]\d{0,2}(\.[0-9])?$/;
    var patt_height = new RegExp(re_height)

    if(!patt_weight.test(weight.value)){
        alert('请输入合适的体重');
        document.getElementById("user_weight").value='';
        document.getElementById("user_weight").focus();
        return false;
    };

    if(!patt_height.test(height.value)){
        alert('请输入合适的身高');
        document.getElementById("user_height").value='';
        document.getElementById("user_height").focus();
        return false;
    };

    return true;
};
