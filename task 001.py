# task 1 factorial

def fact(n):
    if n<2:
        return 1
    else:

        return n*fact(n-1)




number =5
res=fact(number)
print("Entered number is:",number)
print("Factorial of",number,"is",res)


