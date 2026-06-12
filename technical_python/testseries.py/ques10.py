student = {"Rahul": {"age": 20,"marks":85},
           "Tanu":{"age":21,"marks":40},
           "Ritu":{"age":23,"marks":88}
           }


student["Sneha"] = {"age":20,"marks":93}
print(student)


student["Rahul"]["marks"]= 78
print(student)


del student["Tanu"]
print(student)

if "Chirag" in student:
    print("Chirag exists")
else:
    print("Chirag is missing")

