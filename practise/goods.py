#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
读取ecxel，找到对应的图片，对其重命名，
命名格式： $line_$row_$sub_num.png
并将图片对应的产品信息，存储为dict，
多个dict组合为一个货架

格式：
{
    '货架1': {
        'line1':[
            {
            'row1': {
                'Price': "64",
                'Row': "1",
                'Sub_num': "1",
                'Type': "0",
                'UPC': '909090909",
                'imgname': "$line_$row_$sub_num.png",
                'name': "xxx",
                'size': '650"
            },
            'row2': {}
            ]
        },
        'line2': {}
    },
    '货架2': {}
}
"""
import xlrd
import sys, os
from pprint import pprint

class NotExistError(BaseException):
    pass

def parse_excel_and_rename_pic(target_file='/home/zhaoy/Downloads/glfhj_0704.xlsx', pic_directory='/home/zhaoy/Downloads/小图340X480/'):
    """
    数据中包含line号，但输出的并不是需求的dict
    """
    workbook = xlrd.open_workbook(target_file)
    booksheet = workbook.sheet_by_index(0)

    def get(row, col):
        return booksheet.cell(row, col).value

    param = []
    for row in range(1, booksheet.nrows):
        old_name = '%s_%s.png' % (get(row, 14), get(row, 15))
        new_name = '%s_%s_%s.png' %(get(row, 14), get(row, 15), get(row, 16))
        param.append({
            'UPC': get(row, 0),
            'name': get(row, 2),
            'Subcategory': get(row, 3),
            'Pop': get(row, 4),
            'Price': get(row, 5),
            'Size': get(row, 6),
            'Brand': get(row, 8),
            'Line': get(row, 14),
            'Row': get(row, 15),
            'Sub_num': get(row, 16),
            'Type': get(row, 17),
            'imgname': new_name, 
            })

        # todo 
        old_name=pic_directory + old_name
        if os.path.isfile(old_name):
            new_name=pic_directory + new_name
            os.rename(old_name, new_name)
        else:
            pprint('the file %s is not exists.' % old_name)
            
        
        
    return param


def export_value(target_file='/home/zhaoy/Downloads/glfhj_0704.xlsx', pic_directory='/home/zhaoy/Downloads/小图340X480/'):
    """

    """
    data = parse_excel_and_rename_pic(target_file, pic_directory)
    ret_dict = dict()
    for d in data:
        LINE='line%s' % d['Line']
        d.pop('Line')

        try:
            ret_dict[LINE].append(d)
        except Exception:
            ret_dict[LINE] = [d, ]

    return ret_dict


if __name__ == '__main__':
    try:
        xlsx_path = sys.argv[1]
        pic_directory = sys.argv[2]

        if not os.path.isfile(xlsx_path):
            pprint('the %s is not a file.' % xlsx_path)
            raise NotExistError
        
        if not os.path.isdir(pic_directory):
            pprint('the %s is not directory.' % pic_directory)
            raise NotExistError
        
        pprint(export_value(xlsx_path, pic_directory))

    except Exception as e:
        pprint(sys.argv)
        pprint('Usage: python goods.py [xlsx_path] [pic_directory]')
        raise e
