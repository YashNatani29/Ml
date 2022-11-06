# Bisection Method.
# The function is x^2 - x - 2
def func(x):
    return x * x - x - 2


# Prints root of func(x)
# with error of EPSILON
def bisection(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b\n")
        return

    c = a
    while (b - a) >= 0.01:

        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if func(c) == 0.0:
            break

        # Decide the side to repeat the steps
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        print(a, "\t", b)

    print("The value of root is : ", "%.4f" % c)


# Driver code
# Initial values assumed
A = 00
B = 3
print("A\t\t\tB")
bisection(A, B)



# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result

    for i in range(1000000):

        # Find the point that touches x axis
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        # Check if the above found point is root
        if func(c) == 0:
            break

        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        print(a, "\t", b)
    print("The value of root is : ", '%.4f' % c)


# Driver code to test above function
# Initial values assumed
print("\nfalse positioning method\nA\t\tB")
regulaFalsi(A, B)

