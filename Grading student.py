def gradingStudents(grades):
    for i in range(len(grades)):                       #Here we are taken range becoz we are checking each number from list 
        if grades[i] >= 38 and grades[i] % 5 >= 3 :     #here we have taken grades[i]%5>=3 beacuse take ex: grades[i] = 67 then 67 % 5 = 3 and difference between 67 and 70 is 2 
                                                        #so we have taken this you can go with other apporach as well i.e.. 67/5(int value) * 5 + 5
            if grades[i] % 5 == 3 :
                grades[i] += 2
            elif grades[i] % 5 == 4:
                grades[i] += 1  
    return grades                                  #Here we have to forn a list of grades        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') #From line 11 to 27 the have already given in the solution the main solution is in def function

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
    
    
    #link : https://www.hackerrank.com/challenges/grading/problem?h_r=profile
