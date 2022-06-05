from zoneinfo import available_timezones
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, get_object_or_404, redirect
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage , FlexSendMessage
from line_bot.flex_messages import *
from line_bot.connecting_line_server import *
from apps.home.models import *
from line_bot.save_data_to_db import *
from line_bot.line_notifly import *


def liftpage(request):
    return render(request,'home/line_liff/liftpage.html')

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        payload = json.loads(request.body.decode('utf-8'))  # Convert data to json
        print('first payload', payload)
        if len(payload['events']) < 1 :
            print ('Verifly by line Server')
            pass
        elif len(payload['events']) > 0 :
            
            line_token = LineSetting.objects.all().first()
            line_bot_api = LineBotApi(line_token.line_token)
            user_id = payload['events'][0]['source']['userId']
            profile = line_bot_api.get_profile(user_id)
            # print(profile.display_name)
            # print(profile.user_id)
            # print(profile.picture_url)
            # print(profile.status_message)
            reply_token = payload['events'][0]['replyToken']
            if payload['events'][0]['type'] == 'follow' :    
                #ส่งไปบันทึกรายชื่อ
                SaveDB().save_new_user(profile.user_id,profile.display_name,profile.picture_url,profile.status_message)
                flexmessages = FlexMessages().Gressing_messages(profile.display_name)
                SendFlexMessages().ReplyMessage(reply_token,flexmessages)        
            if payload['events'][0]['type'] == 'postback' :
                user_profile = PersonUser.objects.filter(user_userid=user_id).first()
                command = payload['events'][0]['postback']['data']
                if command == 'register':
                    # 1. เช็คว่า userId นี้เคยมีการระบบตำแหน่งไว้ก่อนหน้านี้หรือไม่
                    # position_check = PersonUser.objects.filter(user_userid=user_id).first()
                    position_check = UserListCodeType.objects.filter(userList_userid=user_id).first()
                    print ('ตำแหน่งปัจจุบัน คือ {}'.format(position_check.userList_position))
                    # print ('position check : {}'.format(position_check))
                    # print ('ตำแหน่งปัจจุบัน คือ {}'.format(position_check.userList_position))
                    # if position_check.user_position == None :
                    # if position_check.userList_position == None :
                    if position_check.userList_position == None :
                        # กรณียังไม่เคยมีการเลือกตำแหน่ง
                        flexmessages = FlexMessages().SelectUserType()
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    else :
                        #กรณีมีการเลือกตำแหน่งไว้แล้ว ให้ส่งตำแหน่งเดิมกลับไป
                        #กรณีมีการเลือกตำแหน่งไว้แล้ว ให้ส่งตำแหน่งเดิมกลับไป
                        position_check = PersonUser.objects.filter(user_userid=user_id).first()
                        flexmessages = FlexMessages().DupicateRegister(position_check)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                elif 'STATION-REGISTER-PROCESS' in command:
                    
                    pass
                
                
                
                elif 'SELECT-REGISTER-' in command :
                    print ('command : {}'.format(command[16:]))
                    flexmessages = FlexMessages().ConfirmedPositionSelect(user_id,command[16:])
                    print ('flexmessages : {}'.format(flexmessages))
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'SELECT-TYPE-CONFIRM-' in command :
                    print ('command : {}'.format(command[20:]))
                    user_select_type = command[20:]
                    if user_select_type == 'UserType01' :
                        # ทำการบันทึกตำแหน่งที่ผู้ใช้เลือกไปที่ db
                        user_position_id = Position.objects.filter(position_type='UserType01').values_list('id',flat=True).first()
                        print ('user_position_id : {}'.format(user_position_id))
                        SaveDB().update_position_inapprove(user_id,user_position_id)
                        flexmessages = FlexMessages().SelectStationID()
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                    elif user_select_type == 'UserType02' :
                        # ระดับผู้ช่วยผู้จัดการ
                        pass
                    elif user_select_type == 'UserType03' :
                        # ระดับผู้จัดการเขต
                        area_list = AreaCodeType.objects.filter(area_activate=False).all()
                        flexmessages = FlexMessages().SelectAreaList(area_list)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                    elif user_select_type == 'UserType04' :
                        # ระดับผู้จัดการภาค
                        pass
                    elif user_select_type == 'UserType05' :
                        # ส่วนผู้ดูแลระบบ
                        pass
                
                # elif command == 'UserType01': 
                #     # UserType01 คือ ผู้จัดการสถานี
                #     # ทำการ Updated ตำแหน่งที่เลือกไปที่ PersonUser
                #     # เช็คว่าเคยมีการลงทะเบียนไว้หรือยัง
                #     position_check = PersonUser.objects.filter(user_userid=user_id).first()

                #     if position_check.user_position == None :
                #         # กรณียังไม่เคยเลือกตำแหน่งพนักงานเลย
                #         SaveDB().update_new_user(user_id,command)
                #         flexmessages = FlexMessages().SelectStationID()
                #         SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                #     else :
                #         #กรณีมีการเลือกตำแหน่งไว้แล้ว ให้ส่งตำแหน่งเดิมกลับไป
                #         position_check = PersonUser.objects.filter(user_userid=user_id).first()
                #         flexmessages = FlexMessages().DupicateRegister(position_check)
                #         SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                #         pass
                # elif command == 'UserType02': 
                #     # UserType02 คือ ผู้ช่่วยผู้จัดการ
                #     # ทำการ Updated ตำแหน่งที่เลือกไปที่ PersonUser
                #     # เช็คว่าเคยมีการลงทะเบียนไว้หรือยัง
                #     position_check = PersonUser.objects.filter(user_userid=user_id).first()

                #     if position_check.user_position == None :
                #         # กรณียังไม่เคยเลือกตำแหน่งพนักงานเลย
                #         SaveDB().update_new_user(user_id,command)
                #         flexmessages = FlexMessages().SelectStationID()
                #         SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                #     else :
                #         #กรณีมีการเลือกตำแหน่งไว้แล้ว ให้ส่งตำแหน่งเดิมกลับไป
                #         position_check = PersonUser.objects.filter(user_userid=user_id).first()
                #         flexmessages = FlexMessages().DupicateRegister(position_check)
                #         SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                #         pass
                # elif command == 'UserType03': 
                #     # ทำการ query และส่งรายชื่อผู้จัดการเขตที่ยังไม่ได้ทำการลงทะเบียนไปให้ผู้ใช้งาน
                #     area_list = AreaCodeType.objects.filter(area_activate=False).all()
                #     flexmessages = FlexMessages().SelectAreaList(area_list)
                #     SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                #     # print ('area_list : {}'.format(area_list))
                #     # for i in area_list :
                #     #     print ('i : {}'.format(i))
                #     pass
                #     # UserType03 คือ ผู้ช่่วยผเขต
                #     # ทำการ Updated ตำแหน่งที่เลือกไปที่ PersonUser
                #     # เช็คว่าเคยมีการลงทะเบียนไว้หรือยัง
                #     # position_check = PersonUser.objects.filter(user_userid=user_id).first()
                #     # if position_check.user_area == None :
                #     #     # กรณียังไม่เคยเลือกเขตเลย
                #     #     # SaveDB().update_new_user(user_id,command)
                        
                #     #     pass
                #     # else :
                #     #     #กรณีมีการเลือกตำแหน่งไว้แล้ว ให้ส่งตำแหน่งเดิมกลับไป
                #     #     position_check = PersonUser.objects.filter(user_userid=user_id).first()
                #     #     flexmessages = FlexMessages().DupicateRegister(position_check)
                #     #     SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                #     #     pass
                elif command == 'POSITION-NOK':
                    flexmessages = FlexMessages().SelectUserType()
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'stationregisterOK' in command:
                    station_site = command[17:]
                    print ('ระหัสสาขาที่ทำการลงทะเบียนคือ {}'.format(station_site))
                    # 1. ค้นหารายชื่อผู้จัดการเขตเพื่อส่งไปขออนุมัติ
                    area_in_this_site = StationProfile.objects.filter(station_site=station_site).first()
                    print ('area_in_this_site : {}'.format(area_in_this_site.station_area_manager))
                    # 2. ส่งแจ้งเตือน Line Notify ไปที่ line group ระบบจะทำงานทุกครั้ง แต่จะเช็คเงื่อนไขที่ def send_notify ว่ามีการเปิดการส่งไว้หรือไม่
                    creating_line_data().get_approve_new_station_manager(area_in_this_site,profile,line_token)
                    # 3. ส่ง reply flex message to user แจ้งสถานะรอการอนุมัติ
                    flexmessages = FlexMessages().Reply_approve_new_station_manager()
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    # 4. ส่งการแจ้งเตือนแบบ flex ไปที่ผู้ใช้ โดยเรียกใช้ def create flex message

                    


                    # ส่งไป update db ที่ PersonUser -- > user_station_name
                    # SaveDB().update_new_user_station_name(user_id,station_site)
                    # flexmessages = FlexMessages().StationRegisterCompleted()
                    # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                # elif 'AREA-REGISTER-PROCESS-CONFIRMED' in command:
                    

                #     area_userid = command[17:]
                #     print ('ผู้จัดการเขตที่ทำการลงทะเบียนคือ {}'.format(area_userid))
                    # ทำการ update ตำแหน่งผู้จัดการเขต
                    # SaveDB().update_new_user(user_id,'UserType03')
                    # # นำข้อมูลไป create ที่ตาราง area
                    # SaveDB().create_new_area_manager(user_id)
                    # # ลบข้อมูลในตาราง PersonUser
                    # SaveDB().delete_cacah_area(user_id)
                    # flexmessages = FlexMessages().StationRegisterCompleted()
                    # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'AREA-REGISTER-PROCESS' in command:
                    # ส่ง flex ให้ทางผู้ใช้งานทำการยื่นยันในรายชื่อที่ได้ทำการเลือกอีกครั้ง
                    if 'ENSURE' in command :
                        area_ID = command[28:]
                        print ('ID ผู้จัดการเขตที่ทำการลงทะเบียนคือ {}'.format(area_ID))
                        # ทำการส่งข้อมูลผู้จัดการเขตกลับไปให้ผู้ใช้งานทำการ confirme อีกครั้ง
                        flexmessages = FlexMessages().AreaManagerSendBackDetailToEnsure(area_ID)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    elif 'CONFIRMED' in command :
                        area_userid = command[31:]
                        print ('ผู้จัดการเขตที่ทำการลงทะเบียนคือ {}'.format(area_userid))
                        # 1. ทำการแจ้งเตือนไปที่ line group notify เพื่อแจ้งให้ admin approve
                        creating_line_data().get_approve_new_area_manager(profile,line_token)
                        # 2 . ส่ง reply flex message to user แจ้งสถานะรอการอนุมัติ
                        flexmessages = FlexMessages().Reply_inapprove_new_area_manager()
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        # 3. ทำการ set update table UserListCodeType set userList_position = 3  (ตำแหน่งผู้จัดการเขต)
                        # 4. ทำการ set update table UserListCodeType set userList_member_mode = inapprove  (อยู่ระหว่างการอนมัติจาก admin)
                        user_position_id = Position.objects.filter(position_type='UserType03').values_list('id',flat=True).first()
                        print ('user_position_id : {}'.format(user_position_id))
                        SaveDB().update_position_inapprove(user_id,user_position_id)

                        # ทำการ set update table UserListCodeType set userList_position = 3  (ตำแหน่งผู้จัดการเขต)
                        # user_position_id = 3
                        # SaveDB().update_position(user_id,user_position_id)
                        # ส่ง flex confirmed ทำรายการสำเร็จ 

                    elif 'RESENT' in command :
                        print ('ส่งรายการใหม่อีกครั้ง {}'.format(command))
                        area_list = AreaCodeType.objects.filter(area_activate=False).all()
                        flexmessages = FlexMessages().SelectAreaList(area_list)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    # 1. ทำการ query ไปที่ AreaCodeType where id = area_userid เพื่อส่งข้อมูลกลับไปให้ user ทำการ ยืนยันอีกครั้ง 


                    # ทำการ update ตำแหน่งผู้จัดการเขต
                    # SaveDB().update_new_user(user_id,'UserType03')
                    # # นำข้อมูลไป create ที่ตาราง area
                    # SaveDB().create_new_area_manager(user_id)
                    # # ลบข้อมูลในตาราง PersonUser
                    # SaveDB().delete_cacah_area(user_id)
                    # flexmessages = FlexMessages().StationRegisterCompleted()
                    # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif command == 'botlogin' :
                    # นำ userId ไปเช็คว่าเคยมีการลงทะเบียนไว้หรือยัง
                    # เช็คที่ตาราง StationProfile
                    line_token = LineSetting.objects.all().first()
                    user_check = PersonUser.objects.filter(user_userid=user_id).first()
                    if not user_check :
                        area_check = Area.objects.filter(user_userid=user_id).first()
                        if not area_check :
                            # flexmessages = FlexMessages().Gressing_messages(profile.display_name)
                            # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                        else :
                            if area_check.user_display_name != None :
                                line_bot_api.link_rich_menu_to_user(user_id, line_token.rich_select_munu)
                                flexmessages = FlexMessages().LoginSuccessed(profile)
                                SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            else :
                                flexmessages = FlexMessages().Gressing_messages(profile.display_name)
                                SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    else :
                        # ทำการส่งหน้า link menu
                        if user_check.user_position != None :
                            line_bot_api.link_rich_menu_to_user(user_id, line_token.rich_select_munu)
                            flexmessages = FlexMessages().LoginSuccessed(profile)
                            SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        else :
                                flexmessages = FlexMessages().Gressing_messages(profile.display_name)
                                SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                elif command == 'LOGOUT' :
                    line_bot_api.link_rich_menu_to_user(user_id, line_token.rich_main_menu)
                    flexmessages = FlexMessages().LogOutSuccessed(profile)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                elif command == 'SETTING' :
                    user_check = PersonUser.objects.filter(user_userid=user_id).first()
                    if not user_check :
                        flexmessages = FlexMessages().SettingAreaShowMenu(user_profile)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    else :
                        #เลือกรายการที่ส่วนผู้จัดการต้องการ
                        flexmessages = FlexMessages().StationSetting(user_profile)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)

                        pass
                elif command == 'XREPORT' :
                    # ตรวจสอบว่าผู้เรียกรายงานคือระดับไหน
                    line_token = LineSetting.objects.all().first()
                    user_check = PersonUser.objects.filter(user_userid=user_id).first()
                    # เช็คว่า userId อยู่ในระดับ ผู้จัดการสาขา หรือ ผู้ช่วยผู้จัดการ หรือไม่
                    if not user_check :
                        area_check = Area.objects.filter(user_userid=user_id).first()
                        if not area_check :
                            # ส่งเข้าไปเช็คต่อว่า userId ใช่ระดับ ผู้จัดการเขตหรือไม่
                            # flexmessages=PosReport().Xreport_Area_Selecter(user_id)
                            # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                        else :
                            # ค้นหารายชื่อสาขาที่ผู้จัดการเขตคนนี้ถูกกำหนดไว้อยู่ 
                            area_in_site = PersonUser.objects.filter(user_area=area_check.id).all()
                            print ('ค้นพบรายชื่อสถานีที่ Area คนนี้ดูแลอยู่มีจำนวน {}'.format(len(area_in_site)))
                            flexmessages=PosReport().Xreport_Area_Selecter(area_in_site)
                            SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                    else :
                        # ระดับ userId อยู่ในระดับผู้จัดการสาขา ให้ส่งข้อมูลในสาขานั้นๆไปให้
                        flexmessages=PosReport().Xreport_Station_Select(user_id,user_profile)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass

                    pass
                elif command == 'NOW-XREPORT' :
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().Xreport_Last_Shift(user_id,user_profile)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif command == 'DATE-XREPORT' :
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().Xreport_Date_Select(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'AREA-X-report-SITE' in command :
                    station_id = command[17:]
                    print ('ระหัสสาขาที่ต้องการเรียกรายงาน X Report คือ {}'.format(station_id))
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().Xreport_Date_Select(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif command == 'SMB' :
                    print ("User เรียกใช้รายงาน SMB")
                    # ตรวจสอบว่าผู้เรียกรายงานคือระดับไหน
                    line_token = LineSetting.objects.all().first()
                    user_check = PersonUser.objects.filter(user_userid=user_id).first()
                    # เช็คว่า userId อยู่ในระดับ ผู้จัดการสาขา หรือ ผู้ช่วยผู้จัดการ หรือไม่
                    if not user_check :
                        area_check = Area.objects.filter(user_userid=user_id).first()
                        if not area_check :
                            # ส่งเข้าไปเช็คต่อว่า userId ใช่ระดับ ผู้จัดการเขตหรือไม่
                            # flexmessages=PosReport().Xreport_Area_Selecter(user_id)
                            # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                        else :
                            # ถ้า userId ที่เรียกเข้ามาใช้งานคือ ผู้จัดการสาขา
                            flexmessages=PosReport().SMB_Area_Selecter(user_id)
                            SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                    else :
                        # ระดับ userId อยู่ในระดับผู้จัดการสาขา ให้ส่งข้อมูลในสาขานั้นๆไปให้
                        flexmessages=PosReport().SMB_Selecter_by_stie(user_id)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                elif command == 'NOW-SMB' :
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().SMB_Last_Shift(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif command == 'DATE-SMB' :
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().SMB_Date_Selecter(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'NOW-SMB-DATE' in command :
                    flexmessages=PosReport().SMB_Date_Report(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'SMBSHIFT' in command :
                    shift_id = command[8:9]
                    print ('Shift ที่ User เรียกรายงานคือ {}'.format(shift_id))
                    if shift_id != 'A' :
                        flexmessages=PosReport().SMB_Last_Shift(user_id)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    else :
                        flexmessages=PosReport().SMB_All_Shift(user_id)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)

                    pass
                elif 'AREA-SMB-SITE' in command :
                    station_id = command[13:]
                    print ('ระหัสสาขาที่ต้องการเรียกรายงาน X Report คือ {}'.format(station_id))
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().SMB_Date_Selecter(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif command == 'METER' :
                    print ("User เรียกใช้รายงาน METER")
                    # ตรวจสอบว่าผู้เรียกรายงานคือระดับไหน
                    line_token = LineSetting.objects.all().first()
                    user_check = PersonUser.objects.filter(user_userid=user_id).first()
                    # เช็คว่า userId อยู่ในระดับ ผู้จัดการสาขา หรือ ผู้ช่วยผู้จัดการ หรือไม่
                    if not user_check :
                        area_check = Area.objects.filter(user_userid=user_id).first()
                        if not area_check :
                            # ส่งเข้าไปเช็คต่อว่า userId ใช่ระดับ ผู้จัดการเขตหรือไม่
                            # flexmessages=PosReport().Xreport_Area_Selecter(user_id)
                            # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                        else :
                            # ถ้า userId ที่เรียกเข้ามาใช้งานคือ ผู้จัดการสาขา
                            flexmessages=PosReport().METER_Area_Selecter(user_id)
                            SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                    else :
                        # ระดับ userId อยู่ในระดับผู้จัดการสาขา ให้ส่งข้อมูลในสาขานั้นๆไปให้
                        flexmessages=PosReport().METER_Selecter_by_Site(user_id)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                elif command == 'NOW-METER' :
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().METER_Last_Shift(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif command == 'DATE-METER' :
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().METER_Date_Selecter(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'NOW-METER-DATE' in command :
                    flexmessages=PosReport().METER_Last_Shift(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'AREA-METER-SITE' in command :
                    station_id = command[15:]
                    print ('ระหัสสาขาที่ต้องการเรียกรายงาน X Report คือ {}'.format(station_id))
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().METER_Date_Selecter_Area(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif command == 'PRICE' :
                    print ("User เรียกใช้รายงาน PRICE")
                    # ตรวจสอบว่าผู้เรียกรายงานคือระดับไหน
                    line_token = LineSetting.objects.all().first()
                    user_check = PersonUser.objects.filter(user_userid=user_id).first()
                    # เช็คว่า userId อยู่ในระดับ ผู้จัดการสาขา หรือ ผู้ช่วยผู้จัดการ หรือไม่
                    if not user_check :
                        area_check = Area.objects.filter(user_userid=user_id).first()
                        if not area_check :
                            # ส่งเข้าไปเช็คต่อว่า userId ใช่ระดับ ผู้จัดการเขตหรือไม่
                            # flexmessages=PosReport().Xreport_Area_Selecter(user_id)
                            # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                        else :
                            # ถ้า userId ที่เรียกเข้ามาใช้งานคือ ผู้จัดการสาขา
                            flexmessages=PosReport().PRICE_Area(user_id)
                            SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                    else :
                        # ระดับ userId อยู่ในระดับผู้จัดการสาขา ให้ส่งข้อมูลในสาขานั้นๆไปให้
                        flexmessages=PosReport().PRICE(user_id)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                elif 'AREA-PRICE-SITE' in command :
                    station_id = command[15:]
                    print ('ระหัสสาขาที่ต้องการเรียกรายงาน X Report คือ {}'.format(station_id))
                    # จัดส่งรายงาน X-Report จากระบบ POS จาก Shift ล่าสุด
                    flexmessages=PosReport().PRICE(user_id)
                    SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif command == 'DETAILAREA' :
                    # ค้นหาจาก userId ของผู้จัดการ
                    user_area = PersonUser.objects.filter(user_userid=user_id ,user_area__isnull=False).first()
                    if not user_area :
                        print ('ค้นหาไม่พบรายละเอียดผู้จัดการเขต')
                        flexmessages=PosReport().DetailArea(user_id)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                    else :
                        print ('ค้นพบรายละเอียดผู้จัดการเขต {}'.format(user_area))
                        # print (user_area)
                        flexmessages=PosReport().AreaForStation(user_area)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                    pass
                elif command == 'ADDAREA':
                    # Query ข้อมูลรายชื่อผู้จัดการทั้งหมดส่งให้ทางผู้จัดการสาขาเลือกเอง
                    area_detail = Area.objects.all()
                    print ('จำนวนรายชือผู้จัดการเขต {}'.format(len(area_detail)))
                    if len(area_detail) == 0 :
                        flexmessages=PosReport().AreaLinsNotFlund(area_detail)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                    else:
                        flexmessages=PosReport().AreaList(area_detail)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'SAVEAREAID' in command:
                    area_id = command[10:]
                    print ('ID ของผู้จัดการเขต คือ  {}'.format(area_id))
                    SaveDB().update_area_to_station(user_id,area_id)
                    line_bot_api.reply_message(reply_token, TextSendMessage(text='ทำการบันทึกข้อมูลผู้จัดการเขตเรียบร้อย'))
                    # นำ ID ของ ผู้จัดการเขตไป Update ที่ตาราง StationProfile
                    # ส่งกลับไปแจ้ง User ว่าทำการตั้งค่าผู้จัดการเขตเรียบร้อย

                    
                    pass
                elif command == 'CHANGEAREA':
                    # ค้นหาจาก userId ของผู้จัดการ
                    current_area = PersonUser.objects.filter(user_userid=user_id).first()
                    # ค้นหา ID ของ ผู้จัดการเขตคนปัจจุบัน
                    all_area = Area.objects.all()
                    print ('ผู้จัดการเขตคนปัจจุบัน คือ {} ID {}'.format(current_area.user_area.user_display_name,current_area.user_area.id))
                    for all_areas in all_area :
                        print ('รายชื่อผู้จัดการเขตในระบบ ชื่อ {} ID {}'.format(all_areas.user_display_name,all_areas.id))
                    if not current_area :
                        # print ('ค้นหาไม่พบรายละเอียดผู้จัดการเขต')
                        # flexmessages=PosReport().DetailArea(user_id)
                        # SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                    else :
                        flexmessages=FlexMessages().ChangeAreaList(current_area,all_area)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        pass
                elif 'CHAMGE-NEW-AREAID' in command :
                    new_id_area = command[17:]
                    print ('ID ของผู้จัดการเขตคนใหม่คือ {}'.format(new_id_area))
                    SaveDB().update_area_to_station(user_id,new_id_area)
                    # ค้นหารายชื่อผู้จัดการเขตคนใหม่
                    current_area = PersonUser.objects.filter(user_userid=user_id).first()
                    text_message = 'ทำการเปลี่ยนผู้จัดการเขตเรียบร้อย คนใหม่คือ {}'.format(current_area.user_area.user_display_name)
                    line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message))
                elif command == 'STATION-CHAANGE' :
                    pass
            if payload['events'][0]['type'] == 'message' :
                if payload['events'][0]['message']['type'] == 'sticker' :
                    pass
                if payload['events'][0]['message']['type'] == 'text' :
                    text_message = payload['events'][0]['message']['text']
                    if 'ข้อความระบบ' in text_message :
                        print ('x'*200)
                        return HttpResponse (200)
                    elif 'station' in text_message :
                        station_id = text_message[7:]
                        station_list = StationProfile.objects.filter(station_site=station_id).first()
                        if not station_list :
                            flexmessages = FlexMessages().ConfirmStationFailed()
                            SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        else :
                            print ('รายชื่อสาขาที่ทำการลงทะเบียน คือ {}'.format(station_list))
                            flexmessages = FlexMessages().ConfirmedStationPass(station_list)
                            SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                            pass
                    elif text_message == 'botregister':
                        print ('text from user')
                        flexmessages = FlexMessages().Gressing_messages(profile.display_name)
                        SendFlexMessages().ReplyMessage(reply_token,flexmessages)
                        return HttpResponse (200)
        

        # print ('UserID is {}'.format(user_id))
        
        
        
        return HttpResponse (200)