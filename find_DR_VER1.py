import xml.etree.ElementTree as ET
import os

def xml_read(name_):
    #print(type(name_))
    #print(name_)
    tree = ET.parse(name_)
    root = tree.getroot()
    string1_ = root[0][0][0].text
    string2_ = string1_.split('</')
    for i in string2_:
        if('<value>2021-04-' in i):
            print(name_+","+i)


file_list = os.listdir(r'C:\Users\Charles\Documents\202104Apr\nealson\2021-04-08-152\2021-04-08-152')
name = []

for filename in file_list:
    if("xml" in filename):
        name.append(filename)

for filename in range(152):
    xml_read(name[filename])
#xml_read(name[0])



"""
# 從檔案載入並解析 XML 資料
tree = ET.parse('TL18765177.xml')
root = tree.getroot()
string1_ = root[0][0][0].text
string2_ = string1_.split('</')
#print(len(string2_))

for i in string2_:
    if('<value>2021-03-08' in i):
        print('TL18765177.xml    '+i)
"""