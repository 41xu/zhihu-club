import pymysql
import csv


def get_category_info():
    connect = pymysql.connect(
        host="xxxx",
        port=3306,
        user='root',
        password='xxx',
        db='zhihu',
        charset='utf8mb4'
    )
    cursor = connect.cursor()
    sql = 'select * from category'
    cursor.execute(sql)
    category = cursor.fetchall()
    connect.close()
    return category


def get_club_info():
    connect = pymysql.connect(
        host="xxxx",
        port=3306,
        user='root',
        password='xxx',
        db='zhihu',
        charset='utf8mb4'
    )
    cursor = connect.cursor()
    sql = 'select * from club'
    cursor.execute(sql)
    club = cursor.fetchall()
    connect.close()
    return club


def category_to_csv():
    data=get_category_info()
    filename='data/category.csv'
    with open(filename,'x') as f:
        write=csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)


def club_to_csv():
    data=get_club_info()
    filename='data/club.csv'
    with open(filename,'x') as f:
        write=csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)

if __name__=='__main__':
    category_to_csv()
    club_to_csv()
