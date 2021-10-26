


# Take the following list

students = [{"name": "Steve", "score": 88}, {"name": "Becky", "score": 99}, {"name": "Chad", "score": 76}]

# And print out each of the students' names, scores, and grade they would receive (90-100 A, 80-90 B, etc)
# "Steve got a(n) 88, so this student received a(n) B"


for student in students:
    if student['score'] < 80:
        print(f"{student['name']} got an {student['score']}, so this student recieved a C")
    elif student['score'] < 90:
        print(f"{student['name']} got an {student['score']}, so this student recieved a B")
    elif student['score'] < 100:
        print(f"{student['name']} got an {student['score']}, so this student recieved an A")
    else:
        print("no more names")
