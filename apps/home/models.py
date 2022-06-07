# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.safestring import mark_safe


# Create your models here.

class StationProfile(models.Model):
    station_site = models.CharField(max_length=255, blank=True, null=True)
    station_name = models.CharField(max_length=255, blank=True, null=True)
    station_address = models.CharField(max_length=255, blank=True, null=True)
    station_area_code = models.ForeignKey('CodeInAreaDetail', on_delete=models.CASCADE, blank=True, null=True)
    station_tank = models.IntegerField(blank=True, null=True)
    station_tel = models.CharField(max_length=255, blank=True, null=True)
    station_phone = models.CharField(max_length=255, blank=True, null=True)
    station_email = models.CharField(max_length=255, blank=True, null=True)
    station_tax_id = models.CharField(max_length=255, blank=True, null=True)
    station_ip_address = models.CharField(max_length=255, blank=True, null=True)
    station_port_number = models.CharField(max_length=255, blank=True, null=True)
    station_user = models.CharField(max_length=255, blank=True, null=True)
    station_password = models.CharField(max_length=255, blank=True, null=True)
    station_db_databasename = models.CharField(max_length=255, blank=True, null=True)
    station_line_token = models.CharField(max_length=255, blank=True, null=True)
    station_activate = models.BooleanField(default=False)
    line_notify = models.BooleanField(default=False)
    debug_mode = models.BooleanField(default=False)
    datetime_modify = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.station_name

    class Meta:
        ordering = ('station_site',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ข้อมูลการตั้งค่าสถานี'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ตั้งค่าข้อมูลสถานี'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย

class LineSetting(models.Model):
    
    line_id = models.CharField(max_length=255, blank=True, null=True)
    line_channelID = models.CharField(max_length=255, blank=True, null=True)
    line_destination = models.CharField(max_length=255, blank=True, null=True)
    line_channelID = models.CharField(max_length=255, blank=True, null=True)
    rich_main_menu = models.CharField(max_length=255, blank=True, null=True)
    rich_select_munu = models.CharField(max_length=255, blank=True, null=True)
    line_token = models.TextField(blank=True, null=True)
    line_notify_token = models.TextField(blank=True, null=True , default=None)
    datetime_modify = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.line_token

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ตั้งค่า LineSetting'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ตั้งค่าข้อมูล LineServer'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย



class Position(models.Model):
    position_type = models.CharField(max_length=255, blank=True, null=True)
    position_name = models.CharField(max_length=255, blank=True, null=True)
    timestramp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.position_name

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ข้อมูลตำแหน่งพนักงาน'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ข้อมูลตำแหน่งพนักงาน'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย



class PersonUser(models.Model):
    user_position = models.ForeignKey('Position', on_delete=models.CASCADE, blank=True, null=True)
    user_station_name = models.ForeignKey('StationProfile', on_delete=models.CASCADE, blank=True, null=True)
    user_area = models.ForeignKey('Area', on_delete=models.CASCADE, blank=True, null=True)
    user_userid = models.CharField(max_length=255, blank=True, null=True)
    user_display_name = models.CharField(max_length=255, blank=True, null=True)
    user_picture_url = models.URLField()
    user_status_message = models.CharField(max_length=255, blank=True, null=True)
    user_activate = models.BooleanField(default=False)
    user_station_type = models.CharField(max_length=255, blank=True, null=True)
    user_station_level = models.CharField(max_length=255, blank=True, null=True)
    user_notify = models.BooleanField(default=False)
    timestramp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    @property
    def friendly_email(self):
        return mark_safe(u"%s <%s>") % (escape(self.fullname), escape(self.email_address))
    
    def __str__(self):
        return self.user_display_name

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ข้อมูล ติดต่อสำหรับผู้ใช้งานระบบ'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ข้อมูล ติดต่อสำหรับผู้ใช้งานระบบ'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย

class Area(models.Model):
    DieselPremium = "DieselPremium"
    DieselB7 = "DieselB7"
    Diesel = "Diesel"
    DieselB20 = "DieselB20"
    Benzin = "Benzin"
    Gasohol95 = "Gasohol95"
    Gasohol91 = "Gasohol91"
    GasoholE20 = "GasoholE20"
    GasoholE85 = "GasoholE85"
    product_choices = ((DieselPremium,"DieselPremium"),(DieselB7,"DieselB7"),(Diesel,"Diesel"),(DieselB20,"DieselB20"),(Benzin,"Benzin"),(Gasohol95,"Gasohol95"),(Gasohol91,"Gasohol91"),(GasoholE20,"GasoholE20"),(GasoholE85,"GasoholE85"))
    user_position = models.ForeignKey('Position', on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.CharField(max_length=255, choices=product_choices,default="--")
    user_userid = models.CharField(max_length=255, blank=True, null=True)
    user_display_name = models.CharField(max_length=255, blank=True, null=True)
    user_picture_url = models.URLField(default='none')
    user_status_message = models.CharField(max_length=255, blank=True, null=True)
    user_activate = models.BooleanField(default=False)
    user_notify = models.BooleanField(default=False)
    timestramp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.user_display_name

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ข้อมูลผู้จัดการเขต'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ข้อมูลผู้จัดการเขต'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย

class CodeInAreaDetail(models.Model):
    code_in_area_code_name = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.code_in_area_code_name

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ข้อมูล รายละเอียดเขตการดูแล'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ข้อมูล รายละเอียดเขตการดูแล'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย

class AreaCodeType(models.Model):
    area_code_name = models.CharField(max_length=255, blank=True, null=True)
    area_code_type = models.ForeignKey('CodeInAreaDetail', on_delete=models.CASCADE, blank=True, null=True)
    area_register = models.BooleanField(default=False)
    area_register_datetime = models.DateTimeField(default=None, blank=True, null=True)
    area_activate = models.BooleanField(default=False)
    

    def __str__(self):
        return self.area_code_name

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ข้อมูล รายละเอียด ID ผู้จัดการเขต'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ข้อมูล รายละเอียด ID ผู้จัดการเขต'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย




class StationManagerCodeType(models.Model):
    StationManager_code_name = models.CharField(max_length=255, blank=True, null=True)
    StationManager_code_type = models.CharField(max_length=255, blank=True, null=True , unique=True)
    StationManager_adddatetime = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    StationManager_register = models.BooleanField(default=False)
    StationManager_register_datetime = models.DateTimeField(default=None, blank=True, null=True)
    StationManager_userid = models.CharField(max_length=255, blank=True, null=True)
    StationManager_display_name = models.CharField(max_length=255, blank=True, null=True)
    StationManager_picture_url = models.URLField()
    StationManager_status_message = models.CharField(max_length=255, blank=True, null=True)
    StationManager_activate = models.BooleanField(default=False)
    StationManager_notify = models.BooleanField(default=False)

    def __str__(self):
        return self.area_code_name

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ข้อมูล รายละเอียด ID ผู้จัดการสถานี'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ข้อมูล รายละเอียด ID ผู้จัดการสถานี'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย

class UserListCodeType(models.Model):
    userList_name = models.CharField(max_length=255, blank=True, null=True)
    userList_member_mode = models.CharField(max_length=255, blank=True, null=True , default='register')
    userList_takecare_station = models.CharField(max_length=255, blank=True, null=True , default='single')
    userList_position = models.ForeignKey('Position', on_delete=models.CASCADE, blank=True, null=True)
    userList_station_name = models.ForeignKey('StationProfile', on_delete=models.CASCADE, blank=True, null=True)
    userList_area_name = models.ForeignKey('CodeInAreaDetail', on_delete=models.CASCADE, blank=True, null=True)
    userList_add_bot_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    userList_register = models.BooleanField(default=False)
    userList_register_datetime = models.DateTimeField(default=None, blank=True, null=True)
    userList_userid = models.CharField(max_length=255, blank=True, null=True)
    userList_display_name = models.CharField(max_length=255, blank=True, null=True)
    userList_picture_url = models.URLField()
    userList_status_message = models.CharField(max_length=255, blank=True, null=True)
    userList_approved_datetime = models.DateTimeField(default=None, blank=True, null=True)
    userList_activate = models.BooleanField(default=False)
    userList_notify = models.BooleanField(default=False)

    def __str__(self):
        return self.userList_display_name

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ข้อมูล ID ผู้ใช้งานระบบ'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ข้อมูล ID ผู้ใช้งานระบบ'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย


class NotifyByRequest(models.Model):
    approve_list = models.CharField(max_length=255, blank=True, null=True)
    line_notify_send_to_group = models.BooleanField(default=False)
    flex_message_send_to_user = models.BooleanField(default=False)
    need_admin_approve = models.BooleanField(default=False)
    

    def __int__(self):
        return self.id

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ตั้งค่าการแจ้งเตือน'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ตั้งค่าการแจ้งเตือน'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย

class MultiStationTackCare(models.Model):
    multi_manager_name = models.CharField(max_length=255, blank=True, null=True , default='None')
    multi_manager_number = models.ForeignKey('UserListCodeType', on_delete=models.CASCADE, blank=True, null=True)
    multi_station_number = models.ForeignKey('StationProfile', on_delete=models.CASCADE, blank=True, null=True)
    multi_active = models.BooleanField(default=True)
    active_time = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    deactive_ime = models.DateTimeField(default=None, blank=True, null=True)
   
    

    def __int__(self):
        return self.id

    class Meta:
        ordering = ('id',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ส่วนดูแลสาขา Multi Station'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ส่วนดูแลสาขา Multi Station'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย

class HistoryRequest(models.Model):
    HistoryUserName = models.CharField(max_length=255, blank=True, null=True)
    HistoryUserPosition = models.CharField(max_length=255, blank=True, null=True)
    HistoryUserStationID = models.CharField(max_length=255, blank=True, null=True)
    HistoryPushOrReply = models.CharField(max_length=255, blank=True, null=True)
    HistoryReportTypeRequest = models.CharField(max_length=255, blank=True, null=True)
    HistoryReportDeatil = models.CharField(max_length=255, blank=True, null=True)
    HistoryStatusSend = models.CharField(max_length=255, blank=True, null=True)
    HistoryTimeStramp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
   
    

    def __int__(self):
        return self.id

    class Meta:
        ordering = ('-HistoryTimeStramp',)  # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'ประวัติการทำรายการ'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย
        verbose_name_plural = 'ข้อมูลประวัติการทำรายงาน'  # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย