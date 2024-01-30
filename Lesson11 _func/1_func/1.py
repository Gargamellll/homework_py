#1.Write a Python function to find the Max of three numbers.
def max_func(a,b,c):
    result=0
    for i in a,b,c:
        if i<a:
            result=a
            return result
        elif i<b:
            result=b
            return result
        elif i<c:
            result=c
            return result
    print(result)
            
print(max_func(10,33,5))             

