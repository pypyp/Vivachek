
import xlrd, requests
from xlutils.copy import copy

def read_excel():
    wb = xlrd.open_workbook(r'C:\Users\zf\PycharmProjects\jiekou\1111.xlsx')
    # print(wb)
    # sheet1索引从0开始，得到sheet1表的句柄
    new_book = copy(wb)
    for i in range(len(wb.sheets())):
        print(i)

    # new_sheet = new_book.get_sheet(1)
    #
    # sheet = wb.sheet_by_index(1)
    # rowNum = sheet.nrows
    # colNum = sheet.ncols
    # print(rowNum, colNum)


    # wb1 = xlrd.open_workbook(r'C:\Users\zf\PycharmProjects\jiekou\2.xls')
    # # 获取所有sheet的名字
    # sheet1 = wb1.sheet_by_index(0)
    # rowNum1 = sheet1.nrows
    # colNum1 = sheet1.ncols
    # print(rowNum1, colNum1)



    # for i in range(3, rowNum):
    #     a = sheet.cell(i, 0).value
    #     # print(a)
    #     for j in range(2, rowNum1):
    #
    #         if sheet1.cell(j, 1).value == a:
    #             print(sheet1.cell(j, 4).value)
    #
    #             new_sheet.write(i, 9, sheet1.cell(j, 4).value)
    # new_book.save('book.xlsx')
read_excel()


# import xlrd
#
# # 打开工作簿
# workbook = xlrd.open_workbook(r'C:\Users\zf\PycharmProjects\jiekou\1.xlsx')
# # 获取工作表
# worksheet = workbook.sheet_by_index(0)
# # 获取单元格数据的两种方式
# # cell_value = worksheet.cell(0, 0).value
# cell_value = worksheet.cell_value(1, 0)
# print(cell_value)
