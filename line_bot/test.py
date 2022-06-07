data = {
                                  "type": "flex",
                                  "altText": 'message',
                                  "contents": 
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
                            "text": "X - REPORT",
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

print(data['contents']['body'])