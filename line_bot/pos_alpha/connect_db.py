import pymssql
server = '0.tcp.ngrok.io:15124'
time_out = 20
class ConnectDBAlphaPOS :
    def __init__ (self,station_detail) :
        self.station_NAME = station_detail.station_name
        self.station_IP = station_detail.station_ip_address
        self.station_PORT = station_detail.station_port_number
        self.station_DB = station_detail.station_db_databasename
        self.station_USER = station_detail.station_user
        self.station_PASSWORD = station_detail.station_password
        
        print ('สถานีเรียกใช้ SQL คือ {} IP : {} PORT : {} USER : {} PASSWORD {}'.format(self.station_NAME,self.station_IP,self.station_PORT,self.station_USER,self.station_PASSWORD))
        # ทำการทดสอบการเชื่อมต่อกานั้นกับฐานข้อมูล
        try :
            conn = pymssql.connect(server=self.station_IP, user=self.station_USER, password=self.station_PASSWORD, database=self.station_DB,timeout=time_out)
            cursor = conn.cursor(as_dict=True)
            sql_command = """select @@version as version"""
            cursor.execute (sql_command)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            # return Engine.line_format.create_thai_key_realtime(rows)
            print ('สถานะการเชื่อมต่อ DB ปกคิ {} สถานะ {}'.format(self.station_NAME,rows))
            pass
        except Exception as e:
            print("\nERROR: Unable to connect to the server.",e)
            return False , e

        
        pass

    def Connect_DB (self,sql_command,valible1,type_sql) :
        # pass
        try:
            conn = pymssql.connect(server=self.station_IP, user=self.station_USER, password=self.station_PASSWORD, database=self.station_DB,timeout=time_out)
            cursor = conn.cursor(as_dict=True)
            if type_sql == 1 :
                cursor.execute (sql_command)
            elif type_sql == 2 :
                sql_valible = (valible1)
                cursor.execute (sql_command,sql_valible)
            elif type_sql == 3 :
                cursor.execute (sql_command,valible1)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            # return Engine.line_format.create_thai_key_realtime(rows)
            return True , rows
        except Exception as e:
            print("\nERROR: Unable to connect to the server.",e)
            return False , e
        
    def Connect_SQL_SERVER (self,sql_command,valible,type_sql,command) :
        # pass
        # valible = '2022-06-03'
        try:
            conn = pymssql.connect(server=self.station_IP, user=self.station_USER, password=self.station_PASSWORD, database=self.station_DB,timeout=time_out)
            cursor = conn.cursor(as_dict=True)
            if type_sql == 0 :
                cursor.execute (sql_command)
            elif type_sql == 1 :
                cursor.execute (sql_command,valible)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            # return Engine.line_format.create_thai_key_realtime(rows)
            print ('ส่วนติดต่อฐานข้อมูล ผลจากคำสั่ง {} คือ {}'.format(command,rows))
            return True , rows
        except Exception as e:
            print('ส่วนติดต่อฐานข้อมูล ไม่สามารถทำการติดต่อฐานข้อมูลของคำสั่ง {} ได้ เนื่องจาก {}'.format(command,e))
            return False , e
    def Connect_DB_per_request (self,sql_command,date_request,shift_request) :
        print('date_request ',date_request)
        print('shift_request ',shift_request)
        try:
            conn = pymssql.connect(server=server, user="sa", password="Sa:123456th@1", database="SUSCOBOS")
            cursor = conn.cursor(as_dict=True)
            sql_valible = (date_request,shift_request)
            sql_command = sql_command
            cursor.execute (sql_command,sql_valible)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            print(rows)
            print(len(rows))
            if len(rows) < 1 :
                return False , rows
            elif len(rows) > 1 :
                return True , rows
            # return line_format.create_thai_key(rows)
        except Exception:
            print("\nERROR: Unable to connect to the server.")
            exit(-1)
            return False