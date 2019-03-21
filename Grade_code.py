# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:26:28 2019

@author: jbk48
"""

import os
import subprocess
import pandas as pd
import numpy as np

base_dir = os.getcwd()

with open("testcase.txt" , "r") as f:
    testcase = f.readlines()

testcase = "".join(testcase)

os.chdir("./assignment")
hw_dir = os.getcwd()

folder = os.listdir()

student_grade = {}

for student in folder:

    os.chdir("{}\\{}\\{}".format(hw_dir, student, student))
    
    subprocess.call("g++ main.cpp",shell=True)
    out = subprocess.check_output("a.exe", input = testcase ,shell = True, encoding = "utf-8") 
    
    pred_answer = [int(x) for x in out.split("\n") if x != ""] ## 코드로부터 나온 답
    real_answer = [15, 7, 10] ## 실제 답
    
    if(pred_answer == real_answer):
        student_grade[student] = 1  ## PASS
    else:
        student_grade[student] = 0  ## FAIL


std_id = [id_ for id_ in student_grade]
std_grade = [student_grade[id_] for id_ in student_grade]


result = pd.DataFrame(np.array([std_id, std_grade]).T , columns =["학번","점수"] ,index = None)
os.chdir(base_dir)
result.to_csv("assignment_1.csv" , index = False)


    
