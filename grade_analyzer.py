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

    
stu = {'Alice':[70,80,90], 'Bob':[40,50,60],'Carlo':[]}    

#process_scores(stu)

print(process_scores(stu))
