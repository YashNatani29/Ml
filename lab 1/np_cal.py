import numpy as np
import math

while True:
    x = input('''
    +      Addition
    -      Subtraction
    *      Multiplication
    /      Division
    mod    Modulo
    dot    Dot Product
    sin    sine
    cos    cosine
    tan    tangent
    lg     log -base10
    ln     log -base e
    fact   factorial
    exit   exit
    Enter Operation you want to perform:''')
    if x == 'exit':
        break
    s = int(input("Enter size of array :"))
    arr1 = np.array([])
    arr2 = np.array([])

    for i in range(s):
        z = float(input("Enter element in array 1 :"))
        arr1 = np.append(arr1, z)

    if x == '+' or x == '-' or x == '*' or x == '/' or x == '%' or x == 'dot':
        for i in range(s):
            z = float(input("Enter element in array 2 :"))
            arr2 = np.append(arr2, z)
        print(arr1)
        print(arr2)
        if x == '+':
            ans = arr1 + arr2
        elif x == '-':
            ans = arr1 - arr2
        elif x == '*':
            ans = arr1 * arr2
        elif x == '/':
            p = np.count_nonzero(arr2)
            if p == s:
                ans = arr1 / arr2
            else:
                print("can't divide because of non zero divisor")
        elif x == '%':
            ans = arr1 % arr2
        elif x == 'dot':
            ans = arr1.dot(arr2)
    elif x == 'root':
        ans = np.sqrt(arr1)
    elif x == 'sin':
        ans = np.sin((arr1 * np.pi) / 180)
    elif x == 'cos':
        ans = np.cos((arr1 * np.pi) / 180)
    elif x == 'tan':
        ans = np.tan((arr1 * np.pi) / 180)
    elif x == 'lg':
        ans = np.log10(arr1)
    elif x == 'ln':
        ans = np.log(arr1)
    elif x == 'fact':
        ans = list((math.factorial(x) for x in arr1))
    elif x == 'exit':
        break
    else:
        pass
    print('Ans =>', ans)
