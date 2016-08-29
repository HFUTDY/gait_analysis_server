# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# user role
class User_role(models.Model):
    role = models.SmallIntegerField(default=1)
    role_name = models.CharField(max_length=30, default='普通用户', verbose_name='用户角色')

    class Meta:
        verbose_name = '角色表'
        verbose_name_plural = '角色表'

    def __unicode__(self):
        return self.name


class User_role_admin(admin.ModelAdmin):
    list_display = ('role', 'role_name')


# user information
role_choice = (('1', '普通用户'), ('2', '管理员'))
sex_choice = (('M', '男'), ('F', '女'))  # 1-M，2-F


class Gait_user(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name='用户')
    role = models.CharField(max_length=1, choices=role_choice, verbose_name='用户角色')
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, verbose_name='体重')
    height = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, verbose_name='身高')
    sex = models.CharField(max_length=2, choices=sex_choice, verbose_name='性别', null=True, default='M')
    birthday = models.IntegerField(null=True, blank=True, verbose_name='出生年份')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = '用户信息表'


class Gait_user_admin(admin.ModelAdmin):
    fields = ('user', 'role', 'weight', 'height', 'sex', 'birthday',)


# user token
class Token(models.Model):
    user = models.OneToOneField(User)  # one-to-one
    token = models.CharField('token', max_length=50, unique=True, db_index=True)
    expire = models.BigIntegerField('expire')

    class Meta:
        verbose_name = '用户令牌'
        verbose_name_plural = '用户令牌'

    def __unicode__(self):
        return self.token


admin.site.register(User_role, User_role_admin)
admin.site.register(Gait_user)
admin.site.register(Token)
