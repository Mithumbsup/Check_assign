import csv
import pandas as pd
import numpy as np 
import os ,re

studentInfo = pd.read_csv("C:/Users/mis/Desktop/2020미선/교육보조원/공공데이터사이언스이해_(3주차)과제_제출자명단_201103.csv")
# print(studentInfo)


nameList = studentInfo["이름"]
numberList = studentInfo["사용자 ID"]
number  = [str(i)+"." for i in range(1,len(nameList)+1)]

# 1. 폴더 이름 리스트 만들기 
# dir_name_List = []
# for i in range(len(nameList)-1):
#     stu_Info = number[i] + nameList[i] # + "_" + str(numberList[i]) 
#     dir_name_List.append(stu_Info)
# print(dir_name_List)

# 2. 주차별 폴더 이름 만들기 
week_List = [str(i)+"주차" for i in range(1,5)]

# 3. 이름 폴더 안에 주차별로 폴더 만들기 
dir_path = "C:/Users/mis/Desktop/자기소개서 2차 수정안/자기소개서 2차 수정안"


# for dir_name in dir_name_List : 
#     name_folderList = os.path.join(dir_path + "/" + dir_name + "/")
#     name_folder = os.mkdir(name_folderList)
    # for week_name in week_List:
    #     week_folder = os.mkdir(name_folderList + "/" + week_name + "/")
    #     print(week_folder)



# 폴더 이름 변경하기 
folder_list = os.listdir(dir_path)
print(folder_list)
i = 1
for folderName in folder_list:
    src = dir_path+ "/" + folderName
    dst = dir_path+ "/" + folderName.split(".")[2]
    rename = os.rename(src, dst)
    i += 1
    print(src)
    print(dst)

# df = pd.DataFrame({"팀 명":folder_list})
# df.to_csv("팀리스트.csv", encoding='utf-8-sig')