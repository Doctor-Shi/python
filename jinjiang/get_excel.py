import pymysql
import util


class Excel:
    @staticmethod
    def write_excel(list1):
        output = open('data.xls', 'w', encoding='gbk')
        output.write('学生名字\t课程总数\t消课数\t剩余课数\n')
        for i in range(len(list1)):
            for j in range(len(list1[i])):
                output.write(str(list1[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
                output.write('\t')  # 相当于Tab一下，换一个单元格
            output.write('\n')  # 写完一行立马换行
        output.close()


class Mysql:
    print_list = []

    def __init__(self):
        self.content = pymysql.Connect(
            host='127.0.0.1',  # mysql的公司主机ip
            port=3306,  # 端口
            user='root',  # 用户名
            passwd='123456',  # 数据库密码
            db='course_system',  # 数据库名
            charset='utf8',  # 字符集
        )
        self.birthday_name_list = []
        self.cursor = self.content.cursor()

    # 根据门店名字,获取某月学生姓名
    def query_school(self, school_name):
        if school_name is None:
            sql = "select id,name from school;"
        else:
            sql = "select id,name from school where name = '" + school_name + "';"
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    # 查询某一个月生日的孩子名单
    def query_birthday(self, month, school):
        sql = "select student_name,student_birthday,gender from customer where school_id = '" + school + "';"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            if row[0] is not None:
                if row[1].month == month:
                    print("student_name:%s\t student_birthday:%s\t gender:%s" %
                          (row[0], row[1], util.Util.get_gender(row[2])))
                    self.birthday_name_list.append(row)

        print(f"一共查找到当月生日学生：{len(self.birthday_name_list)} 个")
        # print(self.birthday_name_list)
        # Excel.write_excel(self.birthday_name_list)
        self.birthday_name_list.clear()

    # 查询某一门店的课程剩余情况
    def query_contract(self, month, school):
        sql = "select customer_id,start_at,end_at,course_amount,free_course_amount,used_course_amount from contract " \
              "where school_id = '" + school + "' and status = 'RUNNING';"
        self.cursor.execute(sql)
        contract_list = self.cursor.fetchall()

        # 临时保存数据
        list_l = 4
        temp_list = [0] * list_l
        for row in contract_list:

            # 根据customer_id 查找名字
            sql = "select student_name from customer where id = '" + row[0] + "';"
            self.cursor.execute(sql)
            for name in self.cursor.fetchall():
                temp_list[0] = name[0]

            temp_list[1] = (row[3] + row[4])
            temp_list[2] = row[5]
            temp_list[3] = (row[3] + row[4] - row[5])
            temp_list = [str(i) for i in temp_list]

            print(temp_list)
            self.print_list.append(temp_list)
            temp_list = [0] * list_l

        print(f"一共查找到：{len(self.print_list)}")
        Excel.write_excel(self.print_list)

    def end(self):
        self.cursor.close()
        self.content.close()


if __name__ == '__main__':
    Month = 9
    School_name = "帝景店"

    # 打开连接
    mysql = Mysql()
    school_list = mysql.query_school(School_name)

    for data in school_list:
        print("%s %d月生日的学生名单一共有：" % (data[1], Month))

        # 查找生日列表
        # mysql.query_birthday(Month, data[0])
        mysql.query_contract(Month, data[0])
        # print(mysql.print_list)
    # 关闭连接
    mysql.end()
