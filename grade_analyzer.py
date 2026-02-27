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
        

def generate_report(classified, passing_avg=70):
    print("\n===== Student Grade Report =====\n")
    
    student_report = {}
    
    passed_student = 0
    failed_student = 0
    
    for name, (avg_score, grade) in classified.items():
        
        if(grade != 'F'):
            passed_student +=  1
            status = 'Pass'
            print(f"Name : {name} | Avg : {avg_score} | Grade: {grade} | Status: {status}")
        
        else:
            failed_student += 1
            status = 'Fail'
            print(f"Name : {name} | Avg : {avg_score} | Grade: {grade} | Status: {status}")
    
        student_report[name] = (avg_score, grade, status)
    count_student = 0
    
    for length in classified.items():
        count_student += 1
    
    print("\n================================\n")
    print(f"Total Student : {count_student}")
    print(f"Passed Student : {passed_student}")
    print(f"Failed Student : {failed_student}")
    
    return student_report

stu = {'Alice':[76,89,92,100], 'Bob':[85,51,60,72], 'Carlo':[79,49,59,60], 'Denise':[]}
    
task_1_result = process_scores(stu)
task_2_result = classify_grades(task_1_result)
task_3_result = generate_report(task_2_result)