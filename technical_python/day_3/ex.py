try:
    num = int(input("enter the number"))
    print(10/num)
except ZeroDivisionError:
    print("dont divide with zero")

except ValueError:
    print("type number only")