import os

# file_path 是自动化脚本文件
file_path = "20.py"

# xmlpth是生成的xml数据文件，用来生成最终报告
xmlpath = "./xml"

xmlStr = "pytest -s -q {file_path} --alluredir {xmlpath}".format(file_path=file_path, xmlpath=xmlpath)
print("xmlStr",xmlStr)

# 执行命令，生成xml文件
a = os.system(xmlStr)

# 生成报告，--clean会清除旧文件
htmlStr = "allure generate {0} -o ./report/ --clean".format(xmlpath)
os.system(htmlStr)