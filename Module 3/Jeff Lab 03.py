ef main():
    L = (eval(input("What is the length of the rectangle in inches? ",)))
    W = (eval(input("What is the width of the rectangle in inches? ",)))
    P = (2*L)+(2*W)
    print("The perimeter of your rectangle is ",P)
    T1=(P//12+1)
    T2=(P/12)
    print("The amount of trim that you'll need is ",T1, "or if you want to be more exact ",round(T2,2))
    C1= (T1*1.88)
    C2= (int(C1/12))
    print ("The cost of the trim is $",round(C1,2),)
    W1= (18*12) - (P)
    W2= (W1*(1.88/12))
    print("The waste in inches of trim is",round(W1,2),"and the waste in money is $",round(W2,2))

main()
