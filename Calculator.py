import numpy as np
import pandas as pd
import matplotlib as mtp



def calculator ():
    while True:
        A = input("Enter num1 : ")
        operator = input("Enter a operation [+,-,X,/] : ").lower()
        B = input("Enter num2 : ")

        if A.isdigit() and B.isdigit():
            A = int(A)
            B = int(B)
            if operator == "+":
                add(A,B)
            elif operator == "-":
                sub(A,B)
            elif operator == "x":
                mul(A,B)
            elif operator == "/":
                div(A,B)
            while True:
                oncemore = input("Would you like to do another calculatioin [Y/N] : ").lower()
                if oncemore == "y":
                    break
                else:
                    return


        else:
            while True:
                tryagainOp = input("Invalid input,would you like to try again [Y/N] : ").lower()
                if tryagainOp == "y":
                    calculator()
                    break
                elif tryagainOp == "n":
                    print("Thankyou")
                else:
                    print("invalid choice")
                    continue
def add(A,B):
    print(f"{A} + {B} = {A+B}")
def sub(A,B):
    print(f"{A} - {B} = {A-B}")
def mul(A,B):
    print(f"{A} X {B} = {A*B}")
def div(A,B):
    print(f"{A} / {B} = {A/B}")



calculator()