from email import message
import requests
import datetime
from apps.home.models import *


class creating_line_data :
    def __init__(self):
        # ติดต่อ db เพือขอ line token
        self.line_token = LineSetting.objects.first()
        print ('LINE TOKEN {}'.format(self.line_token.line_notify_token))
        pass
    def send_notify(self,message, notify_approve):
        # เช็คจากหัวข้อ ว่ามีการอนุญาติให้แจ้งเตือนหรือไม่
        result =  NotifyByRequest.objects.filter(id=notify_approve).first()
        print ('result {}'.format(result.line_notify_send_to_group))
        line_notify_send_to_group = result.line_notify_send_to_group
        try:
            if line_notify_send_to_group == True :
                Token = 'Bearer ' + self.line_token.line_notify_token
                LINE_ACCESS_TOKEN = Token
                url = 'https://notify-api.line.me/api/notify'
                headers = {'content-type': 'application/x-www-form-urlencoded',
                                'Authorization': LINE_ACCESS_TOKEN}
                r = requests.post(url, headers=headers, data={'message': message})
                print(r.text)
                print ('SEND LINE NOTIFY')
                return True
            else:
                print ('NOT SEND LINE NOTIFY')
                return True
        except requests.ConnectionError as err:
            print("Connected to Line notify fail")
            return False
    def get_approve_new_station_manager(self,area_in_this_site,profile,line_token):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        # ค้นหาข้อมูล ผู้จัดการเขต 
        area_name = AreaCodeType.objects.filter(area_code_type=area_in_this_site.station_area_code.id).first()
        print ('area_name {}'.format(area_name))
        message_notilfy = 'หัวข้อ : ขออนุมัติผู้จัดการสาขา \n ชื่อสาขา :  {} \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n ผู้อนุมัติ : คุณ {} \n ตำแหน่ง : ผู้จัดการเขต \n สถานะ : รออนุมัติ \n BOT-INFO : http://line.me/ti/p/{}'.format(
                                                                                                                                                                                                            area_in_this_site,
                                                                                                                                                                                                                dt,
                                                                                                                                                                                                                    profile.display_name,
                                                                                                                                                                                                                        area_name,
                                                                                                                                                                                                                            line_token.line_id) 
        notify_approve = 1 #แจ้งเตือนกรณี ลงทะเบียนผู้จัดการสาขา
        self.send_notify(message_notilfy, notify_approve)
    def get_approve_add_more_station_manager(self,area_in_this_site,profile,line_token,area_name_UserList_codeType,area_name_AreaCodeType):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : ขออนุมัติดูแลสาขาเพิ่ม \n ชื่อสาขา :  {} \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n ผู้อนุมัติ : {} \n ตำแหน่ง : ผู้จัดการเขต \n สถานะ : รออนุมัติ \n BOT-INFO : http://line.me/ti/p/{}'.format(
                area_in_this_site,
                    dt,
                        profile.display_name,
                            # area_name_UserList_codeType.userList_display_name,
                            area_name_AreaCodeType.area_code_name,
                                line_token.line_id) 
        notify_approve = 1 #แจ้งเตือนกรณี ลงทะเบียนผู้จัดการสาขา
        self.send_notify(message_notilfy, notify_approve)
    def send_rejected_add_more_station_manager(self,area_in_this_site,profile,line_token,area_name_AreaCodeType):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : ไม่อนุมัติดูแลสาขาเพิ่ม \n ชื่อสาขา :  {} \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n ผู้อนุมัติ : {} \n ตำแหน่ง : ผู้จัดการเขต \n สถานะ : ไม่อนุมัติ \n BOT-INFO : http://line.me/ti/p/{}'.format(
                    area_in_this_site,
                        dt,
                            profile.display_name,
                                area_name_AreaCodeType.area_code_name,
                                    line_token.line_id) 
        notify_approve = 1 #แจ้งเตือนกรณี ลงทะเบียนผู้จัดการสาขา
        self.send_notify(message_notilfy, notify_approve)
    def get_approve_new_area_manager(self,profile,line_token):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : ขออนุมัติผู้จัดการเขต  \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n ผู้อนุมัติ : Admin \n ตำแหน่ง : ส่วนผู้ดูแลระบบ \n สถานะ : รออนุมัติ \n BOT-INFO : http://line.me/ti/p/{}'.format(dt,profile.display_name,line_token.line_id) 
        notify_approve = 2 #แจ้งเตือนกรณี ลงทะเบียนผู้จัดการเขต 
        self.send_notify(message_notilfy, notify_approve)
    def send_approve_new_station_manager(self,area_in_this_site,profile,line_token,manager_user_id2,area_name_approved):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : อนุมัติผู้จัดการสาขา \n ชื่อสาขา :  {} \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n ผู้อนุมัติ : {} \n ตำแหน่ง : ผู้จัดการเขต \n สถานะ : อนุมัติแล้ว \n BOT-INFO : http://line.me/ti/p/{}'.format(
            area_in_this_site,
                    dt,
                        manager_user_id2.userList_display_name,
                            area_name_approved.area_code_name,
                            
                                line_token.line_id) 
        notify_approve = 3 #แจ้งเตือนกรณี ผู้จัดการเขต อนุมัติ ผู้จัดการสาขา 
        self.send_notify(message_notilfy, notify_approve)
    def send_approve_add_more_station_manager(self,area_in_this_site,profile,line_token,manager_user_id2,area_name_approved):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : อนุมัติสาขาเพิ่ม \n ชื่อสาขา :  {} \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n ผู้อนุมัติ : {} \n ตำแหน่ง : ผู้จัดการเขต \n สถานะ : อนุมัติแล้ว \n BOT-INFO : http://line.me/ti/p/{}'.format(
            area_in_this_site,
                    dt,
                        manager_user_id2.userList_display_name,
                            area_name_approved.area_code_name,
                            
                                line_token.line_id) 
        notify_approve = 3 #แจ้งเตือนกรณี ผู้จัดการเขต อนุมัติ ผู้จัดการสาขา 
        self.send_notify(message_notilfy, notify_approve)
    def send_approve_new_area_manager(self,manager_user_id2,line_token):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        # ค้นหาชื่อผู้จัดการเขต จากตาราง AreaCodeType
        area_name = AreaCodeType.objects.filter(area_code_type=manager_user_id2.userList_area_name.id).first()
        print ('รายละเอียดข้อมูล ผู้จัดการเขต : {}'.format(area_name))

        message_notilfy = 'หัวข้อ : อนุมัติผู้จัดการเขต \n วันที่ขออนุมัติ : {} \n เขตที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n LineID : {} \n ผู้อนุมัติ : Admin \n ตำแหน่ง : ผู้จัดการเขต \n สถานะ : อนุมัติแล้ว \n BOT-INFO : http://line.me/ti/p/{}'.format(dt,
                                                                                                                                                                                                                                manager_user_id2.userList_area_name.code_in_area_code_name,
                                                                                                                                                                                                                                    area_name,
                                                                                                                                                                                                                                    manager_user_id2.userList_display_name,
                                                                                                                                                                                                                                        line_token.line_id) 
        notify_approve = 4 #แจ้งเตือนกรณี Admin อนุมัติระดับผู้จัดการเขต 
        self.send_notify(message_notilfy, notify_approve)
    def send_rejected_new_area_manager(self,manager_user_id2,line_token):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : ไม่อนุมัติผู้จัดการเขต \n วันที่ขออนุมัติ : {} \n เขตที่ขออนุมัติ : {} \n LineName : {} \n ผู้อนุมัติ : Admin \n ตำแหน่ง : ผู้จัดการเขต \n สถานะ : ไม่อนุมัติ \n BOT-INFO : http://line.me/ti/p/{}'.format(dt,manager_user_id2.userList_area_name.code_in_area_code_name,manager_user_id2.userList_display_name,line_token.line_id) 
        notify_approve = 4 #แจ้งเตือนกรณี Admin อนุมัติระดับผู้จัดการเขต 
        self.send_notify(message_notilfy, notify_approve)
    def send_approve_new_main_area(self,area_in_this_site,profile,line_token):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : ขออนุมัติผู้จัดการภาค \n ชื่อสาขา :  {} \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n ผู้อนุมัติ : Admin \n ตำแหน่ง : ผู้จัดการภาค \n สถานะ : รออนุมัติ \n BOT-INFO : http://line.me/ti/p/{}'.format(area_in_this_site,dt,profile.display_name,line_token.line_id) 
        notify_approve = 5 #แจ้งเตือนกรณี Admin อนุมัติระดับผู้จัดการภาค 
        self.send_notify(message_notilfy, notify_approve)
    def get_approve_new_main_area_manager(self,profile,line_token):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : อนุมัติผู้จัดการภาค  \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {} \n ผู้อนุมัติ : Admin \n ตำแหน่ง : ส่วนผู้ดูแลระบบ \n สถานะ : อนุมัติแล้ว \n BOT-INFO : http://line.me/ti/p/{}'.format(dt,profile.userList_display_name,line_token.line_id) 
        notify_approve = 5 #แจ้งเตือนกรณี ลงทะเบียนผู้จัดการเขต 
        self.send_notify(message_notilfy, notify_approve)
    def send_rejected_new_main_area_manager(self,manager_user_id2,line_token):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : ไม่อนุมัติผู้จัดการภาค \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {}  \n ผู้อนุมัติ : Admin \n ตำแหน่ง : ผู้ดูแลระบบ \n สถานะ : ไม่อนุมัติ \n BOT-INFO : http://line.me/ti/p/{}'.format(dt,manager_user_id2.userList_display_name,line_token.line_id) 
        notify_approve = 4 #แจ้งเตือนกรณี Admin อนุมัติระดับผู้จัดการเขต 
        self.send_notify(message_notilfy, notify_approve)
    def send_rejected_new_station_manager(self,manager_user_id2,line_token,station_profile):
        dt = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        message_notilfy = 'หัวข้อ : ไม่อนุมัติผู้จัดการสาขา \n สาขา {} \n วันที่ขออนุมัติ : {} \n ผู้ขออนุมัติ : {}  \n ผู้อนุมัติ : Admin \n ตำแหน่ง : ผู้ดูแลระบบ \n สถานะ : ไม่อนุมัติ \n BOT-INFO : http://line.me/ti/p/{}'.format(station_profile.station_name,dt,manager_user_id2.userList_display_name,line_token.line_id) 
        notify_approve = 4 #แจ้งเตือนกรณี Admin อนุมัติระดับผู้จัดการเขต 
        self.send_notify(message_notilfy, notify_approve)
        
    def send_notify_picture(self,path, token,message,site_profile):
        try:
            url = "https://notify-api.line.me/api/notify"
            file = {'imageFile':open(path,'rb')}
            data = ({'message': message,})
            path_opened = True
        except :
            path_opened = False
            datetime_now = datetime.datetime.now().strftime("%d.%m.%y %H:%M")
            print ('CAN NOT OPEN URL PATH FOR LINE PICTURE NOTIFY FOR MESSAGES {} ON {}'.format(message,datetime_now))
        if  path_opened == True:
            LINE_HEADERS = {"Authorization":"Bearer "+token}
            session = requests.Session()
            r=session.post(url, headers=LINE_HEADERS, files=file, data=data)
            if r.status_code == 200 :
                datetime_now = datetime.datetime.now().strftime("%d.%m.%y %H:%M")
                print ('SUCCESS LINE LINE NOTIFY PICTURE FOR MESSAGES {} ON {}'.format(message,datetime_now))
                # file_path = path
                # os.remove(file_path)
                # print ('REMOVED FILE SUCCESS FOR MESSAGES {} ON {}'.format(message,datetime_now))
                return True
            elif r.status_code != 200 :
                datetime_now = datetime.datetime.now().strftime("%d.%m.%y %H:%M")
                # save_data_to_db.SaveDataSendLineFailedToBD('LINE_NOTIFY',path,message,site_profile)
                print ('FAILED SEND LINE GO TO SAVE PICTURE FOR MESSAGES {} ON {}'.format(message,datetime_now))
                return True
        else:
            return None