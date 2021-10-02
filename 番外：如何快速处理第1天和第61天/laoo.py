'''
@Time : 2021-10-02 14:23
@Author : laolao
@FileName: laoo.py
'''
import xlrd
import xlwt


readbook = xlrd.open_workbook('d1.xlsx')
sheet = readbook.sheet_by_index(1)
nrows = sheet.nrows # 行
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
}

word_list=[]

for i in range(nrows):
    cel = sheet.row_values(i)[0].split('、')# 获取i行表格值
    if len(cel) == 2:
        c = cel[1].split('：')
        # print(c)
        word_list.append(c)
    else:
        www=""
        for ss in range(len(cel)):
            if ss>1:
               www+=cel[ss]
        # print(www)
        c = cel[1].split('：')
        print("{}".format([c[0],c[1]+www]))
        word_list.append([c[0],c[1]+www])
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet("sheet2")
# 参数对应 行, 列, 值
worksheet.write(0,0, label ='词语')
worksheet.write(0,1, label ='词语意思')
worksheet.write(0,2, label ='来源url')
i=1
for w  in word_list:
    worksheet.write(i,0, label =w[0])
    worksheet.write(i,1, label =w[1].strip())
    worksheet.write(i,2, label ="")
    i+=1
workbook.save('第61天.xls')