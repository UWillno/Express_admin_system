# 快递管理系统

#### 介绍
通过对传统的快递收发流程进行分析，完成网上快递管理系统的分析设计与开发，使客户能方便在网站上查询自己的快件信息以及网上寄件，同时管理员又能对每天的收到快件进行登记和管理，基本功能要求如下：  
①用户注册、登录，VIP客户登录；  
②运费查询、网点查询、运单查询；  
③网上寄件；  
④管理员对快件信息的录入、查询、修改、删除。  
⑤对网站日常新闻发布、动态进行维护。  
用户使用web端  
管理员使用本地客户端  

#### 额外

1. 我负责编码的管理员端，所以仅有这部分的源码。界面会自动刷新。
2. **额外需要安装的库有`PyQt6 PyQt6-Charts mysql-connector-python`，不要装成了`mysql-connector`，该库已被弃用。**
3. 上面库也可能会被弃用，如有问题，建议查询[PyPI · The Python Package Index](https://pypi.org/)。
4. 部署视频见[课程设计_快递管理系统_管理员端_软件工程_PyQt6_部署演示_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Lw411i7W8/)
5. 抽空乱写的用户端见[UWillno/Express_user_system: 快递管理系统-用户端（课设） (github.com)](https://github.com/UWillno/Express_user_system)，不是WEB端，但可以跨平台。

#### 功能截图
##### 登录功能
![输入图片说明](https://foruda.gitee.com/images/1662602635295190018/3b2211f9_9070787.png "屏幕截图")
##### 快件录入（选择/手动）
![输入图片说明](https://foruda.gitee.com/images/1662602660139067457/4048409a_9070787.png "屏幕截图")
![输入图片说明](https://foruda.gitee.com/images/1662602673933543576/de27ff7a_9070787.png "屏幕截图")
##### 快件管理（查询+编辑+删除）
![输入图片说明](https://foruda.gitee.com/images/1662602705914362534/7f1c1fee_9070787.png "屏幕截图")
![输入图片说明](https://foruda.gitee.com/images/1662602725163737370/4f9deb54_9070787.png "屏幕截图")
![输入图片说明](https://foruda.gitee.com/images/1662602743096803090/1d1b99ab_9070787.png "屏幕截图")
##### 新闻发布
![输入图片说明](https://foruda.gitee.com/images/1662602790741864691/0f873656_9070787.png "屏幕截图")
##### 新闻维护
![输入图片说明](https://foruda.gitee.com/images/1662602817310511762/3a6c68d4_9070787.png "屏幕截图")

#### 使用说明

1.  建表
2.  运行
3. 管理员密码用MD5后的。

![输入图片说明](https://foruda.gitee.com/images/1662602839842151114/0b032f86_9070787.png "屏幕截图")
