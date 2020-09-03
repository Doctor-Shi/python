import pymysql
import util


class QueryInfo:
    def __init__(self):
        self.school_name = None
        self.month = 0
        self.coach_name = None


def set_school_name():
    school_name = str(input("输入学校名称：(不输入表示查询所有校区数据)"))
    if school_name == '':
        school_name = None
    return school_name


def set_month():
    month = input("输入月份：(输入None表示查询所有月份数据)")
    return month


def set_coach_name():
    coach_name = input("输入教练名称：(输入None表示查询所有教练数据)")
    if coach_name == '':
        coach_name = None
    return coach_name


def get_choose():
    print("请输入你想实现的功能：")
    print("1：查看门店学生的合同情况")
    print("2：查看门店学生的查询月份的生日情况")
    return input("输入你的选择")


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

        # 如果传入的是0  表示查询所有孩子的生日信息 按照将查询结果按照月份排序
        if month == 0:
            # 创建保存12个月数据的二维数组
            student_list = [[] for i in range(12)]
            student_number = 0
            for row in self.cursor.fetchall():
                temp_list = [row[0], row[1], util.Util.get_gender(row[2])]
                student_list[row[1].month - 1].append(temp_list)

            #   打印例表中的名单
            for i in range(len(student_list)):
                print(f" {i + 1}月生日学生名单:")
                for j in range(len(student_list[i])):
                    # print(student_list[i][j])
                    student_number += 1
                    print("student_name:%s\t student_birthday:%s\t gender:%s" %
                          (student_list[i][j][0], student_list[i][j][1], student_list[i][j][2]))

            print(f"一共查找到生日学生：{student_number} 个")

        else:
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

    def query_employee(self, school, coach):
        #  根据school 查找教练名单
        if coach is None:
            sql = "select name, id from employee where position = 'COACH' and school_id = '" + school + \
                  "' and is_del = 0;"
        else:
            sql = "select name, id from employee where position = 'COACH' and school_id = '" + school + \
                  "' and is_del = 0 and name = '" + coach + "';"

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def end(self):
        self.cursor.close()
        self.content.close()


if __name__ == '__main__':

    query_info = QueryInfo()
    print("欢迎使用金匠查询系统：")
    query_info.month = int(set_month())
    query_info.school_name = set_school_name()
    choose = get_choose()
    print(choose)

    # 打开连接
    mysql = Mysql()
    school_list = mysql.query_school(query_info.school_name)
    if choose == '1':
        for data in school_list:
            print("%s 本月学生合同情况如下：" % (data[1]))
            mysql.query_contract(query_info.month, data[0])
    elif choose == '2':
        for data in school_list:
            print("%s %d月生日的学生名单一共有：" % (data[1], query_info.month))
            mysql.query_birthday(query_info.month, data[0])
    elif choose == '3':
        query_info.coach_name = set_coach_name()
        for data in school_list:
            employee_list = mysql.query_employee(data[0], query_info.coach_name)

            for coach_data in employee_list:
                print("现在查询的是 %s 教练的数据" % (data[0]))

    # 关闭连接
    mysql.end()
