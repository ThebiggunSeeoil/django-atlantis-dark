from asyncio.windows_events import NULL
from turtle import position
from urllib import request
from django.utils import timezone
from requests import delete
from apps.home.models import *
from datetime import datetime
from linebot import LineBotApi

class SaveDB :
    def __init__(self):
        print('')
    def save_request_history(self,HistoryUserName,HistoryUserPosition,HistoryUserStationID,HistoryPushOrReply,HistoryReportTypeRequest,HistoryReportDeatil,line_result):
        if line_result == 200 :
            status_send = 'success'
        else :
            status_send = 'fail'
        try:
            save_record = HistoryRequest()
            save_record.HistoryUserName = HistoryUserName
            save_record.HistoryUserPosition = HistoryUserPosition
            save_record.HistoryUserStationID = HistoryUserStationID
            save_record.HistoryPushOrReply = HistoryPushOrReply
            save_record.HistoryReportTypeRequest = HistoryReportTypeRequest
            save_record.HistoryReportDeatil = HistoryReportDeatil
            save_record.HistoryStatusSend = status_send
            save_record.HistoryTimeStramp = timezone.now()
            save_record.save(request)
            print ('บันทึกข้อมูลสำเร็จ')
        except Exception as e:
            print ('ไม่สามารถทำรายการบันทึกประวัติการทำรายการได้เนื่องจาก {}'.format(e))
            # print(e)
            pass
            # Do something such send line notify
           

    def save_new_user(self,user_id,user_display_name,user_picture_url,user_status_message):
        pass
        try:
            UserListCodeType.objects.get(userList_userid=user_id)
        except UserListCodeType.DoesNotExist:
            # Do something such send line notify
            save_record = UserListCodeType()
            save_record.userList_userid = user_id
            save_record.userList_display_name = user_display_name
            save_record.userList_picture_url = user_picture_url
            save_record.userList_status_message = user_status_message
            # save_record.userList_activate = 0
            # save_record.user_station_type = 'none'
            # save_record.user_station_level = 'none'
            # save_record.user_notify = 0
            # save_record.timestramp = timezone.now()
            save_record.save(request)
    def update_position_inapprove(self,user_id,user_position,station_detail,area_detail):
        print ('user_position',user_position)
        if user_position == 1:
            # ค้นหาข้อมูลผู้จัดการเขต
            area_name = AreaCodeType.objects.filter(area_code_type=station_detail.station_area_code.id).first()
            print ('area ID สำหรับการ set update คือ {} ชื่อเขต {}'.format(area_name.id,area_name.area_code_type.code_in_area_code_name))
            UserListCodeType.objects.filter(userList_userid=user_id).update(
                                                                            userList_position=user_position,userList_member_mode='inapprove',
                                                                                userList_station_name=station_detail.id,
                                                                                    userList_area_name=area_name.area_code_type.id,
                                                                                        userList_register=True,
                                                                                            userList_register_datetime=datetime.now(),
                                                                                                userList_notify=True)
        elif user_position == 2:
            UserListCodeType.objects.filter(userList_userid=user_id).update(userList_position=user_position,userList_member_mode='inapprove',userList_register=True,userList_register_datetime=datetime.now(),userList_notify=True)
        elif user_position == 3:
            UserListCodeType.objects.filter(userList_userid=user_id).update(userList_position=user_position,userList_member_mode='inapprove',userList_register=True,userList_register_datetime=datetime.now(),userList_area_name=area_detail.area_code_type.id,userList_notify=True)
            AreaCodeType.objects.filter(id=area_detail.id).update(area_activate=True,area_register=True,area_register_datetime=datetime.now())
        elif user_position == 4:
            UserListCodeType.objects.filter(userList_userid=user_id).update(userList_position=user_position,userList_member_mode='inapprove',userList_register=True,userList_register_datetime=datetime.now(),userList_notify=True)
        elif user_position == 5:
            UserListCodeType.objects.filter(userList_userid=user_id).update(userList_position=user_position,userList_member_mode='approved',userList_register=True,userList_register_datetime=datetime.now(),userList_activate=True,userList_notify=True,userList_approved_datetime=datetime.now())
        pass
    
    def update_position_approve(self,manager_user_id2):
        print ('สถานะผู้ถูกปฏิเสธ {}'.format(manager_user_id2.userList_position.id))
        user_position = manager_user_id2.userList_position.id
        if user_position == 1:
            UserListCodeType.objects.filter(id=manager_user_id2.id).update(userList_member_mode = 'approved' , userList_approved_datetime = datetime.now() , userList_activate=True)
        if user_position == 3:
            UserListCodeType.objects.filter(id=manager_user_id2.id).update(userList_member_mode = 'approved' , userList_approved_datetime = datetime.now() , userList_activate=True)
        if user_position == 4:
            UserListCodeType.objects.filter(id=manager_user_id2.id).update(userList_member_mode = 'approved' , userList_approved_datetime = datetime.now() , userList_activate=True)
    def unapproved_member(self,manager_user_id2):
        print ('สถานะผู้ถูกปฏิเสธ {} คือ {}'.format(manager_user_id2.userList_position.id,manager_user_id2.userList_area_name.id))
        user_position = manager_user_id2.userList_position.id
        if user_position == 3:
            UserListCodeType.objects.filter(id=manager_user_id2.id).update(userList_member_mode='register',userList_register='False',userList_register_datetime=None,userList_activate='False',userList_notify='False')
            AreaCodeType.objects.filter(area_code_type=manager_user_id2.userList_area_name.id).update(area_activate='False',area_register='False',area_register_datetime=None)
        elif user_position == 1:
            UserListCodeType.objects.filter(id=manager_user_id2.id).update(userList_area_name=None,userList_station_name=None,userList_member_mode='register',userList_register='False',userList_register_datetime=None,userList_activate='False',userList_notify='False')
        elif user_position == 4:
            UserListCodeType.objects.filter(id=manager_user_id2.id).update(userList_member_mode='register',userList_register='False',userList_register_datetime=None,userList_activate='False',userList_notify='False')
    def addmultistationmanager(self,manager_user_id2,area_in_this_site):
            # # ทำการ set add db MultiStationTackCare --> multi_manager_name = manager_user_id2.userList_display_name , multi_manager_id = manager_user_id2.id , multi_station_id=area_in_this_site.id
            try :
                MultiStationTackCare.objects.get(multi_manager_number=manager_user_id2.id,multi_station_number=area_in_this_site.id,multi_active=True)
                print ('มีข้อมูลอยู่แล้ว')
            except MultiStationTackCare.DoesNotExist: 
                print ('ไม่มีข้อมูล')
                save_record = MultiStationTackCare()
                save_record.multi_manager_name = manager_user_id2.userList_display_name
                save_record.multi_manager_number_id=manager_user_id2.id
                save_record.multi_station_number_id = area_in_this_site.id
                save_record.active_time = timezone.now()
                save_record.save(request)

            # ทำการเปลี่ยนสถานะ ที่ table UserListCodeType ด้วยการ update userList_takecare_station จาก single เป็น multi
            UserListCodeType.objects.filter(id=manager_user_id2.id).update(userList_takecare_station='multi')
    def update_new_user(self,user_id,user_position):
        # นำ user_plsition ไปค้นหา ID จาก Position
        Position_Save = Position.objects.filter(position_type=user_position).first()
        PersonUser.objects.filter(user_userid=user_id).update(user_position=Position_Save.id)
        pass
    def update_new_user_station_name(self,user_id,user_station_name):
        # ส่ง user_station_name ไปค้นหาเลข ID 
        id_save = StationProfile.objects.filter(station_site=user_station_name).first()
        PersonUser.objects.filter(user_userid=user_id).update(user_station_name_id=id_save.id)
    def create_new_area_manager(self,user_id):
        line_token = LineSetting.objects.all().first()
        line_bot_api = LineBotApi(line_token.line_token)
        profile = line_bot_api.get_profile(user_id)
        try:
            Area.objects.get(user_userid=user_id)
        except Area.DoesNotExist:
            # Do something such send line notify
            save_record = Area()
            save_record.user_userid = user_id
            save_record.user_display_name = profile.display_name
            save_record.user_picture_url = profile.picture_url
            save_record.user_status_message = profile.status_message
            save_record.user_activate = 1
            save_record.user_notify = 1
            save_record.timestramp = timezone.now()
            save_record.save(request)
    def set_multi_to_flalse(self,manager_id,station_id):
        # ทำการ set ค่า multi_station_id ให้เป็น flase
        # ทำการเช็คจำนวนสาขาที่ดูแล หากมีแค่ 1 สาขา และยกเลิก จะต้องไป set update table UserListCodeType set userList_takecare_station='single'
        stations = MultiStationTackCare.objects.filter(multi_manager_number=manager_id,multi_active=True).all()
        print ('จำนวนสาขาที่ดูแล {}'.format(len(stations)))
        if len(stations) == 1:
            print ('มีสาขาที่ดูแลเดียว')
            for manager in stations :
                MultiStationTackCare.objects.filter(multi_station_number=station_id).update(multi_active=False,deactive_ime=datetime.now())
                UserListCodeType.objects.filter(id=manager_id).update(userList_takecare_station='single')
                
            

        elif len(stations) > 1:
                print ('มีสาขาอยู่มากกว่า 1 สาขา')
                MultiStationTackCare.objects.filter(multi_station_number=station_id).update(multi_active=False,deactive_ime=datetime.now())
    def set_change_new_area(self,current_area_id,new_ared_manager_id):
        # ทำการเปลี่ยนเขตใหม่
        AreaCodeType.objects.filter(id=current_area_id).update(area_code_type=new_ared_manager_id.area_code_type.id)
        # ทำการ set ให้ผู้จัดการเขตกลายเป็นเขตว่าง
        AreaCodeType.objects.filter(id=new_ared_manager_id.id).update(area_code_type=17)

        pass
    def delete_cacah_area(self,user_id):
        
        PersonUser.objects.filter(user_userid=user_id).delete()

        pass
    def update_area_to_station(self,user_id,area_id):
        # ส่ง user_station_name ไปค้นหาเลข ID 
        PersonUser.objects.filter(user_userid=user_id).update(user_area=area_id)

    



