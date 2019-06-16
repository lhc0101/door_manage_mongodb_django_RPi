# door_manage_mongodb_django_RPi

## 功能介绍：
刷卡，判断数据库中是否又该卡的ID

1、	认证通过，开门
2、	认证未通过，报警
3、	刷卡记录传入数据库

Django端

门禁卡的管理：

增：添加ID
删：删除ID
改：修改ID
查：可以查看历史刷卡记录

后续修改：

树莓派未联网如何认证：
- 利用 MongoDB 的主从 or 主主复制
- django直接部署到派上（尝试服务器环境生成 Docker，然后部署到派上，直接部署 Django 可能会出现兼容性问题）
- 添加可写卡片 data 数据的功能

## 运行截图：

首页：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/index.png?raw=true)

添加：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/%E6%B7%BB%E5%8A%A0.png?raw=true)

查询：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/%E6%9F%A5%E8%AF%A2.png?raw=true)

日志信息查询：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2.png?raw=true)

日志信息条件筛选查询：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/%E6%97%A5%E5%BF%97%E6%9D%A1%E4%BB%B6%E7%AD%9B%E9%80%89%E6%9F%A5%E8%AF%A2.png?raw=true)

日志信息条件筛选查询结果：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/%E6%97%A5%E5%BF%97%E6%9D%A1%E4%BB%B6%E7%AD%9B%E9%80%89%E6%9F%A5%E8%AF%A2%E7%BB%93%E6%9E%9C.png?raw=true)

树莓派相关：

派认证成功：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/pi%E8%AE%A4%E8%AF%81%E6%9C%AA%E9%80%9A%E8%BF%87.png?raw=true)

派认证失败：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/pi%E8%AE%A4%E8%AF%81%E9%80%9A%E8%BF%87.png?raw=true)

未通过：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/%E6%9C%AA%E9%80%9A%E8%BF%87.jpg?raw=true)

通过：

![](https://github.com/lhc0101/door_manage_mongodb_django_RPi/blob/master/Jietu/%E9%80%9A%E8%BF%87.jpg?raw=true)

