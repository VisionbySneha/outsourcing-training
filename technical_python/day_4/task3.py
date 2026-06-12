marks = {"Rahul":85,
"Priya":90,
"Rohan":65}

for student,score in marks.items():
    if score > 75:
        print(student,"- Pass")
    else:
        print(student,"- Fail")