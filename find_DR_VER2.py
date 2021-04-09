import xml.etree.ElementTree as ET
import os
import csv
import time
'''
預計是最終版本
需手動更改path 以及 欲搜尋字串
其餘功能完善可以輸出csv檔
'''
final_list = [] #最終要寫入csv的list
xml_list = []   #拿來存.xml檔的list
count = 0
search_str = '<value>2021-04-' #欲搜尋字串

def xml_read(name_):
    tree = ET.parse(name_)
    root = tree.getroot()
    string1_ = root[0][0][0].text
    string2_ = string1_.split('</')
    for i in string2_:
        if( search_str in i):                     #尋找xml檔是否有所需要的字串
            tmp_str = i.replace('timeStamp><value>','') #將不要的字串給去除
            tmp_str1 = name_ +","+ tmp_str              #接著將檔名和字串以逗號隔開並且存成一個字串
            result_str = tmp_str1.split(',')            #將剛剛處理的字串分割成一個陣列兩個元素
            final_list.append(result_str)               #放到final

file_list = os.listdir(r'C:\Users\Charles\Documents\202104Apr\nealson\2021-04-08-repush-153\2021-04-08-repush-153')
#找出目錄底下的所有檔案名稱把它存進file_list裡面

for filename in file_list:
    if("xml" in filename):
        xml_list.append(filename)
        count = count  +  1

for filename in range(count):
    xml_read(xml_list[filename])

localtime = time.localtime()
result = time.strftime("%Y-%m-%d%M", localtime)
outputname = result+'out.csv'
with open(outputname, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  # 將最終結果寫入二維表格
  writer.writerows(final_list)

print("總共掃描了"+str(count)+"個檔案")
