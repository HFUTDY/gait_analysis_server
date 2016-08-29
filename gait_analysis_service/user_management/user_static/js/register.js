/*
autho:Eric
date:2013.5.23
purpose: form validation for register
*/


window.onload=function(){
var date = new Date();

for(var i=1980; i<date.getFullYear()+1; i++){
    document.getElementById("year").options.add(new Option(i, i));
};


for(var i=1;i<13;i++){
    document.getElementById("month").options.add(new Option(i, i));
};
};

function checkUsername(){
    $.getJSON('/homepage/checkusername', {user_name:$('#user_name').val()}, function(data){
    if (data.result==1){$("#error").attr("class", "icon icon_pass");}
    else{ $("#error").attr("class", "icon icon_warning");}
    })
};

function check(){
    var name=document.getElementById("user_name");
    var nickname=document.getElementById("user_nickname");
    var pwd1=document.getElementById("user_pwd1");
    var pwd2=document.getElementById("user_pwd2");
    var email=document.getElementById("user_email");

    var re= /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/; //email validation
    /* /^(1[0-9]{10})$/ */
    var patt=new RegExp(re);

    if(name.value.length < 1){
        alert('用户名不能为空');
        document.getElementById("user_name").value='';
        document.getElementById("user_name").focus();
        return false;
    };

    if(name.value.length > 30){
        alert('用户名长度不能超过30');
        document.getElementById("user_name").value='';
        document.getElementById("user_name").focus();
        return false;
    };

    if(nickname.value.trim()=='' || nickname.value==null){
        alert('昵称不能为空');
        document.getElementById("user_nickname").focus();
        return false;
    };

    if(nickname.value.length > 30){
        alert('昵称不能超过30');
        document.getElementById("user_nickname").focus();
        return false;
    };

    if(pwd1.value.length<5){
        alert('密码长度不能小于5');
        document.getElementById("user_pwd1").value='';
        document.getElementById("user_pwd2").value='';
        document.getElementById("user_pwd1").focus();
        return false;
    };

    if(pwd1.value != pwd2.value){
        alert('密码不一致');
        document.getElementById("user_pwd1").value='';
        document.getElementById("user_pwd2").value='';
        document.getElementById("user_pwd1").focus();
        return false;
    };

    if(!patt.test(email.value)){
        alert('请输入正确的邮箱名');
        document.getElementById("user_email").value='';
        document.getElementById("user_email").focus();
        return false;
    };
    return true;
};

function checkPWD(){
    var pwd1=document.getElementById("user_pwd1");
    var pwd2=document.getElementById("user_pwd2");
    if(pwd1.value!=pwd2.value){ $("#pwd_error").attr("class", "icon icon_warning");}
    else{$("#pwd_error").attr("class", "icon icon_pass");}
};
