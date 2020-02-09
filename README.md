# zhihu-club
一个爬[知乎圈子](https://www.zhihu.com/club/explore)的小爬虫

## 安装

```
pip3 install -r requirement.txt
```

## 配置

默认使用我的服务器上的mysql数据库，如果你想更改成你的数据库，请在`/zhihu/zhihu/setting.py`中进行如下修改

```
MYSQL_HOST=‘your_host’
MYSQL_DATABASE='your_database'
MYSQL_PORT=3306 # 默认端口号
MYSQL_USER='your_user'
MYSQL_PASSWORD='your_password' 
```

## 运行

下载项目解压并安装好依赖后

```
cd zhihu/
scrapy crawl zhihu-club 
```

爬虫运行结束，将爬到的数据从我的mysql数据库中导出为csv文件

```
cd .. # 进入zhihu-club这个主文件夹中 
python3 savedata.py # 若data中已存在目标文件.csv则需先把那个文件删除或者在savedata里修改要写入的文件名
```

