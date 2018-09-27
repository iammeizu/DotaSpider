import pymysql


class MySQLOperator:

    def __init__(self, address, user, password, database):
        self.addr = address
        self.usr = user
        self.pwd = password
        self.db_name = database

        self.db = self._connect()
        self.cursor = self.db.cursor()

    def _connect(self):
        return pymysql.connect(self.addr, self.act, self.pwd, self.db_name, charset='utf8')

    def find(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print('更新数据失败！')
            self.db.rollback()

    def close(self):
        self.db.close()


if __name__ == '__main__':
    sql_handle = MySQLOperator('localhost', 'root', 'shi7613096', 'DOTA2')
    sql = 'select * from dota2_hero_tbl'
    rv = sql_handle.find(sql)
    print('rv', rv)
