#SAMARANAYAKA GAMAGE NETHUM MIHIRANGA
#IIT ID : - 20230680
#UOW ID : - w2051742
#Date-11/12/2023                            

                          
#Initialize the counts for Grades counting

Progress_count=0
Progress_module_trailer_count=0
Do_not_progress_module_retriever_count=0
exclude_count=0
total_count=0
bar_height=0
grade_list=[]     # open list for store user input data
staff_student_control=True       #for control the "staff_student_control" loop .Asking staff and student versions 



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




#student grade inputs and checking for student outcome
def student_Grades():
    global total_count,total, Progress_count,Progress_module_trailer_count,Do_not_progress_module_retriever_count, exclude_count
    while True:
        Pass=input_student_grade("Please enter your credits at pass :") #"input_student_grade" user define run every Pass,Defer,fail when user enter inputs,after the execution, the "return" function assign values to Pass,Defer or fail
        Defer=input_student_grade("Please enter your credits at defer :")
        fail=input_student_grade("Please enter your credit at fail :")
        total=Pass+Defer+fail
        if(total!=120):
            print("Total incorrect")
        else:
            break    #break the "while True"loop when total is corrected

        
    if(Pass==120):
        grade_list.append(("Progress -",Pass,Defer,fail))   #append data to garde list by using append function
        Progress_count+=1
        print("Progress")
    elif(Pass>=100):
        grade_list.append(("Progress(module trailer) -",Pass,Defer,fail))
        Progress_module_trailer_count+=1
        print("Progress(module trailer)")
    elif(0<=Pass<=80 and 0<=fail<=60):
        grade_list.append(("Do not progress-module retriever -",Pass,Defer,fail))
        Do_not_progress_module_retriever_count+=1
        print("Do not progress-module retriever")
    elif(80<=fail):
        grade_list.append(("Exclude -",Pass,Defer,fail))
        exclude_count+=1
        print("Exclude")
    total_count=Progress_count+Progress_module_trailer_count+Do_not_progress_module_retriever_count+exclude_count
    dec_intput()  #calling dec_input_user_define




#decission input for continue or quit
from graphics import*    #The graphics file Source: Westminster Blackboard

def dec_intput():
    global choice_dec_brake,staff_student_control
    while(choice_dec_brake):
      dec=input('''Would you like to enter another set of data?
Enter "y" for yes or "q" to quit and view results :''')
      
      if (dec=="y"):
         student_Grades()
      elif(dec=="q"): #when user enter y ,student_Grades wiil be executed and when user enter q ,Histrogram wiil be executed

        for x in range(0,len(grade_list)): 
           print(f"{grade_list[x][0]}{grade_list[x][1]},{grade_list[x][2]},{grade_list[x][3]}") 
          
        bar_height=100/total_count
        win = GraphWin('Histrogram', 650,600) 
        win.setBackground("white")
        Head1= Text(Point(160,30), 'Histrogram Results')
        Head1.setTextColor("slategrey")
        Head1.setSize(19)
        Head1.draw(win)

        
        bottom_line=Line(Point(50,500), Point(600,500))  #bottom line
        bottom_line.draw(win)


        def bars (x1,x2,grade_count,colour):    #bars
             box=Rectangle(Point(x1,500), Point(x2,500-bar_height*grade_count)) #bar height calculation
             box.setFill(colour)
             box.draw(win) 
        bars(50,150,Progress_count,"palegreen")
        bars(200,300,Progress_module_trailer_count,"darkseagreen")
        bars(350,450,Do_not_progress_module_retriever_count,"olivedrab")
        bars(500,600,exclude_count,"pink")

        def grade_text(x3,grades):         #Grades
            text=Text(Point(x3,520),grades)
            text.setTextColor("slategrey")
            text.setSize(14)
            text.draw(win)
        grade_text(100,'Progress')
        grade_text(250,'Trailer')
        grade_text(400,'Retriver')
        grade_text(550,'Excluded')

        

        def grade_counts(x4,grade_count):
            count=Text(Point(x4,480-bar_height*grade_count),grade_count)    #grades count
            count.setTextColor("slategrey")
            count.setSize(14)
            count.draw(win)
        grade_counts(100,Progress_count)
        grade_counts(250,Progress_module_trailer_count)
        grade_counts(400,Do_not_progress_module_retriever_count)
        grade_counts(550,exclude_count)

        

        def total_grade_count():     #total count
            total_grade=Text(Point(57,575),total_count)
            total_grade.setTextColor("grey")
            total_grade.setSize(22)
            total_grade.draw(win)
            total_grade_text=Text(Point(187,575),'outcomes in total')
            total_grade_text.setTextColor("slategrey")
            total_grade_text.setSize(19)
            total_grade_text.draw(win)
        total_grade_count()
        win.getMouse()    #when clicked on the histrogram window by user, It will be closed
        win.close()
        staff_student_control = False
        choice_dec_brake=False
        
#starting user define of code.       
def start_point():     
    global choice_dec_brake,staff_student_control
    while (staff_student_control):
        choice=input("Enter 1 for student version or Enter 2 for staff version :")
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
        




 


