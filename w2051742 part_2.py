#SAMARANAYAKA GAMAGE NETHUM MIHIRANGA
#IIT ID : - 20230680
#UOW ID : - w2051742
#Date-11/12/2023

#Initialize the counts for Grades counting

Prog_count=0
trail_count=0
Retri_count=0
exclu_count=0
total_count=0
grade_list=[]   # open list for store user input data
staff_student_control=True    #for control the "staff_student_control" loop .Asking staff and student versions 



#checking when the user inputs the value,If the value is out of range or not an integer ,display massages.
def input_student_grade(credit_value):
    while True:
        try:
          grade=int(input(credit_value))
          if (grade in range(0,121,20)):
              return grade  
              break
          else:
              print("out of range")
              
        except ValueError:
            print("Integer required")
    return grade




#student grade Inputs and checking for student outcome
def student_Grades():
    global total_count,total, Prog_count, trail_count, Retri_count, exclu_count
    while True:
        Pass=input_student_grade("Please enter your credits at pass")  #"input_student_grade" user define run every Pass,Defer,fail when user enter inputs,after the execution, the "return" function assign values to Pass,Defer or fail
        Defer=input_student_grade("Please enter your credits at defer")
        fail=input_student_grade("Please enter your credit at fail")
        total=Pass+Defer+fail
        if(total!=120):
            print("Total incorrect")
        else:
            break    #break the "while True"loop when total is corrected
   
    if(Pass==120):
        grade_list.append(("Progress -",Pass,Defer,fail)) #append data to garde list by using append function
        Prog_count+=1
        print("Progress")
    elif(Pass>=100):
        grade_list.append(("Progress(module trailer) -",Pass,Defer,fail))
        trail_count+=1
        print("Progress(module trailer)")
    elif(0<=Pass<=80 and 0<=fail<=60):
        grade_list.append(("Do not progress-module retriever -",Pass,Defer,fail))
        Retri_count+=1
        print("Do not progress-module retriever")
    elif(80<=fail):
        grade_list.append(("Exclude -",Pass,Defer,fail))
        exclu_count+=1
        print("Exclude")
    total_count=Prog_count+trail_count+Retri_count+exclu_count
    dec_intput()  #calling dec_input_user_define




#decission input for continue or quit
    
def dec_intput():
    
    global choice_dec_brake
    while (choice_dec_brake):
     dec=input('''Would you like to enter another set of data?
Enter "y" for yes or "q" to quit and view results :''')
     
     if (dec=="y"):
         student_Grades()
     elif(dec=="q"):
        Text_File()
        read_text_file()
        choice_dec_brake = False
        staff_student_control=False
        break     



   
def Text_File():  #creat text file for save user input data and processed data.And If user enter the new data ,previous data will be deleted and new data will be overwritten.
        text_file=open('Part3_Text_File.txt','w')
        text_file.write("Part 3 :-\n")
        for x in range(0,len(grade_list)): #build a for loop for write in file which data in the list
           text_file.write(f"{grade_list[x][0]}{grade_list[x][1]},{grade_list[x][2]},{grade_list[x][3]}\n")
        text_file.close()



  
def read_text_file():
        re_open_text_file=open('Part3_Text_File.txt')
        for line in re_open_text_file:
           print(line,end="")  #printing data line by line
        re_open_text_file.close()



        
def start_point():
    global choice_dec_brake,staff_student_control  
    while (staff_student_control):
        choice=input("Enter 1 for student version or Enter 2 for staff version ")
        start_try=False
        choice_dec_brake=True
        if(choice=="1"):
            choice_dec_brake=False
            student_Grades()
            break
        elif(choice=="2"):
            choice_dec_brake=True
            student_Grades()
            break
        else: 
            print("Your respond is invalid.Please enter 1 or 2")
start_point()






 


