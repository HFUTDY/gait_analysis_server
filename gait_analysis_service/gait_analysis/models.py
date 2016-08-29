# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from gait_analysis_service.user_management.models import Gait_user

# Index
class Sta_index(models.Model):
    sta_index = models.AutoField('sta_index', primary_key=True)
    user_id = models.ForeignKey(User)
    device_id = models.CharField('device_id', max_length=30)


class Sta_index_admin(admin.ModelAdmin):
    list_display = ('sta_index', 'user_id', 'device_id')


# Acceleration Information
class Acceleration_l_foot(models.Model):
    user = models.ForeignKey(User)    # one-to-one
    device_id = models.CharField('device_id', max_length=30)
    index_id = models.IntegerField('index_id', db_index=True)   # index to Statistics table
    timestamp = models.BigIntegerField('timestamp')
    acc_l_x = models.SmallIntegerField('acc_l_x')
    acc_l_y = models.SmallIntegerField('acc_l_y')
    acc_l_z = models.SmallIntegerField('acc_l_z')

    class Meta:
        verbose_name = '左加速度'
        verbose_name_plural = '左加速度'


class Acceleration_l_foot_admin(admin.ModelAdmin):
    list_display = ('device_id', 'index_id', 'timestamp', 'acc_l_x', 'acc_l_y', 'acc_l_z')


class Acceleration_r_foot(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')    # one-to-one
    device_id = models.CharField('device_id', max_length=30)
    index_id = models.IntegerField('index_id', db_index=True)   # index to Statistics table
    timestamp = models.BigIntegerField('timestamp')
    acc_r_x = models.SmallIntegerField('acc_r_x')
    acc_r_y = models.SmallIntegerField('acc_r_y')
    acc_r_z = models.SmallIntegerField('acc_r_z')

    class Meta:
        verbose_name = '右加速度'
        verbose_name_plural = '右加速度'


class Acceleration_r_foot_admin(admin.ModelAdmin):
    list_display = ('device_id', 'index_id', 'timestamp', 'acc_r_x', 'acc_r_y', 'acc_r_z')


# Gyroscope Information
class Gyroscope_l_foot(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')  # one-to-one
    device_id = models.CharField('device_id', max_length=30)
    index_id = models.IntegerField('index_id', db_index=True)
    timestamp = models.BigIntegerField('timestamp')
    gyro_l_x = models.SmallIntegerField('gyro_l_x')
    gyro_l_y = models.SmallIntegerField('gyro_l_y')
    gyro_l_z = models.SmallIntegerField('gyro_l_z')

    class Meta:
        verbose_name = '左角速度'
        verbose_name_plural = '左角速度'


class Gyroscope_l_foot_admin(admin.ModelAdmin):
    list_display = ('device_id', 'index_id', 'timestamp', 'gyro_l_x', 'gyro_l_y', 'gyro_l_z')


class Gyroscope_r_foot(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')  # one-to-one
    device_id = models.CharField('device_id', max_length=30)
    index_id = models.IntegerField('index_id', db_index=True)
    timestamp = models.BigIntegerField('timestamp')
    gyro_r_x = models.SmallIntegerField('gyro_r_x')
    gyro_r_y = models.SmallIntegerField('gyro_r_y')
    gyro_r_z = models.SmallIntegerField('gyro_r_z')

    class Meta:
        verbose_name = '右角速度'
        verbose_name_plural = '右角速度'


class Gyroscope_r_foot_admin(admin.ModelAdmin):
    list_display = ('device_id', 'index_id', 'timestamp', 'gyro_r_x', 'gyro_r_y', 'gyro_r_z')


# Pressure Information
class Pressure_l_foot(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')  # one-to-one
    device_id = models.CharField('device_id', max_length=30)
    index_id = models.IntegerField('index_id', db_index=True)
    timestamp = models.BigIntegerField('timestamp')
    pre_l_a = models.SmallIntegerField('pre_l_a')
    pre_l_b = models.SmallIntegerField('pre_l_b')
    pre_l_c = models.SmallIntegerField('pre_l_c')
    pre_l_d = models.SmallIntegerField('pre_l_d')

    class Meta:
        verbose_name = '左压力'
        verbose_name_plural = '左压力'


class Pressure_l_foot_admin(admin.ModelAdmin):
    list_display = ('device_id', 'index_id', 'timestamp', 'pre_l_a', 'pre_l_b', 'pre_l_c', 'pre_l_d')


class Pressure_r_foot(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')  # one-to-one
    device_id = models.CharField('device_id', max_length=30)
    index_id = models.IntegerField('index_id', db_index=True)
    timestamp = models.BigIntegerField('timestamp')
    pre_r_a = models.SmallIntegerField('pre_r_a')
    pre_r_b = models.SmallIntegerField('pre_r_b')
    pre_r_c = models.SmallIntegerField('pre_r_c')
    pre_r_d = models.SmallIntegerField('pre_r_d')

    class Meta:
        verbose_name = '右压力'
        verbose_name_plural = '右压力'


class Pressure_r_foot_admin(admin.ModelAdmin):
    list_display = ('device_id', 'index_id', 'timestamp', 'pre_r_a', 'pre_r_b', 'pre_r_c', 'pre_r_d')


# Signal Strength
class Signal_info(models.Model):
    signal_strength = models.IntegerField('signal_strength')
    timestamp = models.BigIntegerField('timestamp')

    class Meta:
        verbose_name = '信号强度'
        verbose_name_plural = '信号强度'


class Signal_info_admin(admin.ModelAdmin):
    list_display = ('signal_strength', 'timestamp')


# Subscribe Information
class Subscribe_info(models.Model):
    subscribe_from = models.ForeignKey(Gait_user, related_name="subscribe_from", verbose_name='订阅自')  # one-to-many
    subscribe_to = models.ForeignKey(Gait_user, related_name="subscribe_to", verbose_name='订阅到')  # one-to-many

    class Meta:
        verbose_name = '订阅信息'
        verbose_name_plural = '订阅信息'


class Subscribe_info_admin(admin.ModelAdmin):
    list_display = ('subscribe_from', 'subscribe_to')


# Statistics Information
class Statistics_info(models.Model):
    index_id = models.IntegerField('index_id', unique=True)
    start_time = models.BigIntegerField('start_time')
    end_time = models.BigIntegerField('end_time')
    steps = models.IntegerField('steps')
    velocity = models.DecimalField('velocity', max_digits=5, decimal_places=2)
    velocity_max = models.DecimalField('max_velocity', max_digits=5, decimal_places=2)
    distance = models.DecimalField('distance', max_digits=10, decimal_places=2)
    cadence = models.DecimalField('cadence', max_digits=5, decimal_places=3)
    stance_time = models.DecimalField('stance_time', max_digits=5, decimal_places=3)
    swing_time = models.DecimalField('swing_time', max_digits=5, decimal_places=3)
    l_step_length = models.DecimalField('l_steps_length', max_digits=5, decimal_places=3)
    r_step_length = models.DecimalField('r_steps_length', max_digits=5, decimal_places=3)
    double_s_time = models.DecimalField('double_s_time', max_digits=5, decimal_places=3)
    calorie = models.DecimalField('calorie', max_digits=10, decimal_places=2)
    acceleration_time = models.IntegerField('acceleration_time')
    deceleration_time = models.IntegerField('deceleration_time')

    class Meta:
        verbose_name = '统计信息'
        verbose_name_plural = '统计信息'


class Statistics_info_admin(admin.ModelAdmin):
    list_display = ('index_id', 'start_time', 'end_time', 'steps', 'velocity', 'velocity_max', 'distance',
                    'cadence', 'stance_time', 'swing_time', 'l_step_length', 'r_step_length', 'double_s_time',
                    'calorie', 'acceleration_time', 'deceleration_time')


# Trace table
class Trace_info(models.Model):
    index_id = models.IntegerField('index_id', db_index=True)
    x = models.DecimalField('x', max_digits=5, decimal_places=4)
    y = models.DecimalField('y', max_digits=5, decimal_places=4)
    v = models.DecimalField('velocity', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = '轨迹信息'
        verbose_name_plural = '轨迹信息'


class Trace_info_admin(admin.ModelAdmin):
    list_display = ('index_id', 'x', 'y', 'v')


admin.site.register(Sta_index, Sta_index_admin)

admin.site.register(Acceleration_l_foot, Acceleration_l_foot_admin)
admin.site.register(Acceleration_r_foot, Acceleration_r_foot_admin)

admin.site.register(Gyroscope_l_foot, Gyroscope_l_foot_admin)
admin.site.register(Gyroscope_r_foot, Gyroscope_r_foot_admin)

admin.site.register(Pressure_l_foot, Pressure_l_foot_admin)
admin.site.register(Pressure_r_foot, Pressure_r_foot_admin)

admin.site.register(Signal_info, Signal_info_admin)
admin.site.register(Subscribe_info, Subscribe_info_admin)
admin.site.register(Statistics_info, Statistics_info_admin)
admin.site.register(Trace_info, Trace_info_admin)
