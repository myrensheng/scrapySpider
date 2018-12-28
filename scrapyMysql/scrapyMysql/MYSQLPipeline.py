import pymysql.cursors


class MYSQLPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='spider',
            charset='utf8',
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        self.cursor.execute(
            "insert into mingyan2(tag,saying) values (%s,%s)",(item['tag'],item['saying'],)
        )
        self.connect.commit()
        return item
