a=8
b=2
try:
    print("Resource open")
    print(a/b)
    k=int(input())
    print(k)
except ZeroDivisionError as e:
    print("Cannot divide a number by zero",e)
except ValueError as e:
    print("Invalid Input",e)
finally:
   print("Resource Closed")
