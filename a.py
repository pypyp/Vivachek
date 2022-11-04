import os,re
import xlrd,xlwt
from xlutils.copy import copy


apk = '\\app1.3.3_09_2022-04-19_08_56_dev1.3.0_release.apk'
sn_path= os.getcwd()+'\\'+apk


wb = xlrd.open_workbook(r'sn.xlsx')
sheet = wb.sheet_by_name('测试医院')
rowNum = sheet.nrows
colNum = sheet.ncols
new_book = copy(wb)
new_sheet = new_book.get_sheet('测试医院')
def read_excel(i,dev_list):
    for j in range(colNum):
        if j==0:
            new_sheet.write(i, j, i)
        elif j==1:
            new_sheet.write(i, j, dev_list)
        else:
            new_sheet.write(i, j, apk)


import os


dev_list=[]
# 获取设备id列表
def getdevlist():
    connectfile = os.popen('adb devices')
    list_info = connectfile.readlines()
    # print(list)
    for i in range(len(list_info)):
        if list_info[i].find('\tdevice') != -1:
            temp = list_info[i].split('\t')
            dev_list.append(temp[0])
        # print(dev_list)

        new_list = list(dict.fromkeys(dev_list))


    return new_list

connectdevice = input('请输入每次要同时链接的设备数:')
number = int(connectdevice.strip())

while True:
    lists = getdevlist()
    devnum = len(lists)
    id = 1
    tempdevlist = getdevlist()
    if devnum <= number:
        print(f'\n设备未所有识别，应识别{number}台设备!\n当前已识别{devnum}台设备,请链接设备并等待识别:\n\n')
        for i in range(devnum):
            print(f'设备{id}: {lists[i]}')
            if tempdevlist!=[]:
                print(1)
                read_excel(id,[tempdevlist][0])
                connectfile = os.popen("adb shell am start com.android.settings/com.android.settings.Settings && "
                                       "adb uninstall com.vivachek.nova.tnineeightzeroone && adb shell rm -rf /data/data/com.vivachek.nova.tnineeightzeroone/ && "
                                       "adb shell rm -rf /sdcard/crash && adb shell rm -rf /sdcard/backup && adb install -r {} && "
                                       "adb reboot".format(sn_path))

                print(connectfile)

            id = id + 1
    # 等待识别全部设备
    while devnum < number:
        lists = getdevlist()
        curnum = len(lists)
        if curnum > devnum:
            for i in range(len(lists)):
                if lists[i] not in tempdevlist:
                    print(f'设备{id}: {lists[i]}')
                    read_excel(id,lists[i])
                    connectfile = os.popen('adb uninstall com.vivachek.nova.tnineeightzeroone')
                    print(connectfile)
                    id = id + 1
                    tempdevlist = getdevlist()
            devnum = curnum

    new_book.save('book.xlsx')
    print(f'\n全部设备已所有识别!当前有链接{len(getdevlist())}台设备.\n\n')
    break