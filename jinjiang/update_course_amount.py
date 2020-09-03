import xlrd

file_name = "../pythontest/1.xlsx"
file = xlrd.open_workbook(file_name)

i = 0
print(file.nsheets)

sheet = file.sheet_by_name("data")

rows = sheet.nrows

cols = sheet.ncols

cell_value = sheet.cell_value(0, 1)
print("rows : %d, cols : %d", rows, cols)

print(cell_value)

row_value = sheet.row_values(1)
print(row_value)

names = []
amount = []


names = sheet.col_values(0)
# amount = sheet.col_values(4)
# amount_int = list(map(int, amount))
print(names)
# print(amount)

while rows > 0:
    # sql_str = 'update contract set used_course_amount = ' + str(amount_int[i]) + \
    # sql_str = 'select signer,course_amount,free_course_amount,used_course_amount from contract' + \
    #       ' where customer_id = (select id from `customer` where student_name =\'' + names[i] + '\');'
    sql_str = 'select * from contract' + \
          ' where customer_id = (select id from `customer` where student_name =\'' + names[i] + '\');'
    print(sql_str)
    i += 1
    rows -= 1





