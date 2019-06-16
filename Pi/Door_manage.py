# -*- coding: utf-8 -*
from pymongo import MongoClient
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 as rc522
import time
import datetime

settings = {
    "ip":'192.168.123.54',   #ip
    "port":27017,           #端口
    "db_name" : "Door",    #数据库名字，没有则自动创建
    "set_name" : "invitation" ,  #集合名字，没有则自动创建
    "set_log_name" : "log"   #集合名字，没有则自动创建
}

reader = rc522()
Door = 7
READ = 0
WRITE = 1
jingbao = 8
operation = READ

Door_OPENED = False

GPIO.setup(Door, GPIO.OUT)
GPIO.setup(jingbao, GPIO.OUT)

class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]
        self.my_log_set = self.db[settings["set_log_name"]]
    #插入
    def insert(self,dic):
        self.my_log_set.insert(dic)
        print("写入日志成功")
    #更新
    def update(self,dic,newdic):
        self.my_set.update(dic,newdic)
        print("更新成功")
    #删除
    def delete(self,dic):
        self.my_set.remove(dic)
        print("删除成功")
    #查找
    def findAll(self,data):
        global Door_OPENED
        # 查询
        a=0
        for i in self.my_set.find(data):
            a=a+1
            print(a)
        if 0 != a:
            Door_OPENED = True
            print("允许进入")
            GPIO.output(Door, GPIO.HIGH)
            print("Door_on")
            time.sleep(3)
            print("Door_off")
            GPIO.output(Door, GPIO.LOW)
        else:
            Door_OPENED = False
            print("无权限")
            GPIO.output(jingbao, GPIO.HIGH)
            print("警告")
            time.sleep(3)
            GPIO.output(jingbao, GPIO.LOW)


if __name__ == "__main__":
    global Door_OPENED
    while True:
        print("begin reading ")
        id, data = reader.read()
        data = data.strip()
        # id = id.strip()
        print("id is " + str(id))
        print("data is " + str(data))
        dic = {"number": str(id), "name": str(data),"log":str(datetime.datetime.now())}
        print(dic)
        number = {"number":str(id)}
        print(number)
        try:
            MyMongoDB().findAll(number)
            MyMongoDB().insert(dic)
            value = str(data)
            print('input data is ' + str(value))
        except Exception as error:
            print('input data "' + data + '" is not digit only')
            print("error: " + str(error))
    GPIO.output(Door, GPIO.LOW)
    GPIO.cleanup()

