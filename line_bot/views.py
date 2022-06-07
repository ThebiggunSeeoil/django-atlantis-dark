from ast import Break
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
from line_bot.pos_alpha.connect_db import *
from django.db.models import Count
from line_bot.pos_alpha.sql_command import *
from django.db.models import Q
from line_bot.creating_pos_flex_messages import *
import logging

db_logger = logging.getLogger('db')


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
                SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)        
            if payload['events'][0]['type'] == 'postback' :
                user_profile = UserListCodeType.objects.filter(userList_userid=user_id).first()
                command = payload['events'][0]['postback']['data']
                print ('command', command)
                if command == 'register':
                    # 1. เช็คว่า userId นี้เคยมีการระบบตำแหน่งไว้ก่อนหน้านี้หรือไม่
                    position_check = UserListCodeType.objects.filter(userList_userid=user_id).first()
                    print ('ตำแหน่งปัจจุบัน คือ {}'.format(position_check.userList_position))
                    print ('สถานะผู้ใช้งานปัจจุบัน คือ {}'.format(position_check.userList_member_mode))
                    if position_check.userList_member_mode == 'register' :
                        # กรณียังไม่เคยมีการเลือกตำแหน่ง
                        flexmessages = FlexMessages().SelectUserType()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    else :
                        #กรณีมีการเลือกตำแหน่งไว้แล้ว ให้ส่งตำแหน่งเดิมกลับไป
                        #กรณีมีการเลือกตำแหน่งไว้แล้ว ให้ส่งตำแหน่งเดิมกลับไป
                        position_check = PersonUser.objects.filter(user_userid=user_id).first()
                        flexmessages = FlexMessages().DupicateRegister(position_check)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        pass
                elif 'DISPLAY-STATION' in command :
                    if 'BRANCH' in command : 
                        manager_id = command[25:]
                        print ('manager_id', manager_id)
                        # เช็คสถานะ ผู้จัดการว่าเป็น singer หรือ multi
                        manager_takecare_type = UserListCodeType.objects.filter(id=manager_id).first()
                        print ('manager_takecare_type', manager_takecare_type.userList_takecare_station)
                        if manager_takecare_type.userList_takecare_station == 'single' :
                            print ('ผู้จัดการมีสถานะเป็น SINGER')
                            # ค้นหาสถานีหลักที่ดูแลอยู่
                            # 1. ค้นหาสถานีหลักที่ดูแลอยู่
                            main_station_list = UserListCodeType.objects.filter(id=manager_id).all()
                            main_station = UserListCodeType.objects.filter(id=manager_id).first()
                            area_name = AreaCodeType.objects.filter(area_code_type=main_station.userList_area_name.id).first()
                            print ('area_name', area_name.area_code_name)
                            print ('main_station', main_station.userList_station_name.station_name)
                            # 2. ค้นหาสถานีย่อยที่ดูแลอยู่
                            multi_station = MultiStationTackCare.objects.filter(multi_manager_number=manager_id,multi_active=True).all()
                            # len
                            for i in multi_station :
                                print ('multi_station', i.multi_station_number.station_name)
                            # เรียกใช้ Flex Message
                            flexmessages = FlexMessages().StationDetail(main_station_list,main_station,multi_station,area_name)
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        elif manager_takecare_type.userList_takecare_station == 'multi' :
                            print ('ผู้จัดการมีสถานะเป็น MULTI')
                            # 1. ค้นหาสถานีหลักที่ดูแลอยู่
                            main_station_list = UserListCodeType.objects.filter(id=manager_id).all()
                            main_station = UserListCodeType.objects.filter(id=manager_id).first()
                            area_name = AreaCodeType.objects.filter(area_code_type=main_station.userList_area_name.id).first()
                            print ('main_station', main_station.userList_station_name.station_name)
                            # 2. ค้นหาสถานีย่อยที่ดูแลอยู่
                            multi_station = MultiStationTackCare.objects.filter(multi_manager_number=manager_id,multi_active=True).all()
                            # len
                            for i in multi_station :
                                print ('multi_station', i.multi_station_number.station_name)
                            # เรียกใช้ Flex Message
                            # area_name = CodeInAreaDetail.objects.filter(id=area_id).first()
                            flexmessages = FlexMessages().StationDetail(main_station_list,main_station,multi_station,area_name)
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'AREA' in command :
                        print ('คำสั่งที่รับมาคือ AREA')
                        area_id = command[23:]
                        print ('area_id', area_id)
                        # นำ id ของผู้จัดการเขต ไป qurey หาสถานีทั้งหมดที่ดูแลอยู่ 
                        # area_id คือ Table id จาก table CodeInAreaDetail
                        # ค้นหาชื่อเขต
                        area_name = CodeInAreaDetail.objects.filter(id=area_id).first()
                        all_station_in_this_area_manager = StationProfile.objects.filter(station_area_code=area_id).all()
                        station_has_manager = UserListCodeType.objects.filter(userList_area_name=area_id,userList_position=1).first()
                        # print ('station_has_manager {} site take care {}'.format(station_has_manager.id, station_has_manager.userList_station_name.id))
                        # for i in all_station_in_this_area_manager :
                        #     # print ('station name {} station id {}'.format(i.station_name,i.id))
                        #     if i.id == station_has_manager.userList_station_name.id :
                        #         print ('find')

                        flexmessages = FlexMessages().ShowStationListInArea(all_station_in_this_area_manager,station_has_manager,area_name)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages) 
                    elif 'CHANGE' in command :
                        print ('คำสั่งที่รับมาคือ CHANGE')
                        # แสดงเขตที่อยู่ในระบบทั้งหมด
                        # ค้นหาเจ้าของเขต เพื่อ filter ไม่ให้ส่งเขตตัวเองไปแสดง
                        manager_in_area = UserListCodeType.objects.filter(userList_userid=user_id,userList_position=3).first()
                        result=StationProfile.objects.filter(~Q(station_area_code=manager_in_area.userList_area_name.id)).values('station_area_code__code_in_area_code_name','station_area_code__id').annotate(entries=Count('id'))
                        print ('result', result)
                        # for i in all_area_in_this_system :
                        #     print ('area name {} area code {}'.format(i.area_code_name,i.area_code_type))
                        flexmessages = FlexMessages().ShowAreaListInStation(result)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'SHOW' in command :
                        print ('คำสั่งที่รับมาคือ SHOW')
                        area_show = command[20:]
                        print ('area_show', area_show)

                        data_command = 'DISPLAY-STATION-SHOW-ID'
                        data_station_command = 'CODE'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('CODE'):])
                        code_id = (command[command.index(data_station_command) + len(data_station_command): command.index('END'):])
                        if manager_id == 'inwaiting' :
                            # หมายถึงเขตนี้ ตำแหน่งผู้จัดการเขตว่างอยู่
                            print ('คำสั่งที่รับมาคือ SHOW inwaiting')
                            print ('ที่ตำแหน่ง Area ID {} พบว่า ไม่มีการ SET ผู้จัดการเขตไว้'.format(code_id))
                            # ค้นหาสาขาที่อยู่ในเขตนี้ทั้งหมด
                            area_station = StationProfile.objects.filter(station_area_code__id=code_id).all()
                            station_has_manager = UserListCodeType.objects.filter(userList_userid=user_id,userList_position=3).first()
                            # ค้นหา ID ของ สถานีที่ต้องจะย้าย
                            area_id= CodeInAreaDetail.objects.filter(id=code_id).first()
                            manager_detail = '5555'
                            
                            flexmessages = FlexMessages().ShowSiteInAreaNoManager(area_station,station_has_manager,manager_detail,area_id)
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        else : 
                            print ('คำสั่งที่รับมาคือ SHOW')
                            
                            # area_show คือ table Id ของ AreaCodeType
                            # ค้นหา area code ของ area_show
                            area_code_id = AreaCodeType.objects.filter(id=manager_id).first()
                            #ค้นหาข้อมูลสถานีทั้งหมดที่อยู่ในเขตที่ต้องการแสดง
                            area_station = StationProfile.objects.filter(station_area_code__id=area_code_id.area_code_type.id).all()
                            manager_detail = AreaCodeType.objects.filter(id=manager_id).first()
                            station_has_manager = UserListCodeType.objects.filter(userList_userid=user_id,userList_position=3).first()
                            if station_has_manager == None :
                                print ('ไม่มีสถานีที่ดูแลอยู่ในเขตนี้')
                                manager_detail_2 = AreaCodeType.objects.filter(id=manager_id).first()
                                print ('manager_detail_2', manager_detail_2.area_code_name)
                                # ค้นหาข้อมูลผู้จัดการเขต
                                message = 'ไม่สามารถแสดงข้อมูลในเขต {} ได้ อาจจะเนื่องด้วย ผู้จัดการเขตคุณ {} ยังไม่ได้ทำการลงทะเบียน Line Bot'.format(manager_detail.area_code_type,manager_detail.area_code_name)
                                line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                                # flexmessages = FlexMessages().ShowSiteInArea(area_station,station_has_manager,manager_detail)
                                # SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                                
                            else :
                                print ('station_has_manager {} '.format(station_has_manager))
                                print ('station_has_manager {}'.format(station_has_manager.id))
                                for i in area_station :
                                    print ('station name {} station id {}'.format(i.station_name,i.id))
                                flexmessages = FlexMessages().ShowSiteInArea(area_station,station_has_manager,manager_detail)
                                SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                elif 'MAIN-AREA-REGISTER-PROCESS' in command :
                    print ('กรณีที่มีการลงทะเบียนสมาชิก')
                    if 'SELECTER' in command:
                        position_selecter = 'UserType04'
                        flexmessages = FlexMessages().ConfirmedPositionSelect(user_id,position_selecter)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CONFIRMPOSITION' in command :
                        print ('กรณีที่มีการยืนยันตำแหน่ง')
                        # ส่ง line notify แจ้งเตือนสถานะ ได้รับการอนุมัติจาก admin แล้ว
                        manager_user_id2 = UserListCodeType.objects.filter(userList_userid=user_id).first()
                        creating_line_data().send_approve_new_main_area(manager_user_id2,profile,line_token)

                        flexmessages = FlexMessages().Reply_approve_main_area_manager(profile)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)

                        user_position_id = Position.objects.filter(position_type='UserType04').values_list('id',flat=True).first()
                        print ('user_position_id : {}'.format(user_position_id))
                        SaveDB().update_position_inapprove(user_id,user_position_id,None,None)
                        user_line_profile = UserListCodeType.objects.filter(userList_userid=user_id).first()
                        flexmessages = FlexMessages().MainAreaSendToAdminApprove(user_line_profile)
                        admin_user_id = UserListCodeType.objects.filter(userList_position=5).all()
                        SendFlexMessages(payload).PushMessageAreaSendRequestToAdminForApprove(flexmessages,admin_user_id)
                    elif 'APPROVED' in command :
                        data_command = 'MAIN-AREA-REGISTER-PROCESS-APPROVED-ID'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('END'):])
                        print ('manager_id : {}'.format(manager_id))
                        manager_user_id2 = UserListCodeType.objects.filter(id=manager_id).first()
                        manager_user_id3 = UserListCodeType.objects.filter(id=manager_id).all()
                        print ('main manager_id_approved : {}'.format(manager_id))
                        
                        
                        # Query to check last status approve if approved reply another already approved or inapprove go to below process 
                        if manager_user_id2.userList_activate == False and manager_user_id3.userList_approved_datetime == None : 
                            # ส่ง line notify แจ้งเตือนสถานะ ได้รับการอนุมัติจาก admin แล้ว
                            creating_line_data().get_approve_new_main_area_manager(manager_user_id2,line_token)
                            # ส่ง Flex message ส่งไปให้ผู้จัดการเขตรับทราบ Admin approved แล้ว
                            flexmessages = FlexMessages().AdminApprovedNewMainAreaManager(manager_user_id2)
                            # ค้นหา area manager user id เพื่อส่งการแจ้งเตือน ได้รับอนุมัติจาก Admin แล้ว 
                            
                            
                            SendFlexMessages(payload).PushMessageAdminApprovedNewAreaManager(flexmessages,manager_user_id3)

                            # ส่งไป update db table UserListCodeType set update userList_member_mode='approved',userList_approved_datetime=datetime.now(),userList_activate=True
                            SaveDB().update_position_approve(manager_user_id2)
                            # send reply message แจ้งการอนุมัติจาก admin แล้ว
                            message = 'ทำรายการอนุมัติ ตำแหน่งผู้จัดการภาค ให้กับคุณ {} เรียบร้อยแล้ว'.format(manager_user_id2.userList_display_name)
                            line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                        else :
                            try :
                                date_approve = manager_user_id3.userList_approved_datetime.strftime("%d-%m-%Y %H:%M")
                            except :
                                date_approve = 'พบปัญหาในการค้นหาเวลาอนุมัติ'
                            message = 'ตำแหน่งผู้จัดการภาค ของคุณ {} ได้รับการอนุมัติแล้วเมื่อ {}'.format(manager_user_id2.userList_display_name,date_approve)
                            line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                            pass
                    elif 'REJECT' in command :
                        data_command = 'MAIN-AREA-REGISTER-PROCESS-REJECT-ID'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('END'):])
                        print ('main manager_id_rejected : {}'.format(manager_id))
                        manager_user_id2 = UserListCodeType.objects.filter(id=manager_id).first()
                        manager_user_id3 = UserListCodeType.objects.filter(id=manager_id).all()
                        # ทำการเช็คว่าก่้อนหน้าเคยได้รับการ approved หรือยัง
                        last_member_status = manager_user_id2.userList_member_mode
                        print ('last member status : {}'.format(manager_user_id2.userList_member_mode))
                        if last_member_status == 'approved' :
                            print ('สถานะอยู่ในสถานะ approved')
                            # ส่ง reply เพื่อยืนยันการยกเลิกสถานะ approved
                            flexmessages = FlexMessages().UnapprovedMember(manager_user_id2) # ต้องการแค่ ID ของพนักงานที่ต้องการยกเลิกการ approved
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        else :
                            # ส่ง line notify แจ้งเตือนสถานะ ได้รับการอนุมัติจาก admin แล้ว
                            creating_line_data().send_rejected_new_main_area_manager(manager_user_id2,line_token)
                            # ส่ง Flex message ส่งไปให้ผู้จัดการเขตรับทราบ Admin approved แล้ว
                            flexmessages = FlexMessages().AdminRejectedNewMainAreaManager(manager_user_id2)
                            # ค้นหา area manager user id เพื่อส่งการแจ้งเตือน ได้รับอนุมัติจาก Admin แล้ว 
                            SendFlexMessages(payload).PushMessageAdminApprovedNewAreaManager(flexmessages,manager_user_id3)
                            # send reply message แจ้งการอนุมัติจาก admin แล้ว
                            SaveDB().unapproved_member(manager_user_id2)
                            message = 'ทำรายการไม่อนุมัติ ตำแหน่งผู้จัดการภาค ให้กับคุณ {} เรียบร้อยแล้ว'.format(manager_user_id2.userList_display_name)
                            line_bot_api.reply_message(reply_token, TextSendMessage(text=message)) 
                elif 'ADMIN-REGISTER-PROCESS' in command :
                    if 'SELECTER' in command:
                        position_selecter = 'UserType05'
                        flexmessages = FlexMessages().ConfirmedPositionSelect(user_id,position_selecter)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CONFIRMPOSITION' in command:
                        print ('ตำแหน่งที่สมัครสมาชิกคือ {}'.format(command))
                        flexmessages = FlexMessages().AdminConfirmCode()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CANCEL' in command:
                        flexmessages = FlexMessages().SelectUserType()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    pass
                elif 'STATION-REGISTER-PROCESS' in command:
                    if 'SELECTER' in command: # ส่ง Flex เพื่อให้ผู้ใช้ยืนยันว่่าต้องการดำเนินการภายใต้ตำแหน่ง ผู้จัดการสาขา ใช่หรือไม่
                        position_selecter = 'UserType01'
                        flexmessages = FlexMessages().ConfirmedPositionSelect(user_id,position_selecter)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CONFIRMPOSITION' in command:
                        # ทำการบันทึกตำแหน่งที่ผู้ใช้เลือกไปที่ db
                        # user_position_id = Position.objects.filter(position_type='UserType01').values_list('id',flat=True).first()
                        # print ('user_position_id : {}'.format(user_position_id))
                        # SaveDB().update_position_inapprove(user_id,user_position_id)
                        flexmessages = FlexMessages().SelectStationID()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'STATION-REGISTER-PROCESS-CONFIRM-STATION-ID' in command:
                        station_site = command[43:]
                        print ('station_id : {}'.format(station_site))
                        # 1. ค้นหารายชื่อผู้จัดการเขตเพื่อส่งไปขออนุมัติ
                        area_in_this_site = StationProfile.objects.filter(station_site=station_site).first()
                        print ('area_in_this_site : {}'.format(area_in_this_site.station_area_code.code_in_area_code_name))
                        # 2. ส่งแจ้งเตือน Line Notify ไปที่ line group ระบบจะทำงานทุกครั้ง แต่จะเช็คเงื่อนไขที่ def send_notify ว่ามีการเปิดการส่งไว้หรือไม่
                        creating_line_data().get_approve_new_station_manager(area_in_this_site,profile,line_token)
                        # 3. ส่ง reply flex message to user แจ้งสถานะรอการอนุมัติ
                        flexmessages = FlexMessages().Reply_approve_new_station_manager(profile,area_in_this_site)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        # 3. ทำการบันทึกสถานะ inapprove ลง db 
                        user_position_id = Position.objects.filter(position_type='UserType01').values_list('id',flat=True).first()
                        print ('user_position_id : {}'.format(user_position_id))
                        SaveDB().update_position_inapprove(user_id,user_position_id,area_in_this_site,None)
                        # 4. ส่งการแจ้งเตือนแบบ flex ไปที่ผู้ใช้ โดยเรียกใช้ def create flex message
                        # 4.1 ค้นหา line user_id ของ ผู้จัดการเขต
                        # 5 คือ table id ของ ตำแหน่งผู้จัดการเขต
                        # 6 ค้นหา Table ID ของผู้จัดการ ผู้ที่ขออนุมัติ
                        manager_table_id = UserListCodeType.objects.filter(userList_userid=user_id).values_list('id',flat=True).first()
                        
                        # ค้นหาข้อมูลผู้จัดการเขต area_line_user_id
                        # area_name = AreaCodeType.objects.filter(area_code_type=area_in_this_site.station_area_code.id).first()
                        area_line_user_id = UserListCodeType.objects.filter(userList_area_name=area_in_this_site.station_area_code.id,userList_position=3).all()
                        print ('area_line_user_id : {}'.format(area_line_user_id))
                        
                        
                        
                        flexmessages = FlexMessages().NotifyAreaManagerForGetApproveNewManager(profile,area_in_this_site,manager_table_id)
                        SendFlexMessages(payload).PushMessageNewRegistStationManager(flexmessages,area_line_user_id)
                    elif 'NEWSITE' in command:
                        station_site = command[32:]
                        print ('station_id : {}'.format(station_site))
                        # 1. ค้นหารายชื่อผู้จัดการเขตเพื่อส่งไปขออนุมัติ
                        area_in_this_site = StationProfile.objects.filter(station_site=station_site).first()
                        # นำ area_in_this_site.station_area_code.id ไปค้นหา ผู้จัดการเขตที่ AreaCodeType
                        area_name_UserList_codeType = UserListCodeType.objects.filter(userList_area_name=area_in_this_site.station_area_code.id).first()
                        area_name_AreaCodeType = AreaCodeType.objects.filter(area_code_type=area_in_this_site.station_area_code.id).first()
                        List_area_name_AreaCodeType = UserListCodeType.objects.filter(userList_area_name=area_in_this_site.station_area_code.id,userList_position=3).all()
                        print ('area_in_this_site : {}'.format(area_in_this_site.station_area_code.code_in_area_code_name))
                        # # 2. ส่งแจ้งเตือน Line Notify ไปที่ line group ระบบจะทำงานทุกครั้ง แต่จะเช็คเงื่อนไขที่ def send_notify ว่ามีการเปิดการส่งไว้หรือไม่
                        creating_line_data().get_approve_add_more_station_manager(area_in_this_site,profile,line_token,area_name_UserList_codeType,area_name_AreaCodeType)
                        # # 3. ส่ง reply flex message to user แจ้งสถานะรอการอนุมัติ
                        flexmessages = FlexMessages().Reply_approve_add_more_station_manager(profile,area_in_this_site,area_name_AreaCodeType)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                       
                        # user_position_id = Position.objects.filter(position_type='UserType01').values_list('id',flat=True).first()
                        # print ('user_position_id : {}'.format(user_position_id))
                        # SaveDB().update_position_inapprove(user_id,user_position_id,area_in_this_site,None)
                        # # 4. ส่งการแจ้งเตือนแบบ flex ไปที่ผู้ใช้ โดยเรียกใช้ def create flex message
                        # # 4.1 ค้นหา line user_id ของ ผู้จัดการเขต
                        # # 5 คือ table id ของ ตำแหน่งผู้จัดการเขต
                        # # 6 ค้นหา Table ID ของผู้จัดการ ผู้ที่ขออนุมัติ
                        manager_table_id = UserListCodeType.objects.filter(userList_userid=user_id).values_list('id',flat=True).first()
                        # # ค้นหาข้อมูลผู้จัดการเขต area_line_user_id
                        # area_line_user_id = UserListCodeType.objects.filter(userList_area_name=area_in_this_site.station_area_manager.id,userList_position=3).all()
                        # print ('area_line_user_id : {}'.format(area_line_user_id))
                        flexmessages = FlexMessages().NotifyAreaManagerForGetApproveMultiManager(profile,area_in_this_site,manager_table_id)
                        SendFlexMessages(payload).PushMessageNewRegistStationManager(flexmessages,List_area_name_AreaCodeType)
                    elif 'OKMORESITE' in command: # ผู้จัดการเขตอนุมัติ ให้ผู้จัดการดูแลสาขาอื่นๆได้
                        print ('OKMORESITE')
                        approved_user_id = command[36:]
                        print ('approved_user_id : {}'.format(approved_user_id))
                        data_command = 'STATION-REGISTER-PROCESS-OKMORESITE-USERID'
                        data_station_command = 'STATIONID'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('STATIONID'):])
                        station_id = (command[command.index(data_station_command) + len(data_station_command): command.index('END'):])
                        manager_user_id = UserListCodeType.objects.filter(id=manager_id).all()
                        manager_user_id2 = UserListCodeType.objects.filter(id=manager_id).first()
                        print ('manager_id : {}'.format(manager_id))
                        print ('station_id : {}'.format(station_id))
                        # # ทำการแจ้งเตือนสถานะการ อนุมัติ ไปที่ line notify
                        area_in_this_site = StationProfile.objects.filter(id=station_id).first()
                        area_name_AreaCodeType = AreaCodeType.objects.filter(area_code_type=area_in_this_site.station_area_code.id).first()
                        print ('station name : {}'.format(area_in_this_site.station_name))
                        area_name_approved = AreaCodeType.objects.filter(area_code_type=manager_user_id2.userList_area_name.id).first()
                        creating_line_data().send_approve_add_more_station_manager(area_in_this_site,profile,line_token,manager_user_id2,area_name_approved)
                        # # ทำการแจ้งเตือนไปที่่ผู้จัดการสถานีด้วย Flex ว่าได้รับการอนุมัติแล้ว
                        # # ค้นหาข้อมูลผู้จัดการสาขา area_line_user_id
                        
                        print ('manager_user_id : {}'.format(manager_user_id))
                        flexmessages = FlexMessages().AreaApproveNewStationManager(area_in_this_site,manager_user_id2,area_name_approved)
                        SendFlexMessages(payload).PushMessageAreaManagerApprovedNewStationManager(flexmessages,manager_user_id)
                        # # ทำการ set add db MultiStationTackCare --> multi_manager_name = manager_user_id2.userList_display_name , multi_manager_id = manager_user_id2.id , multi_station_id=area_in_this_site.id
                        SaveDB().addmultistationmanager(manager_user_id2,area_in_this_site)
                        # # send reply message แจ้งการอนุมัติจาก admin แล้ว
                        message = 'ทำรายการอนุมัติ ตำแหน่งผู้จัดการสาขา {} ให้กับคุณ {} เรียบร้อยแล้ว'.format(area_in_this_site.station_name,manager_user_id2.userList_display_name)
                        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))  
                    elif 'FAILEDMORESITE' in command: # ผู้จัดการเขต ไม่อนุมัติ ให้ผู้จัดการดูแลสาขาอื่นๆได้
                        print ('FAILEDMORESITE')
                        data_command = 'STATION-REGISTER-PROCESS-FAILEDMORESITE-USERID'
                        data_station_command = 'STATIONID'
                        
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('STATIONID'):])
                        station_id = (command[command.index(data_station_command) + len(data_station_command): command.index('END'):])
                        print ('manager_id_remove : {}'.format(manager_id))
                        print ('station_id_remove : {}'.format(station_id))
                        manager_user_id = UserListCodeType.objects.filter(id=manager_id).all()
                        manager_user_id2 = UserListCodeType.objects.filter(id=manager_id).first()
                        area_in_this_site = StationProfile.objects.filter(id=station_id).first()
                        manager_table_id = UserListCodeType.objects.filter(userList_userid=user_id).values_list('id',flat=True).first()
                        area_name_AreaCodeType = AreaCodeType.objects.filter(area_code_type=area_in_this_site.station_area_code.id).first()
                        
                        # ส่ง line notify แจ้งเตือนสถานะ ได้รับการอนุมัติจาก admin แล้ว
                        creating_line_data().send_rejected_add_more_station_manager(area_in_this_site,profile,line_token,area_name_AreaCodeType)
                        flexmessages = FlexMessages().Area_Un_approve_add_more_station_manager(profile,area_in_this_site,area_name_AreaCodeType)
                        SendFlexMessages(payload).PushMessageNewRegistStationManager(flexmessages,manager_user_id)                        # # ทำการ set add db MultiStationTackCare --> multi_manager_name = manager_user_id2.userList_display_name , multi_manager_id = manager_user_id2.id , multi_station_id=area_in_this_site.id
                        # # send reply message แจ้งการอนุมัติจาก admin แล้ว
                        message = 'ทำรายการไม่อนุมัติ ขอดูแลสาขาเพิ่ม {} ให้กับคุณ {} เรียบร้อยแล้ว'.format(area_in_this_site.station_name,manager_user_id2.userList_display_name)
                        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                    elif 'RESENT' in command:
                        flexmessages = FlexMessages().SelectStationID()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'ADD-MORE' in command:
                        flexmessages = FlexMessages().SelectAddMoreStationID()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CANCEL' in command:
                        flexmessages = FlexMessages().SelectUserType()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'APPROVED' in command:
                        approved_user_id = command[36:]
                        print ('approved_user_id : {}'.format(approved_user_id))
                        data_command = 'STATION-REGISTER-PROCESS-APPROVED-USERID'
                        data_station_command = 'STATIONID'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('STATIONID'):])
                        station_id = (command[command.index(data_station_command) + len(data_station_command): command.index('END'):])
                        print ('manager_id : {}'.format(manager_id))
                        print ('station_id : {}'.format(station_id))
                        manager_user_id = UserListCodeType.objects.filter(id=manager_id).all()
                        manager_user_id2 = UserListCodeType.objects.filter(id=manager_id).first()
                         
                        area_name_approved = AreaCodeType.objects.filter(area_code_type=manager_user_id2.userList_area_name.id).first()
                        # ทำการแจ้งเตือนสถานะการ อนุมัติ ไปที่ line notify
                        area_in_this_site = StationProfile.objects.filter(id=station_id).first()
                        print ('station name : {}'.format(area_in_this_site.station_name))
                        creating_line_data().send_approve_new_station_manager(area_in_this_site,profile,line_token,manager_user_id2,area_name_approved)
                        # ทำการแจ้งเตือนไปที่่ผู้จัดการสถานีด้วย Flex ว่าได้รับการอนุมัติแล้ว
                        # ค้นหาข้อมูลผู้จัดการสาขา area_line_user_id
                        
                        print ('manager_user_id : {}'.format(manager_user_id))
                        flexmessages = FlexMessages().AreaApproveNewStationManager(area_in_this_site,manager_user_id2,area_name_approved)
                        SendFlexMessages(payload).PushMessageAreaManagerApprovedNewStationManager(flexmessages,manager_user_id)
                        # ทำการ set update db UserListCodeType --> userList_member_mode = 'approved' , userList_approved_datetime = time.now , userList_activate=True
                        SaveDB().update_position_approve(manager_user_id2)
                        # send reply message แจ้งการอนุมัติจาก admin แล้ว
                        message = 'ทำรายการอนุมัติ ตำแหน่งผู้จัดการสาขา {} ให้กับคุณ {} เรียบร้อยแล้ว'.format(area_in_this_site.station_name,manager_user_id2.userList_display_name)
                        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))                
                    elif 'REJECT' in command :
                        data_command = 'STATION-REGISTER-PROCESS-REJECT-USERID'
                        data_station_command = 'STATIONID'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('STATIONID'):])
                        station_id = (command[command.index(data_station_command) + len(data_station_command): command.index('END'):])
                        print ('manager_id_rejected : {}'.format(manager_id))
                        print ('station_id_rejected : {}'.format(station_id))
                        manager_user_id2 = UserListCodeType.objects.filter(id=manager_id).first()
                        manager_user_id3 = UserListCodeType.objects.filter(id=manager_id).all()
                        station_profile = StationProfile.objects.filter(id=station_id).first()
                        # ทำการเช็คว่าก่้อนหน้าเคยได้รับการ approved หรือยัง
                        last_member_status = manager_user_id2.userList_member_mode
                        print ('last member status : {}'.format(manager_user_id2.userList_member_mode))
                        if last_member_status == 'approved' :
                            print ('สถานะอยู่ในสถานะ approved')
                            # ส่ง reply เพื่อยืนยันการยกเลิกสถานะ approved
                            flexmessages = FlexMessages().UnapprovedMember(manager_user_id2) # ต้องการแค่ ID ของพนักงานที่ต้องการยกเลิกการ approved
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        else :
                            # ส่ง line notify แจ้งเตือนสถานะ ได้รับการอนุมัติจาก admin แล้ว
                            creating_line_data().send_rejected_new_station_manager(manager_user_id2,line_token,station_profile)
                            # ส่ง Flex message ส่งไปให้ผู้จัดการเขตรับทราบ Admin approved แล้ว
                            flexmessages = FlexMessages().AreaRejectedStationManager(manager_user_id2,station_profile)
                            # ค้นหา area manager user id เพื่อส่งการแจ้งเตือน ได้รับอนุมัติจาก Admin แล้ว 
                            SendFlexMessages(payload).PushMessageAdminApprovedNewAreaManager(flexmessages,manager_user_id3)
                            # send reply message แจ้งการอนุมัติจาก admin แล้ว
                            SaveDB().unapproved_member(manager_user_id2)
                            message = 'ทำรายการไม่อนุมัติ ตำแหน่งผู้จัดการสาขา ให้กับคุณ {} เรียบร้อยแล้ว'.format(manager_user_id2.userList_display_name)
                            line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                    elif 'ADDSTATION' in command :
                        flexmessages = FlexMessages().SelectAddMoreStationID() 
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'REMOVE' in command : # ยกเลิกสาขาที่ดูแลอยู่
                        print ('remove station')
                        data_command = 'STATION-REGISTER-PROCESS-REMOVE-ID'
                        data_station_command = 'BRANCH'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('BRANCH'):])
                        station_id = (command[command.index(data_station_command) + len(data_station_command): command.index('END'):])
                        print ('manager_id_remove : {}'.format(manager_id))
                        print ('station_id_remove : {}'.format(station_id))
                        SaveDB().set_multi_to_flalse(manager_id,station_id)
                        # ค้นหารายชื่อสาขาที่ทำการยกเลิก
                        branch = StationProfile.objects.filter(id=station_id).first()
                        message = 'ทำรายการยกเลิกการดูแลสาขา {} เรียบร้อยแล้ว'.format(branch.station_name)
                        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                elif 'AREA-REGISTER-PROCESS' in command: # ส่ง flex ให้ทางผู้ใช้งานทำการยื่นยันในรายชื่อที่ได้ทำการเลือกอีกครั้ง
                    if 'ENSURE' in command :
                        area_ID = command[28:]
                        print ('ID ผู้จัดการเขตที่ทำการลงทะเบียนคือ {}'.format(area_ID))
                        # ทำการส่งข้อมูลผู้จัดการเขตกลับไปให้ผู้ใช้งานทำการ confirme อีกครั้ง
                        flexmessages = FlexMessages().AreaManagerSendBackDetailToEnsure(area_ID)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'SELECTER' in command:
                        position_selecter = 'UserType03'
                        flexmessages = FlexMessages().ConfirmedPositionSelect(user_id,position_selecter)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CONFIRMPOSITION' in command :
                        area_list = AreaCodeType.objects.filter(area_activate=False).all()
                        flexmessages = FlexMessages().SelectAreaList(area_list)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CONFIRMNAME' in command :
                        area_userid = command[33:]
                        print ('ผู้จัดการเขตที่ทำการลงทะเบียนคือ {} '.format(area_userid))
                        # # 1. ทำการแจ้งเตือนไปที่ line group notify เพื่อแจ้งให้ admin approve
                        area_detail = AreaCodeType.objects.filter(id=area_userid).first()
                        print ('ผู้จัดการเขตที่ทำการลงทะเบียนคือ {} ชือ {} ดูแลเขต {} เขต ID {}'.format(area_detail,
                                                                                                area_detail.area_code_name,
                                                                                                    area_detail.area_code_type,
                                                                                                        area_detail.area_code_type.id))
                        
                        # area_in_this_site = StationProfile.objects.filter(station_area_manager=area_detail.id).first()
                        print ('area_detail : {}'.format(area_detail))
                        creating_line_data().get_approve_new_area_manager(profile,line_token)
                        # # 2 . ส่ง reply flex message to user แจ้งสถานะรอการอนุมัติ
                        flexmessages = FlexMessages().Reply_inapprove_new_area_manager(profile,area_detail)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        # # 3. ทำการ set update table UserListCodeType set userList_position = 3  (ตำแหน่งผู้จัดการเขต)
                        # # 4. ทำการ set update table UserListCodeType set userList_member_mode = inapprove  (อยู่ระหว่างการอนมัติจาก admin)
                        user_position_id = Position.objects.filter(position_type='UserType03').values_list('id',flat=True).first()
                        print ('user_position_id : {}'.format(user_position_id))
                        SaveDB().update_position_inapprove(user_id,user_position_id,None,area_detail)
                        # สร้าง Flex message ส่งไปให้ Admin Approved
                        # ค้นหารายชื่อ Admin ทั้งหมด
                        admin_user_id = UserListCodeType.objects.filter(userList_position=5).all()
                        # ค้นหารายละเอียด line profile ของผู้ใช้งาน
                        user_line_profile = UserListCodeType.objects.filter(userList_userid=user_id).first()
                        flexmessages = FlexMessages().AreaSendToAdminApprove(area_detail,user_line_profile)
                        SendFlexMessages(payload).PushMessageAreaSendRequestToAdminForApprove(flexmessages,admin_user_id)
                    elif 'APPROVED' in command :
                        data_command = 'AREA-REGISTER-PROCESS-APPROVED-ID'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('END'):])
                        manager_user_id2 = UserListCodeType.objects.filter(id=manager_id).first()
                        manager_user_id3 = UserListCodeType.objects.filter(id=manager_id).all()
                        print ('manager_id_approved : {}'.format(manager_id))
                        # ส่ง line notify แจ้งเตือนสถานะ ได้รับการอนุมัติจาก admin แล้ว
                        creating_line_data().send_approve_new_area_manager(manager_user_id2,line_token)
                        # ส่ง Flex message ส่งไปให้ผู้จัดการเขตรับทราบ Admin approved แล้ว
                        flexmessages = FlexMessages().AdminApprovedNewAreaManager(manager_user_id2)
                        # ค้นหา area manager user id เพื่อส่งการแจ้งเตือน ได้รับอนุมัติจาก Admin แล้ว 
                        SendFlexMessages(payload).PushMessageAdminApprovedNewAreaManager(flexmessages,manager_user_id3)

                        # ส่งไป update db table UserListCodeType set update userList_member_mode='approved',userList_approved_datetime=datetime.now(),userList_activate=True
                        SaveDB().update_position_approve(manager_user_id2)
                        # send reply message แจ้งการอนุมัติจาก admin แล้ว
                        area_name = AreaCodeType.objects.filter(area_code_type=manager_user_id2.userList_area_name.id).first()
                        message = 'ทำรายการอนุมัติ ตำแหน่งผู้จัดการเขต {} ให้กับคุณ {} เรียบร้อยแล้ว'.format(manager_user_id2.userList_area_name.code_in_area_code_name,area_name)
                        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                        pass
                    elif 'REJECT' in command :
                        data_command = 'AREA-REGISTER-PROCESS-REJECT-ID'
                        manager_id = (command[command.index(data_command) + len(data_command): command.index('END'):])
                        print ('manager_id_rejected : {}'.format(manager_id))
                        manager_user_id2 = UserListCodeType.objects.filter(id=manager_id).first()
                        manager_user_id3 = UserListCodeType.objects.filter(id=manager_id).all()
                        # ทำการเช็คว่าก่้อนหน้าเคยได้รับการ approved หรือยัง
                        last_member_status = manager_user_id2.userList_member_mode
                        print ('last member status : {}'.format(manager_user_id2.userList_member_mode))
                        if last_member_status == 'approved' :
                            print ('สถานะอยู่ในสถานะ approved')
                            # ส่ง reply เพื่อยืนยันการยกเลิกสถานะ approved
                            flexmessages = FlexMessages().UnapprovedMember(manager_user_id2) # ต้องการแค่ ID ของพนักงานที่ต้องการยกเลิกการ approved
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        else :
                            # ส่ง line notify แจ้งเตือนสถานะ ได้รับการอนุมัติจาก admin แล้ว
                            creating_line_data().send_rejected_new_area_manager(manager_user_id2,line_token)
                            # ส่ง Flex message ส่งไปให้ผู้จัดการเขตรับทราบ Admin approved แล้ว
                            flexmessages = FlexMessages().AdminRejectedNewAreaManager(manager_user_id2)
                            # ค้นหา area manager user id เพื่อส่งการแจ้งเตือน ได้รับอนุมัติจาก Admin แล้ว 
                            SendFlexMessages(payload).PushMessageAdminApprovedNewAreaManager(flexmessages,manager_user_id3)
                            # send reply message แจ้งการอนุมัติจาก admin แล้ว
                            message = 'ทำรายการไม่อนุมัติ ตำแหน่งผู้จัดการเขต {} ให้กับคุณ LineID {} เรียบร้อยแล้ว'.format(manager_user_id2.userList_area_name.code_in_area_code_name,profile.display_name)
                            line_bot_api.reply_message(reply_token, TextSendMessage(text=message)) 
                    elif 'RESENT' in command :
                        print ('ส่งรายการใหม่อีกครั้ง {}'.format(command))
                        area_list = AreaCodeType.objects.filter(area_activate=False).all()
                        flexmessages = FlexMessages().SelectAreaList(area_list)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CANCEL' in command:
                        flexmessages = FlexMessages().SelectUserType()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif 'CHANGE_AREA' in command :
                        data_command_1 = 'AREA-REGISTER-PROCESS-CHANGE_AREA-CURRENTAREAID'
                        data_command_2 = 'NEWAREAID'
                        current_area_id = (command[command.index(data_command_1) + len(data_command_1): command.index('NEWAREAID'):])
                        new_area_id = (command[command.index(data_command_2) + len(data_command_2): command.index('END'):])
                        print ('current_area_id : {}'.format(current_area_id))
                        print ('new_area_id : {}'.format(new_area_id))
                        # ทำการเช็คว่า new_area_id มีผู้จัดการเขตทำการ register line bot มาหรือยัง
                        if new_area_id == '5555':
                            print ('เป็นเขตที่ค้นหาชื้อผู้จัดการเขตไม่เจอ')
                            current_area = AreaCodeType.objects.filter(area_code_type__id=current_area_id).first()
                            flexmessages = FlexMessages().ChangeNewAreaManagerWithNoNewIDManager(current_area)
                            
                            # ค้นหา user_id ของ admin team
                            admin_user_id = UserListCodeType.objects.filter(userList_position=5).all()
                            # Push new message ไปให้ admin
                            SendFlexMessages(payload).PushMessageAreraChangeNewArea(flexmessages,admin_user_id)

                        else :
                        
                        
                            new_area_id_check_register_or_not = UserListCodeType.objects.filter(userList_area_name=new_area_id).first()
                            print ('new_area_id_check : {}'.format(new_area_id_check_register_or_not))
                            if new_area_id_check_register_or_not == None :
                                # ถ้ายังไม่ register ก็จะส่งไปขออนุมัติที่ Admin แทน
                                
                                flexmessages = FlexMessages().ChangeNewAreaManager(current_area_id,new_area_id)
                                # ค้นหา user_id ของ admin team
                                admin_user_id = UserListCodeType.objects.filter(userList_position=5).all()
                                # Push new message ไปให้ admin
                                SendFlexMessages(payload).PushMessageAreraChangeNewArea(flexmessages,admin_user_id)
                                # reply flex message กลับไปแจ้งผู้ขอเปลี่ยนเขต
                                flexmessages = FlexMessages().ReplyBackToUserChangeNewAreaManager(current_area_id,new_area_id)
                                SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                                
                                print ('ไม่มีผู้จัดการเขตที่ทำการ register line bot มา')
                            else :
                                # ถ้า register แล้ว ก็ให้ส่ง Flex ไปแจ้งให้มีการขอใช้เขตนี้
                                print ('มีผู้จัดการเขตที่ทำการ register line bot มา')
                    elif 'RESPOND' in command :
                        if 'SAYYES' in command :
                            print ('ตอบกลับ อนุมัติ {}'.format(command))
                            data_command_1 = 'AREA-REGISTER-PROCESS-RESPOND-SAYYES-CURRENTAREAID'
                            data_command_2 = 'NEWAREAID'
                            current_area_id = (command[command.index(data_command_1) + len(data_command_1): command.index('NEWAREAID'):])
                            new_area_id = (command[command.index(data_command_2) + len(data_command_2): command.index('END'):])
                            print ('current_area_id : {} new_area_id {}'.format(current_area_id,new_area_id))
                            # ทำการสลับเขต
                            current_area_to_new_area = AreaCodeType.objects.filter(area_code_type__id=current_area_id).first()

                            # ค้นหาข้อมูลเขตเดิม
                            # current_area_detail = AreaCodeType.objects.filter(area_code_type__id=current_area_id).first()
                            # print ('current_area_detail : {}'.format(current_area_detail))
                            # ค้นหาข้อมูลของเขตใหม่
                            # new_area_detail = AreaCodeType.objects.filter(area_code_type__id=new_area_id).first()
                            # print ('new_area_detail : {}'.format(new_area_detail))

                            # ค้นหา table id ของเจ้าของเขตใหม่
                            # new_ared_manager_id = AreaCodeType.objects.filter(id=new_area_id).first()
                            # print ('new_ared_manager_id : {}'.format(new_ared_manager_id.area_code_type.code_in_area_code_name))
                            # print ('ผู้จัดการเขตที่ต้องเปลี่ยนสาขา เขตเดิมที่ดูแล คือ {} ชื่อเขต คือ {} table ID คือ {}'.format(new_ared_manager_id,new_ared_manager_id.area_code_type.code_in_area_code_name,new_ared_manager_id.area_code_type.id))
                            # # ค้นหา line_user_id ของผู้จัดการเขตที่ขอเปลี่ยนเขต เพื่อ Push flex message กลับไปแจ้งผลการอนุมัติ
                            # line_user_id = UserListCodeType.objects.filter(userList_area_name__id=current_area_id,userList_position=3).all()
                            # current_area_name = UserListCodeType.objects.filter(userList_area_name__id=current_area_id,userList_position=3).first()
                            # print ('line_user_id : {}'.format(line_user_id))
                            # # ทำการเปลี่ยนเขตใหม่
                            # SaveDB().set_change_new_area(current_area_id,new_ared_manager_id)
                            # # ทำการ Pash flex message กลับไปแจ้ง ผู้จัดการที่ขอเปลี่ยนเขต
                            # flexmessages = FlexMessages().PushApprovedChangeNewAreaManager()
                            # SendFlexMessages(payload).PushMessageAdminApprovedAreraChangeNewArea(flexmessages,line_user_id)
                            # # ทำการ reply message การทำรายการสำเร็จ
                            # message = 'ทำการย้ายเขตของคุณ {} เรียบร้อย '.format(current_area_name.userList_area_name.area_code_name)
                            # line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                        elif 'SAYNO' in command :
                            print ('ตอบกลับ ไม่อนุมัติ {}'.format(command))
                        
                        
                            # ผู้จัดการเขตคนนี้ สามารถเลือกได้ว่าจะ อนุญาตให้ใช้เขตนี้หรือไม่
                            # ถ้า อนุมัติ สถานะของเขตตัวเอง จะถูก Set เป็น avaliable ทันที
                            # ถ้า ไม่อนุมัติ ก็ส่ง Flex แจ้งวผู้ขอว่า ไม่อนุมัติ 
                            pass      
                elif 'UNAPPROVED-MEMBER' in command :
                    # ทำการ set update table UserListCodeType set update userList_member_mode='register',userList_register='False',userList_register_datetime=None,userList_activate='False',userList_notify='False',userList_position='None'
                    manager_id = command[17:]
                    print ('manager_id : {}'.format(manager_id))
                    manager_user_id = UserListCodeType.objects.filter(id=manager_id).first()
                    print ('manager_user_id : {}'.format(manager_user_id))
                    SaveDB().unapproved_member(manager_user_id)
                
                    message = 'ทำการยกเลิกการอนุมัติของคุณ {} ตำแหน่ง {} เรียบร้อยแล้ว'.format(manager_user_id.userList_display_name,manager_user_id.userList_position.position_name)
                    line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                    # ทำการ link rich menu user ไปที่หน้าจอหลัก
                    line_bot_api.link_rich_menu_to_user(manager_user_id.userList_userid, line_token.rich_main_menu)


                    pass
                elif command == 'botlogin' :
                    # นำ userId ไปเช็คว่าเคยมีการลงทะเบียนไว้หรือยัง
                    # เช็คที่ตาราง StationProfile
                    line_token = LineSetting.objects.all().first()
                    user_check = UserListCodeType.objects.filter(userList_userid=user_id).first()
                    print ('user_check : {}'.format(user_check))
                    if user_check.userList_activate == True :
                        if user_check.userList_member_mode == 'register' :
                            print ('ผู้ใช้งานยังไม่ลงทะเบียน')
                            flexmessages = FlexMessages().Gressing_messages(profile.display_name)
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        elif user_check.userList_member_mode == 'inapprove' :
                            print ('ผู้ใช้งานยังกำลังทำการรออนุมัติ')
                            message = 'คุณอยู่ระหว่างรอการอนุมัติให้เข้าระบบ'
                            line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                        elif user_check.userList_member_mode == 'approved' :
                            print ('ผู้ใช้งานได้รับการอนุมัติ')
                            line_bot_api.link_rich_menu_to_user(user_id, line_token.rich_select_munu)
                            flexmessages = FlexMessages().LoginSuccessed(profile,user_check)
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif user_check.userList_activate == False :
                        # if user_check.userList_register == False :
                        if user_check.userList_member_mode == 'register' :
                            print ('ผู้ใช้งานยังไม่ลงทะเบียน')
                            flexmessages = FlexMessages().Gressing_messages(profile.display_name)
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        elif user_check.userList_member_mode == 'inapprove' :
                            print ('ผู้ใช้งานยังกำลังทำการรออนุมัติ')
                            message = 'คุณอยู่ระหว่างรอการอนุมัติให้เข้าระบบ'
                            line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
                        elif user_check.userList_member_mode == 'approved' :
                            print ('ผู้ใช้งานได้รับการอนุมัติ')
                            line_bot_api.link_rich_menu_to_user(user_id, line_token.rich_select_munu)
                            flexmessages = FlexMessages().LoginSuccessed(profile,user_check)
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                elif command == 'LOGOUT' :
                    print ('การลงทะเบียน {}'.format(command))
                    line_bot_api.link_rich_menu_to_user(user_id, line_token.rich_main_menu)
                    flexmessages = FlexMessages().LogOutSuccessed(profile)
                    SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                elif command == 'SETTING' :
                    # แสดงตำแหน่งผู้ที่เรียกรายงานว่าตำแหน่งอะไร
                    current_position = UserListCodeType.objects.filter(userList_userid=user_id).first()
                    postion_id = current_position.userList_position.id
                    print ('postion_id : {}'.format(postion_id))
                    print ('current_position : {}'.format(current_position.userList_position.position_name))
                    if postion_id == 1 :
                        print ('ผู้จัดการสาขา')
                        # 1. แสดงรายชื่อสาขาที่ดูแลอยู่ สำเร็จ
                        # 2. เพิ่ม สาขาดูแล สำเร็จ
                        # 3. ลบ สาขาดูแล สำเร็จ
                        flexmessages = FlexMessages().SettingStationShowMenu(current_position)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                    elif postion_id == 2 :
                        # 1. ไม่ได้รบอนุญาติให้ใช้งาน
                        print ('ผู้ช่วยผู้จัดการสาขา')   
                    elif postion_id == 3 :
                        # 1. แสดงรายชื่อสาขา ในเขตที่ดูแลอยู่
                        # 2. ย้ายเขตดูแล
                        print ('ผู้จัดการเขต')
                        flexmessages = FlexMessages().SettingAreaShowMenu(current_position)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)   
                    elif postion_id == 4 :
                        # 1. ไม่ได้รบอนุญาติให้ใช้งาน
                        print ('ผู้ช่วยผู้จัดการภาค')
                        line_bot_api.reply_message(reply_token, TextSendMessage(text='ส่วนสำหรับผู้ดูแลระบบ'))
                    elif postion_id == 5 :
                        # 1. แสดงรายชื่อผู้จัดการเขต
                        # 2. แสดงรายชื่อผู้จัดการภาค
                        # 3. แสดงรายชื่อสาขาทังหมด
                        # 4. ยกเลิก ผู้จัดการเขต
                        print ('ผู้ดูแลระบบ')
                        line_bot_api.reply_message(reply_token, TextSendMessage(text='อยู่ระหว่างพัฒนาส่วน ADMIN'))                               
                elif command[:6] == 'REPORT' :
                    print ('มีการเรียกใช้คำสั่ง  {}'.format(command))
                    print ('command xxxxxxxxxxxxxxxxx',command[:6])
                    # ตรวจสอบว่าผู้เรียกรายงานคือระดับไหน
                    line_token = LineSetting.objects.all().first()
                    user_check = UserListCodeType.objects.filter(userList_userid=user_id).first()
                    print ('User ที่มีการเรียกใช้งานคือตำแหน่ง {} ID {}'.format(user_check.userList_position,user_check.userList_position.id))
                    position = user_check.userList_position.id
                    station_id = UserListCodeType.objects.filter(userList_userid=user_id).first()
                    import datetime
                    today = datetime.datetime.now()
                    if 'XREPORT' in command :
                        manager_multi_station = user_check.userList_takecare_station
                        if user_check.userList_position.id == 1 : # 1 คือ ผู้จัดการสาขา
                            # เช็คว่า ผู้จัดการดูแลหลายสถานีหรือ
                            if manager_multi_station == 'single' :
                                who_id = station_id.userList_station_name.station_site # station_pbl
                                user_position_simulator = 1
                                line_user_id_simulator = user_id
                                CreateReportPOS(who_id,command,payload,'REPORT-XREPORT',today,user_position_simulator,line_user_id_simulator).ShowSiteOptionByEOD('ShowOptionSiteXREPORT',None) 
                            elif manager_multi_station == 'multi'  :
                                print ('ผู้จัดการสาขาดุแลหลายสาขา {}'.format(command))
                                # ส่งตัวเลือกสาขาที่ดูแล
                                # 1. ค้นหาสถานีหลักที่ดูแลอยู่
                                first_site = UserListCodeType.objects.filter(userList_userid=user_id).first()
                                print ('ผู้จัดการเขต คุณ : {} ID {} ดูแลสาขา {} สาขา  ID {}'.format(first_site,first_site.id,first_site.userList_station_name,first_site.userList_station_name.id))
                                # 2. ค้นหาสถานีที่ดูแลเพิ่มเติม
                                station_add = MultiStationTackCare.objects.filter(multi_manager_number=first_site.id,multi_active=True).all()
                                for i in station_add :
                                    print ('สถานีที่ดูแลเพิ่มเติม {}'.format(i.multi_station_number))
                                report_type = 'XREPORT'
                                PosReport(payload).Multi_site_Selecter(first_site,station_add,report_type)
                        elif user_check.userList_position.id == 3 : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-XREPORT',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList() 
                        elif user_check.userList_position.id in (4,5) : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 4
                            line_user_id_simulator = user_id 
                            CreateReportPOS(who_id,command,payload,'REPORT-XREPORT',today,user_position_simulator,line_user_id_simulator).ShowMainAreaSelectOptionAreaManager()
                    
                        elif user_check.userList_position.id == 3 : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-XREPORT',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList() 
                        elif user_check.userList_position.id in (4,5) : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 4
                            line_user_id_simulator = user_id 
                            CreateReportPOS(who_id,command,payload,'REPORT-XREPORT',today,user_position_simulator,line_user_id_simulator).ShowMainAreaSelectOptionAreaManager()
                    elif 'METER' in command :
                        manager_multi_station = user_check.userList_takecare_station
                        if user_check.userList_position.id == 1 : # 1 คือ ผู้จัดการสาขา
                            # เช็คว่า ผู้จัดการดูแลหลายสถานีหรือ
                            if manager_multi_station == 'single' :
                                who_id = station_id.userList_station_name.station_site # station_pbl
                                user_position_simulator = 1
                                line_user_id_simulator = user_id
                                CreateReportPOS(who_id,command,payload,'REPORT-METER',today,user_position_simulator,line_user_id_simulator).ShowSiteOptionByEOD('ShowOptionSiteMETER',None) 
                            elif manager_multi_station == 'multi'  :
                                print ('ผู้จัดการสาขาดุแลหลายสาขา {}'.format(command))
                                # ส่งตัวเลือกสาขาที่ดูแล
                                # 1. ค้นหาสถานีหลักที่ดูแลอยู่
                                first_site = UserListCodeType.objects.filter(userList_userid=user_id).first()
                                print ('ผู้จัดการเขต คุณ : {} ID {} ดูแลสาขา {} สาขา  ID {}'.format(first_site,first_site.id,first_site.userList_station_name,first_site.userList_station_name.id))
                                # 2. ค้นหาสถานีที่ดูแลเพิ่มเติม
                                station_add = MultiStationTackCare.objects.filter(multi_manager_number=first_site.id,multi_active=True).all()
                                for i in station_add :
                                    print ('สถานีที่ดูแลเพิ่มเติม {}'.format(i.multi_station_number))
                                report_type = 'METER'
                                PosReport(payload).Multi_site_Selecter(first_site,station_add,report_type)
                        elif user_check.userList_position.id == 3 : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-METER',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList() 
                        elif user_check.userList_position.id in (4,5) : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 4
                            line_user_id_simulator = user_id 
                            CreateReportPOS(who_id,command,payload,'REPORT-METER',today,user_position_simulator,line_user_id_simulator).ShowMainAreaSelectOptionAreaManager()
                    elif 'PRICE' in command :
                        manager_multi_station = user_check.userList_takecare_station
                        if user_check.userList_position.id == 1 : # 1 คือ ผู้จัดการสาขา
                            # เช็คว่า ผู้จัดการดูแลหลายสถานีหรือ
                            if manager_multi_station == 'single' :
                                who_id = station_id.userList_station_name.station_site # station_pbl
                                user_position_simulator = 1
                                line_user_id_simulator = user_id
                                CreateReportPOS(who_id,command,payload,'REPORT-PRICE',today,user_position_simulator,line_user_id_simulator).ShowSiteOptionByEOD('ShowOptionSitePRICE',None) 
                            elif manager_multi_station == 'multi'  :
                                print ('ผู้จัดการสาขาดุแลหลายสาขา {}'.format(command))
                                # ส่งตัวเลือกสาขาที่ดูแล
                                # 1. ค้นหาสถานีหลักที่ดูแลอยู่
                                first_site = UserListCodeType.objects.filter(userList_userid=user_id).first()
                                print ('ผู้จัดการเขต คุณ : {} ID {} ดูแลสาขา {} สาขา  ID {}'.format(first_site,first_site.id,first_site.userList_station_name,first_site.userList_station_name.id))
                                # 2. ค้นหาสถานีที่ดูแลเพิ่มเติม
                                station_add = MultiStationTackCare.objects.filter(multi_manager_number=first_site.id,multi_active=True).all()
                                for i in station_add :
                                    print ('สถานีที่ดูแลเพิ่มเติม {}'.format(i.multi_station_number))
                                report_type = 'PRICE'
                                PosReport(payload).Multi_site_Selecter(first_site,station_add,report_type)
                        elif user_check.userList_position.id == 3 : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-PRICE',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList() 
                        elif user_check.userList_position.id in (4,5) : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 4
                            line_user_id_simulator = user_id 
                            CreateReportPOS(who_id,command,payload,'REPORT-PRICE',today,user_position_simulator,line_user_id_simulator).ShowMainAreaSelectOptionAreaManager()
                    elif 'SMB' in command :
                        manager_multi_station = user_check.userList_takecare_station
                        if user_check.userList_position.id == 1 : # 1 คือ ผู้จัดการสาขา
                            # เช็คว่า ผู้จัดการดูแลหลายสถานีหรือ
                            if manager_multi_station == 'single' :
                                who_id = station_id.userList_station_name.station_site # station_pbl
                                user_position_simulator = 1
                                line_user_id_simulator = user_id
                                CreateReportPOS(who_id,command,payload,'REPORT-SMB',today,user_position_simulator,line_user_id_simulator).ShowSiteOptionByEOD('ShowOptionSiteSMB',None) 
                            elif manager_multi_station == 'multi'  :
                                print ('ผู้จัดการสาขาดุแลหลายสาขา {}'.format(command))
                                # ส่งตัวเลือกสาขาที่ดูแล
                                # 1. ค้นหาสถานีหลักที่ดูแลอยู่
                                first_site = UserListCodeType.objects.filter(userList_userid=user_id).first()
                                print ('ผู้จัดการเขต คุณ : {} ID {} ดูแลสาขา {} สาขา  ID {}'.format(first_site,first_site.id,first_site.userList_station_name,first_site.userList_station_name.id))
                                # 2. ค้นหาสถานีที่ดูแลเพิ่มเติม
                                station_add = MultiStationTackCare.objects.filter(multi_manager_number=first_site.id,multi_active=True).all()
                                for i in station_add :
                                    print ('สถานีที่ดูแลเพิ่มเติม {}'.format(i.multi_station_number))
                                report_type = 'SMB'
                                PosReport(payload).Multi_site_Selecter(first_site,station_add,report_type)
                        elif user_check.userList_position.id == 3 : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-SMB',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList() 
                        elif user_check.userList_position.id in (4,5) : # 1 คือ ผู้จัดการเขต
                            who_id = None
                            user_position_simulator = 4
                            line_user_id_simulator = user_id 
                            CreateReportPOS(who_id,command,payload,'REPORT-SMB',today,user_position_simulator,line_user_id_simulator).ShowMainAreaSelectOptionAreaManager()  
                elif command[:4] == 'VIEW' :
                    line_token = LineSetting.objects.all().first()
                    user_check = UserListCodeType.objects.filter(userList_userid=user_id).first()
                    print ('User ที่มีการเรียกใช้งานคือตำแหน่ง {} ID {}'.format(user_check.userList_position,user_check.userList_position.id))
                    print ('มีการเรียกใช้คำสั่ง  {}'.format(command))
                    import datetime
                    today = datetime.datetime.now()
                    if 'X-REPORT' in command:
                        print ('มีการเรียกใช้งาน X-REPORT')
                        if 'SITE' in command :
                            if 'NOW' in command :
                                data_command = 'VIEW-X-REPORT-SITE-NOW-SITE_ID'
                                data_command2 = 'LASTID'
                                station_id = (command[command.index(data_command) + len(data_command): command.index(data_command2):])
                                xreport_id = (command[command.index(data_command2) + len(data_command2): command.index('END'):])
                                print ('ผู้จัดการสถานี เรียกขอข้อมูล X-report by Last Shift สถานี ID {} xreport ID {}'.format(station_id,xreport_id))
                                station_detail = StationProfile.objects.filter(station_site=station_id).first()
                                # ติดต่อ DB เพื่อขอข้อมูลการ shift detail ของวันที่เรียกรายงาน
                                sql_command = mssql_command().get_x_report_per_id()
                                result_pos = ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,xreport_id,2)
                                if result_pos[0] == True : # กรณีติดต่อฐานข้อมูลสำเร็จ
                                    # print ('ข้อมูล X-report  {}'.format(result_pos[1]))
                                    # ส่งข้อมูลที่ได้จากการ Query sql ไปสร้าง Flexmessage template
                                    report_type = 'X-REPORT'
                                    PosReport(payload).Xreport_Last_Shift(station_detail,result_pos[1],report_type)
                                elif result_pos[0] == False : # กรณีติดต่อฐานข้อมูลไม่สำเร็จ
                                    print ('ข้อมูล X-report ไม่สำเร็จ {}'.format(result_pos[1]))
                                    text_message = 'ไม่สามารถเรียกรายงาน X-Report ของรอบปิดกะ  X-Report ID {} ได้ เนื่องจาก {}'.format(xreport_id,result_pos[1])
                                    line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message))
                                    if station_detail.debug_mode == True :
                                        db_logger.exception(result_pos[1])
                            elif 'DAY'in command :
                                data_command = 'VIEW-X-REPORT-SITE-DAY-SITE_ID'
                                station_id = (command[command.index(data_command) + len(data_command): command.index('END'):])
                                date_from_line = payload['events'][0]['postback']['params']['date']
                                print ('ผู้จัดการสถานี เรียกขอข้อมูล X-report by Day สถานี ID {} ของวันที่ {}'.format(station_id,date_from_line))
                                station_detail = StationProfile.objects.filter(station_site=station_id).first()
                                # ติดต่อ DB เพื่อขอข้อมูลการ shift detail ของวันที่เรียกรายงาน
                                sql_command = mssql_command().get_x_report_close_shift_per_EOD()
                                result_pos = ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,date_from_line,2)
                                print (result_pos)
                                if result_pos[0] == True : # กรณีติดต่อฐานข้อมูลสำเร็จ
                                    report_type = 'X-REPORT'
                                    PosReport(payload).Xreport_Date_Select(station_detail,result_pos[1],date_from_line,report_type)
                                elif result_pos[0] == False : # กรณีติดต่อฐานข้อมูลไม่สำเร็จ
                                    print ('ข้อมูล X-report ไม่สำเร็จ {}'.format(result_pos[1]))
                                    text_message = 'ไม่สามารถเรียกรายงาน X-Report ของรอบปิดกะ  X-Report วันที่ {} ได้ เนื่องจาก {}'.format(date_from_line,result_pos[1])
                                    line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message))
                                    if station_detail.debug_mode == True :
                                        db_logger.exception(result_pos[1])
                        if 'AREA' in command :
                            data_command_1 = 'VIEW-X-REPORT-AREA-SITEID'
                            station_ppl = (command[command.index(data_command_1) + len(data_command_1): command.index('END'):])
                            # CreateReportPOS(station_ppl,command,payload,'XREPORT').Get_shift_close_time_by_EOM()
                            who_id = station_ppl # station_pbl
                            user_position_simuler = 1 # จำลองตัวเองเป็นผู้จัดการสถานี
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-XREPORT',today,user_position_simuler,line_user_id_simulator).ShowSiteOptionByEOD('ShowOptionSiteXREPORT',None) 
                        elif 'MAIN' in command :
                            data_command = 'VIEW-X-REPORT-MAIN-SELECTER'
                            user_id_simulator = (command[command.index(data_command) + len(data_command): command.index('END'):])
                            print ('ผู้จัดการภาคเรียกใช้รายงาน X-REPORT ของผู้จัดการเขต line_id {}'.format(user_id))
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id_simulator # จำลอง line user id ของผู้จัดการเขตที่ต้องการ ส่งเข้าไปทำงาน
                            CreateReportPOS(who_id,command,payload,'REPORT-XREPORT',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList() 
                    elif 'SMB' in command :
                        print ('มีการเรียกใช้งาน SMB')
                        if 'NOW' in command :
                            from datetime import datetime
                            data_command = 'VIEW-SMB-SITE-NOW-SITE_ID'
                            data_command2 = 'TRANSCETION'
                            station_id = (command[command.index(data_command) + len(data_command): command.index(data_command2):])
                            meter_transection = (command[command.index(data_command2) + len(data_command2): command.index('END'):])
                            date_time_request_obj = datetime.strptime(meter_transection[:8], '%Y%m%d').strftime('%Y-%m-%d')
                            print ('ผู้จัดการสถานี เรียกใช้งาน SMB NOW ของ สถานี {} Meter Transection {} วันที่เรียกรายงาน {}'.format(station_id,meter_transection,date_time_request_obj))
                            station_detail = StationProfile.objects.filter(station_site=station_id).first()
                            # นำ meter transection ไป query ข้อมูลจากเครื่องสาขา
                            sql_command = mssql_command().SMB_get_report_data()
                            sql_valible = (date_time_request_obj,meter_transection[9:])
                            # แนบค่า 3 คือ ส่งค่าตัวแปร %s มากกว่า 2 
                            result_pos=ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,sql_valible,3)
                            print ('result pos {}'.format(result_pos))
                            if result_pos[0] == True :
                                report_type = 'SMB'
                                PosReport(payload).SMB_Last_Shift(station_detail,result_pos[1],report_type) # แปลง result_pos[1] เป็น list เพื่อส่งไปยังฟังก์ชั่นวน loop ต่อไป
                            elif result_pos[0] == False : # กรณีติดต่อฐานข้อมูลไม่สำเร็จ
                                    print ('ติดต่อขอข้อมูล SMB ไม่สำเร็จ {}'.format(result_pos[1]))
                                    text_message = 'ไม่สามารถเรียกรายงาน SMB  ได้ เนื่องจาก {}'.format(result_pos[1])
                                    line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message))
                                    if station_detail.debug_mode == True :
                                        db_logger.exception(result_pos[1])      
                        elif 'DAY' in command :
                            print ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
                            data_command = 'VIEW-SMB-SITE-DAY-SITE_ID'
                            date_from_line = payload['events'][0]['postback']['params']['date']
                            # data_command2 = 'NGROK'
                            station_id = (command[command.index(data_command) + len(data_command): command.index('END'):])
                            # meter_shift_id = (command[command.index(data_command2) + len(data_command2): command.index('END'):])
                            print ('ผู้จัดการสถานี เรียกใช้งาน SMB DAY ของ สถานี {}วันที่เรียกรายงาน {}'.format(station_id,date_from_line))
                            station_detail = StationProfile.objects.filter(station_site=station_id).first()
                            print ('ผู้จัดการสถานี เรียกใช้งาน SMB DAY ของ สถานี {}'.format(station_id))
                            sql_command = mssql_command().SMB_get_report_data_per_EOD()
                            sql_valible = (date_from_line)
                            # แนบค่า 3 คือ ส่งค่าตัวแปร %s มากกว่า 2 
                            result_pos=ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,sql_valible,2)
                            print ('result pos {}'.format(result_pos))
                            if result_pos[0] == True :
                                if len(result_pos[1]) > 0 :
                                    # ส่งข้อมูลไปทำการสร้าง Flex Message
                                    report_type = 'SMB'
                                    PosReport(payload).SMB_Date_Selecter(station_detail,result_pos,date_from_line,report_type)
                            elif result_pos[0] == False : # กรณีติดต่อฐานข้อมูลไม่สำเร็จ
                                    print ('ติดต่อขอข้อมูล SMB ไม่สำเร็จ {}'.format(result_pos[1]))
                                    text_message = 'ไม่สามารถเรียกรายงาน Meter ของรอบปิดกะ วันที่ {} ได้ เนื่องจาก {}'.format(date_from_line,result_pos[1])
                                    line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message))
                                    if station_detail.debug_mode == True :
                                        db_logger.exception(result_pos[1])
                        elif 'AREA' in command :
                            data_command_1 = 'VIEW-SMB-AREA-ID'
                            station_ppl = (command[command.index(data_command_1) + len(data_command_1): command.index('END'):])
                            # CreateReportPOS(station_ppl,command,payload,'XREPORT').Get_shift_close_time_by_EOM()
                            who_id = station_ppl # station_pbl
                            user_position_simulator = 1
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-SMB',today,user_position_simulator,line_user_id_simulator).ShowSiteOptionByEOD('ShowOptionSiteSMB',None) 
                        elif 'MAIN' in command :
                            data_command = 'VIEW-SMB-MAIN-SELECTER'
                            user_id_simulator = (command[command.index(data_command) + len(data_command): command.index('END'):])
                            print ('ผู้จัดการภาคเรียกใช้รายงาน SMB ของผู้จัดการเขต line_id {}'.format(user_id))
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id_simulator # จำลอง line user id ของผู้จัดการเขตที่ต้องการ ส่งเข้าไปทำงาน
                            CreateReportPOS(who_id,command,payload,'REPORT-SMB',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList() 
                    elif 'PRICE' in command :
                        print ('ผู้จัดการเขต เรียกขอข้อมูล PRICE')
                        if 'AREA' in command :
                            data_command = 'VIEW-PRICE-AREA-ID'
                            station_id = (command[command.index(data_command) + len(data_command): command.index('END'):])
                            print ('ผู้จัดการเขต เรียกขอข้อมูล PRICE สถานี ID {}'.format(station_id))
                            who_id = station_id # station_pbl
                            user_position_simulator = 1
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-PRICE',today,user_position_simulator,line_user_id_simulator).ShowSiteOptionByEOD('ShowOptionSitePRICE',None) 
                        elif 'MAIN' in command :
                            data_command = 'VIEW-PRICE-MAIN-SELECTER'
                            user_id_simulator = (command[command.index(data_command) + len(data_command): command.index('END'):])
                            print ('ผู้จัดการภาคเรียกใช้รายงาน X-REPORT ของผู้จัดการเขต line_id {}'.format(user_id))
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id_simulator # จำลอง line user id ของผู้จัดการเขตที่ต้องการ ส่งเข้าไปทำงาน
                            CreateReportPOS(who_id,command,payload,'REPORT-PRICE',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList()
                    elif 'METER' in command :
                        print ('ผู้จัดการสถานี เรียกใช้งาน METER')
                        if 'NOW' in command :
                            from datetime import datetime
                            data_command = 'VIEW-METER-SITE-NOW-SITE_ID'
                            data_command2 = 'TRANSCETION'
                            station_id = (command[command.index(data_command) + len(data_command): command.index(data_command2):])
                            meter_transection = (command[command.index(data_command2) + len(data_command2): command.index('END'):])
                            date_time_request_obj = datetime.strptime(meter_transection[:8], '%Y%m%d').strftime('%Y-%m-%d')
                            print ('ผู้จัดการสถานี เรียกใช้งาน METER NOW ของ สถานี {} Meter Transection {} วันที่เรียกรายงาน {}'.format(station_id,meter_transection,date_time_request_obj))
                            station_detail = StationProfile.objects.filter(station_site=station_id).first()
                            # นำ meter transection ไป query ข้อมูลจากเครื่องสาขา
                            sql_command = mssql_command().get_meter_by_transection_id()
                            sql_valible = (date_time_request_obj,meter_transection)
                            # แนบค่า 3 คือ ส่งค่าตัวแปร %s มากกว่า 2 
                            result_pos=ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,sql_valible,3)
                            if result_pos[0] == True :
                                report_type = 'METER'
                                PosReport(payload).METER_Last_Shift(station_detail,result_pos[1],report_type)
                            elif result_pos[0] == False : # กรณีติดต่อฐานข้อมูลไม่สำเร็จ
                                print ('ติดต่อขอข้อมูล Meter ไม่สำเร็จ {} '.format(result_pos[1]))
                                dt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                text_message = 'ไม่สามารถเรียกรายงาน Meter ShiftID {} ของสถานี {} ได้ เนื่องจากติดปัญหาการเชื่อมต่อ ณ เวลา {}'.format(meter_transection,station_detail.station_name,dt)
                                line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message))
                                if station_detail.debug_mode == True :
                                        db_logger.exception(result_pos[1])
                        elif 'DAY' in command :
                            data_command = 'VIEW-METER-SITE-DAY-SITE_ID'
                            date_from_line = payload['events'][0]['postback']['params']['date']
                            # data_command2 = 'NGROK'
                            station_id = (command[command.index(data_command) + len(data_command): command.index('END'):])
                            # meter_shift_id = (command[command.index(data_command2) + len(data_command2): command.index('END'):])
                            print ('ผู้จัดการสถานี เรียกใช้งาน METER DAY ของ สถานี {}วันที่เรียกรายงาน {}'.format(station_id,date_from_line))
                            station_detail = StationProfile.objects.filter(station_site=station_id).first()
                            print ('ผู้จัดการสถานี เรียกใช้งาน METER DAY ของ สถานี {}'.format(station_id))
                            # ค้นหาตัวเลือกการปิดกะ ของวันที่เลือก
                            sql_command = mssql_command().get_meter_report_per_EOD()
                            # date_time_request_obj = datetime.strptime(date_from_line, '%Y-%m-%d').strftime('%Y-%m-%d')
                            sql_valible = (date_from_line)
                            result_pos=ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,sql_valible,3)
                            if result_pos[0] == True :
                                if len(result_pos[1]) > 0 :
                                    report_type = 'METER'
                                    PosReport(payload).METER_Date_Selecter(station_detail,result_pos,date_from_line,report_type)
                                elif len(result_pos[1]) == 0 :
                                    # print ('ไม่พบรายงานตัวเลือกแสดงรายการกะของ Meter สถานี {} วันที่  {}'.format(station_detail.station_name,date_from_line))
                                    text_message = 'ไม่พบข้อมูลรายงาน Meter ของรอบปิดกะ วันที่ {} กรุณาเลือกวันที่ใหม่'.format(date_from_line)
                                    line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message))
                                    if station_detail.debug_mode == True :
                                        db_logger.exception(result_pos[1])
                            elif result_pos[0] == False : # กรณีติดต่อฐานข้อมูลไม่สำเร็จ
                                    print ('ติดต่อขอข้อมูล Meter ไม่สำเร็จ {}'.format(result_pos[1]))
                                    text_message = 'ไม่สามารถเรียกรายงาน Meter ของรอบปิดกะ วันที่ {} ได้ เนื่องจาก {}'.format(date_from_line,result_pos[1])
                                    line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message))
                                    if station_detail.debug_mode == True :
                                        db_logger.exception(result_pos[1])
                        if 'AREA' in command :
                            data_command_1 = 'VIEW-METER-AREA-ID'
                            station_ppl = (command[command.index(data_command_1) + len(data_command_1): command.index('END'):])
                            # CreateReportPOS(station_ppl,command,payload,'XREPORT').Get_shift_close_time_by_EOM()
                            who_id = station_ppl # station_pbl
                            user_position_simuler = 1 # จำลองตัวเองเป็นผู้จัดการสถานี
                            line_user_id_simulator = user_id
                            CreateReportPOS(who_id,command,payload,'REPORT-METER',today,user_position_simuler,line_user_id_simulator).ShowSiteOptionByEOD('ShowOptionSiteMETER',None) 
                        elif 'MAIN' in command :
                            data_command = 'VIEW-METER-MAIN-SELECTER'
                            user_id_simulator = (command[command.index(data_command) + len(data_command): command.index('END'):])
                            print ('ผู้จัดการภาคเรียกใช้รายงาน METER ของผู้จัดการเขต line_id {}'.format(user_id))
                            who_id = None
                            user_position_simulator = 3
                            line_user_id_simulator = user_id_simulator # จำลอง line user id ของผู้จัดการเขตที่ต้องการ ส่งเข้าไปทำงาน
                            CreateReportPOS(who_id,command,payload,'REPORT-METER',today,user_position_simulator,line_user_id_simulator).ShowAreaSelectOptionSiteInList() 
                   
                else :
                    print ('ไม่พบคำสั่งที่ต้องการ คือ {}'.format(command))
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
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        else :
                            # เช็คว่าใน UserListCodeType มีการลงทะเบียนไว้แล้วหรือยัง
                            check_user_dupicate_site = UserListCodeType.objects.filter(userList_station_name=station_list.id).first()
                            if check_user_dupicate_site  == None :
                                print ('check_user_dupicate_site {}'.format(check_user_dupicate_site))
                                print ('รายชื่อสาขาที่ทำการลงทะเบียน คือ {}'.format(station_list))
                                flexmessages = FlexMessages().ConfirmedStationPass(station_list)
                                SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                                pass
                            else :
                                line_bot_api.reply_message(reply_token, TextSendMessage(text='มีการลงทะเบียนสถานีไว้แล้ว กรุณาเลือกสถานีใหม่ หรือติดต่อ'))
                    elif 'addmoresite' in text_message :
                        print ('addstation')
                        # ส่วนของผู้จัดการสาขาที่ต้องการ add สาขาอื่นเพื่อดูแล
                        station_id = text_message[11:]
                        print ('station_id {}'.format(station_id))
                        station_list = StationProfile.objects.filter(station_site=station_id).first()
                        if not station_list :
                            print ('ไม่พบสถานีที่ต้องการลงทะเบียน')
                            flexmessages = FlexMessages().ConfirmStationFailed()
                            SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        
                        else :
                            if station_list.station_activate == True :
                                print ('รายชื่อสาขาที่ทำการลงทะเบียน คือ {}'.format(station_list))
                                flexmessages = FlexMessages().ConfirmedAddMoreStationPass(station_list)
                                SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                            elif station_list.station_activate == False :
                                print ('สถานีนี้ถูกปิดการใช้งาน')
                                text_message = 'สถานี {}  ยังไม่่ได้เปิดใช้งาน กรุณาติดต่อผู้ดูแลระบบ'.format(station_list.station_name)
                                line_bot_api.reply_message(reply_token, TextSendMessage(text=text_message)) 
                    elif 'admin' in text_message :
                        command_code = text_message[5:]
                        command_admin_register = ['123456789']
                        print ('คำสั่งที่ส่งมา {}'.format(command_code))
                        if command_code in command_admin_register :
                            # ทำการเช็คในระบบว่าได้รับการ approved หรือไม่
                            user_check = UserListCodeType.objects.filter(userList_userid=user_id).first()
                            if user_check.userList_member_mode == 'register' :
                                print ('สามารถลงทะเบียนสำเร็จ')
                                user_position_id = Position.objects.filter(position_type='UserType05').values_list('id',flat=True).first()
                                print ('user_position_id : {}'.format(user_position_id))
                                station_detail = ''
                                SaveDB().update_position_inapprove(user_id,user_position_id,station_detail,None)
                                line_bot_api.reply_message(reply_token, TextSendMessage(text='ทำการบันทึกข้อมูลตำแหน่ง Admin เรียบร้อย'))
                                line_bot_api.link_rich_menu_to_user(user_id, line_token.rich_select_munu)
                            elif user_check.userList_member_mode == 'approved' :
                                line_bot_api.reply_message(reply_token, TextSendMessage(text='คุณได้รับการอนุมัติแล้ว'))
                            
                        else :
                            print ('คำสั่งที่ส่งไม่ถูกต้อง') 
                    elif text_message in ('MENU','menu','Menu','เมนู','ตัวเลือก') :
                        flexmessages = FlexMessages().Menu_Request()
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        return HttpResponse (200)
                        pass
                    elif text_message == 'botregister':
                        print ('text from user')
                        flexmessages = FlexMessages().Gressing_messages(profile.display_name)
                        SendFlexMessages(payload).ReplyMessage(reply_token,flexmessages)
                        return HttpResponse (200)
        

        # print ('UserID is {}'.format(user_id))
        
        
        
        return HttpResponse (200)