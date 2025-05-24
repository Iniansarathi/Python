
def calculator ():
    A = float(input("Enter num1 : "))
    operator = input("Enter a operation [+,-,X,/] : ")
    B = float(input("Enter num2 : "))

    def operation(A, B, operator):
        if operator == "+":
            print(f"{int(A)} + {int(B)} = {int(A + B)}")
    operation (A,B,operator)


calculator()