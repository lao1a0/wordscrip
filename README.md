# wordscrip
# 编程思路
完成此任务，你需要学习正则语法，xpath语法，爬虫，python操作excel
- 将所有的词编辑成excel格式，方便python处理
- 整理一下词语的格式，用正则提取中文词语，然后百度查意思
- 得到结果后写入一个新的excel
# 需要安装的依赖
- pip install xlrd
- pip install  xlwt
- pip install  lxml 
- pip install  requests
- pip install  urllib
- pip install  re
# 要查的文件
### 第1-20天 - huang
https://www.camscanner.com/s/MHg0NWFkZjZhYQ%3D%3D/E04B87CN?pid=dsa&style=1&share_link_style=0
### 第21-40天 - liu
https://www.camscanner.com/s/MHg0NWFkZjZhYQ%3D%3D/641C3ACN?pid=dsa&style=1&share_link_style=0
### 第41-60天 - wei
https://www.camscanner.com/s/MHg0NWFkZjZhYQ%3D%3D/4238DACN?pid=dsa&style=1&share_link_style=0
### 第61-80天 - dong
https://www.camscanner.com/s/MHg0NWFkZjZhYQ%3D%3D/786258CN?pid=dsa&style=1&share_link_style=0
### 第81-100天 - chen
https://www.camscanner.com/s/MHg0NWFkZjZhYQ%3D%3D/B03AE3CN?pid=dsa&style=1&share_link_style=0

# 1.0使用方法介绍
1.用全能扫描王扫描出来进行OCR识别（用其他的OCR识别也行）

2.整理识别出来的文档，每个词一行，把他们放入excel表格中，我这里命名为"1.xlsx"

![imag1](https://github.com/thinkforanameissohard/wordscrip/blob/main/img/1.png?raw=true)

3.运行”lao.py“，记得更改一下get_explain_for_each_word的参数（代表文件名）还有return_to_excel的第一个参数（代表天）

4.运行结果可以看到还是有的词语是查不出来的，这个时候就要自己手动🐦

![img2](https://github.com/thinkforanameissohard/wordscrip/blob/main/img/2.png?raw=true)

5.如果有更好的查词网站可以自己更改一下，我这里用的是百度汉语（当然改了一定报错啊🤤，需要自己从页面上重新定位，相信各位学弟学妹一定可以创造出更好的脚本）

![img3](https://github.com/thinkforanameissohard/wordscrip/blob/main/img/3.png?raw=true)

# 2.0使用方法介绍
1.将API改成自己的

2.其他跟上一个一样，每人每天只有100次免费的，因为调用api比较慢，等到出现“>>Finish”就好了，学弟学妹们可以积极探索找到另外的api来作为弥补😋

![img4](https://github.com/thinkforanameissohard/wordscrip/blob/main/img/4.png?raw=true)

# 3.0还没写完
目前是一个自动的OCR识别

新的api免费不限量：https://hanyuapp.baidu.com/dictapp/swan/getzicidetail?wd=%E9%80%9A%E7%89%92

# 2.1更新
在原来2.0版本的基础上更新，将原来的输出excel改为了word



