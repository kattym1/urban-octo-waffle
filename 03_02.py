
score = input("Enter Score: ")
try:
    s=float(score)
except:
    print("error, please enter numeric values")
    quit()
if (s>=0.0 and s<=1.0):

    if s>=0.9:
        print("A")
    elif s>=0.8:
        print("B")
    elif s>=0.7:
        print("C")
    elif s>=0.6:
        print("D")
    else:
        print("F")
else:
    print("Insert numeric values between 0.0 and 1.0")
    quit()
