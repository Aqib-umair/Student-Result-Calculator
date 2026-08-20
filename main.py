print(("="*5)+" STUDENT RESULT "+("="*5))
student_name = input("Student name: ")
python_marks = int(input("Python marks: "))
sql_marks = int(input("SQL marks: "))
aiml_marks = int(input("AIML marks: "))
math_marks = int(input("Mathematics marks: "))
english_marks = int(input("English marks: "))
total_marks = python_marks + sql_marks + aiml_marks + math_marks + english_marks
print( "total:"+str(total_marks))
average_marks=total_marks/5
print( "Average :"+str(average_marks))
if average_marks>=90:
    print("Grade: A ")
elif  average_marks>=89:
    print("Grade: B ")  
elif average_marks >=74:
    print("Grade: C")  
elif average_marks>=59:
    print("Grade: D")  
elif average_marks<=40:
    print("Grade: E ")  
else:
    print("Grade: F ") 

#pass/fail
if python_marks<35 :
    print("python marks are below 35") 
else:
      print("pass") 
if sql_marks<35 :
    print("sql marks are below 35")
else:
       print("pass ") 
if aiml_marks<35 :
    print("aiml are below 35")
else:
      print("pass") 
if math_marks<35 :
     print("math marks are below 35")
else:
      print("pass ")  
if english_marks<35 :
    print("English marks are below 35")   
else:
     print("pass")
      
        
      
      
  