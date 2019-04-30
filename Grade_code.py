# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:31:56 2019

@author: jbk48
"""

import os
import re
import subprocess
import pandas as pd
import numpy as np
import pickle

student_df = pd.read_csv("student_list.csv", sep =",")

## 안낸 사람 점수 0점으로 ##
student_df.loc[student_df["제출여부"] == "N", "점수"] = -1


with open("testcase.txt" , "r") as f:
    testcase = f.readlines()

with open("testanwser.txt" , "r") as f:
    answer = f.readlines()

testcase = "".join(testcase)
answer = "".join(answer)

if(os.path.exists("./filename_list.pkl")):
    with open("./filename_list.pkl", 'rb') as f:
        filename_list = pickle.load(f)
else:
    filename_list = os.listdir("./datastructure_HW")
    with open("./filename_list.pkl",'wb') as f:
        pickle.dump(filename_list , f)
    
##filename_list.index("2016310526_20190330011420_368471.c")

os.chdir("./datastructure_HW")

exception_list = [] ## 에러나는거 리스
i = 0

input_filename = exception_list[0]

for input_filename in filename_list:
    
    student_id = input_filename[:10]
    
    fileName =  student_id
    compileStr = "gcc -o ./" + fileName + " ./" + input_filename
    call_value = subprocess.call(compileStr, shell=True)
    if(call_value == 1):
        print("Error for {}, index {}".format(fileName, i))
        i += 1
        exception_list.append(input_filename)
        continue
    else:
        try:
            out = subprocess.check_output(fileName, input = testcase, shell = True, encoding = "utf-8")
        except:
            print("Error for {}, index {}".format(fileName, i))
            i += 1
            exception_list.append(input_filename)
            continue
        
    pred_answer = re.sub("[a-z| A-Z|'\n]", "", out)
    real_answer = re.sub("[a-z| A-Z|'\n]", "", answer)
    
    if(pred_answer == real_answer):
        score = 10
    else:
        score = 0
     
    student_df.loc[student_df["학번"] == int(student_id), "점수"] = score
    
    print("Success for {}, index {}".format(fileName, i))
    student_df.to_csv("student_score.csv", index = False)
    with open("./exception_list.pkl",'wb') as f:
        pickle.dump(exception_list , f)
    
    i += 1
