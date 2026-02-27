def process_scores(students):
    print("\n===== Task 1 =====\n")
    avg_score = {}
    
    for name, scores in students.items():
        print("\n", name, scores, "\n")
        print("Individual Score : ", end=" ")
        
        sum_score = 0
        subject = 0
        
        for score in scores:
            sum_score += score
            subject += 1
            print(score, end=" ")
        
        if(subject != 0):
            average = sum_score / subject
        else: 
            average = 0
        
        print("\nTotal Score : ",sum_score)
        print("Total Subject : ",subject)
        print("--->Average Score : ", average, "\n")
        
        avg_score[name] = round(average, 2)
    
    return avg_score

    
stu = {'Alice':[70,80,90, 90], 'Bob':[40,50,60],'Carlo':[]}    

task_1_result = process_scores(stu)

def classify_grades(averages):
    print("\n===== Task 2 =====\n")
    
    student_grade = {}

    A_threshold = 90
    B_threshold = 75
    C_threshold = 60 


    for name, avg_score in averages.items():
        if(avg_score >= A_threshold):
            grade = 'A'
            print(f"Name : {name} , Average Score : {avg_score}, Grade : {grade}\n")
        
        elif(avg_score >= B_threshold):
            grade = 'B'
            print(f"Name : {name} , Average Score : {avg_score}, Grade : {grade}\n")
        
        elif(avg_score >= C_threshold):
            grade = 'C'
            print(f"Name : {name} , Average Score : {avg_score}, Grade : {grade}\n")
        
        else:
            grade = 'F'
            print(f"Name : {name} , Average Score : {avg_score}, Grade : {grade}\n")
            
    
        student_grade[name] = (avg_score, grade) 
    
    return student_grade
        
task_2_result = classify_grades(task_1_result)
print("--->",task_2_result)