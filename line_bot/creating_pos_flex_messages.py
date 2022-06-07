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
from datetime import datetime, timedelta
import datetime
import logging

db_logger = logging.getLogger('db')

class CreateReportPOS:
    def __init__(self,who_id,command,payload,report_type,today,user_position_simulator,line_user_id_simulator):
        # who_id = id ที่ส่งเข้ามาทำ อาจจะเป็น station ppl , manager id , station_id
        # station_pbl = ระหัสสาขา
        # command = คำสั่งที่ส่งมา
        # manager_user_id = line_id ของผู้ทีเป็นผู้จัดการสาขาที่ส่งคำสั่งมา
        # payload = ข้อมูล webhook ที่ได้มาจาก line
        # report_type = ประเภทของรายงานที่ส่งมา เช่น x-report , SMB , Meter , Price
        print ('who_id : {} , command : {} , payload : {} , report_type : {} , today : {}'.format(who_id,command,payload,report_type,today))
        self.report_type = report_type
        self.user_position_simulator = user_position_simulator
        # ค้นผู้เข้ามาใช้งานว่าคือใคร ผจก เขต ภาค
        self.payload = payload
        self.command_from_line = command
        line_token = LineSetting.objects.all().first()
        line_bot_api = LineBotApi(line_token.line_token)
        
        # self.line_user_id = payload['events'][0]['source']['userId']
        self.line_user_id = line_user_id_simulator
        
        self.line_token = LineSetting.objects.all().first()
        self.line_bot_api = LineBotApi(line_token.line_token)
        self.reply_token = payload['events'][0]['replyToken']
        # ส่วนของผู้ที่กำลังทำรายการอยู่
        self.current_doing_user = UserListCodeType.objects.filter(userList_userid=self.line_user_id).first()
        self.currenty_user_name = self.current_doing_user.userList_display_name
        self.currenty_position_id = self.current_doing_user.userList_position.id
        if self.user_position_simulator == 1 :
            self.currenty_position =  self.current_doing_user.userList_position
            self.currenty_position_id =  self.current_doing_user.userList_position.id
            print ('ผู้ที่กำลังทำรายการอยู่ {}  ตำแหน่ง {} ตำแหน่ง ID {}'.format(self.currenty_user_name,
                                                                            self.currenty_position,
                                                                                self.currenty_position_id))
        elif self.user_position_simulator == 3 :
            self.currenty_position =  self.current_doing_user.userList_position
            self.currenty_position_id =  self.current_doing_user.userList_position.id
            self.currenty_area =  self.current_doing_user.userList_area_name
            self.currenty_area_id =  self.current_doing_user.userList_area_name.id
            print ('ผู้ที่กำลังทำรายการอยู่ {}  ตำแหน่ง {} ตำแหน่ง ID {} ดูแลเขต {} เขต ID {}'.format(self.currenty_user_name,
                                                                            self.currenty_position,
                                                                                self.currenty_position_id,self.currenty_area,self.currenty_area_id))
        elif self.user_position_simulator in (4,5) :
            self.currenty_position =  self.current_doing_user.userList_position
            self.currenty_position_id =  self.current_doing_user.userList_position.id
            
            print ('ผู้ที่กำลังทำรายการอยู่ {}  ตำแหน่ง {} ตำแหน่ง ID {}'.format(self.currenty_user_name,
                                                                            self.currenty_position,
                                                                                self.currenty_position_id,
                                                                                    ))
        # ส่วนแสดงข้อมูลวันที่และเวลา
        self.today = today.strftime("%Y-%m-%d")
        self.today_time =today.strftime("%d-%m-%Y %H:%M")
        self.yesterday = (today - timedelta(days=1)).strftime("%Y-%m-%d")
        print ('วันที่ปัจจุบัน {} วันที่เมื่อวาน {}'.format(self.today,self.yesterday))
        # if  self.report_type in ('REPORT-XREPORT','REPORT-SMB') :
        if self.user_position_simulator == 1 :
            self.station_detail = StationProfile.objects.filter(station_site=who_id).first()
            self.station_name = self.station_detail.station_name
            self.station_pbl = self.station_detail.station_site
            self.station_area_code = self.station_detail.station_area_code
            self.station_area_id = self.station_detail.station_area_code_id
            print ('ข้อมูลส่วนสาขา คำสั่ง {} ชื่อสถานี {} สถานี PBL {} ชื่อเขต {} เขต ID {}'.format(self.command_from_line,self.station_name,self.station_pbl,self.station_area_code,self.station_area_id))
            # ส่วนค้นหาข้อมูลผู้จัดการสาขา และ ผู้จัดการเขต

            # ติดปัญหา กรณี สาขา ที่ยังไม่มี ผจก ลงทะเบียนมา
            self.manager_detail = UserListCodeType.objects.filter(userList_station_name__station_site=self.station_pbl,userList_position=1).first()
            self.area_detail = UserListCodeType.objects.filter(userList_area_name__id=self.station_area_id,userList_position=3).first()
            try :
                self.manager_name = self.manager_detail.userList_display_name
                self.manager_user_list_id = self.manager_detail.id
                self.manager_line_user_id = self.manager_detail.userList_userid
            except :
                self.manager_name = 'None'
                self.manager_user_list_id = 0
                self.manager_line_user_id = 'None'

            self.area_name = self.area_detail.userList_display_name
            self.area_user_list_id = self.area_detail.id
            self.area_line_user_id = self.area_detail.userList_userid
            self.debug_mode = self.station_detail.debug_mode
            print ('ข้อมูลสาขา {} ผู้จัดการสาขา {} ผู้จัดการสาขา ID {}  ผู้จัดการเขต {} ผู้จัดการเขต ID {}'.format(self.station_name,
                                                                                                        self.manager_name,
                                                                                                            self.manager_user_list_id,
                                                                                                                self.area_name,
                                                                                                                    self.area_user_list_id))
            # ส่วนขอมูลติดต่อ line server
            self.manager_line_profile = line_bot_api.get_profile(self.manager_line_user_id)
            self.area_line_profile = line_bot_api.get_profile(self.area_line_user_id)
            # ค้นหาผู้ที่กำลังทำรายการอยู่  
            self.user_id_of_current_requrest = payload['events'][0]['source']['userId']
            self.user_detail_of_current_requrest = UserListCodeType.objects.filter(userList_userid=self.user_id_of_current_requrest).first()
            print ('เรียกใช้คำสั่ง {} สาขา {} สาขา PBL {} เจ้าของสาขาคือ {} ผู้จัดการเขต {} วันที่เรียกรายงาน {} '.format( self.command_from_line,
                                                                                                                self.station_name,
                                                                                                                    self.station_pbl,
                                                                                                                        self.manager_name,
                                                                                                                            self.area_name,
                                                                                                                                self.today_time))    
        elif self.user_position_simulator == 3 :
            # # ค้นหารายชื่อสาขาทั้งหมดที่ผู้จัดการเขตคนนี้ดูแลอยู่
            self.total_site_in_area = StationProfile.objects.filter(station_area_code__id=self.currenty_area_id,station_activate=True).all()
            self.area_profile = AreaCodeType.objects.filter(area_code_type__id=self.currenty_area_id).first()
            self.area_full_name = self.area_profile.area_code_name
            self.area_full_name_id = self.area_profile.id
            self.station_name = 'None'
            self.station_pbl = 'None'
            print ('ข้อมูลในเขตดูแลของคุณ {} TM ID {} มีจำนวน {} สาขา'.format(self.area_full_name,self.area_full_name_id,len(self.total_site_in_area)))       
        elif self.user_position_simulator in (4,5) :
            # # ค้นหารายชื่อสาขาทั้งหมดที่ผู้จัดการเขตคนนี้ดูแลอยู่
            self.all_area_manager = AreaCodeType.objects.filter(area_activate=True).all()
            self.station_name = 'None'
            self.station_pbl = 'None'
            
    
    def ShowAreaSelectOptionSiteInList(self) :
        if self.report_type == 'REPORT-XREPORT' :
            PosReport(self.payload).AreaSelectOptionSiteInList(self.area_profile,self.total_site_in_area,'X-REPORT')
        elif self.report_type == 'REPORT-METER' :
            PosReport(self.payload).AreaSelectOptionSiteInList(self.area_profile,self.total_site_in_area,'METER')
        elif self.report_type == 'REPORT-PRICE' :
            PosReport(self.payload).AreaSelectOptionSiteInList(self.area_profile,self.total_site_in_area,'PRICE')
        elif self.report_type == 'REPORT-SMB' :
            PosReport(self.payload).AreaSelectOptionSiteInList(self.area_profile,self.total_site_in_area,'SMB')
        
    def ShowMainAreaSelectOptionAreaManager(self) :
        if self.report_type == 'REPORT-XREPORT' :
            for i in self.all_area_manager :
                print ('รายชื่อผู้จัดการเขต {} ของรายงาน {} เขต Name {} เขต ID {}'.format(i.area_code_name,self.report_type,i.area_code_type,i.area_code_type.id))
            PosReport(self.payload).MainAreaSelectOptionAreaManager(self.currenty_position,self.currenty_user_name,self.all_area_manager,'X-REPORT')
        elif self.report_type == 'REPORT-METER' :
            for i in self.all_area_manager :
                print ('รายชื่อผู้จัดการเขต {} ของรายงาน {} เขต Name {} เขต ID {}'.format(i.area_code_name,self.report_type,i.area_code_type,i.area_code_type.id))
            PosReport(self.payload).MainAreaSelectOptionAreaManager(self.currenty_position,self.currenty_user_name,self.all_area_manager,'METER')
        elif self.report_type == 'REPORT-PRICE' :
            for i in self.all_area_manager :
                print ('รายชื่อผู้จัดการเขต {} ของรายงาน {} เขต Name {} เขต ID {}'.format(i.area_code_name,self.report_type,i.area_code_type,i.area_code_type.id))
            PosReport(self.payload).MainAreaSelectOptionAreaManager(self.currenty_position,self.currenty_user_name,self.all_area_manager,'PRICE')
        elif self.report_type == 'REPORT-SMB' :
            for i in self.all_area_manager :
                print ('รายชื่อผู้จัดการเขต {} ของรายงาน {} เขต Name {} เขต ID {}'.format(i.area_code_name,self.report_type,i.area_code_type,i.area_code_type.id))
            PosReport(self.payload).MainAreaSelectOptionAreaManager(self.currenty_position,self.currenty_user_name,self.all_area_manager,'SMB')
        
    def ShowSiteOptionByEOD(self,option,who_id):
        # if  self.report_type in ('XREPORT','SMB') :
        if option == 'ShowOptionSiteXREPORT':
            try :
                # ติดต่อ SQL เพื่อขอข้อมูลการปิดกะ ของวัน ณ ปัจจุบัน
                sql_command = mssql_command().get_x_report_close_shift_per_EOD()
                today_valible = self.today
                today_result_post = ConnectDBAlphaPOS(self.station_detail).Connect_SQL_SERVER(sql_command,today_valible,1,self.command_from_line)
                if today_result_post [0] == True:
                    if len(today_result_post[1]) > 0:
                        # xxxxxxxxxxxxxx ตัวแปร xxxxxxxxxxxxxx #
                        self.x_report_by_shift = today_result_post[1]
                        # xxxxxxxxxxxxxx ตัวแปร xxxxxxxxxxxxxx #
                        print ('ข้อมูลการปิดกะของคำสั่ง {} ของวันที่ {} สาขา {} สาขา PBL {} มีข้อมูล {} รายการ'.format(self.command_from_line,self.today,self.station_name,self.station_pbl,len(self.x_report_by_shift)))
                        return self.X_report()
                    elif len(today_result_post[1]) == 0:
                        print ('ไม่พบข้อมูลการปิดกะคำสั่ง {} ของวันที่ {} สาขา {} สาขา PBL {} ไม่มีข้อมูล'.format(self.command_from_line,self.today,self.station_name,self.station_pbl))
                        print ('ทำการเรียกรายการใหม่ โดยส่งวันที่ย้อนหลังไป 1 วัน คือ {} สาขา {} สาขา PBL {}'.format(self.yesterday,self.station_name,self.station_pbl))
                        # ทำการเรียกรายงานใหม่โดยการส่งวันที่ย้อนหลังไป 1 วัน
                        yesterday_result_post = ConnectDBAlphaPOS(self.station_detail).Connect_SQL_SERVER(sql_command,today_valible,2,self.command_from_line)
                        if yesterday_result_post [0] == True:
                            if len(yesterday_result_post[1]) > 0:
                                # xxxxxxxxxxxxxx ตัวแปร xxxxxxxxxxxxxx #
                                self.x_report_by_shift = yesterday_result_post[1]
                                
                                # xxxxxxxxxxxxxx ตัวแปร xxxxxxxxxxxxxx #
                                print ('ข้อมูลการปิดกะของคำสั่ง {} ของวันที่ {} สาขา {} สาขา PBL {} มีข้อมูล {} รายการ'.format(self.command_from_line,self.today,self.station_name,self.station_pbl,len(self.x_report_by_shift)))
                            
                            return self.X_report()
                        elif yesterday_result_post [0] == False:
                            print ('ไม่สามารถเรียกข้อมูลย้อนหลัง SQL ของคำสั่ง {} ของวันที่ย้อนหลัง {} สาขา {} สาขา PBL {} ไม่มีข้อมูล'.format(self.command_from_line,self.yesterday,self.station_name,self.station_pbl))
                            text_message = 'ไม่สามารถเรียกรายงานข้อมูลย้อนหลังของคำสั่ง {} ได้ เนื่องจากติดปัญหา {}  เวลา {}'.format(self.command_from_line,str(today_result_post[1]),self.today_time)
                            self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                            if self.debug_mode == True :
                                    db_logger.exception(yesterday_result_post[1])
                            return False
                elif today_result_post[0] == False:
                    print ('ไม่สามารติดต่อ SQL ของคำสั่ง {} ของวันที่ {} สาขา {} สาขา PBL {} ไม่มีข้อมูล'.format(self.command_from_line,self.today,self.station_name,self.station_pbl))
                    text_message = 'ไม่สามารถเรียกรายงาน {} ได้ เนื่องจากติดปัญหา {}  เวลา {}'.format(self.command_from_line,str(today_result_post[1]),self.today_time)
                    self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                    if self.debug_mode == True :
                            db_logger.exception(today_result_post[1])
                    return False    
            except Exception as e:
                print ('ไม่สามารเชื่อม SQL SERVER ของคำสั่ง {} ของวันที่ {} สาขา {} สาขา PBL {} ไม่มีข้อมูล'.format(self.command_from_line,self.today,self.station_name,self.station_pbl))
                text_message = 'ไม่สามารถเชื่อมต่อ SQL SERVER ของคำสั่ง {} ได้ เนื่องจากติดปัญหา {}  เวลา {}'.format(self.command_from_line,str(today_result_post[1]),self.today_time)
                self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                if self.debug_mode == True :
                        db_logger.exception(today_result_post[1])
                return False
        elif option == 'ShowOptionSiteMETER' :
            station_detail = StationProfile.objects.filter(station_site=self.station_pbl).first()
            date_request = self.today
            sql_command = mssql_command().get_meter_report_per_EOD()
            result_pos = ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,date_request,2)
            if result_pos[0] == True :
                if len(result_pos[1]) > 0 :
                    for evrIdent in result_pos[1] :
                        print ('ข้อมูลการทำรายการปิดกะ {}'.format(evrIdent))
                        # if 'z' not in evrIdent['EvrNum'] :
                        print ('First ข้อมูล Meter ล่าสุด ID {} Shift ID {}'.format(evrIdent['EvrIdent'],evrIdent['EvrNum']))
                        # ส่งข้อมูลไปสร้าง Flex Message
                        # PosReport(self.payload).METER_Selecter_by_Site(self.station_pbl,position,evrIdent)
                        PosReport(self.payload).StationSelectOption(self.station_detail,None,'METER',evrIdent)
                        # if flexmessages[0] == True :
                        #     SendFlexMessages(self.payload).ReplyMessage(self.reply_token,flexmessages[1])
                        #     break
                        # elif flexmessages[0] == False :
                        #     text_message = ('ไม่สามารถสร้างรายงาน Meter ของสาขา {} ได้ เนืองจาก {} '.format(self.station_pbl.userList_station_name,flexmessages[1]))
                        #     self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                        #     if station_detail.debug_mode == True :
                        #         db_logger.info(text_message)
                elif len(result_pos[1]) == 0 :
                        yesterday = self.yesterday
                        # ค้นหาวันที่ย้อนหลัง 1 วัน
                        dt = self.today_time
                        text_message = ('ไม่พบรายการเรียกหาข้อมูลปิดกะรายงาน X-Meter ของสาขา {} วันที่เรียกรายงาน {} ณ เวลา {} ระบบทำการจัดส่งรายงานย้อนหลังให้ 1 วัน'.format(self.station_pbl,date_request,dt))
                        print (text_message)
                        # บันทึกไปที่ log
                        db_logger.info(text_message)
                        # ติดต่อไปที่เครื่อง pos อีกครั้ง โดยส่งวันที่ย้อนหลังไป 1 วัน
                        result_pos_second = ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,yesterday,2)
                        if result_pos_second[0] == True :
                            for evrIdent in result_pos_second[1] :
                                if 'z' not in evrIdent['EvrNum'] : # กรณี EvrNum ลงท้ายด้วย z คึอกะที่ยังไม่ได้ตัดรอบ จะวนหา EvrNum ที่ลงท้ายด้วย 1 2 3 เท่านั้น
                                    print ('Second ข้อมูล Meter ล่าสุด ID {} Shift ID {}'.format(evrIdent['EvrIdent'],evrIdent['EvrNum']))
                                    # ส่งข้อมูลไปสร้าง Flex Message
                                    PosReport(self.payload).StationSelectOption(self.station_detail,None,'METER',evrIdent)
                                    break # สั่ง Break ให้ทำรายการแค่รายการแรกเท่านั้น
                                
                                else : # กรณีส่งวันที่ย้อนหลังไปเรียกรายงานแล้ว ยังไม่มีข้อมูล ก็ให้แจ้ง reply กลับไปแจ้ง User 
                                    dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                    text_message = ('ไม่พบรายการเรียกหาข้อมูลปิดกะรายงาน Meter ของสาขา {} วันที่เรียกรายงาน {} ณ เวลา {} กรุณาติดต่อผู้ดูแลระบบ'.format(self.station_name,yesterday,dt))
                                    self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                                    if station_detail.debug_mode == True :
                                        db_logger.info(text_message)
                                
                        # flexmessages=PosReport(payload).METER_Selecter_by_Site(station_id,position,evrIdent)
                
            elif result_pos[0] == False : # กรณีติดต่อฐานข้อมูลไม่สำเร็จ
                print ('ติดต่อขอข้อมูล Meter ไม่สำเร็จ {} '.format(result_pos[1]))
                dt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                text_message = 'ไม่สามารถเรียกรายงาน Meter ได้ เนื่องจากติดปัญหาการเชื่อมต่อ ณ เวลา {}'.format(dt)
                self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                if station_detail.debug_mode == True :
                    db_logger.exception(result_pos[1])   
            pass
        elif option == 'ShowOptionSitePRICE' :
            station_detail = StationProfile.objects.filter(station_site=self.station_pbl).first()
            sql_command = mssql_command().current_price()
            result_pos = ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,None,1)
            if result_pos[0] == True :
                if len(result_pos[1]) > 0 :
                    print ('ข้อมูลราคาน้ำมันจาก POS ถูกต้อง {}'.format(result_pos[1]))
                    PosReport(self.payload).PRICE(self.station_name,position,result_pos[1],self.report_type)
                elif len(result_pos[1]) == 0 :
                    print ('ไม่สามารถเรียกราคาน้ำมันได้ {}'.format(result_pos[1]))
                    dt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    text_message = 'ไม่สามารถเรียกรายงานราคาน้ำมัน ของสถานี {} ณ เวลา {}'.format(station_detail.station_name,dt)
                    self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))

            elif result_pos[0] == False :
                print ('ข้อมูลราคาน้ำมันจาก POS ไม่ถูกต้อง {}'.format(result_pos[1]))
                dt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            pass
        elif option == 'ShowOptionSiteSMB' :
            #             # ค้นหาข้อมูล Meter ล่าสุด
            
            station_detail = StationProfile.objects.filter(station_site=self.station_pbl).first()
            date_request = self.today
            sql_command = mssql_command().get_meter_report_per_EOD()
            result_pos = ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,date_request,2)
            if result_pos[0] == True :
                
                if len(result_pos[1]) > 0 :
                    for evrIdent in result_pos[1] :
                        print ('ข้อมูลการทำรายการปิดกะ {}'.format(evrIdent))
                        # if 'z' not in evrIdent['EvrNum'] :
                        print ('First ข้อมูล SMB ล่าสุด ID {} Shift ID {}'.format(evrIdent['EvrIdent'],evrIdent['EvrNum']))
                        # ส่งข้อมูลไปสร้าง Flex Message
                        PosReport(self.payload).SMB_Selecter_by_stie_single(self.station_detail,evrIdent,self.report_type)
                        break
                        # if flexmessages[0] == True :
                        #     SendFlexMessages(self.payload).ReplyMessage(self.reply_token,flexmessages[1])
                        #     break
                        # elif flexmessages[0] == False :
                        #     text_message = ('ไม่สามารถสร้างรายงาน SMB ของสาขา {} ได้ เนืองจาก {} '.format(self.station_pbl.userList_station_name,flexmessages[1]))
                        #     self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                        #     if station_detail.debug_mode == True :
                        #         db_logger.info(text_message)
                elif len(result_pos[1]) == 0 :
                        yesterday = self.yesterday
                        # ค้นหาวันที่ย้อนหลัง 1 วัน
                        dt = self.today_time
                        text_message = ('ไม่พบรายการเรียกหาข้อมูลปิดกะรายงาน SMB ของสาขา {} วันที่เรียกรายงาน {} ณ เวลา {} ระบบทำการจัดส่งรายงานย้อนหลังให้ 1 วัน'.format(self.station_pbl,date_request,dt))
                        print (text_message)
                        # บันทึกไปที่ log
                        db_logger.info(text_message)
                        # ติดต่อไปที่เครื่อง pos อีกครั้ง โดยส่งวันที่ย้อนหลังไป 1 วัน
                        result_pos_second = ConnectDBAlphaPOS(station_detail).Connect_DB(sql_command,yesterday,2)
                        if result_pos_second[0] == True :
                            for evrIdent in result_pos_second[1] :
                                if 'z' not in evrIdent['EvrNum'] : # กรณี EvrNum ลงท้ายด้วย z คึอกะที่ยังไม่ได้ตัดรอบ จะวนหา EvrNum ที่ลงท้ายด้วย 1 2 3 เท่านั้น
                                    print ('Second ข้อมูล SMB ล่าสุด ID {} Shift ID {}'.format(evrIdent['EvrIdent'],evrIdent['EvrNum']))
                                    # ส่งข้อมูลไปสร้าง Flex Message
                                    PosReport(self.payload).SMB_Selecter_by_stie_single(self.station_detail,evrIdent,self.report_type)
                    
                                    break # สั่ง Break ให้ทำรายการแค่รายการแรกเท่านั้น
                                
                                else : # กรณีส่งวันที่ย้อนหลังไปเรียกรายงานแล้ว ยังไม่มีข้อมูล ก็ให้แจ้ง reply กลับไปแจ้ง User 
                                    dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                    text_message = ('ไม่พบรายการเรียกหาข้อมูลปิดกะรายงาน SMB ของสาขา {} วันที่เรียกรายงาน {} ณ เวลา {} กรุณาติดต่อผู้ดูแลระบบ'.format(self.station_pbl,yesterday,dt))
                                    self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                                    if station_detail.debug_mode == True :
                                        db_logger.info(text_message)
                                
                
            elif result_pos[0] == False : # กรณีติดต่อฐานข้อมูลไม่สำเร็จ
                print ('ติดต่อขอข้อมูล Meter ไม่สำเร็จ {} '.format(result_pos[1]))
                dt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                text_message = 'ไม่สามารถเรียกรายงาน Meter ได้ เนื่องจากติดปัญหาการเชื่อมต่อ ณ เวลา {}'.format(dt)
                self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
                if station_detail.debug_mode == True :
                    db_logger.exception(result_pos[1])   

    def X_report(self):
        try :
            for last_close_shift in self.x_report_by_shift :
                print ('last_close_shift : {}'.format(last_close_shift))
                if last_close_shift['KhdBasTime'] != None :
                    last_close_shift_id = last_close_shift['KhdIdent']
                    print ('KhdIdent ID : {} '.format(last_close_shift_id))
                    PosReport(self.payload).StationSelectOption(self.station_detail,last_close_shift_id,'X-REPORT',None)
                    break
                else :
                    print ('ยังไม่มีการปิดกะล่าสุด')
                    break
            # บันทึกประวัติการทำรายการ
            # user_id_line = UserListCodeType.objects.filter(userList_userid=user_id).first()
        except Exception as e:
            print ('มีข้อผิดพลาดเกิดขึ้น คือ {}'.format(e))
            text_message = 'มีข้อผิดพลาดเกิดขึ้น ของคำสั่ง {} สาขา {} เนื่องจากติดปัญหา {}  เวลา {}'.format(self.command_from_line,self.station_name,str(e),self.today_time)
            self.line_bot_api.reply_message(self.reply_token, TextSendMessage(text=text_message))
            if self.debug_mode == True :
                    db_logger.exception(str(e))
            return False , e

        