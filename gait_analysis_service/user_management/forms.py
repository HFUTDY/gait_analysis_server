#coding:utf-8

from django import forms


class userLoginoutForm(forms.Form):
    user_name = forms.CharField()
    user_nickname = forms.CharField()
    user_pwd1 = forms.PasswordInput()
    user_pwd2 = forms.PasswordInput()
    user_sex = forms.BooleanField()
    user_weight = forms.IntegerField()
    user_height = forms.IntegerField()
    year = forms.IntegerField()
    month = forms.IntegerField()
    user_email = forms.EmailField(required=False)


class userModifyForm(forms.Form):
    user_nickname = forms.CharField()
    user_sex = forms.BooleanField()
    user_weight = forms.IntegerField()
    user_height = forms.IntegerField()
    year = forms.IntegerField()
    month = forms.IntegerField()
    user_email = forms.EmailField(required=False)
