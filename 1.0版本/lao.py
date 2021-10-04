'''
@Time : 2021-10-02 11:31
@Author : laolao
@FileName: lao.py
查词来源：百度汉语
'''
import xlrd
import xlwt
from lxml import etree
import requests
import urllib
import re
from docx import Document
from docx.shared import Pt, Cm
from docx.shared import Inches
from docx.oxml.ns import qn
from docx import Document
from docx.enum.section import WD_ORIENTATION, WD_SECTION_START

def get_explain_for_each_word(excel_file_name):
    '''
    输入excel文件的名字，文件用orc识别出来的，每个词语一列
    :return:词语，词语的意思，来源网站
    '''
    readbook = xlrd.open_workbook(excel_file_name)
    sheet = readbook.sheet_by_index(0)
    nrows = sheet.nrows # 行
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    }
    word_list=[]
    for i in range(nrows):
        cel = sheet.row_values(i)[0].split('.') # 获取i行表格值
        if len(cel) == 2:
            line = cel[1].strip()
            zh = "".join(re.compile('[^\u4e00-\u9fa5]').split(line)).strip() # 中文的编码范围是：\u4e00到\u9fa5
            # print(zh)
            _url = "https://hanyu.baidu.com/s?wd={}&ptype=zici".format(urllib.parse.quote(zh))
            req = requests.get(url=_url ,headers=headers).text
            html = etree.HTML(req)
            ss = html.xpath('//*[@id="basicmean-wrapper"]/div[1]/dl/dd/p/text()')
            a=''
            for s in ss:
                a+=s.strip()
            word_list.append([cel[1],a,_url])
            # print(cel[1],_url,a)
    return word_list

def return_to_excel(day,dir):
    '''
    结果输入出到excel
    :param day:
    :param dir:
    :return:
    '''
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet("sheet1")
    # 参数对应 行, 列, 值
    worksheet.write(0,0, label ='词语')
    worksheet.write(0,1, label ='词语意思')
    worksheet.write(0,2, label ='来源url')
    i=1
    for d in dir:
        word,meaning,source_url = d
        # print(d)
        worksheet.write(i,0, label =word)
        worksheet.write(i,1, label =meaning)
        worksheet.write(i,2, label =source_url)
        i+=1
    workbook.save('第{}天.xls'.format(day))



if __name__ == '__main__':
   dir = get_explain_for_each_word('1.xlsx')
   # word,meaning,source_url
   return_to_excel(100,dir)