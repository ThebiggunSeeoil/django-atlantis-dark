# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.home.models import *
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.

class StationProfileFilter(AutocompleteFilter): #ขั้นตอนที่ 1
    title = 'เลือกสถานีที่ต้องการ' # กำหนดชื่อที่ต้องการให้แสดงในส่วนหัว
    field_name = 'station_name' # อ้างไปที่ตารางที่ได้มีการทำ foreign key field เอาไว้ กรณีนี้อ้างไปที่ตาราง Site เพื่อเอาชื่อสถานีมาแสดง

class ArtistAdmin(admin.ModelAdmin): #ขั้นตอนที่ 2
    search_fields = ['station_name','station_ip_address'] # อ้างอิงไปที่ตาราง Site และเลือกฟิวที่ต้องการทำการ Filter กรณีนี้ให้เอาชื่อสถานีมาแสดง

@admin.register(StationProfile)
class StationProfileAdmin(ImportExportModelAdmin):
    search_fields = ('station_name','station_ip_address') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    list_filter = ['station_area_code']
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    list_display = [field.name for field in StationProfile._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(LineSetting)
class LineSettingAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    # list_filter = [StationProfileFilter] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    list_display = [field.name for field in LineSetting._meta.fields if field.name not in ("id","NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(PersonUser)
class PersonUserAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    # list_filter = [StationProfileFilter] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    list_display = [field.name for field in PersonUser._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    # list_filter = [StationProfileFilter] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    list_display = [field.name for field in Position._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    # list_filter = [StationProfileFilter] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    list_display = [field.name for field in Area._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(AreaCodeType)
class AreaCodeTypeAdmin(ImportExportModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    # list_filter = [StationProfileFilter] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    list_editable = ('area_register','area_activate','area_code_type')
    list_display = [field.name for field in AreaCodeType._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(UserListCodeType)
class UserListCodeTypeAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    # list_filter = [StationProfileFilter] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    list_display = [field.name for field in UserListCodeType._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(NotifyByRequest)
class NotifyByRequestAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    # list_filter = [StationProfileFilter] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    list_editable = ('line_notify_send_to_group','flex_message_send_to_user','need_admin_approve')
    list_display = [field.name for field in NotifyByRequest._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(MultiStationTackCare)
class MultiStationTackCareAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    list_filter = ['multi_manager_name'] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    # list_editable = ('line_notify_send_to_group','flex_message_send_to_user','need_admin_approve')
    list_display = [field.name for field in MultiStationTackCare._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(CodeInAreaDetail)
class CodeInAreaDetailAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    list_filter = ['code_in_area_code_name'] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    # list_editable = ('line_notify_send_to_group','flex_message_send_to_user','need_admin_approve')
    list_display = [field.name for field in CodeInAreaDetail._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass

@admin.register(HistoryRequest)
class HistoryRequestAdmin(admin.ModelAdmin):
    # search_fields = ('station_name','station_branch') # สร้าง tab ในการค้นหาข้อมูลต่างที่ต้องการ
    list_filter = ['HistoryPushOrReply','HistoryUserName','HistoryUserPosition'] #สร้าง list_filter แล้วอ้างอิงไปที่ Classs ที่ทำไว้ในข้้นตอนที่ 1
    # search_filter =['site',]
    # list_display = ('station_profile','BusinessDate','TransactionBegin','Shift_id','Shift_Number','face_dp','dispenser_number')
    # list_editable = ('line_notify_send_to_group','flex_message_send_to_user','need_admin_approve')
    list_display = [field.name for field in HistoryRequest._meta.fields if field.name not in ("NozzleID")]
    list_per_page = 30
    # def detail(self,obj):
    #     return u'%s %s' % (obj.station_profile, obj.BusinessDate)
    # pass
