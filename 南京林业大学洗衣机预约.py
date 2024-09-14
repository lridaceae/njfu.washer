import ntplib
import time
import sqlite3
print ('南京林业大学洗衣机预约程序')
time.sleep(2)
print ('正在初始化请稍候')
print ('初始化时间模块...')
def checktime():
    ntp_client = ntplib.NTPClient()
    try:
        response = ntp_client.request('ntp.ntsc.ac.cn')
        ntp_time = response.tx_time
        time_tuple = time.localtime(ntp_time)
        new_time = time.strftime('%m - %d %H:%M', time_tuple)
        print(f"Syncing time to: {new_time}")
        return new_time
    except ntplib.NTPException as e:
        print(f"当获取时间时出错: {e}")
        return None
print ('加载数据...')
#.db数据库初始化
print ('初始化查询模块...')
def checkwasher（）:
#数据库查询    
while 1:
