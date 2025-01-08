name=print("enter the name: ")
english=float(input("enter the marks in english: "))
marathi=float(input("enter the marks in marathi: "))
maths=float(input("entre the marks in maths: "))
hindi=float(input("enetr the marks in hindi: "))
total=(english+maths+marathi+hindi)/5
if(total>80):
    print("congradulation you have got best percentage")
else:
    print("you are in lower position")