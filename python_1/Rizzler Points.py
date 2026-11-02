assignment_types = {"Test": 100, "Quiz": 75, "Project": 50, "Reading check": 30, "Homework": 10, "No Work": 5}
grade_tiers:{"95-100": 50, "90-95": 40, "85-90": 35, "80-85": 25, "75-80": 18, "73-75": 5, "70-72": 3, "<=70": 1, "No Grade": 0}
class_name : {"AP Physics 1": 1000, "AP Chemistry": 500, "AP Calculus BC": 250, "AP US History": 125, "AP Human Geography": 75, "Engineering Pathway": 50, "All other Honors Classes": 25, "All other CP classes": 15 ,"Gym or Health": 10, "Art and Music Classes": 5, "Authorized Free Period": 3, "No Class" : 0 }
def assignment_points(atype):
    if atype == "Test": return 100
    if atype == "Quiz": return 75
    if atype == "Project": return 50
    if atype == "Reading check": return 30
    if atype == "Homework": return 10
    return 0
def grade_points(grade):
    if grade >= 95: return 50
    if grade >= 90: return 40
    if grade >= 85: return 35
    if grade >= 80: return 25
    if grade >= 75: return 18
    if grade >= 73: return 5
    if grade > 70:  return 3
    return 0  # 70 or below
 
 
def class_points(cl):
    if cl == "AP Physics 1": return 1000
    if cl == "AP Chemistry": return 500
    if cl == "AP Calculus BC": return 250
    if cl == "AP US History": return 125
    if "AP " in cl: 
        return 75
    if cl == "Engineering Pathway": return 50
    if "Honors" in cl: 
     return 25
    if "CP" in cl: 
     return 15
    if cl == "Gym or Health": return 10
    if cl == "Art and Music Classes": return 5
    if cl == "Authorized Free Period": return 3
    if cl == "No Class": return 0
    return 0
    return 15 #If they type any other class that isn't AP or Honors (like "Biology" or "Geometry"),
    # default to 15 points for a standard CP class.


user_name = input("Enter your name: ")
name_class = input("Enter your class :")
type_assignemnt = input("Enter your assignment type: ")
while True:
    grade_input = input("Enter your grade on that assignment: ")
   
    if grade_input.isdigit():  
        grade_as_number = int(grade_input)
        break  
    else:
        print("\nInvalid input! Starting over from the beginning... Please enter a valid number next time.")
        continue  
points_from_class = class_points(name_class)
points_from_assignment = assignment_points(type_assignemnt)
points_from_grade = grade_points(grade_as_number)
total_points = points_from_class + points_from_assignment + points_from_grade
print(f"{user_name} Rizz Point Tracker")
print(f"Class Points : {points_from_class}")
print(f"fAssignment Points : {points_from_assignment}")
print(f"fGrade Points : {points_from_grade}")
print(f"Total Points: {total_points} ")
print("Rizzler Evaluation : ") #This line of code is evaluating if the user is a good, OK, or bad rizzler based on their total points
if total_points > 500:
    print("You are a great rizzler!")
elif total_points >= 250:
    print("You are an OK rizzler.")
elif total_points >= 50:
    print("You are a bad rizzler.")
else:
    print("You are not a rizzler at all.")
print(f"{user_name} Thank you for using my program")
print("See you again. Peace out")
