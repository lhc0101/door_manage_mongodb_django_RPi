from pymongo import MongoClient

settings = {
    "ip":'192.168.123.54',   #ip
    "port":27017,           #端口
    "db_name" : "Door",    #数据库名字，没有则自动创建
    # "set_name" : "invitation"   #集合名字，没有则自动创建
    "set_name" : "log"   #集合名字，没有则自动创建
}

class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]
    #插入
    def insert(self,dic):
        self.my_set.insert(dic)
        print("插入成功")
    #更新
    def update(self,dic,newdic):
        self.my_set.update(dic,newdic)
        print("更新成功")
    #删除
    def delete(self,dic):
        self.my_set.remove(dic)
        print("删除成功")
    #查找
    def dbFind(self,dic):
        data = self.my_set.find(dic)
        for result in data:
            print(result)
        print("查找成功")
    #查找全部
    def findAll(self,data):
        # 查询全部
        a=0
        for i in self.my_set.find(data):
            a=a+1
            print(a)
        if 0 != a:
            door = True
            print("允许进入")
        else:
            door = False
            print("无权限")


if __name__ == "__main__":
    c = "1"
    data = {"number":c}
    mongo = MyMongoDB()
    dic = {"number": "366456290886", "name": "小明","log":"2018:05:01"}
    # mongo.insert(dic)
    # mongo.findAll(data)



    # mongo.update({"name": "tom"}, {"$set": {"age": "25"}})
    # mongo.dbFind({"name": "tom"})
    #
    # mongo.delete({"name": "tom"})
    # mongo.findAll()