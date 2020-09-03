#   二分查找  输入 数组长度 len  查找数字 num  输出数字在数组中的长度
#   如果数组中不存在该数字  输出数组长度 加1
#   数组有序，从小到大排列

#   arr 输入数组 len   x  查找元素    min 查找范围起始下标   max 查找范围最大值下标


def binary_search(arr, left, right, num):
    if right > left:

        mid = int(left + (right - left) / 2)

        #   正好中间位置的元素就是所要获取的数据
        if arr[mid] == num:
            return mid

        #   中间的数据比所要查找的数据小，在右侧查找
        elif arr[mid] < num:
            return binary_search(arr, mid, right, num)

        #   中间的数据比所要查找的数据大，在左侧查找
        else:
            return binary_search(arr, left, mid, num)

    else:
        # 不存在  返回 -1
        return -1


#   测试数据    5,4,[1,2,4,4,5]
#   期望输出    3

str_arr = "5,4,1,2,4,4,5"

#   分割输入数据获取 输入数组长度  查找数字  查找数组
input_list = str_arr.split(',')
n = int(input_list[0])
x = int(input_list[1])
find_list = list(map(int, input_list[2:7]))

#   调用函数查找 获取目标数字下标
ret = binary_search(find_list, 0, n, x)

if ret == -1:
    print(len(find_list) + 1)
else:
    print(ret + 1)
