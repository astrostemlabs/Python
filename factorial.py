def factorial(n):
    if not isinstance(n,int):
        print ("Factorial is defined for integers only")
        return None
    if n==0:
        return 1
    else:
        recurse=factorial(n-1)
        result=n * recurse
        return result

print(factorial(0.5)) 
