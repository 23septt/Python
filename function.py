def calculate_average(scores):
    summ = float(0)
    count = 0
    for i in scores :
      count +=1
      summ += i
    return summ/count
def get_grade(average_score):

    if average_score >= 80 :
      return "A"
    elif average_score >= 75 :
      return "B+"
    elif average_score >= 70 :
      return "B"
    elif average_score >= 65 :
      return "C+"
    elif average_score >= 60 :
      return "C"
    elif average_score >= 55 :
      return "D+"
    elif average_score >= 50 :
      return "D"
    else :
      return "F"

def process_student_data(stu_data):
 
    name , score = stu_data
    grade = get_grade(calculate_average(score))
    return [name,grade]
    
def print_students_ranked_by_grades(list_of_stu_data):
    output = []
    for i in range(len(list_of_stu_data)) :
       output.append(process_student_data(list_of_stu_data[i]))
    rank = {"A" : 0 ,"B+" : 1 , "B" : 2 ,"C+" : 3 , "C" : 4 ,"D+" : 5 , "D" : 6 , "F" : 7}
    output.sort(key = lambda x : (rank[x[1]] , x[0]))
    for n , g in output :
       print(n,g)
       
# ห้ามแก ้ไขบรรทัดข ้างล่างทั4งหมดนี4
while (cmd:=input().strip()):
 exec(cmd)
 if cmd[-1]==';': break