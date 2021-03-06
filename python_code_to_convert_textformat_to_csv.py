# -*- coding: utf-8 -*-
"""python_code_for_internshala_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oukv-BDyBSGIkdhxTfA2PQxo54lG_zFC
"""

"""importing pandas"""
import pandas as pd 

"""Opening the text file and printing it using open and print function"""
with open(r'C:\Users\Ashwini M\OneDrive\Desktop\assignment\Assignment - MathonGo\Assignment - MathonGo\Source TXT Files\Sample Question File_q.txt') as f:
    contents = f.read()
    #print(contents)

"""splitting the text at ###0 as it is the end of each question"""
contents=contents.split("###0")

#content_0=contents[1].split("@@@")

#content_0=contents[1].split("@@@")
#content_0[1]

#len(contents)

"""Now splitting the question and options into two list using forloop and split function"""
question=[]
Options=[]


for i in range(len(contents)-1):
  content_0=contents[i].split("@@@")
  splitted=(content_0[0].replace("\n","")).split(". ")
  question.append(splitted)
  Options.append(content_0[1].split("\n"))
  
"""Now splitting the question number and the text of the question and storing into new lists."""
question_number=[]
question_text=[]
for j in range(len(question)):
  question_number.append(question[j][0])
  question_text.append(question[j][1])


"""Now adding each options to different option list."""
Option1=[]
Option2=[]
Option3=[]
Option4=[]

for j in range(len(Options)):
  if(len(Options[j])==6):
    Option1.append(Options[j][1])
    #print(Option1)
    Option2.append(Options[j][2])
    #print(Option2)
    Option3.append(Options[j][3])
    #print(Option3)
    Option4.append(Options[j][4])
    #print(Option4)
  else:
    Option1.append("null")
    #print(Option1)
    Option2.append("null")
    #print(Option2)
    Option3.append("null")
    #print(Option3)
    Option4.append("null")
    #print(Option4)



#Options=[]
#for k in range(len(contents)):
#  content_1=contents[k].split("@@@")
#Options

#len(Options)

#print(df_question)

#print(Options[2][1])
#print(Options[2][2])
#print(Options[2][3])
#print(Options[2][4])

#question

"""Reading solution file."""
with open(r'C:\Users\Ashwini M\OneDrive\Desktop\assignment\Assignment - MathonGo\Assignment - MathonGo\Source TXT Files\Sample Solution File_s.txt') as f:
    solution_contents = f.read()
    #print(solution_contents)

"""Spliting the solution at ###0"""
solution_list=solution_contents.split("###0")

#solution_list
"""adding the options to answer list"""
answer=[]

for g in range(len(solution_list)):

  ans=solution_list[g].split("###1")
  if len(ans)==2:
    #print(ans[0])
    answer.append(ans[0])
    #print(ans[1])
    answer.append(ans[1])

  else:
    answer.append(solution_list[g])
    #print(solution_list[g])

"""splitting the answer_key and solution_text"""
ans_key=[]
solutions=[]
for n in range(len(answer)-1):
  #print(answer[n])
  spliting_the_number_and_answer=answer[n].split(". ")
  #print(spliting_the_number_and_answer)
  spliting_key_and_answer=spliting_the_number_and_answer[1].split("\n")
  #print(spliting_key_and_answer)
  ans_key.append(spliting_key_and_answer[0])
  solutions.append(spliting_key_and_answer[1])

#solutions

#solution_number=[]
#Solution=[]

#for r in range(len(solution_list)-1):
  #print(solution_list[r])
  
 # full=solution_list[r].split(". ")
  #Solution.append(full[1])
  
  #full[0]=full[0].replace("\n", "")
  #solution_number.append(full[0])
  #print(full[0])

  #Solution.append(full[1])
  #print(len(Solution))


#print(solution_number)

#for z in range(len(question_number)):
 # if str(z+1) not in solution_number:
  #  print(z)
   # solution_number.insert(z,str(z+1))
    #Solution.insert(z,"null")

#answer_key=[]
#solution=[]
#for t in range(len(Solution)):
 # if solution[t]=="null":
  #  answer_key.append("null")
   # solution.append(complete_solution[1])
 # complete_solution=solution[t].split("\n")
 # answer_key.append(complete_solution[0])
 # solution.append(complete_solution[1])


#answer_key
#solution
df_options = pd.DataFrame(list(zip(Option1, Option2, Option3, Option4)), columns =["Option1","Option2","Option3","Option4"]) 
#print(df_options)
df_question = pd.DataFrame(list(zip(question_number, question_text)), columns =['question_number', 'question_text']) 
#print(df_question)
df_solution = pd.DataFrame(zip(ans_key,solutions), columns =["Ans Key","Solution"]) 
#print(df_solution)

final_ouput=pd.concat([df_question, df_options,df_solution], axis=1, join='inner')
final_ouput.insert(1,'Null','Null')
final_ouput.to_csv(r'C:\Users\Ashwini M\OneDrive\Desktop\assignment\Assignment - MathonGo\Assignment - MathonGo\Source TXT Files\final_ouput.csv',index=False)

