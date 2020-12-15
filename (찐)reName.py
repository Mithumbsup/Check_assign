import sys 
from os import rename, listdir
import os 
import pandas as pd 

# os.walk 모든 파일/폴더 출력하기 
# 파이썬 조각 코드 모음집 : https://wikidocs.net/book/536
workDIr = os.path.abspath('.')

def DirInfo(path):
    for dirpath, dirnames, filenames in os.walk(workDIr):
        filenames = filenames
    return filenames    

def delTxtFile(filenames):
    for fileName in filenames:
        split_filename = fileName.split(".")
        if split_filename[-1] == "txt":
            os.remove(fileName)
    reFileNames = [reFileName for reFileName in DirInfo(workDIr)]
    print("\n"+"제출완료된 파일의 수는", len(reFileNames)-1, "개 입니다"+"\n")   
    return reFileNames

def changeFileName(reFileNames):
    filenames = list(reFileNames)
    df = pd.DataFrame(columns=["assignment","student_ID","submit_Date","title"])

    for fileName in filenames:
        split_filename = fileName.split("_") 

        if '확인' not in split_filename:
            # print(fileName)
            if fileName == "reName.py":
                pass 
            else :
                data = {
                    "title": fileName,
                }
                df = df.append(data, ignore_index=True)
        else :
            # 과제 확인여부 위치 
            Confirm_index = split_filename.index('확인')
            # 학번 
            student_ID = split_filename[Confirm_index-1]
            # 제출날짜 
            submit_Date = split_filename[Confirm_index+1] 
            # 과제제목
            title = student_ID+"_"+''.join(split_filename[Confirm_index+2:])
            new_filename = fileName.replace(fileName, title)
            os.rename(fileName, title)

            # 과제명
            assignment = ''.join(split_filename[:split_filename.index(student_ID)])
            
            data = {
                "assignment" : assignment,
                "student_ID": student_ID,
                "submit_Date": submit_Date,
                "title": title
            }
            df = df.append(data, ignore_index=True)
    
    #과제명 추출 
    assignment = df["assignment"][0]
    #중복제거한 학생 아이디 리스트  > 제출한 학생 학번만 볼 수 있음 
    student_ID = list(set(df["student_ID"]))

    if str(student_ID[0]) == 'nan':
        print("과제제출된 파일은", len(df["title"]) ," 개 입니다" )
    else:
        print(assignment,"과제를 제출한 학생은", len(student_ID),"명 입니다"+"\n")

    return df 


filenames = DirInfo(workDIr)
reFileNames = delTxtFile(filenames)
df = changeFileName(reFileNames)
