import requests
from apps.home.models import *
import json
import logging
from apps.home.models import *
from line_bot.save_data_to_db import *
db_logger = logging.getLogger('db')

class SendFlexMessages :
    def __init__(self,payload):
        self.payload = payload
        line_token = LineSetting.objects.all().first()
        line_bot_api = LineBotApi(line_token.line_token)
        self.line_user_id = payload['events'][0]['source']['userId']
        self.line_token = LineSetting.objects.all().first()
        self.line_bot_api = LineBotApi(line_token.line_token)
        self.reply_token = payload['events'][0]['replyToken']
        self.user_id_line = UserListCodeType.objects.filter(userList_userid=self.line_user_id).first()
        self.display_name = self.user_id_line.userList_display_name
        self.position = self.user_id_line.userList_position.position_name
        self.postion_id = self.user_id_line.userList_position.id
        if self.postion_id == 1 :
            self.station_name = self.user_id_line.userList_station_name.station_name
        elif self.postion_id in (3,4,5) :
            self.station_name = None

    def ReplyTextMessage(self,Reply_token, TextMessage,command):
        try : 
            LINE_API = 'https://api.line.me/v2/bot/message/reply'
            Authorization = 'Bearer {}'.format(self.line_token)
            print(Authorization)
            headers = {
                'Content-Type': 'application/json; charset=UTF-8',
                'Authorization': Authorization
            }

            data = {
                "replyToken": Reply_token,
                "messages": [{
                    "type": "text",
                    "text": TextMessage
                }]
            }

            data = json.dumps(data)  ## dump dict >> Json Object
            r = requests.post(LINE_API, headers=headers, data=data)
            if r.status_code == 200:
                messages=('LINE : ทำรายการ OK ส่งคำสั่ง {} ข้อความ {} สถานะ Status Code : {} สถานะผลการส่ง {}'.format(command,TextMessage,r.status_code,r.text))
                print(messages)
                db_logger.info(command)
                SaveDB().save_request_history(self.display_name,
                                                self.position,
                                                        self.station_name,
                                                            'push',
                                                                'Meter',
                                                                    command,
                                                                        r.status_code)
                return True
            else:
                messages = ('LINE : ทำรายการ NOK ส่งคำสั่ง {} ข้อความ {} ปัญหาคือ {}'.format(command,TextMessage,str(r.text)))
                print (messages)
                db_logger.warning(str(r.text))
        except Exception as e:
            messages = ('LINE : ทำรายการ NOK ส่งคำสั่ง {} ข้อความ {} ปัญหาคือ {}'.format(command,TextMessage,str(e)))
            print (messages)
            db_logger.warning(str(e))
            SaveDB().save_request_history(self.display_name,
                                                self.position,
                                                        self.station_name,
                                                            'Reply',
                                                                'Meter',
                                                                    command,
                                                                        r.status_code)
                
            return False 
    def ReplyMessageToUser(self,Reply_token,TextMessage,command):
        try : 
            LINE_API = 'https://api.line.me/v2/bot/message/reply'
            # print('line API {}'.format(TextMessage))
            Authorization = 'Bearer {}'.format(self.line_token)
            print(Authorization)
            headers = {
                'Content-Type': 'application/json; charset=UTF-8',
                'Authorization': Authorization
            }

            data = {
                "replyToken": Reply_token,
                "messages": [TextMessage], }

            data = json.dumps(data)
            # print('data to line {}'.format(data))
            r = requests.post(LINE_API, headers=headers, data=data)
            # print(r.text)
            # print(r.status_code)
            if r.status_code == 200:
                messages=('LINE : ทำรายการ OK ส่งคำสั่ง {} ข้อความ {} สถานะ Status Code : {} สถานะผลการส่ง {}'.format(command,TextMessage,r.status_code,r.text))
                print(messages)
                db_logger.info(command)
                SaveDB().save_request_history(self.display_name,
                                                self.position,
                                                        self.station_name,
                                                            'Reply',
                                                                command,
                                                                    command,
                                                                        r.status_code)
                return True
            else:
                messages = ('LINE : ทำรายการ NOK ส่งคำสั่ง {} ข้อความ {} ปัญหาคือ {}'.format(command,TextMessage,str(r.text)))
                print (messages)
                db_logger.warning(str(r.text))
                SaveDB().save_request_history(self.display_name,
                                                self.position,
                                                        self.station_name,
                                                            'Reply',
                                                                command,
                                                                    command,
                                                                        r.status_code)
                return True
        except Exception as e:
            messages = ('LINE : ทำรายการ NOK ส่งคำสั่ง {} ข้อความ {} ปัญหาคือ {}'.format(command,TextMessage,str(e)))
            print (messages)
            db_logger.warning(str(e))
            return False 
    def ReplyMessage(self,Reply_token,TextMessage):
        LINE_API = 'https://api.line.me/v2/bot/message/reply'
        # print('line API {}'.format(TextMessage))
        Authorization = 'Bearer {}'.format(self.line_token)
        print(Authorization)
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': Authorization
        }

        data = {
            "replyToken": Reply_token,
            "messages": [TextMessage], }

        data = json.dumps(data)
        # print('data to line {}'.format(data))
        r = requests.post(LINE_API, headers=headers, data=data)
        print(r.text)
        print(r.status_code)
        return r
    def PushMessage(self,push_new_messasge,user_id):
        
        LINE_API = 'https://api.line.me/v2/bot/message/push'
        # print('line API {}'.format(push_new_messasge))

        Authorization = 'Bearer {}'.format(self.line_token)
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': Authorization
        }

        data = {
            "to": user_id,
            "messages": [push_new_messasge], }

        # print('data to line {}'.format(data))
        data = json.dumps(data)
        r = requests.post(LINE_API, headers=headers, data=data)
        print(r.text)
        print(r.status_code)
        return r              
    def PushMessageNewRegistStationManager(self,flexmessages,area_line_user_id):
        #แจ้งเตือนกรณี ลงทะเบียนผู้จัดการสาขา
        #ทำการเช็คการตั้งค่าในระบบว่าอนุญาตให้แจ้งเตือน Flex หรือไม่
        # 1 = แจ้งเตือนกรณี ลงทะเบียนผู้จัดการสาขา
        result =  NotifyByRequest.objects.filter(id=1).first()
        flex_allow_send_to_user = result.flex_message_send_to_user
        print ('อนุญาติให้ทำการส่ง Flex หรือไม่ สถานะ :  {}'.format(flex_allow_send_to_user))
        if flex_allow_send_to_user == True :
            for send_user in area_line_user_id :
                line_area_id = send_user.userList_userid
                send_flex_allow = send_user.userList_notify
                # area_status_activate = send_user.userList_area_name.area_activate
                print ('line_id ที่จะต้องส่ง Flex {}'.format(line_area_id))
                print ('สถานะการแจ้งข้อความ {}'.format(send_flex_allow))
                # print ('Check ว่าผู้ใช้งานคนนี้่มี สถานะอยู่ใน Mode Active หรือไม่ {}'.format(area_status_activate))
                if send_flex_allow == True  :
                    self.PushMessage(flexmessages,line_area_id)
                else :
                    print ('ผู้ใช้งานคนนี้ไม่ต้องส่ง Flex')
        else :
            print ('รายการไม่อนุญาติให้ทำการส่ง Flex')
    def PushMessageAreaManagerApprovedNewStationManager(self,flexmessages,manager_user_id):
        #ทำการเช็คการตั้งค่าในระบบว่าอนุญาตให้แจ้งเตือน Flex หรือไม่
        # 3 = แจ้งเตือนกรณี ผู้จัดการเขต อนุมัติ ผู้จัดการสาขา
        result =  NotifyByRequest.objects.filter(id=3).first()
        flex_allow_send_to_user = result.flex_message_send_to_user
        print ('อนุญาติให้ทำการส่ง Flex หรือไม่ สถานะ :  {}'.format(flex_allow_send_to_user))
        if flex_allow_send_to_user == True :
            for send_user in manager_user_id :
                line_area_id = send_user.userList_userid
                send_flex_allow = send_user.userList_notify
                # area_status_activate = send_user.userList_area_name.area_activate
                print ('line_id ที่จะต้องส่ง Flex {}'.format(line_area_id))
                print ('สถานะการแจ้งข้อความ {}'.format(send_flex_allow))
                # print ('Check ว่าผู้ใช้งานคนนี้่มี สถานะอยู่ใน Mode Active หรือไม่ {}'.format(area_status_activate))
                if send_flex_allow == True  :
                    self.PushMessage(flexmessages,line_area_id)
                else :
                    print ('ผู้ใช้งานคนนี้ไม่ต้องส่ง Flex')
        else :
            print ('รายการไม่อนุญาติให้ทำการส่ง Flex')
    def PushMessageAreaSendRequestToAdminForApprove(self,flexmessages,admin_user_id):
        #ทำการเช็คการตั้งค่าในระบบว่าอนุญาตให้แจ้งเตือน Flex หรือไม่
        # 4 = แจ้งเตือนกรณี Admin อนุมัติระดับผู้จัดการเขต
        result =  NotifyByRequest.objects.filter(id=4).first()
        flex_allow_send_to_user = result.flex_message_send_to_user
        print ('อนุญาติให้ทำการส่ง Flex หรือไม่ สถานะ :  {}'.format(flex_allow_send_to_user))
        if flex_allow_send_to_user == True :
            for send_user in admin_user_id :
                line_area_id = send_user.userList_userid
                send_flex_allow = send_user.userList_notify
                print ('line_id ที่จะต้องส่ง Flex {}'.format(line_area_id))
                print ('สถานะการแจ้งข้อความ {}'.format(send_flex_allow))
                if send_flex_allow == True  :
                    self.PushMessage(flexmessages,line_area_id)
                else :
                    print ('ผู้ใช้งานคนนี้ไม่ต้องส่ง Flex')
        else :
            print ('รายการไม่อนุญาติให้ทำการส่ง Flex')
    def PushMessageAdminApprovedNewAreaManager(self,flexmessages,manager_user_id3):
        #ทำการเช็คการตั้งค่าในระบบว่าอนุญาตให้แจ้งเตือน Flex หรือไม่
        # 4 = แจ้งเตือนกรณี Admin อนุมัติระดับผู้จัดการเขต
        result =  NotifyByRequest.objects.filter(id=4).first()
        flex_allow_send_to_user = result.flex_message_send_to_user
        print ('อนุญาติให้ทำการส่ง Flex หรือไม่ สถานะ :  {}'.format(flex_allow_send_to_user))
        if flex_allow_send_to_user == True :
            for send_user in manager_user_id3 :
                line_area_id = send_user.userList_userid
                send_flex_allow = send_user.userList_notify
                print ('line_id ที่จะต้องส่ง Flex {}'.format(line_area_id))
                print ('สถานะการแจ้งข้อความ {}'.format(send_flex_allow))
                if send_flex_allow == True  :
                    self.PushMessage(flexmessages,line_area_id)
                else :
                    print ('ผู้ใช้งานคนนี้ไม่ต้องส่ง Flex')
        else :
            print ('รายการไม่อนุญาติให้ทำการส่ง Flex')
    def PushMessageAreraChangeNewArea(self,flexmessages,user_id):
        #ทำการเช็คการตั้งค่าในระบบว่าอนุญาตให้แจ้งเตือน Flex หรือไม่
        # 6 = แจ้งเตือนกรณี ผู้จัดการเขต แจ้งขอเปลี่ยนเขตใหม่
        result =  NotifyByRequest.objects.filter(id=6).first()
        flex_allow_send_to_user = result.flex_message_send_to_user
        print ('อนุญาติให้ทำการส่ง Flex หรือไม่ สถานะ :  {}'.format(flex_allow_send_to_user))
        if flex_allow_send_to_user == True :
            for send_user in user_id :
                line_area_id = send_user.userList_userid
                send_flex_allow = send_user.userList_notify
                print ('line_id ที่จะต้องส่ง Flex {}'.format(line_area_id))
                print ('สถานะการแจ้งข้อความ {}'.format(send_flex_allow))
                if send_flex_allow == True  :
                    self.PushMessage(flexmessages,line_area_id)
                else :
                    print ('ผู้ใช้งานคนนี้ไม่ต้องส่ง Flex')
        else :
            print ('รายการไม่อนุญาติให้ทำการส่ง Flex')
    def PushMessageAdminApprovedAreraChangeNewArea(self,flexmessages,user_id):
        #ทำการเช็คการตั้งค่าในระบบว่าอนุญาตให้แจ้งเตือน Flex หรือไม่
        # 7 = แจ้งเตือนกรณี Admin หรือ ผู้จัดการเขต มีการอนุมัติให้เปลี่ยนเขต
        result =  NotifyByRequest.objects.filter(id=7).first()
        flex_allow_send_to_user = result.flex_message_send_to_user
        print ('อนุญาติให้ทำการส่ง Flex หรือไม่ สถานะ :  {}'.format(flex_allow_send_to_user))
        if flex_allow_send_to_user == True :
            for send_user in user_id :
                line_area_id = send_user.userList_userid
                send_flex_allow = send_user.userList_notify
                print ('line_id ที่จะต้องส่ง Flex {}'.format(line_area_id))
                print ('สถานะการแจ้งข้อความ {}'.format(send_flex_allow))
                if send_flex_allow == True  :
                    self.PushMessage(flexmessages,line_area_id)
                else :
                    print ('ผู้ใช้งานคนนี้ไม่ต้องส่ง Flex')
        else :
            print ('รายการไม่อนุญาติให้ทำการส่ง Flex')

        
    

            
        