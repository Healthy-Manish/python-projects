def add(a,b):
    answer = a+b
    print(str(a)+' + '+str(b)+' = '+str(answer))

def sub(a,b):
        answer = a-b
        print(str(a)+' - '+str(b)+' = '+str(answer))

def mul(a,b):
          answer = a*b
          print(str(a)+' x '+str(b)+' = '+str(answer))
        
def div(a,b):
          answer = a/b
          print(str(a)+' / '+str(b)+' = '+str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter your choice: ")
    if choice.lower() == 'a':
            print("Addition")
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            add(a,b)
            print("********************************")
    elif choice.lower()=='b':
                print("Subtraction")
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                sub(a,b)
                print("********************************")

    elif choice.lower()=='c':
                print("Multiplication")
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                mul(a,b)
                print("********************************")

    elif choice.lower()=='d':
                print("Division")
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                div(a,b)
                print("********************************")

    else:
            print("Exiting the programm")
            quit()