'''THis is a test file for STT Lab 1'''

A = 2
B = 3

C = A+B

# Now, we check the value of C

if C==5:
    print("C is 5")
else:
    print("C is not 5")

while C>0:
    print(C)
    C = C-1

if C == 0:
    print("C is 0")

for i in range(5):
    print(i)


def f(a,b):
    '''This is a function to multiply two numbers'''
    return a*b

D = f(A,B)

print(D)

if D == 6:
    print("d is 6")
else:
    print("d is not 6")

print("End of .py file")
