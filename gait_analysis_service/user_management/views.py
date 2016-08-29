# coding: utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import random
import string
import simplejson

from django.contrib import auth

from django.contrib.auth.models import User

from gait_analysis_service.user_management.models import Gait_user
from gait_analysis_service.user_management.forms import userLoginoutForm, userModifyForm

from django.template.loader import get_template

def noneIfEmptyString(value):
    if value == "":
        return None
    return value
def noneIfNoKey(dict, key):
    if key in dict:
        value = dict[key]
        if value == "":
            return None
        return value

    return None
class myError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def index(request):
    user_name = request.COOKIES.get('gait_user_name', '')
    user_password = request.COOKIES.get('gait_user_pwd', '')
    template = get_template('homepage/login.html')
    html = template.render({'username': user_name, 'password': user_password}, request)
    return HttpResponse(html)


def register(request):
    try:
        if request.method == "POST":
            user_name = request.POST['user_name']
            user_pwd1 = request.POST['user_pwd1']
            user_pwd2 = request.POST['user_pwd2']
            user_nickname = request.POST['user_nickname']

            user_sex = request.POST['user_sex']
            user_height = request.POST['user_height']
            user_weight = request.POST['user_weight']
            user_birthday = request.POST['year'] + request.POST['month']
            user_email = request.POST['user_email']
            errors = {}

            # FORM VALIDATION
            form = userLoginoutForm(request.POST)
            if not form.is_valid():
                errors = form.errors
                template = get_template('homepage/register.html')
                html = template.render({'errors': errors, 'form': form}, request)
                return HttpResponse(html)
            if user_pwd1 != user_pwd2:
                errors['error_pwd'] = '两次输入的密码不一致！'
                template = get_template('homepage/register.html')
                html = template.render({'errors': errors, 'form': form}, request)
                return HttpResponse(html)

            filterUser = User.objects.filter(username=user_name)
            if len(filterUser) > 0:
                errors['error_username'] = '用户名已存在'
                template = get_template('homepage/register.html')
                html = template.render({'errors': errors, 'form': form}, request)
                return HttpResponse(html)

            user = User()
            user.username = user_name
            user.set_password(user_pwd1)
            user.first_name = user_nickname
            user.email = user_email
            user.save()

            gaituser = Gait_user(user=user, role=1, sex=user_sex, height=user_height, weight=user_weight,
                                 birthday=user_birthday)
            gaituser.save()

            new_user = auth.authenticate(username=user_name, password=user_pwd1)
            if new_user is not None:
                auth.login(request, new_user)
                return HttpResponseRedirect('/analysis/index/')
    except Exception:
        response = HttpResponse()
        response.write("<script>alert('注册失败，请重新注册'),window.location.href='/homepage/register/'</script>")
        return response

    template = get_template('homepage/register.html')
    html = template.render({}, request)
    return HttpResponse(html)


def userRegister_mobile(request):
    try:
        data = simplejson.loads(request.body)

        user_name = data['user']['name']
        user_pwd1 = data['user']['password']
        user_nickname = noneIfNoKey(data['user'], 'real_name')

        user_sex = noneIfNoKey(data['user'], 'sex')
        user_height = noneIfNoKey(data['user'], 'height')
        user_weight = noneIfNoKey(data['user'], 'weight')
        user_birthday = noneIfNoKey(data['user'], 'birthday')
        user_email = noneIfNoKey(data['user'], 'email')

        if user_nickname is None:
            user_nickname = 'user'
        if user_email is None:
            user_email = 'no email'

        user = User()
        user.username = user_name
        user.first_name = user_nickname
        user.set_password(user_pwd1)
        user.email = user_email
        user.save()

        gaituser = Gait_user(user=user, role=1, sex=user_sex, height=user_height, weight=user_weight,
                             birthday=user_birthday)
        gaituser.save()

        result = {
            'successful': True,
            'error': {
                'id': '',
                'message': ''
            }
        }

    except Exception as e:
        result = {
            'successful': False,
            'error': {
                'id': '1024',
                'message': e.args
            }
        }
    finally:
        return HttpResponse(simplejson.dumps(result), content_type="application/json")


def userLogin(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name', '')
        user_password = request.POST.get('user_pwd', '')
        user_remember = request.POST.get('remember_pwd', '')

        try:
            user = auth.authenticate(username=user_name, password=user_password)
            if user and user.is_active:
                auth.login(request, user)
                response = HttpResponseRedirect('/analysis/index/')
                if user_remember == 'user_select':
                    response.set_cookie('gait_user_name', user_name, 60 * 60 * 24 * 7)
                    response.set_cookie('gait_user_pwd', user_password, 60 * 60 * 24 * 7)
                return response
            else:
                response = HttpResponse()
                response.write("<script>alert('登录失败，请重新登录'),window.location.href='/homepage/index/'</script>")
                return response
        except Exception as e:
            print('login error: %s', e)
            response = HttpResponse()
            response.write("<script>alert('登录失败，请重新登录'),window.location.href='/homepage/index/'</script>")
            return response
    else:
        template = get_template('homepage/index.html')
        html = template.render({}, request)
        return HttpResponse(html)


def userLogin_mobile(request):
    try:
        data = simplejson.loads(request.body)
        u_name = data['user']['name']
        u_password = data['user']['password']

        customerUser = auth.authenticate(username=u_name, password=u_password)

        if customerUser:
            customerToken = ''.join(random.sample(string.ascii_letters + string.digits, 30))
            User.objects.filter(username=u_name).update(last_name=customerToken)

            result = {
                'data': {
                    'token': customerToken,
                    'expire': -1
                },
                'successful': True,
                'error': {
                    'id': '',
                    'message': ''
                }
            }
    except Exception as e:
        result = {
            'successful': False,
            'error': {
                'id': '1024',
                'message': e.args
            }
        }
    finally:
        return HttpResponse(simplejson.dumps(result), content_type="application/json")


def userLogout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/homepage/index/')
    # response.delete_cookie('gait_user_name')
    # response.delete_cookie('gait_user_pwd')
    return response


def userLogout_mobile(request):
    try:
        data = simplejson.loads(request.body)
        # 获取用户令牌
        customerToken = data['token']
        token = User.objects.get(last_name=customerToken)
        token.delete()
        result = {
            'successful': True,
            'error': {
                'id': '',
                'message': ''
            }
        }
    except Exception as e:
        result = {
            'successful': False,
            'error': {
                'id': '1024',
                'message': e.args
            }
        }
    finally:
        return HttpResponse(simplejson.dumps(result), content_type="application/json")


def checkUsername(request):
    if request.method == 'GET':
        try:
            user = User.objects.get(username=request.GET['user_name'])
            if user is not None:
                return HttpResponse(simplejson.dumps({'result': 0}))
        except Exception:
            return HttpResponse(simplejson.dumps({'result': 1}))


def modify(request):
    try:
        if request.user.is_authenticated:
            user = request.user
            gaituser = Gait_user.objects.get(user=user)

            user_sex = gaituser.sex

            user_birthday = gaituser.birthday
            year = str(user_birthday)[0:4]
            month = str(user_birthday)[4:]

            result = {}
            result['nickname'] = user.first_name
            result['user_weight'] = gaituser.weight
            result['user_height'] = gaituser.height
            result['email'] = user.email
            result['year'] = year
            result['month'] = month

            template = get_template('homepage/modify.html')
            html = template.render({'result': result, 'sex': simplejson.dumps(user_sex)}, request)
            return HttpResponse(html)
        else:
            response = HttpResponse()
            response.write("<script>alert('请先登录'),window.location.href='/homepage/index/'</script>")
            return response

    except Exception as e:
        response = HttpResponse()
        response.write("<script>alert('请先登录'),window.location.href='/homepage/index/'</script>")
        return response


def queryInformation_mobile(request):
    try:
        data = simplejson.loads(request.body)

        customerUser = User.objects.get(last_name=data['token'])
        gaituser = Gait_user.objects.get(user=customerUser)
        result = {
            'user': {
                "name": customerUser.username,
                "real_name": customerUser.first_name,
                "height": gaituser.height,
                "weight": gaituser.weight,
                "sex": gaituser.sex,
                "birthday": gaituser.birthday,
                "email": customerUser.email
            },
            'successful': True,
            'error': {
                'id': '',
                'message': ''
            }
        }
    except Exception as e:
        result = {
            'successful': False,
            'error': {
                'id': '1024',
                'message': e.args
            }
        }
    finally:
        return HttpResponse(simplejson.dumps(result), content_type="application/json")


def modifyPassword(request):
    if request.user.is_authenticated():
        try:
            if request.method == "POST":
                old_pwd = request.POST['oldpwd']
                new_pwd1 = request.POST['newpwd1']
                new_pwd2 = request.POST['newpwd2']

                response = HttpResponse()
                if not old_pwd:
                    response.write("<script>alert('请输入原始密码！',window.location.href='/homepage/userprofile/')</script>")
                    return response

                if new_pwd1 != new_pwd2:
                    response.write(
                        "<script>alert('两次输入的密码不一致！',window.location.href='/homepage/userprofile/')</script>")
                    return response

                user = auth.authenticate(username=request.user, password=old_pwd)

                if user and user.is_active:
                    user.set_password(new_pwd1)
                    user.save()
                    response.write("<script>alert('修改成功！'),window.location.href='/homepage/index/'</script>")
                    return response
                else:
                    response.write("<script>alert('原始密码错误！'),window.location.href='/homepage/userprofile/'</script>")
                    return response

        except Exception as e:
            print(e)
            response = HttpResponse()
            response.write("<script>alert('修改失败'),window.location.href='/homepage/userprofile/'</script>")
            return response
    else:
        response = HttpResponse()
        response.write("<script>alert('修改失败'),window.location.href='/homepage/userprofile/'</script>")
        return response


def modifyPassword_mobile(request):
    try:
        data = simplejson.loads(request.body)

        user_token = User.objects.get(last_name=data['token'])
        user = auth.authenticate(username=request.user, password=data['user']['old_password'])

        if user and user.is_active and user == user_token:
            user.set_password(data['user']['new_password'])
            user.save()

            result = {
                'successful': True,
                'error': {
                    'id': '',
                    'message': ''
                }
            }
        else:
            raise myError('原密码输入错误！')
    except myError as e:
        result = {
            'successful': False,
            'error': {
                'id': '3',
                'message': e.value
            }
        }
    except Exception as e:
        result = {
            'successful': False,
            'error': {
                'id': '1024',
                'message': e.args
            }
        }
    finally:
        return HttpResponse(simplejson.dumps(result), content_type="application/json")


def modifyInformation(request):
    if request.user.is_authenticated():
        try:
            if request.method == "POST":
                nickname = request.POST['user_nickname']
                user_sex = request.POST['user_sex']
                user_birthday = request.POST['year'] + request.POST['month']
                user_weight = request.POST['user_weight']
                user_height = request.POST['user_height']
                email = request.POST['user_email']

                form = userModifyForm(request.POST)
                if not form.is_valid():
                    print(form.errors)
                    response = HttpResponse()
                    response.write("<script>alert('修改失败'),window.location.href='/homepage/userprofile/'</script>")
                    return response
                else:
                    user = request.user
                    gaituser = Gait_user.objects.get(user=request.user)

                    user.first_name = nickname
                    user.email = email
                    gaituser.weight = user_weight
                    gaituser.height = user_height
                    gaituser.sex = user_sex
                    gaituser.birthday = user_birthday

                    user.save()
                    gaituser.save()

                    response = HttpResponse()
                    response.write("<script>alert('修改成功'),window.location.href='/homepage/userprofile/'</script>")
                    return response

        except Exception as e:
            print(e)
            response = HttpResponse()
            response.write("<script>alert('修改失败'),window.location.href='/homepage/userprofile/'</script>")
            return response

    else:
        response = HttpResponse()
        response.write("<script>alert('请先登录'),window.location.href='/homepage/userprofile/'</script>")
        return response


def modifyInformation_mobile(request):
    try:
        data = simplejson.loads(request.body)
        user = User.objects.get(last_name=data['token'])
        gaituser = Gait_user.objects.get(user=request.user)
        if 'real_name' in data['user']:
            user.first_name = noneIfEmptyString(data['user']['real_name'])
        if 'height' in data['user']:
            gaituser.height = noneIfEmptyString(data['user']['height'])
        if 'weight' in data['user']:
            gaituser.weight = noneIfEmptyString(data['user']['weight'])
        if 'sex' in data['user']:
            gaituser.sex = noneIfEmptyString(data['user']['sex'])
        if 'birthday' in data['user']:
            gaituser.birthday = noneIfEmptyString(data['user']['birthday'])
        if 'email' in data['user']:
            user.email = noneIfEmptyString(data['user']['email'])
        user.save()
        result = {
            'successful': True,
            'error': {
                'id': '',
                'message': ''
            }
        }
    except Exception as e:
        result = {
            'successful': False,
            'error': {
                'id': '1024',
                'message': e.args
            }
        }
    finally:
        return HttpResponse(simplejson.dumps(result), content_type="application/json")
