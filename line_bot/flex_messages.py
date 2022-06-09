# -*- coding: utf-8 -*-
# !/usr/bin/env python
from email import message
from certifi import contents
from linebot import LineBotApi
from apps.home.models import *
from datetime import datetime
from apps.home.models import *
from dateutil.relativedelta import relativedelta
from line_bot.connecting_line_server import *
import logging
db_logger = logging.getLogger('db')



class FlexMessages :
    def __init__(self):
        print ('Start To Create FlexMessages')
    def Menu_Request(self):
      centent = {
  "type": "bubble",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "margin": "none",
    "align": "start",
    "gravity": "center",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "SUSCO",
      "uri": "https://www.susco.co.th/index.asp"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "เลือกรายงานที่ต้องการ",
        "weight": "bold",
        "size": "lg",
        "align": "center",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "X-REPORT",
            "weight": "bold",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT ปัจจุบัน",
              "data": "REPORT-XREPORT"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "SMB คะแนนสะสม",
            "weight": "bold",
            "size": "md",
            "flex": 2,
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล SMB ",
              "data": "REPORT-SMB"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "เลขมิเตอร์",
            "weight": "bold",
            "size": "md",
            "flex": 2,
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ",
              "data": "REPORT-METER"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "ราคาน้ำมัน",
            "weight": "bold",
            "size": "md",
            "flex": 2,
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล PRICE",
              "data": "REPORT-PRICE"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "การตั้งค่า",
            "weight": "bold",
            "size": "md",
            "flex": 2,
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล SMB ",
              "data": "SETTING"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "text",
        "text": "ตัวเลือกรายงาน",
        "weight": "bold",
        "size": "lg",
        "color": "#AA1C1CFF",
        "align": "center",
        "gravity": "top",
        "wrap": True,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def PushApprovedChangeNewAreaManager(self):
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "อนุมัติเปลี่ยนเขตดูแล",
        "weight": "bold",
        "size": "xl",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ข้อมูลเขตใหม่",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "เขต Susco10",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "ชื่อเจ้าของเขต",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "คุณ xxxxxxxxxxxxxxxx",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "Line_ID ยังไม่มีการ Register",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "spacer",
        "size": "sm"
      },
      {
        "type": "text",
        "text": "ผู้อนุมัติ : Admin",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "วันที่อนุมัติ : 21/05/22 15:15",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ReplyBackToUserChangeNewAreaManager(self,current_area_id,new_area_id):
      dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      # ทำการ query ข้อมูลผู้จัดการเขตที่มีอยู่ในระบบทั้งหมด
      all_area_manager_in_user_list = UserListCodeType.objects.filter(userList_position=3,userList_activate=True).all()
      for i in all_area_manager_in_user_list :
        print ('5555555555',i.userList_area_name.id)
      # ทำการค้นหาข้อมูลของผู้จัดการเขต ที่ต้องการจะเปลี่ยน
      area_profile = AreaCodeType.objects.filter(id=new_area_id).first()
      # ค้นหาข้อมูลผู้จัดการเขตคนเดิม
      for current_area_manager in all_area_manager_in_user_list :
        print ('current_area_manager',current_area_manager.userList_area_name.id)
        print ('current_area_manager 5555555',current_area_id)

        if current_area_manager.userList_area_name.id == int(current_area_id) :
          print ('ข้อมูลผู้จัดการเขตคนเดิมค้นพบ')
          #ค้นหาชื่อ ผู้จัดการเขต
          current_area_manager_name = AreaCodeType.objects.filter(area_code_type__id=current_area_manager.userList_area_name.id).first()
          print ('current_area_manager_name',current_area_manager_name)
          current_area_code = current_area_manager.userList_area_name.code_in_area_code_name
          current_area_name = current_area_manager_name.area_code_name
          current_area_line_id = current_area_manager.userList_display_name

      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ขออนุมัติเปลี่ยนเขตดูแล",
        "weight": "bold",
        "size": "xl",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ข้อมูลเขตเดิม",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "เขต " + current_area_code,
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "คุณ " + current_area_name,
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "LineID : " + current_area_line_id,
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "วันที่ขออนุมัติ {}".format(dt),
        "weight": "bold",
        "size": "xs",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ข้อมูลเขตใหม่",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "เขต " + area_profile.area_code_type.code_in_area_code_name,
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "ชื่อเจ้าของเขต",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "คุณ " + area_profile.area_code_name,
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "Line_ID ยังไม่มีการ Register",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ขออนุมัติอีกครั้ง",
          "text": "ข้อความระบบ : กำลังทำรายการขออนุมัติอีกครั้ง",
          "data": "AREA-REGISTER-PROCESS-CHANGE_AREA-CURRENTAREAID{}NEWAREAID{}END".format(current_area_id,new_area_id)
        },
        "color": "#078025FF",
        "margin": "none",
        "height": "sm",
        "style": "secondary"
      },
      
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ChangeNewAreaManager(self,current_area_id,new_area_id):
      dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      # ทำการ query ข้อมูลผู้จัดการเขตที่มีอยู่ในระบบทั้งหมด
      all_area_manager_in_user_list = UserListCodeType.objects.filter(userList_position=3,userList_activate=True).all()
      for i in all_area_manager_in_user_list :
        print ('5555555555',i.userList_area_name.id)
      # ทำการค้นหาข้อมูลของผู้จัดการเขต ที่ต้องการจะเปลี่ยน
      area_profile = AreaCodeType.objects.filter(id=new_area_id).first()
      # ค้นหาข้อมูลผู้จัดการเขตคนเดิม
      for current_area_manager in all_area_manager_in_user_list :
        print ('current_area_manager',current_area_manager.userList_area_name.id)
        print ('current_area_manager 5555555',current_area_id)

        if current_area_manager.userList_area_name.id == int(current_area_id) :
          print ('ข้อมูลผู้จัดการเขตคนเดิมค้นพบ')
          #ค้นหาชื่อ ผู้จัดการเขต
          current_area_manager_name = AreaCodeType.objects.filter(area_code_type__id=current_area_manager.userList_area_name.id).first()
          print ('current_area_manager_name',current_area_manager_name)
          current_area_code = current_area_manager.userList_area_name.code_in_area_code_name
          current_area_name = current_area_manager_name.area_code_name
          current_area_line_id = current_area_manager.userList_display_name

      centent = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ขออนุมัติเปลี่ยนเขตดูแล",
                      "weight": "bold",
                      "size": "xl",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "ข้อมูลเขตเดิม",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เขต " + current_area_code,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text":"คุณ" +  current_area_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": current_area_line_id,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "วันที่ขออนุมัติ {}".format(dt),
                      "weight": "bold",
                      "size": "xs",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "ข้อมูลเขตใหม่",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เขต " + area_profile.area_code_type.code_in_area_code_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ชื่อเจ้าของเขต",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "คุณ " + area_profile.area_code_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "Line_ID ยังไม่มีการ Register",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 0,
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "อนุมัติ",
                        "text": "ข้อความระบบ : กำลังทำรายการอนุมัติ",
                        "data": "AREA-REGISTER-PROCESS-RESPOND-SAYYES-CURRENTAREAID{}NEWAREAID{}END".format(current_area_id,new_area_id)
                      },
                      "color": "#078025FF",
                      "margin": "none",
                      "height": "sm",
                      "style": "secondary"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "ไม่อนุมัติ",
                        "text": "ข้อความระบบ : กำลังทำรายการไม่อนุมัติ",
                        "data": "AREA-REGISTER-PROCESS-RESPOND-SAYNO-CURRENTAREAID{}NEWAREAID{}END".format(current_area_id,new_area_id)
                      },
                      "color": "#706C6CFF",
                      "height": "sm",
                      "style": "primary"
                    },
                    {
                      "type": "spacer",
                      "size": "sm"
                    }
                  ]
                }
              }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
                            
    def ChangeNewAreaManagerWithNoNewIDManager(self,current_area):
      dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
     
      centent = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ขออนุมัติเปลี่ยนเขตดูแล",
                      "weight": "bold",
                      "size": "xl",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "ข้อมูลเขตเดิม",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เขต " + current_area.area_code_type.code_in_area_code_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text":"คุณ" +  current_area.area_code_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    # {
                    #   "type": "text",
                    #   "text": 'current_area_line_id',
                    #   "weight": "bold",
                    #   "color": "#293CCDFF",
                    #   "align": "center",
                    #   "margin": "lg",
                    #   "wrap": True,
                    #   "contents": []
                    # },
                    {
                      "type": "text",
                      "text": "วันที่ขออนุมัติ {}".format(dt),
                      "weight": "bold",
                      "size": "xs",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "ข้อมูลเขตใหม่",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เขต " + 'area_profile.area_code_type.code_in_area_code_name',
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ชื่อเจ้าของเขต",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "คุณ " + 'area_profile.area_code_name',
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "Line_ID ยังไม่มีการ Register",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 0,
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "อนุมัติ",
                        "text": "ข้อความระบบ : กำลังทำรายการอนุมัติ",
                        "data": "AREA-REGISTER-PROCESS-RESPOND-SAYYES-CURRENTAREAID{}NEWAREAID{}END".format('current_area_id','new_area_id')
                      },
                      "color": "#078025FF",
                      "margin": "none",
                      "height": "sm",
                      "style": "secondary"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "ไม่อนุมัติ",
                        "text": "ข้อความระบบ : กำลังทำรายการไม่อนุมัติ",
                        "data": "AREA-REGISTER-PROCESS-RESPOND-SAYNO-CURRENTAREAID{}NEWAREAID{}END".format('current_area_id','new_area_id')
                      },
                      "color": "#706C6CFF",
                      "height": "sm",
                      "style": "primary"
                    },
                    {
                      "type": "spacer",
                      "size": "sm"
                    }
                  ]
                }
              }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data

    def ShowSiteInArea(self,area_station,station_has_manager,manager_detail):
      # station_has_manager คือ ข้อมูลเขต ของ user_id ที่เรียกรายงาน
      # manager_detail คือ ข้อมูลเขต ที่โดนเรียกใช้ เพื่อขอดูข้อมูลสาขาที่อยู่ในเขตนี้
      print ('ข้อมูลเขต ID ของผู้จัดการที่ต้องการดูข้อมูลสาขา คือ ID {} ::::::: ข้อมูลเขต ID ของผู้จัดการเขตที่เรียกรายงาน {}'.format(manager_detail.id,station_has_manager.userList_area_name.id))
      if manager_detail.id == station_has_manager.userList_area_name.id :
        print ('OKKKKKK')
        label =  "เขตปัจจุบันของคุณ"
        text =  "ข้อความระบบ : เขตปัจจุบันของคุุณ ไม่สามารถย้ายเขตได้ กรุณาเลือกเขตใหม่"
        data =  "None"
      else :
        label =  "ย้ายเขตมานี้ กดที่นี้"
        text =  "ข้อความระบบ : รอสักครู่ กำลังจัดส่งตัวเลือก "
        data =  "AREA-REGISTER-PROCESS-CHANGE_AREA-CURRENTAREAID{}NEWAREAID{}END".format(station_has_manager.userList_area_name.id,manager_detail.id)
      
      # ค้นหาชื่อผู้จัดการเขต
      arae_name = AreaCodeType.objects.filter(area_code_type__id=station_has_manager.userList_area_name.id).first()
      #station_has_manager.userList_area_name.code_in_area_code_name
      centent = {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "margin": "none",
                    "align": "start",
                    "gravity": "center",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "SUSCO",
                      "uri": "https://www.susco.co.th/index.asp"
                    }
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "เขต " + manager_detail.area_code_type.code_in_area_code_name,
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการเขต",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": manager_detail.area_code_name,
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ชื่อสาขา",
                            "weight": "bold",
                            "size": "sm",
                            "flex": 1,
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          }
                          
                        ]
                      },
                      #ข้อมูลสาขา
                      
                      
                      {
                        "type": "separator",
                        "margin": "lg"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "รายชื่อในเขตดูแล",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#AA1C1CFF",
                        "align": "center",
                        "gravity": "top",
                        "wrap": True,
                        "contents": []
                      },
                      
                      {
                        "type": "separator"
                      },
                      {
                        "type": "text",
                        "text": "ข้อมูลเขตปัจจุบัน",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "เขต " + station_has_manager.userList_area_name.code_in_area_code_name,
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการเขต",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": arae_name.area_code_name,
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": label,
                          "text": text,
                          "data": data
                        },
                        "color": "#12AA3DFF",
                        "margin": "md",
                        "height": "sm"
                      }
                    ]
                  }
                }
      
      for i in area_station :
        if i.id == station_has_manager.id :
          manager_register = 'OK'
          color = '#0C7537FF'
          post_back = 'DISPLAY-STATION-BRANCH-ID{}'.format(station_has_manager.id)
        else : 
          manager_register = 'NOK'
          color = '#FF0000'
          post_back = 'NONE'
        station = {
                          "type": "box",
                          "layout": "horizontal",
                          "margin": "lg",
                          "contents": [
                            {
                              "type": "text",
                              "text": "{}".format(i.station_name),
                              "weight": "bold",
                              "size": "xs",
                              "flex": 5,
                              "align": "start",
                              "gravity": "center",
                              "margin": "sm",
                              "contents": []
                            }

                            
                          ]
                        }
        centent['body']['contents'].insert(-1,station)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ShowSiteInAreaNew(self,area_station,station_has_manager,manager_detail):
          # station_has_manager คือ ข้อมูลเขต ของ user_id ที่เรียกรายงาน
      # manager_detail คือ ข้อมูลเขต ที่โดนเรียกใช้ เพื่อขอดูข้อมูลสาขาที่อยู่ในเขตนี้
      print ('ข้อมูลเขต ID ของผู้จัดการที่ต้องการดูข้อมูลสาขา คือ ID {} ::::::: ข้อมูลเขต ID ของผู้จัดการเขตที่เรียกรายงาน {}'.format(manager_detail.id,station_has_manager.userList_area_name.id))
      if manager_detail.id == station_has_manager.userList_area_name.id :
        print ('OKKKKKK')
        label =  "เขตปัจจุบันของคุณ"
        text =  "ข้อความระบบ : เขตปัจจุบันของคุุณ ไม่สามารถย้ายเขตได้ กรุณาเลือกเขตใหม่"
        data =  "None"
      else :
        label =  "ย้ายเขตมานี้ กดที่นี้"
        text =  "ข้อความระบบ : รอสักครู่ กำลังจัดส่งตัวเลือก "
        data =  "AREA-REGISTER-PROCESS-CHANGE_AREA-CURRENTAREAID{}NEWAREAID{}END".format(station_has_manager.userList_area_name.id,manager_detail.id)
      
      # ค้นหาชื่อผู้จัดการเขต
      arae_name = AreaCodeType.objects.filter(area_code_type__id=station_has_manager.userList_area_name.id).first()
      #station_has_manager.userList_area_name.code_in_area_code_name
      centent = {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "margin": "none",
                    "align": "start",
                    "gravity": "center",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "SUSCO",
                      "uri": "https://www.susco.co.th/index.asp"
                    }
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "เขต " + manager_detail.area_code_type.code_in_area_code_name,
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการเขต",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": manager_detail.area_code_name,
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ชื่อสาขา",
                            "weight": "bold",
                            "size": "sm",
                            "flex": 1,
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          }
                          
                        ]
                      },
                      #ข้อมูลสาขา
                      
                      
                      {
                        "type": "separator",
                        "margin": "lg"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "รายชื่อในเขตดูแล",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#AA1C1CFF",
                        "align": "center",
                        "gravity": "top",
                        "wrap": True,
                        "contents": []
                      },
                      
                      {
                        "type": "separator"
                      },
                      {
                        "type": "text",
                        "text": "ข้อมูลเขตปัจจุบัน",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "เขต " + station_has_manager.userList_area_name.code_in_area_code_name,
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการเขต",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": arae_name.area_code_name,
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": label,
                          "text": text,
                          "data": data
                        },
                        "color": "#12AA3DFF",
                        "margin": "md",
                        "height": "sm"
                      }
                    ]
                  }
                }
      
      for i in area_station :
        if i.id == station_has_manager.id :
          manager_register = 'OK'
          color = '#0C7537FF'
          post_back = 'DISPLAY-STATION-BRANCH-ID{}'.format(station_has_manager.id)
        else : 
          manager_register = 'NOK'
          color = '#FF0000'
          post_back = 'NONE'
        station = {
                          "type": "box",
                          "layout": "horizontal",
                          "margin": "lg",
                          "contents": [
                            {
                              "type": "text",
                              "text": "{}".format(i.station_name),
                              "weight": "bold",
                              "size": "xs",
                              "flex": 5,
                              "align": "start",
                              "gravity": "center",
                              "margin": "sm",
                              "contents": []
                            }

                            
                          ]
                        }
        centent['body']['contents'].insert(-1,station)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ShowSiteInAreaNoManager(self,area_station,station_has_manager,manager_detail,area_id):
      # station_has_manager คือ ข้อมูลเขต ของ user_id ที่เรียกรายงาน
      # manager_detail คือ ข้อมูลเขต ที่โดนเรียกใช้ เพื่อขอดูข้อมูลสาขาที่อยู่ในเขตนี้
      # print ('ข้อมูลเขต ID ของผู้จัดการที่ต้องการดูข้อมูลสาขา คือ ID {} ::::::: ข้อมูลเขต ID ของผู้จัดการเขตที่เรียกรายงาน {}'.format(manager_detail.id,station_has_manager.userList_area_name.id))
      # if manager_detail.id == station_has_manager.userList_area_name.id :
      #   print ('OKKKKKK')
      #   label =  "เขตปัจจุบันของคุณ"
      #   text =  "ข้อความระบบ : เขตปัจจุบันของคุุณ ไม่สามารถย้ายเขตได้ กรุณาเลือกเขตใหม่"
      #   data =  "None"
      # else :
      label =  "ย้ายเขตมานี้ กดที่นี้"
      text =  "ข้อความระบบ : รอสักครู่ กำลังจัดส่งตัวเลือก "
      data =  "AREA-REGISTER-PROCESS-CHANGE_AREA-CURRENTAREAID{}NEWAREAID{}END".format(station_has_manager.userList_area_name.id,manager_detail)
      
      # ค้นหาชื่อผู้จัดการเขต
      arae_name = AreaCodeType.objects.filter(area_code_type__id=station_has_manager.userList_area_name.id).first()
      #station_has_manager.userList_area_name.code_in_area_code_name
      centent = {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "margin": "none",
                    "align": "start",
                    "gravity": "center",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "SUSCO",
                      "uri": "https://www.susco.co.th/index.asp"
                    }
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "เขต " + area_id.code_in_area_code_name ,
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการเขต",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ไม่มีระบุชื่อผู้จัดการเขต",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ชื่อสาขา",
                            "weight": "bold",
                            "size": "sm",
                            "flex": 1,
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          }
                          
                        ]
                      },
                      #ข้อมูลสาขา
                      
                      
                      {
                        "type": "separator",
                        "margin": "lg"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "รายชื่อในเขตดูแล",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#AA1C1CFF",
                        "align": "center",
                        "gravity": "top",
                        "wrap": True,
                        "contents": []
                      },
                      
                      {
                        "type": "separator"
                      },
                      {
                        "type": "text",
                        "text": "ข้อมูลเขตปัจจุบัน",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "เขต " + arae_name.area_code_type.code_in_area_code_name ,
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการเขต",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": 'คุณ ' + arae_name.area_code_name,
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": label,
                          "text": text,
                          "data": data
                        },
                        "color": "#12AA3DFF",
                        "margin": "md",
                        "height": "sm"
                      }
                    ]
                  }
                }
      
      for i in area_station :
        if i.id == station_has_manager.id :
          manager_register = 'OK'
          color = '#0C7537FF'
          post_back = 'DISPLAY-STATION-BRANCH-ID{}'.format(station_has_manager.id)
        else : 
          manager_register = 'NOK'
          color = '#FF0000'
          post_back = 'NONE'
        station = {
                          "type": "box",
                          "layout": "horizontal",
                          "margin": "lg",
                          "contents": [
                            {
                              "type": "text",
                              "text": "{}".format(i.station_name),
                              "weight": "bold",
                              "size": "xs",
                              "flex": 5,
                              "align": "start",
                              "gravity": "center",
                              "margin": "sm",
                              "contents": []
                            }

                            
                          ]
                        }
        centent['body']['contents'].insert(-1,station)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ShowAreaListInStation(self,all_station_count_with_area_name,all_manager_in_system):
      
      centent = {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "เลือกเขตที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                              {
                                "type": "text",
                                "text": "ชื่อเขต",
                                "weight": "bold",
                                "size": "sm",
                                "align": "start",
                                "gravity": "center",
                                "margin": "sm",
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "จำนวนสาขา",
                                "weight": "bold",
                                "size": "sm",
                                "align": "center",
                                "gravity": "center",
                                "margin": "sm",
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "ข้อมูล",
                                "weight": "bold",
                                "size": "sm",
                                "align": "end",
                                "gravity": "center",
                                "margin": "sm",
                                # "action": {
                                #   "type": "postback",
                                #   "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                                #   "data": "AREA-SMB-SITE5001"
                                # },
                                "contents": []
                              }
                            ]
                          },
                          # ข้อมูลสาขา
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "รายชื่อเขตเรียงตามเขตดูแล",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "กด เลือก เพื่อให้ระบบส่งข้อมูลรายชื่อสาขาที่อยู่ในเขตทั้งหมด",
                            "weight": "bold",
                            "size": "xs",
                            "align": "center",
                            "wrap": True,
                            "contents": []
                          }
                        ]
                      }
                    }
      for area in all_station_count_with_area_name :
        # print (area)
        # ค้นหา id ของผู้จัดการเขต
        # print ('station_area_code__id ',area['station_area_code__id'])
        CodeTypeCode = area['station_area_code__id']
        area_name = AreaCodeType.objects.filter(area_code_type__id=area['station_area_code__id']).first()
        if area_name == None :
          print ('ไม่พบข้อมูลของเขตที่ต้องการ ID {}'.format(area['station_area_code__id']))
          area_name_2 = 'inwaiting'
        else :
          area_name_2 = area_name.id
        # print (type(area_name))
        # print ('area_name {}'.format(area_name))
        # print ('area_name_ID {}'.format(area_name.id))
        
        area_detail = {
                              "type": "box",
                              "layout": "horizontal",
                              "margin": "lg",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": area['station_area_code__code_in_area_code_name'],
                                  "weight": "bold",
                                  "size": "xs",
                                  "align": "start",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "contents": []
                                },
                                {
                                  "type": "text",
                                  "text": str(area['entries']),
                                  "weight": "bold",
                                  "size": "sm",
                                  "color": "#0C7537FF",
                                  "align": "center",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "action": {
                                    "type": "postback",
                                    "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                                    "data": "DISPLAY-STATION-SHOW-ID{}CODE{}END".format(str(area_name_2),str(CodeTypeCode))
                                  },
                                  "contents": []
                                },
                                {
                                  "type": "text",
                                  "text": "เลือก",
                                  "weight": "bold",
                                  "size": "sm",
                                  "color": "#CA1F12FF",
                                  "align": "end",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "action": {
                                    "type": "postback",
                                
                                    "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                                    "data": "DISPLAY-STATION-SHOW-ID{}CODE{}END".format(str(area_name_2),str(CodeTypeCode))
                                  },
                                  "contents": []
                                }
                              ]
                            }
        centent["body"]["contents"].insert(-1,area_detail)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    
    def ShowStationListInArea(self,area_id):
      # Check Station TM in Inwaiting or not 
      TM_Status_Last = area_id.area_code_type.id
      # if TM_Status_Last != 17 : #inwaiting
      


      
        
      
      all_station_in_this_area_manager = StationProfile.objects.filter(station_area_code=area_id).all()
      station_has_manager = UserListCodeType.objects.filter(userList_area_name=area_id,userList_position=1).first()
      
      
      centent = {
                              "type": "bubble",
                              "direction": "ltr",
                              "hero": {
                                "type": "image",
                                "url": "https://www.susco.co.th/images/logo_susco.png",
                                "margin": "none",
                                "align": "start",
                                "gravity": "center",
                                "size": "full",
                                "aspectRatio": "22:6",
                                "aspectMode": "fit",
                                "backgroundColor": "#F2EC3EFF",
                                "action": {
                                  "type": "uri",
                                  "label": "SUSCO",
                                  "uri": "https://www.susco.co.th/index.asp"
                                }
                              },
                              "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "เขต "+area_name.code_in_area_code_name,
                                    "weight": "bold",
                                    "size": "lg",
                                    "align": "center",
                                    "contents": []
                                  },
                                  {
                                    "type": "text",
                                    "text": "เลือกสถานีที่ต้องการ",
                                    "weight": "bold",
                                    "size": "lg",
                                    "align": "center",
                                    "contents": []
                                  },
                                  {
                                    "type": "separator",
                                    "margin": "lg"
                                  },
                                  {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "margin": "lg",
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "ชื่อสาขา",
                                        "weight": "bold",
                                        "size": "sm",
                                        "flex": 1,
                                        "align": "center",
                                        "gravity": "center",
                                        "margin": "sm",
                                        "contents": []
                                      },
                                      {
                                        "type": "text",
                                        "text": "ผู้จัดการสาขา",
                                        "weight": "bold",
                                        "size": "sm",
                                        "align": "end",
                                        "gravity": "center",
                                        "margin": "sm",
                                        "action": {
                                          "type": "postback",
                                          "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                                          "data": "AREA-SMB-SITE5001"
                                        },
                                        "contents": []
                                      }
                                    ]
                                  },
                                  # ข้อมูลสาขาที่อยู่ใน เขต 
                                  
                                  
                                  {
                                    "type": "separator",
                                    "margin": "lg"
                                  }
                                ]
                              },
                              "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "รายชื่อในเขตดูแล",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#AA1C1CFF",
                                    "align": "center",
                                    "gravity": "top",
                                    "wrap": True,
                                    "contents": []
                                  },
                                  {
                                    "type": "text",
                                    "text": "สถานะ OK คือผู้จัดการสาขาทำการลงทะเบียนแล้ว สถานะ NOK คือ ยังไม่มีผู้จัดการสาขาลงทะเบียน  กดเลือกที่ OK เพื่อดูสถานะของผู้จัดการสาขา",
                                    "weight": "bold",
                                    "size": "xs",
                                    "align": "center",
                                    "wrap": True,
                                    "contents": []
                                  }
                                ]
                              }
                            }
      for i in all_station_in_this_area_manager :
        if i.id == station_has_manager.userList_station_name.id :
          manager_register = 'OK'
          color = '#0C7537FF'
          post_back = 'DISPLAY-STATION-BRANCH-ID{}'.format(station_has_manager.id)
        else : 
          manager_register = 'NOK'
          color = '#FF0000'
          post_back = 'NONE'

        station_in_area = {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "contents": [
                          {
                            "type": "text",
                            "text": "{}".format(i.station_name),
                            "weight": "bold",
                            "size": "xs",
                            "flex": 5,
                            "align": "start",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": manager_register,
                            "weight": "bold",
                            "size": "sm",
                            "color": color,
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "action": {
                              "type": "postback",
                              "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลผู้จัดการสาขา",
                              "data": post_back
                            },
                            "contents": []
                          }
                        ]
                      }
        
        
        centent['body']['contents'].append(station_in_area)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def AdminConfirmCode(self) :
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "กรุณาพิมพ์ admin ตามด้วยระหัส เพื่อยืนยันตัวตน",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "หากหน้าจอไม่แสดงแป้นพิมพ์ ให้กดที่รูปแป้นพิมพ์ตรงด้านล่างมุมซ้ายของหน้าจอ",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "xl",
        "wrap": True  ,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def Gressing_messages(self,display_name):
        data = {
                                              "type": "flex",
                                              "altText": 'message',
                                              "contents": {
                                              "type": "bubble",
                                              "hero": {
                                                "type": "image",
                                                "url": "https://www.susco.co.th/images/logo_susco.png",
                                                "margin": "xs",
                                                "align": "center",
                                                "gravity": "bottom",
                                                "size": "full",
                                                "aspectRatio": "22:6",
                                                "aspectMode": "fit",
                                                "backgroundColor": "#F2EC3EFF",
                                                "action": {
                                                  "type": "uri",
                                                  "label": "Line",
                                                  "uri": "https://linecorp.com/"
                                                },
                                                "position": "relative"
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "text": "SUSCO/ORPAK",
                                                    "weight": "bold",
                                                    "size": "xl",
                                                    "color": "#225508FF",
                                                    "align": "center",
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": display_name,
                                                    "weight": "bold",
                                                    "size": "sm",
                                                    "color": "#225508FF",
                                                    "align": "center",
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "ขอบคุณที่เพิ่มเราเป็นเพื่อน",
                                                    "align": "center",
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "separator",
                                                    "margin": "lg",
                                                    "color": "#E42424FF"
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "เราคือบริการ BOT ของ SUSCO สำหรับใช้ในระบบ POS NOTIFY เท่านั้น",
                                                    "weight": "bold",
                                                    "color": "#293CCDFF",
                                                    "align": "center",
                                                    "margin": "lg",
                                                    "wrap": True  ,
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "separator",
                                                    "margin": "xl",
                                                    "color": "#E42424FF"
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "flex": 0,
                                                "spacing": "sm",
                                                "contents": [
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "postback",
                                                      "label": "กด - ลงทะเบียนใช้งาน",
                                                      "data": "register"
                                                    },
                                                    "color": "#078025FF",
                                                    "margin": "none",
                                                    "height": "sm",
                                                    "style": "secondary"
                                                  },
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  }
                                                ]
                                              }
}
                                                }
        return data
    def SelectUserType(self):
      data = {
                                              "type": "flex",
                                              "altText": 'message',
                                              "contents": {
                                      "type": "bubble",
                                      "direction": "ltr",
                                      "hero": {
                                        "type": "image",
                                        "url": "https://www.susco.co.th/images/logo_susco.png",
                                        "margin": "none",
                                        "align": "start",
                                        "gravity": "center",
                                        "size": "full",
                                        "aspectRatio": "22:6",
                                        "aspectMode": "fit",
                                        "backgroundColor": "#F2EC3EFF",
                                        "action": {
                                          "type": "uri",
                                          "label": "SUSCO",
                                          "uri": "https://www.susco.co.th/index.asp"
                                        }
                                      },
                                      "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "เลือกระดับผู้ใช้งาน",
                                            "weight": "bold",
                                            "size": "md",
                                            "align": "center",
                                            "contents": []
                                          },
                                          {
                                            "type": "separator",
                                            "margin": "lg"
                                          },
                                          {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "lg",
                                            "position": "relative",
                                            "contents": [
                                              {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "text": "ผู้จัดการสาขา",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "align": "start",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "เลือก",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "color": "#FA4204FF",
                                                    "align": "end",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "action": {
                                                      "type": "postback",
                                                      "text": "ข้อความระบบ : เลือกผู้ใช้งานระดับ ผู้จัดการสาขา",
                                                      "data": "STATION-REGISTER-PROCESS-SELECTER"
                                                    },
                                                    "contents": []
                                                  }
                                                ]
                                              },
                                              {
                                                "type": "box",
                                                "layout": "baseline",
                                                "margin": "md",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "text": "ผู้ช่วยผู้จัดการ",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "align": "start",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "เลือก",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "color": "#FA4204FF",
                                                    "align": "end",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "action": {
                                                      "type": "postback",
                                                      "text": "ข้อความระบบ : เลือกผู้ใช้งานระดับ ผู้ช่วยผู้จัดการ",
                                                      "data": "SUB-STATION-REGISTER-PROCESS-SELECTER"
                                                    },
                                                    "contents": []
                                                  }
                                                ]
                                              },
                                              {
                                                "type": "box",
                                                "layout": "baseline",
                                                "margin": "md",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "text": "ผู้จัดการเขต",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "align": "start",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "เลือก",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "color": "#FA4204FF",
                                                    "align": "end",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "action": {
                                                      "type": "postback",
                                                      "text": "ข้อความระบบ : เลือกผู้ใช้งานระดับ ผู้จัดการเขต",
                                                      "data": "AREA-REGISTER-PROCESS-SELECTER"
                                                    },
                                                    "contents": []
                                                  }
                                                ]
                                              },
                                              {
                                                "type": "box",
                                                "layout": "baseline",
                                                "margin": "md",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "text": "ผู้จัดการภาค",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "align": "start",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "เลือก",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "color": "#FA4204FF",
                                                    "align": "end",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "action": {
                                                      "type": "postback",
                                                      "text": "ข้อความระบบ : เลือกผู้ใช้งานระดับ ผู้จัดการภาค",
                                                      "data": "MAIN-AREA-REGISTER-PROCESS-SELECTER"
                                                    },
                                                    "contents": []
                                                  }
                                                ]
                                              },
                                              {
                                                "type": "box",
                                                "layout": "baseline",
                                                "margin": "md",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "text": "ส่วนผู้ดูแลระบบ",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "align": "start",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "contents": []
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "เลือก",
                                                    "weight": "bold",
                                                    "size": "md",
                                                    "color": "#FA4204FF",
                                                    "align": "end",
                                                    "gravity": "center",
                                                    "margin": "sm",
                                                    "action": {
                                                      "type": "postback",
                                                      "text": "ข้อความระบบ : เลือกผู้ใช้งานระดับ ส่วนผู้ดูแลระบบ",
                                                      "data": "ADMIN-REGISTER-PROCESS-SELECTER"
                                                    },
                                                    "contents": []
                                                  }
                                                ]
                                              }
                                            ]
                                          },
                                          {
                                            "type": "separator",
                                            "margin": "lg"
                                          }
                                        ]
                                      },
                                      "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "flex": 0,
                                        "spacing": "sm",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "ลงทะเบียนผู้ใช้งาน",
                                            "weight": "bold",
                                            "size": "lg",
                                            "color": "#AA1C1CFF",
                                            "align": "center",
                                            "gravity": "center",
                                            "wrap": True  ,
                                            "contents": []
                                          }
                                        ]
                                      }
}
                                                }
      return data
    def ConfirmStationFailed(self):
      
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ไม่พบระหัสในการยืนยันสาขา กรุณาติดต่อฝ่ายบริการเพื่อตรวจสอบระหัสยืนยันตัวตน",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "หากหน้าจอไม่แสดงแป้นพิมพ์ ให้กดที่รูปแป้นพิมพ์ตรงด้านล่างมุมซ้ายของหน้าจอ",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "xl",
        "wrap": True  ,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def SelectStationID(self):
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "กรุณาพิมพ์ station ตามด้วยระหัสสาขาของท่าน เพื่อยืนยันตัวตน",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "หากหน้าจอไม่แสดงแป้นพิมพ์ ให้กดที่รูปแป้นพิมพ์ตรงด้านล่างมุมซ้ายของหน้าจอ",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "xl",
        "wrap": True  ,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def SelectAddMoreStationID(self):
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "กรุณาพิมพ์ addmoresite ตามด้วยระหัสสาขาของท่าน เพื่อยืนยันตัวตน ในการเพิ่มสาขาที่ดูแล",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "หากหน้าจอไม่แสดงแป้นพิมพ์ ให้กดที่รูปแป้นพิมพ์ตรงด้านล่างมุมซ้ายของหน้าจอ",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "xl",
        "wrap": True  ,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ConfirmedStationPass(self,station_list):
      confirmed_station = 'STATION-REGISTER-PROCESS-CONFIRM-STATION-ID' + str(station_list.station_site)
      centent = {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://www.susco.co.th/images/logo_susco.png",
                      "align": "center",
                      "gravity": "bottom",
                      "size": "full",
                      "aspectRatio": "22:6",
                      "aspectMode": "fit",
                      "backgroundColor": "#F2EC3EFF",
                      "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                      },
                      "position": "relative"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "ยืนยันสาขา ตามรายละเอียดนี้",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True  ,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": station_list.station_name,
                          "weight": "bold",
                          "color": "#D01111FF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": station_list.station_address,
                          "weight": "bold",
                          "color": "#D01111FF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 0,
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "ยืนยันใช่ฉัน",
                            "text": "ข้อความระบบ : รอสักครู่ กำลังทำการลงทะเบียน",
                            "data": confirmed_station
                          },
                          "color": "#078025FF",
                          "margin": "none",
                          "height": "sm",
                          "style": "secondary"
                        },
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "ไม่ใช่ ฉัน",
                            "text": "ข้อความระบบ : กรุณาทำรายการอีกครั้ง",
                            "data": "STATION-REGISTER-PROCESS-RESENT"
                          },
                          "color": "#706C6CFF",
                          "height": "sm",
                          "style": "primary"
                        },
                        {
                          "type": "spacer",
                          "size": "sm"
                        }
                      ]
                    }
                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ConfirmedAddMoreStationPass(self,station_list):
      confirmed_station = 'STATION-REGISTER-PROCESS-NEWSITE' + str(station_list.station_site)
      centent = {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://www.susco.co.th/images/logo_susco.png",
                      "align": "center",
                      "gravity": "bottom",
                      "size": "full",
                      "aspectRatio": "22:6",
                      "aspectMode": "fit",
                      "backgroundColor": "#F2EC3EFF",
                      "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                      },
                      "position": "relative"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "ยืนยันสาขา ตามรายละเอียดนี้",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True  ,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": station_list.station_name,
                          "weight": "bold",
                          "color": "#D01111FF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": station_list.station_address,
                          "weight": "bold",
                          "color": "#D01111FF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 0,
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "ยืนยันใช่ฉัน",
                            "text": "ข้อความระบบ : รอสักครู่ กำลังทำการลงทะเบียน",
                            "data": confirmed_station
                          },
                          "color": "#078025FF",
                          "margin": "none",
                          "height": "sm",
                          "style": "secondary"
                        },
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "ไม่ใช่ ฉัน",
                            "text": "ข้อความระบบ : กรุณาทำรายการอีกครั้ง",
                            "data": "STATION-REGISTER-PROCESS-ADD-MORE"
                          },
                          "color": "#706C6CFF",
                          "height": "sm",
                          "style": "primary"
                        },
                        {
                          "type": "spacer",
                          "size": "sm"
                        }
                      ]
                    }
                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def StationRegisterCompleted(self):
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ลงทะเบียนสำเร็จ",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "text",
        "text": "เลือกแถบ ส่วนสมาชิก แล้วเลือก",
        "weight": "bold",
        "color": "#D01111FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "text",
        "text": "สมาชิกเข้าใช้งาน",
        "weight": "bold",
        "color": "#D01111FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "หากหน้าจอไม่แสดงแถบเมนู ให้กดที่รูปเครื่องหมายขีดๆ ตรงด้านล่างมุมซ้ายของหน้าจอ",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def DupicateRegister(self,position_check):
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "มีการลงทะเบียนไว้แล้ว",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "text",
        "text": position_check.user_station_name.station_name,
        "weight": "bold",
        "color": "#D01111FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "text",
        "text": position_check.user_position.position_name,
        "weight": "bold",
        "color": "#D01111FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ConfirmedAreaPass(self):
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ลงทะเบียนสำเร็จ",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "text",
        "text": "ตำแหน่ง ผู้จัดการเขต",
        "weight": "bold",
        "color": "#D01111FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "กรุณาแจ้งผู้จัดการในเขตดูแลของท่าน ให้ทำการเลือกผู้จัดการเขตในระบบต่อไป",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ConfirmedAreaSelecter(self,user_id,command):
      # if command == 'UserType01':
      #   position = 'ผู้จัดการสาขา'
      #   user_confirmed = 'UserType01'
      #   pass
      # elif command == 'UserType02':
      #   position = 'ผู้ช่วยผู้จัดการ'
      #   user_confirmed = 'UserType02'
      #   pass
      # elif command == 'UserType03':
      #   position = 'ผู้จัดการเขต'
      #   user_confirmed = 'UserType03'
      #   pass
      # elif command == 'UserType04':
      #   position = 'ผู้จัดการภาค'
      #   user_confirmed = 'UserType04'
      #   pass
      # elif command == 'UserType05':
      #   position = 'ส่วนผู้ดูแลระบบ'
      #   user_confirmed = 'UserType05'
      #   pass
      
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ยืนยัน ตำแหน่งที่คุณต้องการลงทะเบียน",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "text",
        "text": position,
        "weight": "bold",
        "color": "#D01111FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ยืนยัน",
          "text": "รอสักครู่ กำลังทำการลงทะเบียน",
          "data": user_confirmed
        },
        "color": "#078025FF",
        "margin": "none",
        "height": "sm",
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ไม่ใช่",
          "text": "กรุณาเลือกรายการใหม่",
          "data": "POSITION-NOK"
        },
        "color": "#706C6CFF",
        "height": "sm",
        "style": "primary"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ConfirmedPositionSelect(self,user_id,command):
      if command == 'UserType01':
        position = 'ผู้จัดการสาขา'
        user_confirmed = 'STATION-REGISTER-PROCESS-CONFIRMPOSITION'
        user_cancel = 'STATION-REGISTER-PROCESS-CANCEL'
        pass
      elif command == 'UserType02':
        position = 'ผู้ช่วยผู้จัดการ'
        user_confirmed = 'SUB-STATION-REGISTER-PROCESS-CONFIRMPOSITION'
        user_cancel = 'SUB-STATION-REGISTER-PROCESS-CANCEL'
        pass
      elif command == 'UserType03':
        position = 'ผู้จัดการเขต'
        user_confirmed = 'AREA-REGISTER-PROCESS-CONFIRMPOSITION'
        user_cancel = 'AREA-REGISTER-PROCESS-CANCEL'
        pass
      elif command == 'UserType04':
        position = 'ผู้จัดการภาค'
        user_confirmed = 'MAIN-AREA-REGISTER-PROCESS-CONFIRMPOSITION'
        user_cancel = 'MAIN-AREA-REGISTER-PROCESS-CANCEL'
        pass
      elif command == 'UserType05':
        position = 'ส่วนผู้ดูแลระบบ'
        user_confirmed = 'ADMIN-REGISTER-PROCESS-CONFIRMPOSITION'
        user_cancel = 'ADMIN-REGISTER-PROCESS-CANCEL'
        pass
      
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ยืนยัน ตำแหน่งที่คุณต้องการลงทะเบียน",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "text",
        "text": position,
        "weight": "bold",
        "color": "#D01111FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ยืนยัน",
          "text": "รอสักครู่ กำลังทำการลงทะเบียน",
          "data": user_confirmed
        },
        "color": "#078025FF",
        "margin": "none",
        "height": "sm",
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ไม่ใช่",
          "text": "กรุณาเลือกรายการใหม่",
          "data": user_cancel
        },
        "color": "#706C6CFF",
        "height": "sm",
        "style": "primary"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def LoginSuccessed(self,profile,user_check):
      dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      centent = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "เข้าสู่ระบบเรียบร้อย",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True  ,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": dt,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True  ,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": profile.display_name,
                      "weight": "bold",
                      "color": "#D01111FF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": user_check.userList_position.position_name,
                      "weight": "bold",
                      "color": "#D01111FF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 0,
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "ออกจากระบบ",
                        "text": "รอสักครู่ กำลังออกจากระบบ",
                        "data": "LOGOUT"
                      },
                      "color": "#078025FF",
                      "margin": "none",
                      "height": "sm",
                      "style": "secondary"
                    },
                    {
                      "type": "spacer",
                      "size": "sm"
                    }
                  ]
                }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def LogOutSuccessed(self,profile):
      dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      centent = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "ออกจากระบบเรียบร้อย",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True  ,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": dt,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True  ,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": profile.display_name,
                      "weight": "bold",
                      "color": "#D01111FF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 0,
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "เข้าสู่ระบบ",
                        "text": "รอสักครู่ กำลังออกจากระบบ",
                        "data": "botlogin"
                      },
                      "color": "#078025FF",
                      "margin": "none",
                      "height": "sm",
                      "style": "secondary"
                    },
                    {
                      "type": "spacer",
                      "size": "sm"
                    }
                  ]
                }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def StationSetting(self,user_profile):
      dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      centent = {
                              "type": "bubble",
                              "direction": "ltr",
                              "hero": {
                                "type": "image",
                                "url": "https://www.susco.co.th/images/logo_susco.png",
                                "margin": "none",
                                "align": "start",
                                "gravity": "center",
                                "size": "full",
                                "aspectRatio": "22:6",
                                "aspectMode": "fit",
                                "backgroundColor": "#F2EC3EFF",
                                "action": {
                                  "type": "uri",
                                  "label": "SUSCO",
                                  "uri": "https://www.susco.co.th/index.asp"
                                }
                              },
                              "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": user_profile.user_station_name.station_name,
                                    "weight": "bold",
                                    "size": "md",
                                    "align": "center",
                                    "contents": []
                                  },
                                  {
                                    "type": "text",
                                    "text": "เลือกรายการที่ต้องการแก้ไข",
                                    "weight": "bold",
                                    "size": "md",
                                    "align": "center",
                                    "contents": []
                                  },
                                  {
                                    "type": "separator",
                                    "margin": "lg"
                                  },
                                  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "lg",
                                    "position": "relative",
                                    "contents": [
                                      
                                      {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "ข้อมูลผู้จัดการเขต",
                                            "weight": "bold",
                                            "size": "sm",
                                            "align": "start",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          },
                                          {
                                            "type": "text",
                                            "text": "เลือก",
                                            "weight": "bold",
                                            "size": "md",
                                            "color": "#FA4204FF",
                                            "align": "end",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "action": {
                                              "type": "postback",
                                              "text": "ข้อความระบบ : เลือกผู้ใช้งานระดับ ผู้ช่วยผู้จัดการ",
                                              "data": "DETAILAREA"
                                            },
                                            "contents": []
                                          }
                                        ]
                                      },
                                      {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "เปลี่ยนผู้จัดการเขต",
                                            "weight": "bold",
                                            "size": "sm",
                                            "align": "start",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          },
                                          {
                                            "type": "text",
                                            "text": "เลือก",
                                            "weight": "bold",
                                            "size": "md",
                                            "color": "#FA4204FF",
                                            "align": "end",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "action": {
                                              "type": "postback",
                                              "text": "ข้อความระบบ : ระบบกำลังจัดส่งตัวเลือกการเปลี่ยนผู้จัดการเขต",
                                              "data": "CHANGEAREA"
                                            },
                                            "contents": []
                                          }
                                        ]
                                      },
                                      {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "ย้าย สาขา",
                                            "weight": "bold",
                                            "size": "sm",
                                            "align": "start",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          },
                                          {
                                            "type": "text",
                                            "text": "เลือก",
                                            "weight": "bold",
                                            "size": "md",
                                            "color": "#FA4204FF",
                                            "align": "end",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "action": {
                                              "type": "postback",
                                              "text": "ข้อความระบบ : ระบบกำลังจัดส่งตัวเลือกการเปลี่ยนสาขา",
                                              "data": "STATION-CHAANGE"
                                            },
                                            "contents": []
                                          }
                                        ]
                                      },
                                      {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "เพิ่มสาขาดูแล",
                                            "weight": "bold",
                                            "size": "sm",
                                            "align": "start",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          },
                                          {
                                            "type": "text",
                                            "text": "เลือก",
                                            "weight": "bold",
                                            "size": "md",
                                            "color": "#FA4204FF",
                                            "align": "end",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "action": {
                                              "type": "postback",
                                              "text": "ข้อความระบบ : เลือกผู้ใช้งานระดับ ส่วนผู้ดูแลระบบ",
                                              "data": "UserType03"
                                            },
                                            "contents": []
                                          }
                                        ]
                                      }
                                    ]
                                  },
                                  {
                                    "type": "separator",
                                    "margin": "lg"
                                  }
                                ]
                              },
                              "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "แก้ไขการตั้งค่ารายงาน",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#AA1C1CFF",
                                    "align": "center",
                                    "gravity": "center",
                                    "wrap": True  ,
                                    "contents": []
                                  }
                                ]
                              }
                            }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def StationSettingReject(self):
      dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ส่วนสำหรับผู้จัดการสาขา",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "เป็นส่วนการตั้งค่าสำหรับผู้จัดการสาขา กรณี เช่น เปลี่ยนแปลงชื่อสาขา , เปลี่ยนแปลงผู้จัดการเขต",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "xl",
        "wrap": True  ,
        "contents": []
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def ChangeAreaList(self,current_area,all_area):
      data = {
              "type": "flex",
                        "altText": 'message',
                        "contents": {
            "type": "carousel",
            "contents": [
              
              
            ]
          }
                                      }
# สร้างข้อมูลผู้จัดการเขตแล้วนำไป appendใส่ใน contents
      for i in all_area :
        if i.id == current_area.user_area.id:
          select_area = 'ผู้จัดการเขตปัจจุบัน'
          color = '#E1E0F9FF'
          text = 'ท่านเลือกผู้จัดการคนเดิม คือ ' + i.user_display_name
          text_data = 'NONEED'
        else :
          select_area = 'เลือกผู้จัดการเขต'
          color = "#078025FF"
          text = "ข้อมูลระบบ : ท่านเลือกผู้จัดการเขต คุณ " + i.user_display_name
          text_data = "CHAMGE-NEW-AREAID" + str(i.id)
        
        area_data = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "รายละเอียดผู้จัดการเขต",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": i.user_display_name,
                      "weight": "bold",
                      "color": "#1142D0FF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "image",
                      "url": i.user_picture_url,
                      "margin": "md"
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#078025FF"
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 0,
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": select_area,
                        "text": text ,
                        "data": text_data
                      },
                      "color": color,
                      "margin": "none",
                      "height": "sm",
                      "style": "secondary"
                    },
                    {
                      "type": "spacer",
                      "size": "sm"
                    }
                  ]
                }
              }
        data['contents']['contents'].append(area_data)

      return data
      pass
    def SettingAreaShowMenu(self,user_profile):
      
      centent = {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "margin": "none",
                    "align": "start",
                    "gravity": "center",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "SUSCO",
                      "uri": "https://www.susco.co.th/index.asp"
                    }
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "เลือกรายการที่ต้องการ",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "position": "relative",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                              {
                                "type": "text",
                                "text": "แสดงรายชื่อสาขาดูแล",
                                "weight": "bold",
                                "size": "sm",
                                "flex": 3,
                                "align": "start",
                                "gravity": "center",
                                "margin": "sm",
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "เลือก",
                                "weight": "bold",
                                "size": "md",
                                "color": "#FA4204FF",
                                "align": "end",
                                "gravity": "center",
                                "margin": "sm",
                                "action": {
                                  "type": "postback",
                                  "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกสาขาในเขตที่ดูแล",
                                  "data": "DISPLAY-STATION-AREA-ID{}".format(str(user_profile.userList_area_name.id))
                                },
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                              {
                                "type": "text",
                                "text": "ย้ายเขตดูแล",
                                "weight": "bold",
                                "size": "sm",
                                "align": "start",
                                "gravity": "center",
                                "margin": "sm",
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "เลือก",
                                "weight": "bold",
                                "size": "md",
                                "color": "#FA4204FF",
                                "align": "end",
                                "gravity": "center",
                                "margin": "sm",
                                "action": {
                                  "type": "postback",
                                  "text": "ข้อความระบบ : เลือกผู้ใช้งานระดับ ผู้ช่วยผู้จัดการ",
                                  "data": "DISPLAY-STATION-CHANGE-ID{}".format(str(user_profile.userList_area_name.id))
                                },
                                "contents": []
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "แก้ไขการตั้งค่ารายงาน",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#AA1C1CFF",
                        "align": "center",
                        "gravity": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
                  }
                }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def SettingStationShowMenu(self,current_position):
      centent = {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "margin": "none",
                    "align": "start",
                    "gravity": "center",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "SUSCO",
                      "uri": "https://www.susco.co.th/index.asp"
                    }
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "เลือกรายการที่ต้องการ",
                        "weight": "bold",
                        "size": "md",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "position": "relative",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                              {
                                "type": "text",
                                "text": "แสดงรายชื่อสาขาดูแล",
                                "weight": "bold",
                                "size": "sm",
                                "flex": 3,
                                "align": "start",
                                "gravity": "center",
                                "margin": "sm",
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "เลือก",
                                "weight": "bold",
                                "size": "md",
                                "color": "#FA4204FF",
                                "align": "end",
                                "gravity": "center",
                                "margin": "sm",
                                "action": {
                                  "type": "postback",
                                  "text": "ข้อความระบบ : กำลังจัดส่งรายชื่อสาขาที่ดูแล",
                                  "data": "DISPLAY-STATION-BRANCH-ID" + str(current_position.id)
                                },
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                              {
                                "type": "text",
                                "text": "เพิ่ม สาขาดูแล",
                                "weight": "bold",
                                "size": "sm",
                                "align": "start",
                                "gravity": "center",
                                "margin": "sm",
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "เลือก",
                                "weight": "bold",
                                "size": "md",
                                "color": "#FA4204FF",
                                "align": "end",
                                "gravity": "center",
                                "margin": "sm",
                                "action": {
                                  "type": "postback",
                                  "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกในการเพิ่มสาขาดูแล",
                                  "data": "STATION-REGISTER-PROCESS-ADDSTATION"
                                },
                                "contents": []
                              }
                            ]
                          }
                          
                        ]
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "แก้ไขการตั้งค่ารายงาน",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#AA1C1CFF",
                        "align": "center",
                        "gravity": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
                  }
                }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def SelectAreaList(self,area_list):
      centent = {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "เลือกรายชื่อผู้จัดการเขต",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          },
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ลงทะเบียนผู้จัดการเขต",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True,
                            "contents": []
                          }
                        ]
                      }
                    }
      for area in area_list :
        loop_area_list = {
                              "type": "box",
                              "layout": "horizontal",
                              "margin": "lg",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": 'คุณ '+ area.area_code_name,
                                  "weight": "bold",
                                  "size": "xs",
                                  "flex": 5,
                                  "align": "start",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "contents": []
                                },
                                {
                                  "type": "text",
                                  "text": "เลือก",
                                  "weight": "bold",
                                  "size": "sm",
                                  "color": "#FA4204FF",
                                  "align": "end",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "action": {
                                    "type": "postback",
                                    "text": "ข้อความระบบ : กำลังทำการลงทะเบียนระดับผู้จัดการ",
                                    "data": "AREA-REGISTER-PROCESS-ENSURE"+ str(area.id)
                                  },
                                  "contents": []
                                }
                              ]
                            }
        centent["body"]["contents"].append(loop_area_list)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
      pass
    def Reply_approve_main_area_manager(self,profile):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "รายการขออนุมัติ",
                      "weight": "bold",
                      "size": "xl",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ผู้จัดการภาค",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    
                    {
                      "type": "text",
                      "text": "วันที่ขออนุมัติ " + dt,
                      "weight": "bold",
                      "size": "xs",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "รายละเอียดผู้ขออนุมัติ",
                      "weight": "bold",
                      "size": "md",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "image",
                      "url": profile.picture_url,
                      "size": "4xl"
                    },
                    {
                      "type": "text",
                      "text": profile.display_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "สถานะ : รอการอนุมัติ",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ผู้อนุมัติ : Admin " ,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    }
                  ]
                }
              }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def Reply_approve_new_station_manager(self,profile,area_in_this_site):
      # ค้นหาผู้จัดการเขต 
      area_name = AreaCodeType.objects.filter(area_code_type=area_in_this_site.station_area_code.id).first()
      print 
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "รายการขออนุมัติ",
                      "weight": "bold",
                      "size": "xl",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ผู้จัดการสถานี",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": area_in_this_site.station_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "วันที่ขออนุมัติ " + dt,
                      "weight": "bold",
                      "size": "xs",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "รายละเอียดผู้ขออนุมัติ",
                      "weight": "bold",
                      "size": "md",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "image",
                      "url": profile.picture_url,
                      "size": "4xl"
                    },
                    {
                      "type": "text",
                      "text": profile.display_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "สถานะ : รอการอนุมัติ",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ผู้อนุมัติ : คุณ " + area_name.area_code_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    }
                  ]
                }
              }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
      pass
    def Reply_approve_add_more_station_manager(self,profile,area_in_this_site,area_name_AreaCodeType):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "รายการขออนุมัติ",
                      "weight": "bold",
                      "size": "xl",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ดูแลสาขาเพิ่ม",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": area_in_this_site.station_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "วันที่ขออนุมัติ " + dt,
                      "weight": "bold",
                      "size": "xs",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "รายละเอียดผู้ขออนุมัติ",
                      "weight": "bold",
                      "size": "md",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "image",
                      "url": profile.picture_url,
                      "size": "4xl"
                    },
                    {
                      "type": "text",
                      "text": profile.display_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "สถานะ : รอการอนุมัติ",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ผู้อนุมัติ : คุณ " + area_name_AreaCodeType.area_code_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 0,
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "ขออนุมัติใหม่",
                        "text": "ข้อความระบบ : รอสักครู่ กำลังส่งขออนุมัติใหม่อีกครั้ง",
                        "data": "STATION-REGISTER-PROCESS-NEWSITE{}".format(str(area_in_this_site.station_site))
                      },
                      "color": "#078025FF",
                      "margin": "none",
                      "height": "sm",
                      "style": "secondary"
                    },
                    
                    {
                      "type": "spacer",
                      "size": "sm"
                    }
                  ]
                }
                            }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
      pass
    def Area_Un_approve_add_more_station_manager(self,profile,area_in_this_site,area_name_AreaCodeType):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://www.susco.co.th/images/logo_susco.png",
                  "align": "center",
                  "gravity": "bottom",
                  "size": "full",
                  "aspectRatio": "22:6",
                  "aspectMode": "fit",
                  "backgroundColor": "#F2EC3EFF",
                  "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                  },
                  "position": "relative"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "รายการไม่อนุมัติ",
                      "weight": "bold",
                      "size": "xl",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ดูแลสาขาเพิ่ม",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": area_in_this_site.station_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "วันที่ขออนุมัติ " + dt,
                      "weight": "bold",
                      "size": "xs",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "รายละเอียดผู้ขออนุมัติ",
                      "weight": "bold",
                      "size": "md",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "wrap": True,
                      "contents": []
                    },
                    {
                      "type": "image",
                      "url": profile.picture_url,
                      "size": "4xl"
                    },
                    {
                      "type": "text",
                      "text": profile.display_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "separator",
                      "margin": "lg",
                      "color": "#E42424FF"
                    },
                    {
                      "type": "text",
                      "text": "สถานะ : ไม่อนุมัติ",
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "ผู้อนุมัติ : คุณ " + area_name_AreaCodeType.area_code_name,
                      "weight": "bold",
                      "color": "#293CCDFF",
                      "align": "center",
                      "margin": "lg",
                      "contents": []
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 0,
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "ขออนุมัติใหม่",
                        "text": "ข้อความระบบ : รอสักครู่ กำลังส่งขออนุมัติใหม่อีกครั้ง",
                        "data": "STATION-REGISTER-PROCESS-NEWSITE{}".format(str(area_in_this_site.station_site))
                      },
                      "color": "#078025FF",
                      "margin": "none",
                      "height": "sm",
                      "style": "secondary"
                    },
                    
                    {
                      "type": "spacer",
                      "size": "sm"
                    }
                  ]
                }
                            }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def Reply_inapprove_new_area_manager(self,profile,area_detail):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://www.susco.co.th/images/logo_susco.png",
                      "align": "center",
                      "gravity": "bottom",
                      "size": "full",
                      "aspectRatio": "22:6",
                      "aspectMode": "fit",
                      "backgroundColor": "#F2EC3EFF",
                      "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                      },
                      "position": "relative"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "รายการขออนุมัติ",
                          "weight": "bold",
                          "size": "xl",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้จัดการเขต",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "คุณ " + area_detail.area_code_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "วันที่ขออนุมัติ " + dt,
                          "weight": "bold",
                          "size": "xs",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "รายละเอียดผู้ขออนุมัติ",
                          "weight": "bold",
                          "size": "md",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "image",
                          "url": profile.picture_url,
                          "size": "4xl"
                        },
                        {
                          "type": "text",
                          "text": profile.display_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "สถานะ : รอการอนุมัติ",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้อนุมัติ : Admin",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        }
                      ]
                    }
                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
      
    def AreaManagerSendBackDetailToEnsure(self,area_ID):
      area_detail = AreaCodeType.objects.filter(id=area_ID).first()
      centent = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "ยืนยัน ชื่อผู้จัดการเขต",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True  ,
        "contents": []
      },
      {
        "type": "text",
        "text": area_detail.area_code_name,
        "weight": "bold",
        "color": "#D01111FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ยืนยัน",
          "text": "รอสักครู่ กำลังทำการลงทะเบียน",
          "data": 'AREA-REGISTER-PROCESS-CONFIRMNAME' + area_ID
        },
        "color": "#078025FF",
        "margin": "none",
        "height": "sm",
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ไม่ใช่",
          "text": "กรุณาเลือกรายการใหม่",
          "data": "AREA-REGISTER-PROCESS-RESENT"
        },
        "color": "#706C6CFF",
        "height": "sm",
        "style": "primary"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def NotifyAreaManagerForGetApproveNewManager(self,profile,area_in_this_site,manager_table_id):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      responds = "STATION-REGISTER-PROCESS-APPROVED-USERID{}STATIONID{}END".format(manager_table_id,area_in_this_site.id)
      reject_user =  "STATION-REGISTER-PROCESS-REJECT-USERID{}STATIONID{}END".format(manager_table_id,area_in_this_site.id)
      centent = {
                  "type": "bubble",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "Line",
                      "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      },
                      {
                        "type": "text",
                        "text": "รายการขออนุมัติ",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการสาขา",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": area_in_this_site.station_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "วันที่ขออนุมัติ " + dt,
                        "weight": "bold",
                        "size": "xs",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "รายละเอียดผู้ขออนุมัติ",
                        "weight": "bold",
                        "size": "md",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "image",
                        "url": profile.picture_url,
                        "size": "4xl"
                      },
                      {
                        "type": "text",
                        "text": profile.display_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "อนุมัติ",
                          "text": "ข้อความระบบ : กำลังทำรายการอนุมัติ",
                          "data": responds
                        },
                        "color": "#078025FF",
                        "margin": "none",
                        "height": "sm",
                        "style": "secondary"
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "ไม่อนุมัติ",
                          "text": "ข้อความระบบ : กำลังทำรายการไม่อนุมัติ",
                          "data": reject_user
                        },
                        "color": "#706C6CFF",
                        "height": "sm",
                        "style": "primary"
                      },
                      {
                        "type": "spacer",
                        "size": "sm"
                      }
                    ]
                  }
                }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data 
    def NotifyAreaManagerForGetApproveMultiManager(self,profile,area_in_this_site,manager_table_id):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      responds = "STATION-REGISTER-PROCESS-OKMORESITE-USERID{}STATIONID{}END".format(manager_table_id,area_in_this_site.id)
      reject_user =  "STATION-REGISTER-PROCESS-FAILEDMORESITE-USERID{}STATIONID{}END".format(manager_table_id,area_in_this_site.id)
      centent = {
                  "type": "bubble",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "Line",
                      "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      },
                      {
                        "type": "text",
                        "text": "รายการขออนุมัติ",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ดูแลสาขาเพิ่ม",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": area_in_this_site.station_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "วันที่ขออนุมัติ " + dt,
                        "weight": "bold",
                        "size": "xs",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "รายละเอียดผู้ขออนุมัติ",
                        "weight": "bold",
                        "size": "md",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "image",
                        "url": profile.picture_url,
                        "size": "4xl"
                      },
                      {
                        "type": "text",
                        "text": profile.display_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "อนุมัติ",
                          "text": "ข้อความระบบ : กำลังทำรายการอนุมัติ",
                          "data": responds
                        },
                        "color": "#078025FF",
                        "margin": "none",
                        "height": "sm",
                        "style": "secondary"
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "ไม่อนุมัติ",
                          "text": "ข้อความระบบ : กำลังทำรายการไม่อนุมัติ",
                          "data": reject_user
                        },
                        "color": "#706C6CFF",
                        "height": "sm",
                        "style": "primary"
                      },
                      {
                        "type": "spacer",
                        "size": "sm"
                      }
                    ]
                  }
                }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data 
    def AreaApproveNewStationManager(self,area_in_this_site,manager_user_id,area_name_approved):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                          "type": "bubble",
                          "hero": {
                            "type": "image",
                            "url": "https://www.susco.co.th/images/logo_susco.png",
                            "align": "center",
                            "gravity": "bottom",
                            "size": "full",
                            "aspectRatio": "22:6",
                            "aspectMode": "fit",
                            "backgroundColor": "#F2EC3EFF",
                            "action": {
                              "type": "uri",
                              "label": "Line",
                              "uri": "https://linecorp.com/"
                            },
                            "position": "relative"
                          },
                          "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "lg",
                                "color": "#E42424FF"
                              },
                              {
                                "type": "text",
                                "text": "รายการอนุมัติ",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#293CCDFF",
                                "align": "center",
                                "margin": "lg",
                                "wrap": True,
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "ผู้จัดการสถานี",
                                "weight": "bold",
                                "color": "#293CCDFF",
                                "align": "center",
                                "margin": "lg",
                                "wrap": True,
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": area_in_this_site.station_name,
                                "weight": "bold",
                                "color": "#293CCDFF",
                                "align": "center",
                                "margin": "lg",
                                "wrap": True,
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "วันที่อนุมัติ " + dt,
                                "weight": "bold",
                                "size": "xs",
                                "color": "#293CCDFF",
                                "align": "center",
                                "margin": "lg",
                                "wrap": True,
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "รายละเอียดผู้ขออนุมัติ",
                                "weight": "bold",
                                "size": "md",
                                "color": "#293CCDFF",
                                "align": "center",
                                "margin": "lg",
                                "wrap": True,
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": manager_user_id.userList_display_name,
                                "weight": "bold",
                                "color": "#293CCDFF",
                                "align": "center",
                                "margin": "lg",
                                "contents": []
                              },
                              {
                                "type": "separator",
                                "margin": "lg",
                                "color": "#E42424FF"
                              },
                              {
                                "type": "text",
                                "text": "สถานะ : อนุมัติแล้ว",
                                "weight": "bold",
                                "color": "#293CCDFF",
                                "align": "center",
                                "margin": "lg",
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "ผู้อนุมัติ : " + area_name_approved.area_code_name,
                                "weight": "bold",
                                "color": "#293CCDFF",
                                "align": "center",
                                "margin": "lg",
                                "contents": []
                              }
                            ]
                          }
                        }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def AreaSendToAdminApprove(self,area_detail,user_line_profile):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      message_approve = 'AREA-REGISTER-PROCESS-APPROVED-ID{}END'.format(user_line_profile.id)
      message_reject = 'AREA-REGISTER-PROCESS-REJECT-ID{}END'.format(user_line_profile.id)
      centent = {
                  "type": "bubble",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "Line",
                      "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      },
                      {
                        "type": "text",
                        "text": "รายการขออนุมัติ",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการเขต",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "คุณ " + area_detail.area_code_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "วันที่ขออนุมัติ " + dt,
                        "weight": "bold",
                        "size": "xs",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "รายละเอียดผู้ขออนุมัติ",
                        "weight": "bold",
                        "size": "md",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "image",
                        "url": user_line_profile.userList_picture_url,
                        "size": "4xl"
                      },
                      {
                        "type": "text",
                        "text": user_line_profile.userList_display_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "อนุมัติ",
                          "text": "ข้อความระบบ : กำลังทำรายการอนุมัติ",
                          "data": message_approve
                        },
                        "color": "#078025FF",
                        "margin": "none",
                        "height": "sm",
                        "style": "secondary"
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "ไม่อนุมัติ",
                          "text": "ข้อความระบบ : กำลังทำรายการไม่อนุมัติ",
                          "data": message_reject
                        },
                        "color": "#706C6CFF",
                        "height": "sm",
                        "style": "primary"
                      },
                      {
                        "type": "spacer",
                        "size": "sm"
                      }
                    ]
                  }
                }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def MainAreaSendToAdminApprove(self,user_line_profile):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      message_approve = 'MAIN-AREA-REGISTER-PROCESS-APPROVED-ID{}END'.format(user_line_profile.id)
      message_reject = 'MAIN-AREA-REGISTER-PROCESS-REJECT-ID{}END'.format(user_line_profile.id)
      centent = {
                  "type": "bubble",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "Line",
                      "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      },
                      {
                        "type": "text",
                        "text": "รายการขออนุมัติ",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการภาค",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      
                      {
                        "type": "text",
                        "text": "วันที่ขออนุมัติ " + dt,
                        "weight": "bold",
                        "size": "xs",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "รายละเอียดผู้ขออนุมัติ",
                        "weight": "bold",
                        "size": "md",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "image",
                        "url": user_line_profile.userList_picture_url,
                        "size": "4xl"
                      },
                      {
                        "type": "text",
                        "text": user_line_profile.userList_display_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "อนุมัติ",
                          "text": "ข้อความระบบ : กำลังทำรายการอนุมัติ",
                          "data": message_approve
                        },
                        "color": "#078025FF",
                        "margin": "none",
                        "height": "sm",
                        "style": "secondary"
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "ไม่อนุมัติ",
                          "text": "ข้อความระบบ : กำลังทำรายการไม่อนุมัติ",
                          "data": message_reject
                        },
                        "color": "#706C6CFF",
                        "height": "sm",
                        "style": "primary"
                      },
                      {
                        "type": "spacer",
                        "size": "sm"
                      }
                    ]
                  }
                }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def AdminApprovedNewAreaManager(self,manager_user_id2):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                  "type": "bubble",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "Line",
                      "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      },
                      {
                        "type": "text",
                        "text": "รายการอนุมัติ",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการเขต {}".format(manager_user_id2.userList_area_name.code_in_area_code_name),
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      
                      {
                        "type": "text",
                        "text": "วันที่อนุมัติ " + dt,
                        "weight": "bold",
                        "size": "xs",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "รายละเอียดผู้ขออนุมัติ",
                        "weight": "bold",
                        "size": "md",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": manager_user_id2.userList_display_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },
                      
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      },
                      {
                        "type": "text",
                        "text": "สถานะ : อนุมัติแล้ว",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้อนุมัติ : Admin",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      }
                    ]
                  }
                }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def AdminApprovedNewMainAreaManager(self,manager_user_id2):
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                  "type": "bubble",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "Line",
                      "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      },
                      {
                        "type": "text",
                        "text": "รายการอนุมัติ",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้จัดการภาค",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      
                      {
                        "type": "text",
                        "text": "วันที่อนุมัติ " + dt,
                        "weight": "bold",
                        "size": "xs",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "รายละเอียดผู้ขออนุมัติ",
                        "weight": "bold",
                        "size": "md",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "wrap": True,
                        "contents": []
                      },
                      
                      {
                        "type": "text",
                        "text": "LineName : " + manager_user_id2.userList_display_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#E42424FF"
                      },
                      {
                        "type": "text",
                        "text": "สถานะ : อนุมัติแล้ว",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "ผู้อนุมัติ : Admin",
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      }
                    ]
                  }
                }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data  
    def AdminRejectedNewAreaManager(self,manager_user_id2):
      # นำ ID  manager_user_id2.userList_area_name ที่ได้มาไปค้นหาต่อที่ AreaCodeType
      re_approve_manager_id = AreaCodeType.objects.get(area_code_type_id=manager_user_id2.userList_area_name)

      command_re_approved = 'AREA-REGISTER-PROCESS-CONFIRMNAME{}'.format(re_approve_manager_id.id) 
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://www.susco.co.th/images/logo_susco.png",
                      "align": "center",
                      "gravity": "bottom",
                      "size": "full",
                      "aspectRatio": "22:6",
                      "aspectMode": "fit",
                      "backgroundColor": "#F2EC3EFF",
                      "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                      },
                      "position": "relative"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "รายการไม่อนุมัติ",
                          "weight": "bold",
                          "size": "xl",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้จัดการเขต",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        
                        {
                          "type": "text",
                          "text": "วันที่อนุมัติ " + dt,
                          "weight": "bold",
                          "size": "xs",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "รายละเอียดผู้ขออนุมัติ",
                          "weight": "bold",
                          "size": "md",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "สาขา "+manager_user_id2.userList_area_name.code_in_area_code_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                        "type": "text",
                        "text": "LineName : " + manager_user_id2.userList_display_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },

                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "สถานะ : ไม่อนุมัติ",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้อนุมัติ : Admin",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 0,
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "ขออนุมัติใหม่",
                            "text": "ข้อความระบบ : กำลังทำรายการขออนุมัติใหม่",
                            "data": command_re_approved
                          },
                          "color": "#078025FF",
                          "margin": "none",
                          "height": "sm",
                          "style": "secondary"
                        },
                        {
                          "type": "spacer",
                          "size": "sm"
                        }
                      ]
                    }
                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def AdminRejectedNewMainAreaManager(self,manager_user_id2):
      command_re_approved = 'MAIN-AREA-REGISTER-PROCESS-CONFIRMPOSITION{}'.format(manager_user_id2.id) 
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://www.susco.co.th/images/logo_susco.png",
                      "align": "center",
                      "gravity": "bottom",
                      "size": "full",
                      "aspectRatio": "22:6",
                      "aspectMode": "fit",
                      "backgroundColor": "#F2EC3EFF",
                      "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                      },
                      "position": "relative"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "รายการไม่อนุมัติ",
                          "weight": "bold",
                          "size": "xl",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้จัดการภาค",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        
                        {
                          "type": "text",
                          "text": "วันที่อนุมัติ " + dt,
                          "weight": "bold",
                          "size": "xs",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "รายละเอียดผู้ขออนุมัติ",
                          "weight": "bold",
                          "size": "md",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": manager_user_id2.userList_display_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        

                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "สถานะ : ไม่อนุมัติ",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้อนุมัติ : Admin",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 0,
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "ขออนุมัติใหม่",
                            "text": "ข้อความระบบ : กำลังทำรายการขออนุมัติใหม่",
                            "data": command_re_approved
                          },
                          "color": "#078025FF",
                          "margin": "none",
                          "height": "sm",
                          "style": "secondary"
                        },
                        {
                          "type": "spacer",
                          "size": "sm"
                        }
                      ]
                    }
                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def AreaRejectedStationManager(self,manager_user_id2,station_profile):
      command_re_approved = 'STATION-REGISTER-PROCESS-CONFIRM-STATION-ID{}'.format(station_profile.station_site) 
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://www.susco.co.th/images/logo_susco.png",
                      "align": "center",
                      "gravity": "bottom",
                      "size": "full",
                      "aspectRatio": "22:6",
                      "aspectMode": "fit",
                      "backgroundColor": "#F2EC3EFF",
                      "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                      },
                      "position": "relative"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "รายการไม่อนุมัติ",
                          "weight": "bold",
                          "size": "xl",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้จัดการสาขา",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "สาขา : " + station_profile.station_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        
                        {
                          "type": "text",
                          "text": "วันที่อนุมัติ " + dt,
                          "weight": "bold",
                          "size": "xs",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "รายละเอียดผู้ขออนุมัติ",
                          "weight": "bold",
                          "size": "md",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": manager_user_id2.userList_display_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        

                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "สถานะ : ไม่อนุมัติ",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้อนุมัติ : Admin",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 0,
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "ขออนุมัติใหม่",
                            "text": "ข้อความระบบ : กำลังทำรายการขออนุมัติใหม่",
                            "data": command_re_approved
                          },
                          "color": "#078025FF",
                          "margin": "none",
                          "height": "sm",
                          "style": "secondary"
                        },
                        {
                          "type": "spacer",
                          "size": "sm"
                        }
                      ]
                    }
                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def AreaRejectedAddMoreStationManager(self,manager_user_id2,station_profile):
      command_re_approved = 'STATION-REGISTER-PROCESS-CONFIRM-STATION-ID{}'.format(station_profile.station_site) 
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      centent = {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://www.susco.co.th/images/logo_susco.png",
                      "align": "center",
                      "gravity": "bottom",
                      "size": "full",
                      "aspectRatio": "22:6",
                      "aspectMode": "fit",
                      "backgroundColor": "#F2EC3EFF",
                      "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                      },
                      "position": "relative"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "รายการไม่อนุมัติ",
                          "weight": "bold",
                          "size": "xl",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้จัดการสาขา",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "สาขา : " + station_profile.station_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        
                        {
                          "type": "text",
                          "text": "วันที่อนุมัติ " + dt,
                          "weight": "bold",
                          "size": "xs",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "รายละเอียดผู้ขออนุมัติ",
                          "weight": "bold",
                          "size": "md",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": manager_user_id2.userList_display_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        

                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "สถานะ : ไม่อนุมัติ",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "ผู้อนุมัติ : Admin",
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 0,
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                            "type": "postback",
                            "label": "ขออนุมัติใหม่",
                            "text": "ข้อความระบบ : กำลังทำรายการขออนุมัติใหม่",
                            "data": command_re_approved
                          },
                          "color": "#078025FF",
                          "margin": "none",
                          "height": "sm",
                          "style": "secondary"
                        },
                        {
                          "type": "spacer",
                          "size": "sm"
                        }
                      ]
                    }
                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def UnapprovedMember(self,manager_user_id2):
      command_un_approved = 'UNAPPROVED-MEMBER{}'.format(manager_user_id2.id) 
      dt = datetime.now().strftime("%d-%m-%y %H:%M")
      print ('สถานะผู้ถูกปฏิเสธ {}'.format(manager_user_id2.userList_position.id))
      user_position = manager_user_id2.userList_position.id
      if user_position == 3:
        name_of_user = manager_user_id2.userList_area_name.code_in_area_code_name
      elif user_position == 4:
        name_of_user = manager_user_id2.userList_display_name
      elif user_position == 1:
        name_of_user = manager_user_id2.userList_display_name

      centent = {
                    "type": "bubble",
                    "hero": {
                      "type": "image",
                      "url": "https://www.susco.co.th/images/logo_susco.png",
                      "align": "center",
                      "gravity": "bottom",
                      "size": "full",
                      "aspectRatio": "22:6",
                      "aspectMode": "fit",
                      "backgroundColor": "#F2EC3EFF",
                      "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                      },
                      "position": "relative"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        },
                        {
                          "type": "text",
                          "text": "สถานะผู้ใช้งาน",
                          "weight": "bold",
                          "size": "xl",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": manager_user_id2.userList_position.position_name,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        
                        {
                          "type": "text",
                          "text": "วันที่ได้รับอนุมัติ " + manager_user_id2.userList_approved_datetime.strftime("%d-%m-%y %H:%M"),
                          "weight": "bold",
                          "size": "xs",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "รายละเอียดผู้ได้รับอนุมัติ",
                          "weight": "bold",
                          "size": "md",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "wrap": True,
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": name_of_user,
                          "weight": "bold",
                          "color": "#293CCDFF",
                          "align": "center",
                          "margin": "lg",
                          "contents": []
                        },
                        {
                        "type": "text",
                        "text": "LineName : " + manager_user_id2.userList_display_name,
                        "weight": "bold",
                        "color": "#293CCDFF",
                        "align": "center",
                        "margin": "lg",
                        "contents": []
                      },

                        {
                          "type": "separator",
                          "margin": "lg",
                          "color": "#E42424FF"
                        }
                      ]
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 0,
                      "spacing": "sm",
                      "contents": [
                       {
                            "type": "button",
                            "action": {
                              "type": "postback",
                              "label": "ยกเลิกการอนุมัติ",
                              "text": "ข้อความระบบ : กำลังทำรายการยกเลิกการอนุมัติ",
                              "data": command_un_approved
                            },
                            "color": "#BC2C29FF",
                            "margin": "none",
                            "height": "sm",
                            "style": "secondary"
                          },
                          {
                            "type": "button",
                            "action": {
                              "type": "postback",
                              "label": "ยกเลิกไม่ทำรายการไดๆ",
                              "text": "ข้อความระบบ : ยกเลิกการทำรายการ",
                              "data": "OK"
                            },
                            "color": "#078025FF",
                            "margin": "xl",
                            "height": "sm",
                            "style": "secondary"
                          },
                          {
                            "type": "spacer",
                            "size": "sm"
                          }
                      ]
                    }
                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data
    def StationDetail(self,main_station_list,main_station,multi_station,area_name):
      count_station = len(main_station_list)+len(multi_station)
      print ('จำนวนสาขาที่ดูแล คือ {}'.format(count_station))
      
      centent = {
                        "type": "bubble",
                        "direction": "ltr",
                        "hero": {
                          "type": "image",
                          "url": "https://www.susco.co.th/images/logo_susco.png",
                          "margin": "none",
                          "align": "start",
                          "gravity": "center",
                          "size": "full",
                          "aspectRatio": "22:6",
                          "aspectMode": "fit",
                          "backgroundColor": "#F2EC3EFF",
                          "action": {
                            "type": "uri",
                            "label": "SUSCO",
                            "uri": "https://www.susco.co.th/index.asp"
                          }
                        },
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "คุณ {}".format(main_station.userList_display_name),
                              "weight": "bold",
                              "size": "md",
                              "align": "center",
                              "contents": []
                            },
                            {
                              "type": "text",
                              "text": "จำนวนสาขาที่ดูแล {} สาขา".format(str(count_station)),
                              "weight": "bold",
                              "size": "md",
                              "align": "center",
                              "contents": []
                            },
                            {
                              "type": "separator",
                              "margin": "lg",
                              "color": "#210404FF"
                            },
                            
                            # Branch detail
                            
                          ]
                        },
                        "footer": {
                          "type": "box",
                          "layout": "vertical",
                          "flex": 0,
                          "spacing": "sm",
                          "contents": [
                            {
                              "type": "text",
                              "text": "แสดงรายชื่อสาขาที่ดูแล",
                              "weight": "bold",
                              "size": "lg",
                              "color": "#AA1C1CFF",
                              "align": "center",
                              "gravity": "center",
                              "wrap": True,
                              "contents": []
                            }
                          ]
                        }
                      }
      
      branch_1 = {
                              "type": "box",
                              "layout": "vertical",
                              "margin": "lg",
                              "position": "relative",
                              "contents": [
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "สาขาหลัก",
                                      "weight": "bold",
                                      "size": "md",
                                      "flex": 5,
                                      "align": "center",
                                      "gravity": "center",
                                      "margin": "sm",
                                      "contents": []
                                    }
                                  ]
                                },
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "margin": "sm",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "{}".format(main_station.userList_station_name.station_name),
                                      "weight": "bold",
                                      "size": "sm",
                                      "flex": 5,
                                      "align": "center",
                                      "gravity": "center",
                                      "margin": "sm",
                                      "contents": []
                                    }
                                  ]
                                },
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "margin": "md",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "ผู้จัดการเขต",
                                      "weight": "bold",
                                      "size": "md",
                                      "align": "center",
                                      "gravity": "center",
                                      "margin": "sm",
                                      "contents": []
                                    }
                                  ]
                                },
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "margin": "md",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "คุณ {}".format(area_name.area_code_name),
                                      "weight": "bold",
                                      "size": "md",
                                      "align": "center",
                                      "gravity": "center",
                                      "margin": "sm",
                                      "contents": []
                                    }
                                  ]
                                },
                                {
                                  "type": "separator",
                                  "margin": "lg",
                                  "color": "#210404FF"
                                }
                              ]
                            }
      centent['body']['contents'].append(branch_1)
      
      for i in multi_station :
        #ค้นหารายชื่อผู้จัดการเขต
        area_name = AreaCodeType.objects.filter(area_code_type=i.multi_station_number.station_area_code.id).first()
       
        branch_2 = {
                              "type": "box",
                              "layout": "vertical",
                              "margin": "lg",
                              "position": "relative",
                              "contents": [
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "สาขารอง",
                                      "weight": "bold",
                                      "size": "md",
                                      "flex": 5,
                                      "align": "center",
                                      "gravity": "center",
                                      "margin": "sm",
                                      "contents": []
                                    }
                                  ]
                                },
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "margin": "sm",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "{}".format(i.multi_station_number.station_name),
                                      "weight": "bold",
                                      "size": "sm",
                                      "flex": 5,
                                      "align": "center",
                                      "gravity": "center",
                                      "margin": "sm",
                                      "contents": []
                                    }
                                  ]
                                },
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "margin": "md",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "ผู้จัดการเขต",
                                      "weight": "bold",
                                      "size": "md",
                                      "align": "center",
                                      "gravity": "center",
                                      "margin": "sm",
                                      "contents": []
                                    }
                                  ]
                                },
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "margin": "md",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "คุณ {}".format(area_name.area_code_name),
                                      "weight": "bold",
                                      "size": "md",
                                      "align": "center",
                                      "gravity": "center",
                                      "margin": "sm",
                                      "contents": []
                                    }
                                  ]
                                },
                                {
                                  "type": "button",
                                  "action": {
                                    "type": "postback",
                                    "label": "ยกเลิกดูแลสาขา",
                                    "text": "ข้อความระบบ : กำลังทำการยกเลิกสาขา {}".format(i.multi_station_number.station_name),
                                    "data": "STATION-REGISTER-PROCESS-REMOVE-ID{}BRANCH{}END".format(i.multi_manager_number.id,i.multi_station_number.id)
                                  },
                                  "color": "#DAEE86FF",
                                  "margin": "lg",
                                  "height": "md",
                                  "style": "secondary",
                                  "position": "relative"
                                },
                                {
                                  "type": "separator",
                                  "margin": "lg",
                                  "color": "#210404FF"
                                }
                              ]
                            }
        centent['body']['contents'].append(branch_2)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      return data

class PosReport :
  def __init__(self,payload):
        print ('ส่วนติดต่อฐานข้อมูล POS')
        # ค้นผู้เข้ามาใช้งานว่าคือใคร ผจก เขต ภาค
        self.payload = payload
        line_token = LineSetting.objects.all().first()
        line_bot_api = LineBotApi(line_token.line_token)
        self.line_user_id = payload['events'][0]['source']['userId']
        self.line_token = LineSetting.objects.all().first()
        self.line_bot_api = LineBotApi(line_token.line_token)
        self.reply_token = payload['events'][0]['replyToken']

  def StationSelectOption(self,user_profile,last_close_shift_id,report_type,evrIdent):
    print ('ข้อมูลที่ได้รับมา {}'.format(last_close_shift_id))
    try :
      today = datetime.now().strftime("%Y-%m-%d")
      new_date = (datetime.now() - relativedelta(days=60)).strftime("%Y-%m-%d")
      # if position == 1 :
      #   print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการสาขสาขา')
      #   station_name = user_profile.userList_station_name.station_name
      #   post_back_last_shift = 'VIEW-X-REPORT-SITE-NOW-SITE_ID{}LASTID{}END'.format(user_profile.userList_station_name.station_site,last_close_shift_id)
      #   post_back_businessdate = 'VIEW-X-REPORT-SITE-DAY-SITE_ID{}END'.format(user_profile.userList_station_name.station_site)
      # elif position == 3 :
      #   print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการเขต')
      station_name = user_profile.station_name
      if report_type == 'X-REPORT' :
        post_back_last_shift = 'VIEW-X-REPORT-SITE-NOW-SITE_ID{}LASTID{}END'.format(user_profile.station_site,last_close_shift_id)
        post_back_businessdate = 'VIEW-X-REPORT-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
        report_buttom = report_type
        command_save = post_back_last_shift
      elif report_type == 'METER' :
        post_back_last_shift = 'VIEW-METER-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(user_profile.station_site,evrIdent['EvrNum'])
        post_back_businessdate = 'VIEW-METER-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
        report_buttom = report_type
        command_save = post_back_last_shift
        # station_name = user_profile.station_name
        # post_back_last_shift = 'VIEW-METER-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(user_profile.station_site,evrIdent['EvrNum'])
        # post_back_businessdate = 'VIEW-METER-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
        pass

      centent = {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "margin": "none",
                    "align": "start",
                    "gravity": "center",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "SUSCO",
                      "uri": "https://www.susco.co.th/index.asp"
                    }
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": station_name,
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "เลือกวิธีการเรียกรายงาน",
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "contents": [
                          {
                            "type": "text",
                            "text": "กะ ล่าสุด",
                            "weight": "bold",
                            "size": "md",
                            "align": "start",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "เลือก",
                            "weight": "bold",
                            "size": "md",
                            "color": "#FA4204FF",
                            "align": "end",
                            "gravity": "center",
                            "margin": "sm",
                            "action": {
                              "type": "postback",
                              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล {} ปัจจุบัน".format(report_buttom),
                              "data": post_back_last_shift
                            },
                            "contents": []
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ระบุวันที่ปิดวัน",
                            "weight": "bold",
                            "size": "md",
                            "align": "start",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          },
                                        {
                            "type": "text",
                            "text": "เลือก",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#FA4204FF",
                            "align": "end",
                            "gravity": "center",
                            "margin": "sm",
                            "action": {
                              "type": "datetimepicker",
                              "data": post_back_businessdate,
                              "mode": "date",
                              "initial": today,
                              "max": today,
                              "min": new_date
                            },
                          # {
                          #   "type": "text",
                          #   "text": "เลือก",
                          #   "weight": "bold",
                          #   "size": "md",
                          #   "color": "#FA4204FF",
                          #   "align": "end",
                          #   "gravity": "center",
                          #   "margin": "sm",
                          #   "action": {
                          #     "type": "postback",
                          #     "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล X-Report ย้อนหลัง10 วัน",
                          #     "data": post_back_businessdate
                          #   },
                            "contents": []
                          }
                        ]
                      },
                      {
                        "type": "separator",
                        "margin": "lg"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": report_buttom,
                        "weight": "bold",
                        "size": "lg",
                        "color": "#AA1C1CFF",
                        "align": "center",
                        "gravity": "top",
                        "wrap": True  ,
                        "contents": []
                      }
                    ]
                  }
  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ ข้อมูลรายงาน สาขา {} '.format(command_save,user_profile.station_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,command_save)
      # return True , data
    except Exception as e:
      print ('ไม่สามารถสร้างรายงาน {} ได้ เนื่องจาก {}'.format(report_type,e))
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ  ชื่อสาขา {} ปัญหา {}'.format(report_type,user_profile.station_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
  def Xreport_Last_Shift(self,station_detail,result_pos,report_type):
# ทำการ loop เพื่อเอาข้อมูลจากรายงาน
    try : 
      dt = datetime.now().strftime("%d-%m-%Y %H:%M")
      for index,detail in enumerate(result_pos,) :
        # print ('index {} : Detail {}'.format(index,detail))
        if 'POS' in detail['Desc']: 
          POS_ID = detail['Desc']
        elif 'กะที่' in detail['Desc']:
          Shift_ID = detail['Desc']
        elif 'วันที่เริ่ม' in detail['Desc']:
          Shift_Start_Date = detail['Desc']
        elif 'วันที่สิ้นสุด' in detail['Desc']:
          Shift_End_Date = detail['Desc']
        elif '**ยอดขายน้ำมัน' in detail['Desc']:
          Oil_Sale = detail['Amt']
        elif '**ยอดขายสินค้า' in detail['Desc']:
          Product_Sale = detail['Amt']
        # elif '**ยอดขายสินค้า' not in detail['Desc']:
        #   Product_Sale = '0'
        elif 'ยอดขายทั้งหมด' in detail['Desc']:
          Total_Sale = detail['Amt']
        # elif 'ยอดขายทั้งหมด' not in detail['Desc']:
        #   Total_Sale = '0'
        elif 'ยอดขายสุทธิ' in detail['Desc']:
          Net_Sale = detail['Amt']
        elif 'ยอดรวม รวม VAT' in detail['Desc']:
          Total_Vat = detail['Amt']
        elif 'ยอดขายไม่รวมภาษีมูลค่าเพิ่ม' in detail['Desc']:
          Total_No_Vat = detail['Amt']
        elif 'ภาษีมูลค่าเพิ่ม' in detail['Desc']:
          Vat = detail['Amt']
        elif '  เงินสด' in detail['Desc']:
          Cash = "{:.2f}".format(float(detail['Num']))
          # Cash = str(detail['Num'])
          TotalCash = detail['Amt']
        elif 'ยอดรวม การเก็บเงิน (THB)' in detail['Desc']:
          Total_recived_Cash_number = "{:.2f}".format(float(detail['Num']))
          Total_recived_Cash = detail['Amt']
        elif 'ยอดเปิดกะ' in detail['Desc']:
          Open_Shift = detail['Amt']
        elif 'ยอดขายเงินสด' in detail['Desc']:
          Cash_Sale = detail['Amt']
        elif 'ยอดเงินในลิ้นชัก' in detail['Desc']:
          Cash_In_Drawer = detail['Amt']
        elif 'ยอดเงินปิดกะ' in detail['Desc']:
          Money_Close_Shift = detail['Amt']
        elif 'เกิน / ขาด' in detail['Desc']:
          Over_Short = detail['Amt']
        elif 'หมายเลขใบเสร็จเริ่มต้น' in detail['Desc']:
          Start_Receipt_Number = detail['Amt']
        elif 'หมายเลขใบเสร็จสิ้นสุด ' in detail['Desc']:
          End_Receipt_Number = detail['Amt']
        elif 'จำนวนรายการทั้งหมด' in detail['Desc']:
          Total_Receipt = detail['Amt']
        elif 'จำนวนรายการขาย' in detail['Desc']:
          Total_Sale_Receipt = detail['Amt']
        elif 'จำนวนรายการคืนสินค้า' in detail['Desc']:
          Total_Return_Receipt = detail['Amt']
        elif 'จำนวนรายการทดสอบน้ำมัน' in detail['Desc']:
          Total_Oil_Receipt = detail['Amt']
        elif index == 45 :
          Total_Money_SALE = detail['Desc']
        elif index == 47 :
          Total_Receipt_ALL = detail['Desc']

        

      centent = {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://www.susco.co.th/images/logo_susco.png",
          "margin": "none",
          "align": "start",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "22:6",
          "aspectMode": "fit",
          "backgroundColor": "#F2EC3EFF",
          "action": {
            "type": "uri",
            "label": "SUSCO",
            "uri": "https://www.susco.co.th/index.asp"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                
                {
                  "type": "text",
                  "text": "ยอดขายน้ำมันเครื่องรวม(dry stock) ",
                  "weight": "bold",
                  "align": "start",
                  "contents": []
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "สาขา " + str(station_detail.station_name),
                  "size": "xxs",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": POS_ID,
                  "size": "xxs",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": Shift_ID,
                  "size": "xxs",
                  "contents": []
                },
                {
                  "type": "separator",
                  "margin": "xs",
                  "color": "#4B5107D6"
                },
                {
                  "type": "text",
                  "text": Shift_Start_Date,
                  "size": "xxs",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": Shift_End_Date,
                  "size": "xxs",
                  "contents": []
                },
                {
                  "type": "separator",
                  "margin": "xs",
                  "color": "#4B5107D6"
                },
                {
                  "type": "text",
                  "text": "รายละเอียดการขาย (THB)",
                  "weight": "bold",
                  "size": "xs",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "** ยอดขายน้ำมัน",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Oil_Sale,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "** ยอดขายสินค้า",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": 'Product_Sale',
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "md",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดขายทั้งหมด",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_Sale,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดขายสุทธิ(THB)",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Net_Sale,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "separator",
                  "margin": "md",
                  "color": "#4B5107D6"
                },
                {
                  "type": "text",
                  "text": "ภาษีมูลค่าเพิ่ม (THB)",
                  "weight": "bold",
                  "size": "xs",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดรวม รวม VAT",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_Vat,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดขายไม่รวมภาษีมูลค่าเพิ่ม",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_No_Vat,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ภาษีมูลค่าเพิ่ม",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Vat,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "separator",
                  "margin": "md",
                  "color": "#4B5107D6"
                },
                {
                  "type": "text",
                  "text": "ประเภทการชำระเงิน (THB)",
                  "weight": "bold",
                  "size": "xs",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "เงินสด",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Cash,
                      "size": "xs",
                      "align": "center",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": TotalCash,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดรวม การเก็บเงิน",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_recived_Cash_number,
                      "size": "xs",
                      "align": "center",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_recived_Cash,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "separator",
                  "margin": "md",
                  "color": "#4B5107D6"
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "ณ เวลา {}".format(dt),
              "size": "xs",
              "align": "center",
              "gravity": "center",
              "wrap": True  ,
              "contents": []
            }
          ]
        }
      },
      {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://www.susco.co.th/images/logo_susco.png",
          "margin": "none",
          "align": "start",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "22:6",
          "aspectMode": "fit",
          "backgroundColor": "#F2EC3EFF",
          "action": {
            "type": "uri",
            "label": "SUSCO",
            "uri": "https://www.susco.co.th/index.asp"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "ยอดขายน้ำมันเครื่องรวม(dry stock) ",
                  "weight": "bold",
                  "align": "start",
                  "contents": []
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "สาขา " + str(station_detail.station_name),
                  "size": "xxs",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": POS_ID,
                  "size": "xxs",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": Shift_ID,
                  "size": "xxs",
                  "contents": []
                },
                {
                  "type": "separator",
                  "margin": "xs",
                  "color": "#4B5107D6"
                },
                {
                  "type": "text",
                  "text": Shift_Start_Date,
                  "size": "xxs",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": Shift_End_Date,
                  "size": "xxs",
                  "contents": []
                },
                {
                  "type": "separator",
                  "margin": "xs",
                  "color": "#4B5107D6"
                },
                {
                  "type": "text",
                  "text": "รายละเอียดเงินสด (THB)",
                  "weight": "bold",
                  "size": "xs",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดเปิดกะ",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Open_Shift,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดขายเงินสด",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Cash_Sale,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดเงินในลิ้นชัก",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Cash_In_Drawer,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดเงินปิดกะ",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Money_Close_Shift,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "เกิน / ขาด",
                      "size": "xs",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Over_Short,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "separator",
                  "margin": "md",
                  "color": "#4B5107D6"
                },
                {
                  "type": "text",
                  "text": "รายการที่ไม่ใช่เงินสด (THB)",
                  "weight": "bold",
                  "size": "xs",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Metrological Sample",
                      "size": "xs",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "คำนวณยอดได้",
                      "size": "xs",
                      "align": "center",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "0.00",
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Counted",
                      "size": "xs",
                      "align": "start",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "0.00",
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดที่คำนวณได้",
                      "size": "xs",
                      "align": "center",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "0.00",
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "separator",
                  "margin": "md",
                  "color": "#4B5107D6"
                },
                {
                  "type": "text",
                  "text": "รายละเอียดอื่นๆ (THB)",
                  "weight": "bold",
                  "size": "xs",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "หมายเลขใบเสร็จเริ่มต้น",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Start_Receipt_Number,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "หมายเลขใบเสร็จสิ้นสุด",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": End_Receipt_Number,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "จำนวนรายการทั้งหมด",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_Receipt,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "จำนวนรายการขาย",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_Sale_Receipt,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "จำนวนรายการคืนสินค้า",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_Return_Receipt,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "จำนวนรายการทดสอบน้ำมัน",
                      "size": "xs", 
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_Oil_Receipt,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ยอดขายสะสม (THB)",
                      "size": "xs",
                      "flex": 0,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_Money_SALE,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                },{
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ใบเสร็จสะสม",
                      "size": "xs",
                      "flex": 2,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": Total_Receipt_ALL,
                      "size": "xs",
                      "align": "end",
                      "contents": []
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "ณ เวลา {}".format(dt),
              "size": "xs",
              "align": "center",
              "gravity": "center",
              "wrap": True  ,
              "contents": []
            }
          ]
        }
      }
    ]
  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": centent
                              }
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ ข้อมูลรายงาน สาขา {} '.format(report_type,station_detail.station_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,report_type)
    except Exception as e:
      print ('ไม่สามารถสร้างรายงาน {} ได้ เนื่องจาก {}'.format(report_type,e))
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ  ชื่อสาขา {} ปัญหา {}'.format(report_type,station_detail.station_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
  
  def Xreport_Date_Select(self,station_detail,result_pos,date_from_line,report_type):
    try:
      
      date_time_str = date_from_line
      date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
      print ('date_time_obj xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx {}'.format(date_time_obj))

      contents = {
                          "type": "carousel",
                          "contents": [
                            
                            
                          ]
                        }
      
      
      for date in result_pos :
        print ('date xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx {}'.format(date))
        if date['KhdModTim'] != None:
          print ('วันที่ {}'.format(date))
          print ('ข้อมูล X Report ตามรายการ ID {} ')
          date_start_x_report = date['KhdInsTim'].strftime('%d-%m-%Y %H:%M')
          date_end_x_report = date['KhdModTim'].strftime('%d-%m-%Y %H:%M')
          # print ('วันที่เริ่มต้นรายงาน {}'.format(date_start_x_report))
          report_id = date['KhdIdent']

          # post_back = 'VIEW-X-REPORT-SITE-SHIFT{}-SITE_ID{}END'.format(report_id,station_detail.station_site)
          post_back = 'VIEW-X-REPORT-SITE-NOW-SITE_ID{}LASTID{}END'.format(station_detail.station_site,report_id)
          
          detail = {
                                  "type": "bubble",
                                  "direction": "ltr",
                                  "hero": {
                                    "type": "image",
                                    "url": "https://www.susco.co.th/images/logo_susco.png",
                                    "margin": "none",
                                    "align": "start",
                                    "gravity": "center",
                                    "size": "full",
                                    "aspectRatio": "22:6",
                                    "aspectMode": "fit",
                                    "backgroundColor": "#F2EC3EFF",
                                    "action": {
                                      "type": "uri",
                                      "label": "SUSCO",
                                      "uri": "https://www.susco.co.th/index.asp"
                                    }
                                  },
                                  "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "สาขา {}".format(station_detail.station_name),
                                        "weight": "bold",
                                        "size": "md",
                                        "wrap": True,
                                        "align": "center",
                                        "contents": []
                                      },
                                      {
                                        "type": "text",
                                        "text": "รายละเอียดรอบปิดกะ",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "margin": "sm",
                                        "contents": []
                                      },
                                      {
                                        "type": "text",
                                        "text": "วันที่ {}".format(date_time_obj.strftime("%d-%m-%Y" )),
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "center",
                                        "margin": "sm",
                                        "contents": []
                                      },
                                      {
                                        "type": "separator",
                                        "margin": "lg"
                                      },
                                      {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "margin": "lg",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "X-Report ID",
                                            "weight": "bold",
                                            "size": "sm",
                                            "flex": 5,
                                            "align": "start",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          },
                                          {
                                            "type": "text",
                                            "text": str(report_id),
                                            "weight": "bold",
                                            "size": "sm",
                                            "flex": 6,
                                            "align": "end",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          }
                                        ]
                                      },
                                      {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "margin": "lg",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "วันที่เริ่มต้น",
                                            "weight": "bold",
                                            "size": "sm",
                                            "flex": 5,
                                            "align": "start",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          },
                                          {
                                            "type": "text",
                                            "text": date_start_x_report,
                                            "weight": "bold",
                                            "size": "sm",
                                            "flex": 6,
                                            "align": "end",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          }
                                        ]
                                      },
                                      {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "margin": "lg",
                                        "contents": [
                                          {
                                            "type": "text",
                                            "text": "วันที่สิ้นสุด",
                                            "weight": "bold",
                                            "size": "sm",
                                            "flex": 5,
                                            "align": "start",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          },
                                          {
                                            "type": "text",
                                            "text": date_end_x_report,
                                            "weight": "bold",
                                            "size": "sm",
                                            "flex": 6,
                                            "align": "end",
                                            "gravity": "center",
                                            "margin": "sm",
                                            "contents": []
                                          }
                                        ]
                                      },
                                      {
                                        "type": "separator",
                                        "margin": "lg"
                                      }
                                    ]
                                  },
                                  "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "flex": 0,
                                    "spacing": "sm",
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "X-REPORT",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#AA1C1CFF",
                                        "align": "center",
                                        "gravity": "top",
                                        "wrap": True,
                                        "contents": []
                                      },
                                      {
                                        "type": "button",
                                        "action": {
                                          "type": "postback",
                                          "label": "เลือกรายงาน",
                                          "text": "ข้อความระบบ : กำลังจัดส่งรายละเอียด",
                                          "data": post_back
                                        },
                                        "color": "#078025FF",
                                        "style": "secondary"
                                      }
                                    ]
                                  }
                                }
          contents["contents"].append(detail)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": contents
                              }
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ ข้อมูลรายงาน สาขา {} '.format(report_type,station_detail.station_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,report_type)
    except Exception as e:
      print ('ไม่สามารถสร้างรายงาน {} ได้ เนื่องจาก {}'.format(report_type,e))
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ  ชื่อสาขา {} ปัญหา {}'.format(report_type,station_detail.station_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
  
  def AreaSelectOptionSiteInList(self,area_profile,area_in_site,report_type):
    try :
      if report_type == 'X-REPORT' :
        ReportButton = report_type
      elif report_type == 'METER' :
        ReportButton = report_type
      elif report_type == 'PRICE' :
        ReportButton = report_type
      elif report_type == 'SMB' :
        ReportButton = report_type
      

      data = {
                                    "type": "flex",
                                    "altText": 'message',
                                    "contents": {
                        "type": "bubble",
                        "direction": "ltr",
                        "hero": {
                          "type": "image",
                          "url": "https://www.susco.co.th/images/logo_susco.png",
                          "margin": "none",
                          "align": "start",
                          "gravity": "center",
                          "size": "full",
                          "aspectRatio": "22:6",
                          "aspectMode": "fit",
                          "backgroundColor": "#F2EC3EFF",
                          "action": {
                            "type": "uri",
                            "label": "SUSCO",
                            "uri": "https://www.susco.co.th/index.asp"
                          }
                        },
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "เขต {}".format(area_profile.area_code_type),
                              "weight": "bold",
                              "size": "lg",
                              "align": "center",
                              "contents": []
                            },
                            {
                              "type": "text",
                              "text": "คุณ {}".format(area_profile.area_code_name),
                              "weight": "bold",
                              "size": "lg",
                              "align": "center",
                              "contents": []
                            },
                            {
                              "type": "text",
                              "text": "เลือกสถานีที่ต้องการ",
                              "weight": "bold",
                              "size": "lg",
                              "align": "center",
                              "contents": []
                            },
                            {
                              "type": "separator",
                              "margin": "lg"
                            }
                            # ส่วนวนลูปข้อมูลสถานี
                            
                            # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                            
                            ,
                            
                            
                            
                            {
                              "type": "separator",
                              "margin": "lg"
                            }
                          ]
                        },
                        "footer": {
                          "type": "box",
                          "layout": "vertical",
                          "flex": 0,
                          "spacing": "sm",
                          "contents": [
                            {
                              "type": "text",
                              "text": ReportButton,
                              "weight": "bold",
                              "size": "lg",
                              "color": "#AA1C1CFF",
                              "align": "center",
                              "gravity": "top",
                              "wrap": True  ,
                              "contents": []
                            }
                          ]
                        }
                      }
                                                  }
      for i in area_in_site :
        if report_type == 'X-REPORT' :
          post_back = "VIEW-X-REPORT-AREA-SITEID{}END".format(i.station_site)
        elif report_type == 'METER' :
          post_back = "VIEW-METER-AREA-ID{}END".format(i.station_site)
        elif report_type == 'PRICE' :
          post_back = "VIEW-PRICE-AREA-ID{}END".format(i.station_site)
        elif report_type == 'SMB' :
          post_back = "VIEW-SMB-AREA-ID{}END".format(i.station_site)


        contents_data = {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "lg",
                    "contents": [
                      {
                        "type": "text",
                        "text": i.station_name,
                        "weight": "bold",
                        "size": "xs",
                        "flex": 5,
                        "align": "start",
                        "gravity": "center",
                        "margin": "sm",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "เลือก",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#FA4204FF",
                        "align": "end",
                        "gravity": "center",
                        "margin": "sm",
                        "action": {
                          "type": "postback",
                          "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                          "data": post_back
                        },
                        "contents": []
                      }
                    ]
                  }
        data['contents']['body']['contents'].insert(-1,contents_data)
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ ข้อมูลรายงาน ผู้จัดการเขต {} ชื่อเขต {}'.format(report_type,area_profile.area_code_type,area_profile.area_code_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,report_type)
    except Exception as e:
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ ข้อมูลรายงาน ผู้จัดการเขต {} ชื่อเขต {} ปัญหา {}'.format(report_type,area_profile.area_code_type,area_profile.area_code_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages().ReplyTextMessage(self.reply_token,messages,report_type)
  
  
  def Multi_site_Selecter(self,first_site,station_add,report_type):
    try :
      if report_type == 'XREPORT' :
        report_buttum = 'XREPORT'
        post_back_station_main = "VIEW-X-REPORT-AREA-SITEID{}END".format(first_site.userList_station_name.station_site)
      elif report_type == 'METER' :
        report_buttum = 'METER'
        post_back_station_main = "VIEW-METER-AREA-ID{}END".format(first_site.userList_station_name.station_site)
      elif report_type == 'PRICE' :
        report_buttum = 'PRICE'
        post_back_station_main = "VIEW-PRICE-AREA-ID{}END".format(first_site.userList_station_name.station_site)
      elif report_type == 'SMB' :
        report_buttum = 'SMB'
        post_back_station_main = "VIEW-SMB-AREA-ID{}END".format(first_site.userList_station_name.station_site)
      data = {
                                    "type": "flex",
                                    "altText": 'message',
                                    "contents": {
                        "type": "bubble",
                        "direction": "ltr",
                        "hero": {
                          "type": "image",
                          "url": "https://www.susco.co.th/images/logo_susco.png",
                          "margin": "none",
                          "align": "start",
                          "gravity": "center",
                          "size": "full",
                          "aspectRatio": "22:6",
                          "aspectMode": "fit",
                          "backgroundColor": "#F2EC3EFF",
                          "action": {
                            "type": "uri",
                            "label": "SUSCO",
                            "uri": "https://www.susco.co.th/index.asp"
                          }
                        },
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            
                            {
                              "type": "text",
                              "text": "เลือกสถานีที่ต้องการ",
                              "weight": "bold",
                              "size": "lg",
                              "align": "center",
                              "contents": []
                            },
                            {
                              "type": "separator",
                              "margin": "lg"
                            },
                            # ส่วนวนลูปข้อมูลสถานี
                            {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "lg",
                    "contents": [
                      {
                        "type": "text",
                        "text": first_site.userList_station_name.station_name,
                        "weight": "bold",
                        "size": "xs",
                        "flex": 5,
                        "align": "start",
                        "gravity": "center",
                        "margin": "sm",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "เลือก",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#FA4204FF",
                        "align": "end",
                        "gravity": "center",
                        "margin": "sm",
                        "action": {
                          "type": "postback",
                          "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                          "data": post_back_station_main
                        },
                        "contents": []
                      }
                    ]
                  }
                            # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                            
                            ,
                            
                            
                            
                            {
                              "type": "separator",
                              "margin": "lg"
                            }
                          ]
                        },
                        "footer": {
                          "type": "box",
                          "layout": "vertical",
                          "flex": 0,
                          "spacing": "sm",
                          "contents": [
                            {
                              "type": "text",
                              "text": report_buttum,
                              "weight": "bold",
                              "size": "lg",
                              "color": "#AA1C1CFF",
                              "align": "center",
                              "gravity": "top",
                              "wrap": True  ,
                              "contents": []
                            }
                          ]
                        }
                      }
                                                  }

      for i in station_add :
        if report_type == 'XREPORT' :
          post_back_station_add = "VIEW-X-REPORT-AREA-SITEID{}END".format(i.multi_station_number.station_site)
        elif report_type == 'METER' :
          post_back_station_add = "VIEW-METER-AREA-ID{}END".format(i.multi_station_number.station_site)
        elif report_type == 'PRICE' :
          post_back_station_add = "VIEW-PRICE-AREA-ID{}END".format(i.multi_station_number.station_site)
        elif report_type == 'SMB' :
          post_back_station_add = "VIEW-SMB-AREA-ID{}END".format(i.multi_station_number.station_site)
        
        contents_data = {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "lg",
                    "contents": [
                      {
                        "type": "text",
                        "text": i.multi_station_number.station_name,
                        "weight": "bold",
                        "size": "xs",
                        "flex": 5,
                        "align": "start",
                        "gravity": "center",
                        "margin": "sm",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "เลือก",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#FA4204FF",
                        "align": "end",
                        "gravity": "center",
                        "margin": "sm",
                        "action": {
                          "type": "postback",
                          "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                          "data": post_back_station_add
                        },
                        "contents": []
                      }
                    ]
                  }
        data['contents']['body']['contents'].insert(-1,contents_data)

      print ('สร้าง Flex Message สำหรับรายงาน {} '.format('command_save'))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,'command_save')
    except Exception as e:
      print ('ไม่สามารถสร้างรายงาน {} ได้ เนื่องจาก {}'.format(report_type,e))
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ  ชื่อสาขา {} ปัญหา {}'.format(report_type,'user_profile.station_name',str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
    
    
  
  def SMB_Multi_site_Selecter(self,first_site,station_add):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          
                          {
                            "type": "text",
                            "text": "เลือกสถานีที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          },
                          # ส่วนวนลูปข้อมูลสถานี
                          {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": first_site.userList_station_name.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-SMB-AREA-ID{}END".format(first_site.userList_station_name.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "SMB REPORT",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in station_add :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.multi_station_number.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-SMB-AREA-ID{}END".format(i.multi_station_number.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def METER_Multi_site_Selecter(self,first_site,station_add):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          
                          {
                            "type": "text",
                            "text": "เลือกสถานีที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          },
                          # ส่วนวนลูปข้อมูลสถานี
                          {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": first_site.userList_station_name.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-METER-AREA-ID{}END".format(first_site.userList_station_name.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "METER REPORT",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in station_add :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.multi_station_number.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-METER-AREA-ID{}END".format(i.multi_station_number.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def PRICE_Multi_site_Selecter(self,first_site,station_add):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          
                          {
                            "type": "text",
                            "text": "เลือกสถานีที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          },
                          # ส่วนวนลูปข้อมูลสถานี
                          {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": first_site.userList_station_name.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-PRICE-AREA-ID{}END".format(first_site.userList_station_name.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "PRICE",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in station_add :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.multi_station_number.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-PRICE-AREA-ID{}END".format(i.multi_station_number.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def SMB_Area_Selecter(self,area_in_site,area_profile):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "เขต {}".format(area_profile.area_code_type),
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "คุณ {}".format(area_profile.area_code_name),
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "เลือกสถานีที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                          # ส่วนวนลูปข้อมูลสถานี
                          
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "SMB REPORT",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in area_in_site :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-SMB-AREA-ID{}END".format(i.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def METER_Area_Selecter(self,area_in_site,area_profile):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "เขต {}".format(area_profile.area_code_type),
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "คุณ {}".format(area_profile.area_code_name),
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "เลือกสถานีที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                          # ส่วนวนลูปข้อมูลสถานี
                          
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "METER",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in area_in_site :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-METER-AREA-ID{}END".format(i.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def PRICE_Area_Selecter(self,area_in_site,area_profile):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "เขต {}".format(area_profile.area_code_type),
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "คุณ {}".format(area_profile.area_code_name),
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "เลือกสถานีที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                          # ส่วนวนลูปข้อมูลสถานี
                          
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "PRICE",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in area_in_site :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.station_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
                        "data": "VIEW-PRICE-AREA-ID{}END".format(i.station_site)
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def MainAreaSelectOptionAreaManager(self,position,display_name,all_area_manager,report_type):
    try :
      if report_type == 'X-REPORT' :
        ReportButton = report_type
      elif report_type == 'METER' :
        ReportButton = report_type
      elif report_type == 'PRICE' :
        ReportButton = report_type
      elif report_type == 'SMB' :
        ReportButton = report_type
        
        
      data = {
                                    "type": "flex",
                                    "altText": 'message',
                                    "contents": {
                        "type": "bubble",
                        "direction": "ltr",
                        "hero": {
                          "type": "image",
                          "url": "https://www.susco.co.th/images/logo_susco.png",
                          "margin": "none",
                          "align": "start",
                          "gravity": "center",
                          "size": "full",
                          "aspectRatio": "22:6",
                          "aspectMode": "fit",
                          "backgroundColor": "#F2EC3EFF",
                          "action": {
                            "type": "uri",
                            "label": "SUSCO",
                            "uri": "https://www.susco.co.th/index.asp"
                          }
                        },
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "เลือกผู้จัดการเขตที่ต้องการ",
                              "weight": "bold",
                              "size": "lg",
                              "align": "center",
                              "contents": []
                            },
                            {
                              "type": "separator",
                              "margin": "lg"
                            }
                            # ส่วนวนลูปข้อมูลสถานี
                            
                            # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                            
                            ,
                            
                            
                            
                            {
                              "type": "separator",
                              "margin": "lg"
                            }
                          ]
                        },
                        "footer": {
                          "type": "box",
                          "layout": "vertical",
                          "flex": 0,
                          "spacing": "sm",
                          "contents": [
                            {
                              "type": "text",
                              "text": ReportButton,
                              "weight": "bold",
                              "size": "lg",
                              "color": "#AA1C1CFF",
                              "align": "center",
                              "gravity": "top",
                              "wrap": True  ,
                              "contents": []
                            }
                          ]
                        }
                      }
                                                  }
      
      for i in all_area_manager :
        # ค้นหา line user_id ด้วยการ
        
        if report_type == 'X-REPORT' :
          line_user_id = UserListCodeType.objects.filter(userList_area_name__id=i.area_code_type.id).first()
          print ('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz',line_user_id)
          postback = "VIEW-X-REPORT-MAIN-SELECTER{}END".format(str(line_user_id.userList_userid))
          
        elif report_type == 'METER' :
          line_user_id = UserListCodeType.objects.filter(userList_area_name__id=i.area_code_type.id).first()
          print (line_user_id)
          postback = "VIEW-METER-MAIN-SELECTER{}END".format(str(line_user_id.userList_userid))
        
        elif report_type == 'PRICE' :
          line_user_id = UserListCodeType.objects.filter(userList_area_name__id=i.area_code_type.id).first()
          print (line_user_id)
          postback = "VIEW-PRICE-MAIN-SELECTER{}END".format(str(line_user_id.userList_userid))
        elif report_type == 'SMB' :
          line_user_id = UserListCodeType.objects.filter(userList_area_name__id=i.area_code_type.id).first()
          print (line_user_id)
          postback = "VIEW-SMB-MAIN-SELECTER{}END".format(str(line_user_id.userList_userid))
        
        contents_data = {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "lg",
                    "contents": [
                      {
                        "type": "text",
                        "text": i.area_code_name,
                        "weight": "bold",
                        "size": "xs",
                        "flex": 5,
                        "align": "start",
                        "gravity": "center",
                        "margin": "sm",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "เลือก",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#FA4204FF",
                        "align": "end",
                        "gravity": "center",
                        "margin": "sm",
                        "action": {
                          "type": "postback",
                          "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขาในเขตนี้",
                          "data": postback
                        },
                        "contents": []
                      }
                    ]
                  }
        data['contents']['body']['contents'].insert(-1,contents_data)

      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ  ตำแหน่ง {} ชื่อ {}'.format(report_type,position,display_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,report_type)
      return True
      
    except Exception as e:
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ ตำแหน่ง {} ชื่อ {} ปัญหา {}'.format(report_type,position,display_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
  def SMB_Main_Area_Selecter(self,all_area_manager):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "เลือกผู้จัดการเขตที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                          # ส่วนวนลูปข้อมูลสถานี
                          
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "SMB REPORT",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in all_area_manager :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.area_code_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขาในเขตนี้",
                        "data": "VIEW-SMB-MAIN-SELECTER{}END".format(str(i.area_code_type.id))
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def METER_Main_Area_Selecter(self,all_area_manager):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "เลือกผู้จัดการเขตที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                          # ส่วนวนลูปข้อมูลสถานี
                          
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "METER",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in all_area_manager :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.area_code_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขาในเขตนี้",
                        "data": "VIEW-METER-MAIN{}END".format(str(i.area_code_type.id))
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def PRICE_Main_Area_Selecter(self,all_area_manager):
    
    data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": {
                      "type": "bubble",
                      "direction": "ltr",
                      "hero": {
                        "type": "image",
                        "url": "https://www.susco.co.th/images/logo_susco.png",
                        "margin": "none",
                        "align": "start",
                        "gravity": "center",
                        "size": "full",
                        "aspectRatio": "22:6",
                        "aspectMode": "fit",
                        "backgroundColor": "#F2EC3EFF",
                        "action": {
                          "type": "uri",
                          "label": "SUSCO",
                          "uri": "https://www.susco.co.th/index.asp"
                        }
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "เลือกผู้จัดการเขตที่ต้องการ",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                          # ส่วนวนลูปข้อมูลสถานี
                          
                          # ส่วนสิ้นสุดวนลูปข้อมูลสถานี
                          
                          ,
                          
                          
                          
                          {
                            "type": "separator",
                            "margin": "lg"
                          }
                        ]
                      },
                      "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "PRICE",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#AA1C1CFF",
                            "align": "center",
                            "gravity": "top",
                            "wrap": True  ,
                            "contents": []
                          }
                        ]
                      }
                    }
                                                }

    for i in all_area_manager :
      contents_data = {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "lg",
                  "contents": [
                    {
                      "type": "text",
                      "text": i.area_code_name,
                      "weight": "bold",
                      "size": "xs",
                      "flex": 5,
                      "align": "start",
                      "gravity": "center",
                      "margin": "sm",
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "เลือก",
                      "weight": "bold",
                      "size": "sm",
                      "color": "#FA4204FF",
                      "align": "end",
                      "gravity": "center",
                      "margin": "sm",
                      "action": {
                        "type": "postback",
                        "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขาในเขตนี้",
                        "data": "VIEW-PRICE-MAIN{}END".format(str(i.area_code_type.id))
                      },
                      "contents": []
                    }
                  ]
                }
      data['contents']['body']['contents'].insert(-1,contents_data)

    return data
  def SMB_Selecter_by_stie(self,user_profile,position):
    if position == 1 :
      print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการสาขสาขา')
      station_name = user_profile.station_name
      post_back_last_shift = 'VIEW-SMB-SITE-NOW-SITE_ID{}END'.format(user_profile.station_site)
      post_back_businessdate = 'VIEW-SMB-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
    elif position in (3,4,5) :
      print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการเขต')
      station_name = user_profile.station_name
      post_back_last_shift = 'VIEW-SMB-SITE-NOW-SITE_ID{}END'.format(user_profile.station_site)
      post_back_businessdate = 'VIEW-SMB-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
    
    contents = {
  "type": "bubble",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "margin": "none",
    "align": "start",
    "gravity": "center",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "SUSCO",
      "uri": "https://www.susco.co.th/index.asp"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": station_name,
        "weight": "bold",
        "size": "lg",
        "align": "center",
        "contents": []
      },
      
      {
        "type": "text",
        "text": "เลือกวิธีการเช็คคะแนนสะสม",
        "weight": "bold",
        "size": "lg",
        "align": "center",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "คะแนนปัจจุบัน",
            "weight": "bold",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล SMB ปัจจุบัน",
              "data": post_back_last_shift
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "คะแนนระบุวัน",
            "weight": "bold",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล SMB ย้อนหลัง10 วัน",
              "data": post_back_businessdate
            },
            "contents": []
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "text",
        "text": "SMB คะแนนสะสม",
        "weight": "bold",
        "size": "lg",
        "color": "#AA1C1CFF",
        "align": "center",
        "gravity": "top",
        "wrap": True ,
        "contents": []
      }
    ]
  }
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
      
  def SMB_Selecter_by_stie_single(self,user_profile,evrIdent,report_type):
    try : 
      today = datetime.now().strftime("%Y-%m-%d")
      new_date = (datetime.now() - relativedelta(days=60)).strftime("%Y-%m-%d")
      # if position == 1 :
      #   print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการสาขสาขา')
      station_name = user_profile.station_name
      post_back_last_shift = 'VIEW-SMB-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(user_profile.station_site,evrIdent['EvrNum'])
      post_back_businessdate = 'VIEW-SMB-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
      # elif position in (3,4,5) :
      #   print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการเขต')
      #   station_name = user_profile.station_name
      #   post_back_last_shift = 'VIEW-SMB-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(user_profile.station_site,evrIdent['EvrNum'])
      #   post_back_businessdate = 'VIEW-SMB-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
      
      contents = {
                                                    "type": "bubble",
                                                    "direction": "ltr",
                                                    "hero": {
                                                      "type": "image",
                                                      "url": "https://www.susco.co.th/images/logo_susco.png",
                                                      "margin": "none",
                                                      "align": "start",
                                                      "gravity": "center",
                                                      "size": "full",
                                                      "aspectRatio": "22:6",
                                                      "aspectMode": "fit",
                                                      "backgroundColor": "#F2EC3EFF",
                                                      "action": {
                                                        "type": "uri",
                                                        "label": "SUSCO",
                                                        "uri": "https://www.susco.co.th/index.asp"
                                                      }
                                                    },
                                                    "body": {
                                                      "type": "box",
                                                      "layout": "vertical",
                                                      "contents": [
                                                        {
                                                          "type": "text",
                                                          "text": station_name,
                                                          "weight": "bold",
                                                          "size": "lg",
                                                          "align": "center",
                                                          "wrap": True ,
                                                          "contents": []
                                                        },
                                                        
                                                        {
                                                          "type": "text",
                                                          "text": "เลือกรายการที่ต้องการ",
                                                          "weight": "bold",
                                                          "size": "lg",
                                                          "align": "center",
                                                          "contents": []
                                                        },
                                                        {
                                                          "type": "separator",
                                                          "margin": "lg"
                                                        },
                                                        {
                                                          "type": "box",
                                                          "layout": "horizontal",
                                                          "margin": "lg",
                                                          "contents": [
                                                            {
                                                              "type": "text",
                                                              "text": "SMB ปัจจุบัน",
                                                              "weight": "bold",
                                                              "size": "md",
                                                              "align": "start",
                                                              "gravity": "center",
                                                              "margin": "sm",
                                                              "contents": []
                                                            },
                                                            {
                                                              "type": "text",
                                                              "text": "เลือก",
                                                              "weight": "bold",
                                                              "size": "md",
                                                              "color": "#FA4204FF",
                                                              "align": "end",
                                                              "gravity": "center",
                                                              "margin": "sm",
                                                              "action": {
                                                                "type": "postback",
                                                                "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                                                                "data": post_back_last_shift
                                                              },
                                                              "contents": []
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "box",
                                                          "layout": "horizontal",
                                                          "margin": "lg",
                                                          "contents": [
                                                            {
                                                              "type": "text",
                                                              "text": "SMB ระบุวัน",
                                                              "weight": "bold",
                                                              "size": "md",
                                                              "align": "start",
                                                              "gravity": "center",
                                                              "margin": "sm",
                                                              "contents": []
                                                            },
                                                            {
                                                              "type": "text",
                                                              "text": "เลือก",
                                                              "weight": "bold",
                                                              "size": "sm",
                                                              "color": "#CA1F12FF",
                                                              "align": "end",
                                                              "gravity": "center",
                                                              "margin": "sm",
                                                              "action": {
                                                                "type": "datetimepicker",
                                                                "label": "test",
                                                                "data": post_back_businessdate,
                                                                "mode": "date",
                                                                "initial": today,
                                                                "max": today,
                                                                "min": new_date
                                                              },
                                                              "contents": []
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "separator",
                                                          "margin": "lg"
                                                        }
                                                      ]
                                                    },
                                                    "footer": {
                                                      "type": "box",
                                                      "layout": "vertical",
                                                      "flex": 0,
                                                      "spacing": "sm",
                                                      "contents": [
                                                        {
                                                          "type": "text",
                                                          "text": "SMB",
                                                          "weight": "bold",
                                                          "size": "lg",
                                                          "color": "#AA1C1CFF",
                                                          "align": "center",
                                                          "gravity": "top",
                                                          "wrap": True ,
                                                          "contents": []
                                                        }
                                                      ]
                                                    }
                                                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": contents
                              }
      # print ('data is {}'.format(data))
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ ข้อมูลรายงาน สาขา {} '.format('SMB',user_profile.station_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,'SMB')
    except Exception as e:
      print ('ไม่สามารถสร้างรายงาน {} ได้ เนื่องจาก {}'.format(report_type,e))
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ  ชื่อสาขา {} ปัญหา {}'.format(report_type,user_profile.station_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
  
  def SMB_Last_Shift(self,station_detail,result_pos,report_type):
    try :
      # ทำการรวมจำนวนกะในระบบ
      shift_store = []
      product_store = []
      for shift_id in result_pos :
        if shift_id['ShiftNo'] not in shift_store :
          shift_store.append(shift_id['ShiftNo'])
      for product_id in result_pos :
        if product_id['StokNam'] not in product_store :
          product_store.append(product_id['StokNam'])

      print ('shift_store is {}'.format(shift_store))
      print ('product_store is {}'.format(product_store))

      contents =  {
      "type": "carousel",
      "contents": [
        # ส่วนวนลูปมาแสดงข้อมูล
        
    
  ]
}     
      for comapre in product_store :
        for tanks in result_pos : 
          if tanks['StokNam'] == comapre :
            dt=datetime.now().strftime("%d-%m-%Y %H:%M")
            SMB_contents = {
            "type": "bubble",
            "hero": {
              "type": "image",
              "url": "https://www.susco.co.th/images/logo_susco.png",
              "align": "start",
              "size": "full",
              "aspectRatio": "22:6",
              "aspectMode": "fit",
              "backgroundColor": "#F2EC3EFF",
              "action": {
                "type": "uri",
                "label": "Action",
                "uri": "https://linecorp.com"
              }
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "spacing": "md",
              "action": {
                "type": "uri",
                "label": "Action",
                "uri": "https://linecorp.com"
              },
              "contents": [
                {
                  "type": "text",
                  "text": "สาขา {}".format(station_detail.station_name),
                  "weight": "bold",
                  "size": "lg",
                  "align": "center",
                  "wrap": True,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "รายงานสะสมแต้ม",
                  "weight": "bold",
                  "size": "lg",
                  "align": "center",
                  "contents": []
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "BusinessDate",
                          "weight": "bold",
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": tanks['BusinessDate'],
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "ShiftNo",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": str(tanks['ShiftNo']),
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "StokNam",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": tanks['StokNam'],
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "CountTransaction",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": str(tanks['CountTransaction']),
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "SumQTY",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "{:.2f}".format(tanks['SumQTY']),
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "SumSaleAmount",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "{:.2f}".format(tanks['SumSaleAmount']),
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "SumTycheQTY",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "{:.2f}".format(tanks['SumTycheQTY']),
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "SumTycheSaleAmount",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "1",
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": str(tanks['CountTycheTransaction']),
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "1",
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "TotalPointEarned",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": str(tanks['TotalPointEarned']),
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "TotalPointSpent",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text":str(tanks['TotalPointSpent']),
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "TotalSpentAmount",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": "{:.2f}".format(tanks['TotalSpentAmount']),
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Time_requests",
                          "weight": "bold",
                          "flex": 0,
                          "align": "start",
                          "margin": "sm",
                          "contents": []
                        },
                        {
                          "type": "text",
                          "text": dt,
                          "size": "sm",
                          "color": "#AAAAAA",
                          "align": "end",
                          "contents": []
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          }
            contents["contents"].append(SMB_contents)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": contents
                              }
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ ข้อมูลรายงาน สาขา {} '.format('SMB',station_detail.station_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,'SMB')
    except Exception as e:
      print ('ไม่สามารถสร้างรายงาน {} ได้ เนื่องจาก {}'.format(report_type,e))
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ  ชื่อสาขา {} ปัญหา {}'.format(report_type,station_detail.station_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
  def SMB_Date_Selecter(self,station_detail,result_pos,date_from_line,report_type):
    # print ('type 0f data_from_line {} จำนวน'.format(type(result_pos[1])))
    # print ('len 0f data_from_line {} จำนวน'.format(len(result_pos[1])))
    # คำนวณหาจำนวนกะ เพราะถ้าเกิน 4 กะ อาจจะส่ง flex ไม่ได้ เนื่องจาก line จำกัดที่ 2000 ตัวอักษร
    data_len = len(result_pos[1])
    print ('data_len {} จำนวน'.format(data_len))
   
    try:
      # คำนวณหาจำนวน shift ในระบบ
      sum_shift_store = []
      total_shift = []
      for sum_shift in result_pos[1]:
        if sum_shift['ShiftNo'] not in sum_shift_store:
          sum_shift_store.append(sum_shift['ShiftNo'])
          data = {'BusinessDate':sum_shift['BusinessDate'],'ShiftNo':sum_shift['ShiftNo']}
          total_shift.append(data)
      print ('total_shift {} จำนวน'.format(total_shift))

      
      date_time_str = date_from_line
      date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
      print ('date_time_obj xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx {}'.format(date_time_obj))
      
      contents = {
                          "type": "carousel",
                          "contents": [
                            
                            
                          ]
                        }
      
      
      for data in total_shift :
       
        
        print ('วันที่ {}'.format(data))
        print ('ข้อมูล SMB ตามรายการ ID {} ')
        #ทำการเปลี่ยน date format ใหม่
        date_time_str = data['BusinessDate']
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
        new_time_request = date_time_obj.strftime('%Y%m%d') 
        trensection_shift = '{}_{}'.format(new_time_request,data['ShiftNo'])
        post_back = 'VIEW-SMB-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(station_detail.station_site,trensection_shift)
        # post_back2 = 'VIEW-METER-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(station_detail.station_site,data['EvrNum'][:-2])
        # if data_len >= 4 :
        #   label =  "แสดงทุกกะ"
        #   text = "ข้อความระบบ : ไม่สามารถแสดงรายงานได้เนื่องจากจำนวนกะเกิน 3 กะ เกิน Limit ของข้อจำกัดของ Line กรุณาเลือกการแสดงผลที่ละกะ"
        #   # text = "ข้อความระบบ : xxxxxxxxxxxxxxxxxx",
        #   postback2 = 'post_back'
        # elif data_len <= 3 :
        # label =  "แสดงทุกกะ"
        # text = "ข้อความระบบ : กำลังจัดส่งข้อมูล Meter ของกะที่ต้องการ"
        # postback2 = 'VIEW-SMB-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(station_detail.station_site,data['EvrNum'][:-2])

        # print ('วันที่เริ่มต้นรายงาน {}'.format(date_start_x_report))
        # report_id = data['EvrNum'][9:]

        
        
        detail = {
                                "type": "bubble",
                                "direction": "ltr",
                                "hero": {
                                  "type": "image",
                                  "url": "https://www.susco.co.th/images/logo_susco.png",
                                  "margin": "none",
                                  "align": "start",
                                  "gravity": "center",
                                  "size": "full",
                                  "aspectRatio": "22:6",
                                  "aspectMode": "fit",
                                  "backgroundColor": "#F2EC3EFF",
                                  "action": {
                                    "type": "uri",
                                    "label": "SUSCO",
                                    "uri": "https://www.susco.co.th/index.asp"
                                  }
                                },
                                "body": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "สาขา {}".format(station_detail.station_name),
                                      "weight": "bold",
                                      "size": "md",
                                      "wrap": True,
                                      "align": "center",
                                      "contents": []
                                    },
                                    {
                                      "type": "text",
                                      "text": "รายละเอียดรอบปิดกะ",
                                      "weight": "bold",
                                      "size": "md",
                                      "align": "center",
                                      "margin": "sm",
                                      "contents": []
                                    },
                                    {
                                      "type": "text",
                                      "text": "วันที่ปิดวัน {}".format(data['BusinessDate']),
                                      "weight": "bold",
                                      "size": "md",
                                      "align": "center",
                                      "margin": "sm",
                                      "contents": []
                                    },
                                    {
                                      "type": "separator",
                                      "margin": "lg"
                                    },
                                    {
                                      "type": "box",
                                      "layout": "horizontal",
                                      "margin": "lg",
                                      "contents": [
                                        {
                                          "type": "text",
                                          "text": "รอบกะที่ ",
                                          "weight": "bold",
                                          "size": "sm",
                                          "flex": 5,
                                          "align": "start",
                                          "gravity": "center",
                                          "margin": "sm",
                                          "contents": []
                                        },
                                        {
                                          "type": "text",
                                          "text": str(data['ShiftNo']),
                                          "weight": "bold",
                                          "size": "sm",
                                          "flex": 6,
                                          "align": "end",
                                          "gravity": "center",
                                          "margin": "sm",
                                          "contents": []
                                        }
                                      ]
                                    },
                                    {
                                      "type": "box",
                                      "layout": "horizontal",
                                      "margin": "lg",
                                      "contents": [
                                        {
                                          "type": "text",
                                          "text": "วันที่ปิดวัน",
                                          "weight": "bold",
                                          "size": "sm",
                                          "flex": 5,
                                          "align": "start",
                                          "gravity": "center",
                                          "margin": "sm",
                                          "contents": []
                                        },
                                        {
                                          "type": "text",
                                          "text": '{}'.format(data['BusinessDate']),
                                          "weight": "bold",
                                          "size": "sm",
                                          "flex": 6,
                                          "align": "end",
                                          "gravity": "center",
                                          "margin": "sm",
                                          "contents": []
                                        }
                                      ]
                                    },
                                    
                                    {
                                      "type": "separator",
                                      "margin": "lg"
                                    }
                                  ]
                                },
                                "footer": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "flex": 0,
                                  "spacing": "sm",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "SMB",
                                      "weight": "bold",
                                      "size": "lg",
                                      "color": "#AA1C1CFF",
                                      "align": "center",
                                      "gravity": "top",
                                      "wrap": True,
                                      "contents": []
                                    },
                                    {
                                      "type": "button",
                                      "action": {
                                        "type": "postback",
                                        "label": "เลือกรายงานกะนี้",
                                        "text": "ข้อความระบบ : กำลังจัดส่งรายละเอียด SMB ",
                                        "data": post_back
                                      },
                                      "color": "#078025FF",
                                      "style": "secondary"
                                    }
                                  ]
                                }
                              }
        contents["contents"].append(detail)
        
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": contents
                              }
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ ข้อมูลรายงาน สาขา {} '.format('SMB',station_detail.station_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,'SMB')
    except Exception as e:
      print ('ไม่สามารถสร้างรายงาน {} ได้ เนื่องจาก {}'.format(report_type,e))
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ  ชื่อสาขา {} ปัญหา {}'.format(report_type,station_detail.station_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
    
    
  def SMB_Date_Report(self,user_id):
    contents = {
  "type": "bubble",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "margin": "none",
    "align": "start",
    "gravity": "center",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "SUSCO",
      "uri": "https://www.susco.co.th/index.asp"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "เลือกรายการรอบปิดกะที่ต้องการ",
        "weight": "bold",
        "size": "md",
        "align": "center",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "วันที่ 22-03-2022",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Shift 1",
                "weight": "bold",
                "size": "md",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "เลือก",
                "weight": "bold",
                "size": "md",
                "color": "#FA4204FF",
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "action": {
                  "type": "postback",
                  "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล SMB ปัจจุบัน",
                  "data": "SMBSHIFT1-22-03-2022"
                },
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [
              {
                "type": "text",
                "text": "Shift 2",
                "weight": "bold",
                "size": "md",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "เลือก",
                "weight": "bold",
                "size": "md",
                "color": "#FA4204FF",
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "action": {
                  "type": "postback",
                  "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล SMB ปัจจุบัน",
                  "data": "SMBSHIFT2-22-03-2022"
                },
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [
              {
                "type": "text",
                "text": "Shift 3",
                "weight": "bold",
                "size": "md",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "เลือก",
                "weight": "bold",
                "size": "md",
                "color": "#FA4204FF",
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "action": {
                  "type": "postback",
                  "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล SMB ปัจจุบัน",
                  "data": "SMBSHIFT3-22-03-2022"
                },
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [
              {
                "type": "text",
                "text": "All-Shift",
                "weight": "bold",
                "size": "md",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "เลือก",
                "weight": "bold",
                "size": "md",
                "color": "#FA4204FF",
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "action": {
                  "type": "postback",
                  "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล SMB ปัจจุบัน",
                  "data": "SMBSHIFTA-22-03-2022"
                },
                "contents": []
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "text",
        "text": "SMB คะแนนสะสม",
        "weight": "bold",
        "size": "lg",
        "color": "#AA1C1CFF",
        "align": "center",
        "gravity": "center",
        "wrap": True,
        "contents": []
      }
    ]
  }
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
  def SMB_All_Shift(self,user_id):
    contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "align": "start",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "รายงานสะสมแต้ม",
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "contents": []
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "BusinessDate",
                    "weight": "bold",
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "2021-11-26",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "ShiftNo",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "StokNam",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "DSLB7",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "CountTransaction",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "3",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumQTY",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "12.2160",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumSaleAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "305.4000",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumTycheQTY",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "305.4000",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumTycheSaleAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "CountTycheTransection",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalPointEarned",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "5",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalPointSpent",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "0",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalSpentAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Time_requests",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "06-01-22 10:07",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "align": "start",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "รายงานสะสมแต้ม",
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "contents": []
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "BusinessDate",
                    "weight": "bold",
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "2021-11-26",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "ShiftNo",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "StokNam",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "DSLB7",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "CountTransaction",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "3",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumQTY",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "12.2160",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumSaleAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "305.4000",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumTycheQTY",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "305.4000",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumTycheSaleAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "CountTycheTransection",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalPointEarned",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "5",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalPointSpent",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "0",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalSpentAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Time_requests",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "06-01-22 10:07",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "align": "start",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "รายงานสะสมแต้ม",
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "contents": []
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "BusinessDate",
                    "weight": "bold",
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "2021-11-26",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "ShiftNo",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "StokNam",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "DSLB7",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "CountTransaction",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "3",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumQTY",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "12.2160",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumSaleAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "305.4000",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumTycheQTY",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "305.4000",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "SumTycheSaleAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "CountTycheTransection",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalPointEarned",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "5",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalPointSpent",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "0",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "TotalSpentAmount",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "1",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Time_requests",
                    "weight": "bold",
                    "flex": 0,
                    "align": "start",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "06-01-22 10:07",
                    "size": "sm",
                    "color": "#AAAAAA",
                    "align": "end",
                    "contents": []
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  ]
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data

  def METER_Selecter_by_Site(self,user_profile,position,evrIdent):
    try : 
      today = datetime.now().strftime("%Y-%m-%d")
      new_date = (datetime.now() - relativedelta(days=60)).strftime("%Y-%m-%d")
      if position == 1 :
        print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการสาขสาขา')
        station_name = user_profile.userList_station_name.station_name
        post_back_last_shift = 'VIEW-METER-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(user_profile.userList_station_name.station_site,evrIdent['EvrNum'])
        post_back_businessdate = 'VIEW-METER-SITE-DAY-SITE_ID{}END'.format(user_profile.userList_station_name.station_site)
      elif position in (3,4,5) :
        print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการเขต')
        station_name = user_profile.station_name
        post_back_last_shift = 'VIEW-METER-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(user_profile.station_site,evrIdent['EvrNum'])
        post_back_businessdate = 'VIEW-METER-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
      
      contents = {
                                                    "type": "bubble",
                                                    "direction": "ltr",
                                                    "hero": {
                                                      "type": "image",
                                                      "url": "https://www.susco.co.th/images/logo_susco.png",
                                                      "margin": "none",
                                                      "align": "start",
                                                      "gravity": "center",
                                                      "size": "full",
                                                      "aspectRatio": "22:6",
                                                      "aspectMode": "fit",
                                                      "backgroundColor": "#F2EC3EFF",
                                                      "action": {
                                                        "type": "uri",
                                                        "label": "SUSCO",
                                                        "uri": "https://www.susco.co.th/index.asp"
                                                      }
                                                    },
                                                    "body": {
                                                      "type": "box",
                                                      "layout": "vertical",
                                                      "contents": [
                                                        {
                                                          "type": "text",
                                                          "text": station_name,
                                                          "weight": "bold",
                                                          "size": "lg",
                                                          "align": "center",
                                                          "contents": []
                                                        },
                                                        
                                                        {
                                                          "type": "text",
                                                          "text": "เลือกรายการที่ต้องการ",
                                                          "weight": "bold",
                                                          "size": "lg",
                                                          "align": "center",
                                                          "contents": []
                                                        },
                                                        {
                                                          "type": "separator",
                                                          "margin": "lg"
                                                        },
                                                        {
                                                          "type": "box",
                                                          "layout": "horizontal",
                                                          "margin": "lg",
                                                          "contents": [
                                                            {
                                                              "type": "text",
                                                              "text": "Meter ปัจจุบัน",
                                                              "weight": "bold",
                                                              "size": "md",
                                                              "align": "start",
                                                              "gravity": "center",
                                                              "margin": "sm",
                                                              "contents": []
                                                            },
                                                            {
                                                              "type": "text",
                                                              "text": "เลือก",
                                                              "weight": "bold",
                                                              "size": "md",
                                                              "color": "#FA4204FF",
                                                              "align": "end",
                                                              "gravity": "center",
                                                              "margin": "sm",
                                                              "action": {
                                                                "type": "postback",
                                                                "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                                                                "data": post_back_last_shift
                                                              },
                                                              "contents": []
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "box",
                                                          "layout": "horizontal",
                                                          "margin": "lg",
                                                          "contents": [
                                                            {
                                                              "type": "text",
                                                              "text": "Meter ระบุวัน",
                                                              "weight": "bold",
                                                              "size": "md",
                                                              "align": "start",
                                                              "gravity": "center",
                                                              "margin": "sm",
                                                              "contents": []
                                                            },
                                                            {
                                                              "type": "text",
                                                              "text": "เลือก",
                                                              "weight": "bold",
                                                              "size": "sm",
                                                              "color": "#CA1F12FF",
                                                              "align": "end",
                                                              "gravity": "center",
                                                              "margin": "sm",
                                                              "action": {
                                                                "type": "datetimepicker",
                                                                "label": "test",
                                                                "data": post_back_businessdate,
                                                                "mode": "date",
                                                                "initial": today,
                                                                "max": today,
                                                                "min": new_date
                                                              },
                                                              "contents": []
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "type": "separator",
                                                          "margin": "lg"
                                                        }
                                                      ]
                                                    },
                                                    "footer": {
                                                      "type": "box",
                                                      "layout": "vertical",
                                                      "flex": 0,
                                                      "spacing": "sm",
                                                      "contents": [
                                                        {
                                                          "type": "text",
                                                          "text": "METER",
                                                          "weight": "bold",
                                                          "size": "lg",
                                                          "color": "#AA1C1CFF",
                                                          "align": "center",
                                                          "gravity": "top",
                                                          "wrap": True ,
                                                          "contents": []
                                                        }
                                                      ]
                                                    }
                                                  }
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": contents
                              }
      # print ('data is {}'.format(data))
      return True , data
    except Exception as e:
      print ('ไม่สามารถสร้างรายงานตัวเลือก ได้ เนื่องจาก {}'.format(e))
      return False , e
    
  def METER_Selecter_by_Multi_Site(self,user_profile,position):
    if position == 1 :
      print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการสาขสาขา')
      station_name = user_profile.station_name
      post_back_last_shift = 'VIEW-METER-SITE-NOW-SITE_ID{}END'.format(user_profile.station_site)
      post_back_businessdate = 'VIEW-METER-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
    elif position in (3,4,5) :
      print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการเขต')
      station_name = user_profile.station_name
      post_back_last_shift = 'VIEW-METER-SITE-NOW-SITE_ID{}END'.format(user_profile.station_site)
      post_back_businessdate = 'VIEW-METER-SITE-DAY-SITE_ID{}END'.format(user_profile.station_site)
    
    contents = {
  "type": "bubble",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "margin": "none",
    "align": "start",
    "gravity": "center",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "SUSCO",
      "uri": "https://www.susco.co.th/index.asp"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": station_name,
        "weight": "bold",
        "size": "lg",
        "align": "center",
        "contents": []
      },
      
      {
        "type": "text",
        "text": "เลือกรายการที่ต้องการ",
        "weight": "bold",
        "size": "lg",
        "align": "center",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "Meter ปัจจุบัน",
            "weight": "bold",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
              "data": post_back_last_shift
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "Meter ระบุวัน",
            "weight": "bold",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "md",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งตัวเ",
              "data": post_back_businessdate
            },
            "contents": []
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "text",
        "text": "METER",
        "weight": "bold",
        "size": "lg",
        "color": "#AA1C1CFF",
        "align": "center",
        "gravity": "top",
        "wrap": True ,
        "contents": []
      }
    ]
  }
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
    

  def METER_Last_Shift(self,station_detail,METER_Last_Shift,report_type):
    
    try :

      #ส่วนค้นหาขายรวมของ Meter ทั้งหมด
      All_meter = 0
      for total_nozzle in METER_Last_Shift:
        try :
          sum_start_end =  total_nozzle['End_Volume'] - total_nozzle['Stat_Volume']
          All_meter += sum_start_end
        except :
          sum_start_end = float(0.00)
          All_meter += sum_start_end
      #ส่วนค้นหารายละเอียดสาขา ด้วยการวน loop แค่ loop แรกเท่านั้น
      for shift_detail in METER_Last_Shift:
        try :
          day_of_shift = shift_detail['Businessdate']
          break
        except Exception as e: 
          day_of_shift = 'None'
          shift_close_time = 'None'
          if station_detail.debug_mode == True :
            message = ('สถานี {}'.format(station_detail.station_name) + '\n' + 'ข้อผิดพลาด : ' + str(e))
            db_logger.warning(message)
            db_logger.exception(e)
      contents =    {
              "type": "carousel",
              "contents": [
                {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://www.susco.co.th/images/logo_susco.png",
                    "margin": "none",
                    "align": "start",
                    "gravity": "center",
                    "size": "full",
                    "aspectRatio": "22:6",
                    "aspectMode": "fit",
                    "backgroundColor": "#F2EC3EFF",
                    "action": {
                      "type": "uri",
                      "label": "SUSCO",
                      "uri": "https://www.susco.co.th/index.asp"
                    }
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "สถานี : {}".format(station_detail.station_name),
                        "weight": "bold",
                        "size": "sm",
                        "wrap": True,
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "รายงานตัวเลข Pump Totalizer",
                        "weight": "bold",
                        "size": "sm",
                        "align": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "Businessdate :  {}".format(day_of_shift),
                        "weight": "bold",
                        "size": "xs",
                        "align": "start",
                        "contents": []
                      },
                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#111505FF"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Product",
                            "weight": "bold",
                            "size": "xs",
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "Total",
                            "weight": "bold",
                            "size": "xs",
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "Price",
                            "weight": "bold",
                            "size": "xs",
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          }
                        ]
                      },
                      # ส่วนแสดงผลสรุปรวมตามชนิดน้ำมันด้วยการวน loop ข้อมูล

                      {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#111505FF"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "contents": [
                          {
                            "type": "text",
                            "text": "รวมยอดทั้งหมด",
                            "weight": "bold",
                            "align": "center",
                            "gravity": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "{:.2f}".format(All_meter),
                            "weight": "bold",
                            "size": "3xl",
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "ลิตร",
                            "weight": "bold",
                            "align": "center",
                            "gravity": "center",
                            "contents": []
                          }
                        ]
                      }
                    ]
                  }
                }
                
    
  ]
      }
      # ส่วนของการวน loop เพื่อรวมชนิดน้ำมัน
      product_lable = []
      product_sum = []
      shift_store = []
      total_shift = []
      for product in METER_Last_Shift:
        # loop หาน้ำมันแต่ละชนิด
        if product['Product'] not in product_lable:
          product_lable.append(product['Product'])
          data = {'Product': product['Product'], 'Total': 0, 'Price': product['Price']}
          product_sum.append(data)
      for shift_loop in METER_Last_Shift:
        if shift_loop['ShiftNo'] not in shift_store:
          shift_store.append(int(shift_loop['ShiftNo']))
          data = {'ShiftNo': shift_loop['ShiftNo'], 'Businessdate': shift_loop['Businessdate'] ,'CloseShiftDate': shift_loop['CloseShiftDate'],'CloseShiftTime': shift_loop['CloseShiftTime']}
          total_shift.append(data)
      # ทำการ loop เพื่อรวมจำนวนชนิดน้ำมัน
      for sum_of_nozzle in METER_Last_Shift:
        for product in product_sum:
          if sum_of_nozzle['Product'] == product['Product']:
            print (sum_of_nozzle)
            try :
              result_sum_nozzle =  sum_of_nozzle['End_Volume'] - sum_of_nozzle['Stat_Volume']
              product['Total'] += result_sum_nozzle
            except :
              result_sum_nozzle = float(0.00)
              product['Total'] += result_sum_nozzle
      print (product_lable)
      print (product_sum)
      print (total_shift)
      # นำข้อมูลที่เสร็จแล้วจาก product_sum มาทำการ loop อีกครั้ง
      for show_product in product_sum:
        product_sum = {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": show_product['Product'],
                            "size": "xxs",
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "{:.2f}".format(show_product['Total']),
                            "size": "xxs",
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": show_product['Price'],
                            "size": "xxs",
                            "align": "center",
                            "gravity": "center",
                            "margin": "sm",
                            "contents": []
                          }
                        ]
                      }
        contents["contents"][0]['body']['contents'].insert(-2,product_sum)
      
      
      #--------------------------------------------------------------------#
      # ส่วนแสดงข้อมูล Meter ที่ละกะ  
      # คำนวนหารายละเอียดของกะ โดยการวน loop แรก เท่านั้น
      for loop_shitf_id in total_shift:
        print ('loop_shitf_id',loop_shitf_id)
        try :
              day_of_shift = loop_shitf_id['Businessdate']
              shift_close_day = loop_shitf_id['CloseShiftDate']
              shift_close_time = loop_shitf_id['CloseShiftTime']
              shift_number = loop_shitf_id['ShiftNo']     
        except Exception as e: 
          day_of_shift = 'None'
          shift_close_day = 'None'
          shift_close_time = 'None'
          if station_detail.debug_mode == True :
            message = ('สถานี {}'.format(station_detail.station_name) + '\n' + 'ข้อผิดพลาด : ' + str(e))
            db_logger.warning(message)
            db_logger.exception(e)
        part_of_nozzle = {
                        "type": "bubble",
                        "direction": "ltr",
                        "hero": {
                          "type": "image",
                          "url": "https://www.susco.co.th/images/logo_susco.png",
                          "margin": "none",
                          "align": "start",
                          "gravity": "center",
                          "size": "full",
                          "aspectRatio": "22:6",
                          "aspectMode": "fit",
                          "backgroundColor": "#F2EC3EFF",
                          "action": {
                            "type": "uri",
                            "label": "SUSCO",
                            "uri": "https://www.susco.co.th/index.asp"
                          }
                        },
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "รายงานตัวเลข Pump Totalizer",
                              "weight": "bold",
                              "size": "sm",
                              "align": "center",
                              "contents": []
                            },
                            {
                              "type": "text",
                              "text": "Businessdate :  {}".format(day_of_shift),
                              "weight": "bold",
                              "size": "xs",
                              "align": "start",
                              "contents": []
                            },
                            {
                              "type": "text",
                              "text": "CloseShiftDate :  {}".format(shift_close_day),
                              "weight": "bold",
                              "size": "xs",
                              "align": "start",
                              "contents": []
                            },
                            {
                              "type": "text",
                              "text": "CloseShiftTime : {}".format(shift_close_time),
                              "weight": "bold",
                              "size": "xs",
                              "align": "start",
                              "contents": []
                            },
                            {
                              "type": "text",
                              "text": "ShiftNumber (Sft) :  {}".format(shift_number),
                              "weight": "bold",
                              "size": "xs",
                              "align": "start",
                              "contents": []
                            },
                            {
                              "type": "separator",
                              "margin": "lg",
                              "color": "#111505FF"
                            },
                            {
                              "type": "box",
                              "layout": "horizontal",
                              "margin": "lg",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "Sft",
                                  "weight": "bold",
                                  "size": "xs",
                                  "align": "center",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "contents": []
                                },
                                {
                                  "type": "text",
                                  "text": "Pup",
                                  "weight": "bold",
                                  "size": "xs",
                                  "align": "center",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "contents": []
                                },
                                {
                                  "type": "text",
                                  "text": "Noz",
                                  "weight": "bold",
                                  "size": "xs",
                                  "align": "center",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "contents": []
                                },
                                {
                                  "type": "text",
                                  "text": "Start",
                                  "weight": "bold",
                                  "size": "xs",
                                  "flex": 2,
                                  "align": "center",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "contents": []
                                },
                                {
                                  "type": "text",
                                  "text": "End",
                                  "weight": "bold",
                                  "size": "xs",
                                  "flex": 2,
                                  "align": "center",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "contents": []
                                },
                                {
                                  "type": "text",
                                  "text": "Sum",
                                  "weight": "bold",
                                  "size": "xs",
                                  "align": "end",
                                  "gravity": "center",
                                  "margin": "sm",
                                  "contents": []
                                }
                              ]
                            },
                            
                            # ส่วนแสดงผลข้อมูลมือจ่าย
                            
                            
                            {
                              "type": "separator",
                              "margin": "lg",
                              "color": "#111505FF"
                            }
                            
                          ]
                        }
                      }
        # วนลูปข้อมูลมือจ่ายโดยเลือก shiftID ให้ตรงกัน
        All_meter = 0
        for nozzle_detail in METER_Last_Shift :
          if nozzle_detail['ShiftNo'] == loop_shitf_id['ShiftNo']:
            store_all_sum_meter = 0
            try :
              sum_of_start_end =  nozzle_detail['End_Volume'] - nozzle_detail['Stat_Volume']
              store_all_sum_meter += sum_of_start_end
              All_meter += sum_of_start_end
            except :
              sum_of_start_end = float(0.00)
              store_all_sum_meter += sum_of_start_end
              All_meter += sum_of_start_end
            total_meter_sum_in_Shift = {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "contents": [
                          {
                            "type": "text",
                            "text": "รวม {} ลิตร".format("{:.2f}".format(All_meter)),
                            "weight": "bold",
                            "align": "center",
                            "gravity": "center",
                            "contents": []
                          },
                          
                          
                        ]
                      }
            past_of_nozzle_detail = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": str(nozzle_detail['ShiftNo']),
                "size": "xxs",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": str(nozzle_detail['PumpNo']),
                "size": "xxs",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": str(nozzle_detail['NozNo']),
                "size": "xxs",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "{:.0f}".format(nozzle_detail['Stat_Volume']),
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "{:.0f}".format(nozzle_detail['End_Volume']),
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "{:.0f}".format(store_all_sum_meter),
                "size": "xxs",
                "flex": 1,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
              
            ]
          }
            # part_of_nozzle["body"]['contents'].insert(-1,total_meter_sum_in_Shift)
            part_of_nozzle["body"]['contents'].insert(-1,past_of_nozzle_detail)
            
            

            # part_of_nozzle["body"]['contents'].insert(-1,total_meter_sum_in_Shift)
        part_of_nozzle["body"]['contents'].append(total_meter_sum_in_Shift)
        contents["contents"].append(part_of_nozzle)
      
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": contents
                              }
      
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ '.format(report_type))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,report_type)
      return True
    except Exception as e:
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ ปัญหา {}'.format(report_type,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
  def METER_Date_Selecter(self,station_detail,result_pos,date_from_line,report_type):
    # print ('type 0f data_from_line {} จำนวน'.format(type(result_pos[1])))
    # print ('len 0f data_from_line {} จำนวน'.format(len(result_pos[1])))
    # คำนวณหาจำนวนกะ เพราะถ้าเกิน 4 กะ อาจจะส่ง flex ไม่ได้ เนื่องจาก line จำกัดที่ 2000 ตัวอักษร
    data_len = len(result_pos[1])
    print ('data_len {} จำนวน'.format(data_len))
   
    try:
      
      date_time_str = date_from_line
      date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
      print ('date_time_obj xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx {}'.format(date_time_obj))
      
      contents = {
                          "type": "carousel",
                          "contents": [
                            
                            
                          ]
                        }
      
      
      for data in result_pos[1] :
        if 'z' not in data['EvrNum'] :
          if data['EvrInsTim'] != None:
            print ('วันที่ {}'.format(data))
            print ('ข้อมูล Meter ตามรายการ ID {} ')
            EOD_date = data['EvrTarih'].strftime('%d-%m-%Y %H:%M')
            date_end_shift = data['EvrInsTim'].strftime('%d-%m-%Y %H:%M')
            post_back = 'VIEW-METER-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(station_detail.station_site,data['EvrNum'])
            # post_back2 = 'VIEW-METER-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(station_detail.station_site,data['EvrNum'][:-2])
            # if data_len >= 4 :
            #   label =  "แสดงทุกกะ"
            #   text = "ข้อความระบบ : ไม่สามารถแสดงรายงานได้เนื่องจากจำนวนกะเกิน 3 กะ เกิน Limit ของข้อจำกัดของ Line กรุณาเลือกการแสดงผลที่ละกะ"
            #   # text = "ข้อความระบบ : xxxxxxxxxxxxxxxxxx",
            #   postback2 = 'post_back'
            # elif data_len <= 3 :
            label =  "แสดงทุกกะ"
            text = "ข้อความระบบ : กำลังจัดส่งข้อมูล Meter ของกะที่ต้องการ"
            postback2 = 'VIEW-METER-SITE-NOW-SITE_ID{}TRANSCETION{}END'.format(station_detail.station_site,data['EvrNum'][:-2])

            # print ('วันที่เริ่มต้นรายงาน {}'.format(date_start_x_report))
            report_id = data['EvrNum'][9:]

            
            
            detail = {
                                    "type": "bubble",
                                    "direction": "ltr",
                                    "hero": {
                                      "type": "image",
                                      "url": "https://www.susco.co.th/images/logo_susco.png",
                                      "margin": "none",
                                      "align": "start",
                                      "gravity": "center",
                                      "size": "full",
                                      "aspectRatio": "22:6",
                                      "aspectMode": "fit",
                                      "backgroundColor": "#F2EC3EFF",
                                      "action": {
                                        "type": "uri",
                                        "label": "SUSCO",
                                        "uri": "https://www.susco.co.th/index.asp"
                                      }
                                    },
                                    "body": {
                                      "type": "box",
                                      "layout": "vertical",
                                      "contents": [
                                        {
                                          "type": "text",
                                          "text": "สาขา {}".format(station_detail.station_name),
                                          "weight": "bold",
                                          "size": "md",
                                          "wrap": True,
                                          "align": "center",
                                          "contents": []
                                        },
                                        {
                                          "type": "text",
                                          "text": "รายละเอียดรอบปิดกะ",
                                          "weight": "bold",
                                          "size": "md",
                                          "align": "center",
                                          "margin": "sm",
                                          "contents": []
                                        },
                                        {
                                          "type": "text",
                                          "text": "วันที่ปิดวัน {}".format(EOD_date),
                                          "weight": "bold",
                                          "size": "md",
                                          "align": "center",
                                          "margin": "sm",
                                          "contents": []
                                        },
                                        {
                                          "type": "separator",
                                          "margin": "lg"
                                        },
                                        {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "margin": "lg",
                                          "contents": [
                                            {
                                              "type": "text",
                                              "text": "รอบกะที่ ",
                                              "weight": "bold",
                                              "size": "sm",
                                              "flex": 5,
                                              "align": "start",
                                              "gravity": "center",
                                              "margin": "sm",
                                              "contents": []
                                            },
                                            {
                                              "type": "text",
                                              "text": str(report_id),
                                              "weight": "bold",
                                              "size": "sm",
                                              "flex": 6,
                                              "align": "end",
                                              "gravity": "center",
                                              "margin": "sm",
                                              "contents": []
                                            }
                                          ]
                                        },
                                        {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "margin": "lg",
                                          "contents": [
                                            {
                                              "type": "text",
                                              "text": "วันที่ปิดกะ",
                                              "weight": "bold",
                                              "size": "sm",
                                              "flex": 5,
                                              "align": "start",
                                              "gravity": "center",
                                              "margin": "sm",
                                              "contents": []
                                            },
                                            {
                                              "type": "text",
                                              "text": date_end_shift,
                                              "weight": "bold",
                                              "size": "sm",
                                              "flex": 6,
                                              "align": "end",
                                              "gravity": "center",
                                              "margin": "sm",
                                              "contents": []
                                            }
                                          ]
                                        },
                                        
                                        {
                                          "type": "separator",
                                          "margin": "lg"
                                        }
                                      ]
                                    },
                                    "footer": {
                                      "type": "box",
                                      "layout": "vertical",
                                      "flex": 0,
                                      "spacing": "sm",
                                      "contents": [
                                        {
                                          "type": "text",
                                          "text": "METER",
                                          "weight": "bold",
                                          "size": "lg",
                                          "color": "#AA1C1CFF",
                                          "align": "center",
                                          "gravity": "top",
                                          "wrap": True,
                                          "contents": []
                                        },
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "postback",
                                            "label": "เลือกรายงานกะนี้",
                                            "text": "ข้อความระบบ : กำลังจัดส่งรายละเอียด Meter กะที่ {}".format(report_id),
                                            "data": post_back
                                          },
                                          "color": "#078025FF",
                                          "style": "secondary"
                                        },
                                        {
                                          "type": "button",
                                          "action": {
                                            "type": "postback",
                                            "label":label,
                                            "text": text,
                                            "data": postback2
                                          },
                                          "color": "#078025FF",
                                          "style": "secondary"
                                        }
                                      ]
                                    }
                                  }
            contents["contents"].append(detail)
        
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": contents
                              }
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ '.format(report_type))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,report_type)
      return True
    except Exception as e:
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ ปัญหา {}'.format(report_type,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
    
  def Meter_Date_Detail_Select(self,station_detail):
    
    shift_1_post_back = 'VIEW-METER-SHIFT{}ID{}END'.format('1',station_detail.station_site)
    shift_2_post_back = 'VIEW-METER-SHIFT{}ID{}END'.format('2',station_detail.station_site)
    shift_3_post_back = 'VIEW-METER-SHIFT{}ID{}END'.format('3',station_detail.station_site)
    shift_4_post_back = 'VIEW-METER-SHIFT{}ID{}END'.format('4',station_detail.station_site)
    shift_99_post_back = 'VIEW-METER-SHIFT{}ID{}END'.format('99',station_detail.station_site)
    contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "สาขา {}".format(station_detail.station_name),
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  SHIFT 1 ",
                      "data": shift_1_post_back
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT SHIFT 2 ",
                      "data": shift_2_post_back
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT SHIFT 3 ",
                      "data": shift_3_post_back
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ALL-SHIFT ",
                      "data": shift_99_post_back
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "METER",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT SHIFT 1",
                      "data": shift_1_post_back
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  SHIFT 2",
                      "data": shift_2_post_back
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  SHIFT 3",
                      "data": shift_3_post_back
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ALL SHIFT",
                      "data": shift_99_post_back
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดกะที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "วันที่ 22-03-2022",
                "weight": "bold",
                "size": "md",
                "align": "center",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 1",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 2",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Shift 3",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "All-Shift",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Total",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกวันที่อื่นๆ เพิ่มเติม",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "position": "relative",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "เลือกวันอื่นๆ",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล XREPORT  ปัจจุบัน",
                      "data": "NOW-XREPORT"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "X - REPORT",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True  ,
            "contents": []
          }
        ]
      }
    }
  ]
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
  def METER_Date_Selecter_Area(self,user_id):

    contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "สน.ซัสโก้.สาขา ป่าซาง",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดวันที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "22-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "21-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "20-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "19-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "18-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "17-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "16-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "15-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "14-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "13-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "METER READING",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เลือกรายการรอบปิดวันที่ต้องการ",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "12-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "11-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "10-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "09-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "08-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "07-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "06-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "05-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "04-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "03-03-2022",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "เลือก",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FA4204FF",
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "action": {
                      "type": "postback",
                      "text": "ข้อความระบบ : กำลังจัดส่งข้อมูล METER ปัจจุบัน",
                      "data": "NOW-METER-DATE-22-03-2022"
                    },
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "METER READING",
            "weight": "bold",
            "size": "lg",
            "color": "#AA1C1CFF",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          }
        ]
      }
    }
  ]
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
  def PRICE (self,user_profile,position,PRICE,report_type):
    try : 
      # if position == 1 :
      #   print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการสาขสาขา')
      #   station_name = user_profile.userList_station_name.station_name
        
      # elif position in (3,4,5) :
      #   print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการเขต')
      #   station_name = user_profile.station_name
      station_name = user_profile
      dt = datetime.now().strftime("%d-%m-%Y %H:%M") 
      contents =  {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://www.susco.co.th/images/logo_susco.png",
          "margin": "none",
          "align": "start",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "22:6",
          "aspectMode": "fit",
          "backgroundColor": "#F2EC3EFF",
          "action": {
            "type": "uri",
            "label": "SUSCO",
            "uri": "https://www.susco.co.th/index.asp"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ราคาน้ำมันซัสโก้ปัจจุบัน",
              "weight": "bold",
              "size": "lg",
              "align": "center",
              "contents": []
            },
            {
              "type": "text",
              "text": "สาขา {}".format(station_name),
              "weight": "bold",
              "size": "lg",
              "wrap": True,
              "align": "center",
              "contents": []
            },
            {
              "type": "separator",
              "margin": "lg"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "margin": "lg",
              "contents": [
                {
                  "type": "text",
                  "text": "Product",
                  "weight": "bold",
                  "size": "xs",
                  "align": "start",
                  "gravity": "center",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "CurrentPrice",
                  "weight": "bold",
                  "size": "xs",
                  "align": "end",
                  "gravity": "center",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "PriceChange",
                  "weight": "bold",
                  "size": "xs",
                  "align": "end",
                  "gravity": "center",
                  "margin": "sm",
                  "contents": []
                }
              ]
            }
            # ส่วนแสดงราคาน้ำมัน 1
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "หมายเหตุ : ราคาน้ำมันตรวจสอบจากระบบ POS",
              "size": "xs",
              "align": "center",
              "gravity": "center",
              "wrap": True,
              "contents": []
            },
            {
              "type": "text",
              "text": "ณ เวลา {}".format(dt),
              "size": "xs",
              "align": "center",
              "gravity": "center",
              "wrap": True,
              "contents": []
            }
          ]
        }
      },
      # ส่วนหน้าที่ 2
      {
        "type": "bubble",
        "direction": "ltr",
        "hero": {
          "type": "image",
          "url": "https://www.susco.co.th/images/logo_susco.png",
          "margin": "none",
          "align": "start",
          "gravity": "center",
          "size": "full",
          "aspectRatio": "22:6",
          "aspectMode": "fit",
          "backgroundColor": "#F2EC3EFF",
          "action": {
            "type": "uri",
            "label": "SUSCO",
            "uri": "https://www.susco.co.th/index.asp"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "สาขา {}".format(station_name),
              "weight": "bold",
              "size": "lg",
              "align": "center",
              "wrap": True,
              "contents": []
            },
            {
              "type": "text",
              "text": "ราคาน้ำมันย้อนหลัง",
              "weight": "bold",
              "size": "lg",
              "align": "center",
              "contents": []
            },
            {
              "type": "separator",
              "margin": "lg"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "margin": "lg",
              "contents": [
                {
                  "type": "text",
                  "text": "Previous",
                  "weight": "bold",
                  "size": "xs",
                  "align": "start",
                  "gravity": "center",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "Doc",
                  "weight": "bold",
                  "size": "xs",
                  "align": "start",
                  "gravity": "center",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "Created",
                  "weight": "bold",
                  "size": "xs",
                  "gravity": "center",
                  "margin": "sm",
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "Activated",
                  "weight": "bold",
                  "size": "xs",
                  "align": "end",
                  "gravity": "center",
                  "margin": "sm",
                  "contents": []
                }
              ]
            }
            # ส่วนแสดงประวัติราคาน้ำมัน
            
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "หมายเหตุ : ราคาน้ำมันตรวจสอบจากระบบ POS",
              "size": "xs",
              "align": "center",
              "gravity": "center",
              "wrap": True,
              "contents": []
            },
            {
              "type": "text",
              "text": "ณ เวลา {}".format(dt),
              "size": "xs",
              "align": "center",
              "gravity": "center",
              "wrap": True,
              "contents": []
            }
          ]
        }
      }
    ]
  }
      for price_detail in PRICE :
        price_detail_1 = {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "none",
                        "contents": [
                          {
                            "type": "text",
                            "text": price_detail["StokKod"],
                            "size": "xxs",
                            "flex": 4,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": str(price_detail["CurrentPrice"]),
                            "size": "xxs",
                            "flex": 2,
                            "align": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "ตั้งเวลา",
                            "size": "xxs",
                            "flex": 2,
                            "align": "center",
                            "contents": []
                          }
                        ]
                      }
        price_detail_2 = {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "{:.2f}".format(price_detail["PreviousPrice"]),
                    "size": "xxs",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "{:.2f}".format(price_detail["PriceInDoc"]),
                    "size": "xxs",
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": price_detail['DocumentCreatedDate'].strftime("%d-%m-%y %H:%M"),
                    "size": "xxs",
                    "flex": 2,
                    "align": "start",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": price_detail['ActivateDateTime'].strftime("%d-%m-%y %H:%M"),
                    "size": "xxs",
                    "flex": 2,
                    "align": "end",
                    "gravity": "center",
                    "margin": "sm",
                    "contents": []
                  }
                ]
              }
        
        contents['contents'][0]['body']['contents'].append(price_detail_1)
        contents['contents'][1]['body']['contents'].append(price_detail_2)
      data = {
                "type": "flex",
                "altText": 'message',
                "contents": contents
                              }
      print ('สร้าง Flex Message สำหรับรายงาน {} สำเร็จ ข้อมูลรายงาน สาขา {} '.format('PRICE',station_name))
      SendFlexMessages(self.payload).ReplyMessageToUser(self.reply_token,data,'PRICE')
    except Exception as e:
      print ('ไม่สามารถสร้างรายงาน {} ได้ เนื่องจาก {}'.format(report_type,e))
      messages=('สร้าง Flex Message สำหรับรายงาน {} ไม่สำเร็จ  ชื่อสาขา {} ปัญหา {}'.format(report_type,station_name,str(e)))
      db_logger.warning(messages)
      return SendFlexMessages(self.payload).ReplyTextMessage(self.reply_token,messages,report_type)
  def PRICE_Muti (self,user_profile,position):

    if position == 1 :
      print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการสาขสาขา')
      station_name = user_profile.station_name
      
    elif position in (3,4,5) :
      print ('ส่วนติดต่อฐานข้อมูล POS สำหรับผู้จัดการเขต')
      station_name = user_profile.station_name

     
    contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": station_name,
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "contents": []
          },
          {
            "type": "text",
            "text": "ราคาน้ำมันซัสโก้ปัจจุบัน",
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "Product",
                "weight": "bold",
                "size": "xs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "CurrentPrice",
                "weight": "bold",
                "size": "xs",
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "PriceChange",
                "weight": "bold",
                "size": "xs",
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Diesel B7",
                "size": "xxs",
                "flex": 4,
                "contents": []
              },
              {
                "type": "text",
                "text": "28.19",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              },
              {
                "type": "text",
                "text": "ตั้งเวลา",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "none",
            "contents": [
              {
                "type": "text",
                "text": "Diesel",
                "size": "xxs",
                "flex": 4,
                "contents": []
              },
              {
                "type": "text",
                "text": "28.19",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              },
              {
                "type": "text",
                "text": "ตั้งเวลา",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "none",
            "contents": [
              {
                "type": "text",
                "text": "Extra Gasohol E20",
                "size": "xxs",
                "flex": 4,
                "contents": []
              },
              {
                "type": "text",
                "text": "29.19",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              },
              {
                "type": "text",
                "text": "ตั้งเวลา",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "none",
            "contents": [
              {
                "type": "text",
                "text": "Super Gasohol 95",
                "size": "xxs",
                "flex": 4,
                "contents": []
              },
              {
                "type": "text",
                "text": "30.07",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              },
              {
                "type": "text",
                "text": "ตั้งเวลา",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "none",
            "contents": [
              {
                "type": "text",
                "text": "Premium Diesel B7",
                "size": "xxs",
                "flex": 4,
                "contents": []
              },
              {
                "type": "text",
                "text": "34.71",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              },
              {
                "type": "text",
                "text": "ตั้งเวลา",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "none",
            "contents": [
              {
                "type": "text",
                "text": "Premium Gasohol 95",
                "size": "xxs",
                "flex": 4,
                "contents": []
              },
              {
                "type": "text",
                "text": "38.19",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              },
              {
                "type": "text",
                "text": "ตั้งเวลา",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "none",
            "contents": [
              {
                "type": "text",
                "text": "Premium Gasohol 91",
                "size": "xxs",
                "flex": 4,
                "contents": []
              },
              {
                "type": "text",
                "text": "30.43",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              },
              {
                "type": "text",
                "text": "ตั้งเวลา",
                "size": "xxs",
                "flex": 2,
                "align": "center",
                "contents": []
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "หมายเหตุ : ราคาน้ำมันตรวจสอบจากระบบ POS",
            "size": "xs",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          },
          {
            "type": "text",
            "text": "ณ เวลา 02-04-21 15:00",
            "size": "xs",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          }
        ]
      }
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "hero": {
        "type": "image",
        "url": "https://www.susco.co.th/images/logo_susco.png",
        "margin": "none",
        "align": "start",
        "gravity": "center",
        "size": "full",
        "aspectRatio": "22:6",
        "aspectMode": "fit",
        "backgroundColor": "#F2EC3EFF",
        "action": {
          "type": "uri",
          "label": "SUSCO",
          "uri": "https://www.susco.co.th/index.asp"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "ราคาน้ำมันย้อนหลัง",
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "contents": []
          },
          {
            "type": "separator",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "lg",
            "contents": [
              {
                "type": "text",
                "text": "Previous",
                "weight": "bold",
                "size": "xs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "Doc",
                "weight": "bold",
                "size": "xs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "Created",
                "weight": "bold",
                "size": "xs",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "Activated",
                "weight": "bold",
                "size": "xs",
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "28.69",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "28.19",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "21/12/21 04:21",
                "size": "xxs",
                "flex": 2,
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "22/12/21 05:00",
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "28.69",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "28.19",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "21/12/21 04:21",
                "size": "xxs",
                "flex": 2,
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "22/12/21 05:00",
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "29.49",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "29.19",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "21/12/21 04:21",
                "size": "xxs",
                "flex": 2,
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "22/12/21 05:00",
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "31.00",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "30.70",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "21/12/21 04:21",
                "size": "xxs",
                "flex": 2,
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "22/12/21 05:00",
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "35.21",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "34.71",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "21/12/21 04:21",
                "size": "xxs",
                "flex": 2,
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "22/12/21 05:00",
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "38.49",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "38.19",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "21/12/21 04:21",
                "size": "xxs",
                "flex": 2,
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "22/12/21 05:00",
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "30.73",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "30.43",
                "size": "xxs",
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "21/12/21 04:21",
                "size": "xxs",
                "flex": 2,
                "align": "start",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              },
              {
                "type": "text",
                "text": "22/12/21 05:00",
                "size": "xxs",
                "flex": 2,
                "align": "end",
                "gravity": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "หมายเหตุ : ราคาน้ำมันตรวจสอบจากระบบ POS",
            "size": "xs",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          },
          {
            "type": "text",
            "text": "ณ เวลา 02-04-21 15:00",
            "size": "xs",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "contents": []
          }
        ]
      }
    }
  ]
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
  def PRICE_Area(self,user_id):
    contents = {
  "type": "bubble",
  "direction": "ltr",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "margin": "none",
    "align": "start",
    "gravity": "center",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "SUSCO",
      "uri": "https://www.susco.co.th/index.asp"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "เลือกสถานีที่ต้องการ",
        "weight": "bold",
        "size": "lg",
        "align": "center",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "สน.ซัสโก้.สาขา ป่าซาง",
            "weight": "bold",
            "size": "xs",
            "flex": 5,
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "sm",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
              "data": "AREA-PRICE-SITE5001"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "สน.ซัสโก้.สาขา บางระกำ",
            "weight": "bold",
            "size": "xs",
            "flex": 5,
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "sm",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
              "data": "AREA-PRICE-SITE5001"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "สน.ซัสโก้.สาขา วังทรายพูน",
            "weight": "bold",
            "size": "xs",
            "flex": 5,
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "sm",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
              "data": "AREA-PRICE-SITE5001"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "lg",
        "contents": [
          {
            "type": "text",
            "text": "สน.ซัสโก้.สาขา ดีลเลอร์ส สันทราย",
            "weight": "bold",
            "size": "xs",
            "flex": 5,
            "align": "start",
            "gravity": "center",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "เลือก",
            "weight": "bold",
            "size": "sm",
            "color": "#FA4204FF",
            "align": "end",
            "gravity": "center",
            "margin": "sm",
            "action": {
              "type": "postback",
              "text": "ข้อความระบบ : กำลังจัดส่งตัวเลือกข้อมูลสาขา",
              "data": "AREA-PRICE-SITE5001"
            },
            "contents": []
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "text",
        "text": "ราคาน้ำมันปัจจุบัน",
        "weight": "bold",
        "size": "lg",
        "color": "#AA1C1CFF",
        "align": "center",
        "gravity": "top",
        "wrap": True,
        "contents": []
      }
    ]
  }
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
  def DetailArea(self,user_id):
    contents = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "สน.ซัสโก้.สาขา ป่าซาง",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "รายละเอียดผู้จัดการเขต",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "ไม่พบข้อมูลผู้จัดการ",
        "weight": "bold",
        "color": "#D01E11FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ตั้งค่าผู้จัดการเขต",
          "text": "รอสักครู่ กำลังจัดส่งข้อมูล",
          "data": "ADDAREA"
        },
        "color": "#078025FF",
        "margin": "none",
        "height": "sm",
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "ติดต่อผู้จัดการเขต",
          "text": "กรุณาติดต่อ CBRE เพื่อยืนยันอีกครั้ง",
          "data": "NOK"
        },
        "color": "#706C6CFF",
        "height": "sm",
        "style": "primary"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
  def AreaList(self,area_detail):
    
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": {
  "type": "carousel",
  "contents": [
    
    
  ]
}
                            }
# สร้างข้อมูลผู้จัดการเขตแล้วนำไป appendใส่ใน contents
    for i in area_detail :
      area_data = {
              "type": "bubble",
              "hero": {
                "type": "image",
                "url": "https://www.susco.co.th/images/logo_susco.png",
                "align": "center",
                "gravity": "bottom",
                "size": "full",
                "aspectRatio": "22:6",
                "aspectMode": "fit",
                "backgroundColor": "#F2EC3EFF",
                "action": {
                  "type": "uri",
                  "label": "Line",
                  "uri": "https://linecorp.com/"
                },
                "position": "relative"
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "separator",
                    "margin": "lg",
                    "color": "#E42424FF"
                  },
                  {
                    "type": "text",
                    "text": "รายละเอียดผู้จัดการเขต",
                    "weight": "bold",
                    "color": "#293CCDFF",
                    "align": "center",
                    "margin": "lg",
                    "wrap": True,
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": i.user_display_name,
                    "weight": "bold",
                    "color": "#1142D0FF",
                    "align": "center",
                    "margin": "lg",
                    "contents": []
                  },
                  {
                    "type": "image",
                    "url": i.user_picture_url,
                    "margin": "md"
                  },
                  {
                    "type": "separator",
                    "margin": "lg",
                    "color": "#E42424FF"
                  }
                ]
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "flex": 0,
                "spacing": "sm",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "postback",
                      "label": "เลือกผู้จัดการเขต",
                      "text": "ข้อมูลระบบ : ท่านเลือกผู้จัดการเขต คุณ " + str(i.user_display_name),
                      "data": "SAVEAREAID" + str(i.id)
                    },
                    "color": "#078025FF",
                    "margin": "none",
                    "height": "sm",
                    "style": "secondary"
                  },
                  {
                    "type": "spacer",
                    "size": "sm"
                  }
                ]
              }
            }
      data['contents']['contents'].append(area_data)

    return data
  def AreaLinsNotFlund(self):
    contents = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": "รายละเอียดผู้จัดการเขต",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "ไม่พบข้อมูลผู้จัดการ",
        "weight": "bold",
        "color": "#D01E11FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "text",
        "text": "ระบบค้นหาไม่พบรายละเอียดผู้จัดการเขต ",
        "weight": "bold",
        "size": "sm",
        "align": "center",
        "gravity": "center",
        "wrap": True,
        "contents": []
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": contents
                            }
    return data
  def AreaForStation(self,user_area):
    data = {
              "type": "flex",
              "altText": 'message',
              "contents": {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.susco.co.th/images/logo_susco.png",
    "align": "center",
    "gravity": "bottom",
    "size": "full",
    "aspectRatio": "22:6",
    "aspectMode": "fit",
    "backgroundColor": "#F2EC3EFF",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://linecorp.com/"
    },
    "position": "relative"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      },
      {
        "type": "text",
        "text": user_area.user_station_name.station_name,
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": "รายละเอียดผู้จัดการเขต",
        "weight": "bold",
        "color": "#293CCDFF",
        "align": "center",
        "margin": "lg",
        "wrap": True,
        "contents": []
      },
      {
        "type": "text",
        "text": user_area.user_area.user_display_name,
        "weight": "bold",
        "color": "#1132D0FF",
        "align": "center",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "image",
        "url": user_area.user_area.user_picture_url,
        "margin": "md"
      },
      {
        "type": "separator",
        "margin": "lg",
        "color": "#E42424FF"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "text",
        "text": "รายละเอียดผู้จัดการเขต",
        "weight": "bold",
        "color": "#2D12F0FF",
        "align": "center",
        "gravity": "center",
        "margin": "none",
        "contents": []
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
                            }
    return data






















