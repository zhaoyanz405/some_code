#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
def batch_save(excel_file):
    """从excel文件中导入院校数据

    模板限制:  1. 数据项从第4行开始记录
                2. 共有5列
                3. 所有数据项均为数字
                4. 只读取sheet1的数据
                
    return: (code, fail_item_list)  
        code: 1 success
                0 fail
        fail_item_list 写入失败的item行号                    
    """
    import xlrd

    workbook = xlrd.open_workbook(excel_file)
    booksheet = workbook.sheet_by_index(0)

    for row in range(3, booksheet.nrows):
        for col in range(5):
            value = booksheet.cell(row, col).value
            if col == 0:
                if  isinstance(value, float):
                    value = int(value)
                print(value, type(value))
                print(re.match(r'^1\d{4,5}$', str(value))



if __name__ == "__main__":
    batch_save('/home/zhaoy/Downloads/院校批量导入模板.xlsx')