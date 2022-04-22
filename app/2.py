# -*- coding: UTF-8 -*
import re
import os
BASE_DIR = (os.path.dirname(os.path.abspath(__file__)))
#print("##%s"%BASE_DIR)
def staff_file(filename):
    """
    读取员工信息文件
    :return: 返回读取结果
    """
    with open(filename, 'r', encoding="utf-8") as f:
        f = list(f)   # 将结果转换成列表
        return f      # 返回结果

def file_exist_check(file_name):
    if not os.path.exists(file_name):
        print("Error: file %s is not exist!!!" % file_name)
        exit(2)


def server_options1():
    """
    打印一个服务项
    :return:返回用户输入的选项
    """
    for staff_tabe in range(1):
        print("1.查询员工信息\n2.增加员工信息\n3.修改员工信息\n4.退出")    # 循环打印选项
        serial_number = input("请选择你的服务:")   # 获取用户输入的选项
        if serial_number.isdigit():   # 判断是否是数字
            serial_number = int(serial_number)   # 转成数字类型
            return serial_number   # 返回选项结果
        else:
            print("请输入规范的服务编号")
            continue

def query_function():
    """
    员工模糊查询功能选项
    :return: 返回最终的查询结果
    """
    file_name = (BASE_DIR+"\staff.txt")    # 获取员工信息文件
    file_exist_check(file_name) # 检查文件是否存在
    file = staff_file(file_name)
    for fm in range(1):
        print("1.员工年龄\n2.员工职业\n3.员工登记日期")    # 循环打印选项
        fm_server = input("请选择你要查询的服务:")   # 获取用户输入的选项
        if fm_server.isdigit():   # 判断是否是数字
            fm_server = int(fm_server)   # 转成数字类型
            if fm_server <= 3 and fm_server >= 0:   # 判断是否有不规则的选项
                if fm_server == 1:
                    staff_age = input("请输入员工年龄：")   # 获取用户输入的年龄数
                    # 判断员工信息表里是否有用户输入的年龄数
                    while True:
                        loginSucces = False
                        flag = 0   # 记录查询到的信息数
                        for staff_fm in file:
                            tmp_file = (staff_fm.strip('\n').split(','))
                            # 如果有这个年龄数的就打印输出列表
                            if staff_age in tmp_file[2]:
                                print(tmp_file)
                                flag += 1
                            else:
                                continue   # 递归查询列表
                            loginSucces = True   # 如果查询到了列表就定义为True
                        if loginSucces == True:print("查询到%s条您要的员工信息\n"%flag) # 打印输出查询到的信息数
                        if loginSucces == True:break
                        else:   # 如果没有查询到列表就打印此输出，并退出查询
                            print("\033[31;1m没有此年龄段的用户！\033[0m\n")
                            break
                elif fm_server == 2:
                    staff_work = input("请输入员工职业：")   # 获取用户输入的职业名
                    # 判断员工信息表里是否有用户输入的职业名
                    while True:
                        loginSucces = False
                        flag = 0   # 记录查询到的信息数
                        for staff_fm in file:
                            tmp_file = (staff_fm.strip('\n').split(','))
                            if staff_work in tmp_file[4]:   # 如果有这个职业名的就打印输出列表
                                print(tmp_file)
                                flag += 1
                            else:
                                continue   # 递归查询列表
                            loginSucces = True   # 如果查询到了列表就定义为True
                        if loginSucces == True:print("查询到%s条您要的员工信息\n"%flag)   # 打印输出查询到的信息数
                        if loginSucces == True:break
                        else:   # 如果没有查询到列表就打印此输出，并退出查询
                            print("\033[31;1m没有此职业的用户！\033[0m\n")
                            break
                elif fm_server == 3:
                    staff_Date_Fegistration = input("请输入员工登记日：")   # 获取用户输入的登记日
                    # 判断员工信息表里是否有用户输入的登记日
                    while True:
                        loginSucces = False
                        flag = 0   # 记录查询到的信息数
                        for staff_fm in file:
                            tmp_file = str(staff_fm.strip('\n').split(','))
                            # 如果有这个登记日，并且符合规范的就打印输出列表，例如2018-03-14
                            if staff_Date_Fegistration in tmp_file[5]:
                                filter_files = re.search(
                                    '(.*\d+-\d+-\d+).*', tmp_file)
                                print(filter_files.group())
                                flag += 1
                            else:
                                continue   # 递归查询列表
                            loginSucces = True   # 如果查询到了列表就定义为True
                        if loginSucces == True:print("查询到%s条您要的员工信息\n"%flag)   # 打印输出查询到的信息数
                        if loginSucces == True:break
                        else:   # 如果没有查询到列表就打印此输出，并退出查询
                            print("\033[31;1m没有此登记日的用户！\033[0m\n")
                            break



def list_number(file_name):
    """
    获取文件的总行数
    :return: 返回一个总行数
    """
    with open(file_name, 'r', encoding="utf-8") as f:
        text = f.read()
        length = len(text.splitlines())
        return length


def add_function():
    """
    创建一条新的员工数据项，把新的数据项写入原文件
    :return:
    """
    file_name = (BASE_DIR + "\staff.txt")  # 获取员工信息文件
    file_exist_check(file_name)  # 检查文件是否存在
    while True:
        flag = list_number(file_name)    # 获取员工信息列表的总行数
        try:
            staff_name, staff_age, staff_phone, staff_work, staff_date = input(
                '请输入新员工详细信息:').strip().split()   # 获取用户输入的各项新员工详细信息
        except ValueError:
            print('信息不符合规范！请规范填写以空格隔开，例如：姓名 年龄 电话号码 职业 入职日期')
        else:
            staff_phone = str(staff_phone)   # 用户输入的新员工电话号要做特殊处理
            if re.search('(\d{11})', staff_phone):   # 判断是否是11位的电话号
                file_tmp = staff_file(file_name)   # 读取员工信息列表
                for staff_fm in file_tmp:
                    staff_number = staff_fm.strip('\n').split(',')
                    staff_number = staff_number[3]   # 截取列表每行的电话号码
                    if staff_phone in staff_number:   # 判断用户输入的新员工电话号是否有在列表里
                        print('%s\n这个号码已经存在!' % staff_number)
                    else:
                        continue   # 递归查询列表
                else:
                    # 判断用户输入的除电话号意外的所有信息数据类型是否符合规范
                    if staff_name.isalpha() and staff_age.isdigit() and staff_work.isalpha()\
                            and re.search('(\d{4}-\d{2}-\d{2})', staff_date):
                        with open('staff.txt', 'a+', encoding='utf-8') as f_c:
                            flag += 1   # 行数自加
                            # 把规范的新员工信息写入员工信息表
                            f_c.write(
                                "\n%s,%s,%s,%s,%s,%s" %
                                (flag, staff_name, staff_age, staff_phone, staff_work, staff_date))
                            print('添加成功')
                            break
                    else:   # 如果有不符合规范的数据类型就打印此输出
                        print('输入的信息有不规范的类型，请重新输入!')
                        continue   #重新输入新员工信息
            else:   # 如果有不符合规范的电话号就打印此输出
                print('请输入规范的11位数的电话号码！')


def file_tmp1(file_tmp):
    """
    :param file_tmp:
    :return:
    """
    for line_tmp in file_tmp:
        line_tmp = line_tmp.strip('\n').split(',')
        print(line_tmp)
    return file_tmp


def update_function():
    file_name = (BASE_DIR + "\staff.txt")  # 获取员工信息文件
    file_exist_check(file_name)  # 检查文件是否存在
    while True:
        flag = list_number(file_name)   # 获取员工信息文件的行数
        file_tmp1(staff_file(file_name))   # 循环打印出整个员工信息列表
        staff_id = input('请输入要修改的员工ID号:').strip()   # 获取用户输入的员工ID号
        if re.match('\d', str(staff_id)):   # 判断用户输入的ID号是否是数据类型
            # 判断用户输入的ID号数是否等于列表的行数并且不等于0
            if int(staff_id) == int(flag) and int(staff_id) > 0:
                with open('staff.txt', 'r', encoding='utf-8')as f:
                    lines = f.readlines()   # 读取整个员工信息列表
                with open('staff.txt', 'w', encoding='utf-8')as f_up:   # 写入员工列表
                    for line in lines:   # 循环已逗号分割员工列表
                        single_list = line.strip('\n').split(',')
                        # 判断用户输入的ID号是否有在员工列表里，有就打印出这个列表
                        if str(staff_id) in single_list:
                            print(single_list)
                            # 获取用户要修改这个列表的具体数据项
                            staff_info = input('请输入要修改的员工信息：').strip()
                            # 获取用户输入的新数据项
                            new_staff_info = input('请输入要修改的新员工信息：').strip()
                            # 判断用户输入的要修改项是否在这个列表里
                            if staff_info in single_list:
                                # 如果有这个选项就把旧的数据替换成新的数据
                                single_list[single_list.index(staff_info)] = new_staff_info
                                # 把这个列表以逗号重新责成一个新列表
                                new_single_list = ','.join(single_list)
                                # 把之前匹配到的列表替换成新的列表
                                line = line.replace(line, new_single_list)
                            else:
                                print("没有此信息的用户")
                        # 如果用户输入的ID不在这个员工列表里，把这个列表直接写入文件
                        f_up.write("%s\n" % line.strip())
                    break
            else:
                print("没有这个员工ID号！")
        else:
            print("请输入规范的员工ID号")


while True:
    serial_number = server_options1()
    if serial_number <= 4 and serial_number >= 0:
        if serial_number == 1:   # 选项1进入查询员工服务
            query_function()
        elif serial_number == 2:   # 选项2进入创建员工服务
            add_function()
        elif serial_number == 3:   # 选项3进入修改员工服务
            update_function()
        elif serial_number == 4:   # 退出员工管理系统
            exit("谢谢使用，再见！")
    else:
        print("请输入规范的服务编号！\n")
        continue
