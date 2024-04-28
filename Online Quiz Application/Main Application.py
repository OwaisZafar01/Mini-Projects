from Online_Quiz_Application import *

print('Welcome to "Owais Academy Quiz Application"')
print ("*" * 48)

print("OUR TOPICS: ")
print ("*" * 13)

print("1: General Knowledge\n2: Mathematics\n3: Chemistry\n4: Physics\n5: Exit")
print ("*" * 22)

while True:
    choice = int(input("Enter your choice: "))
    print("*" * 30)
    if choice == 1:
        GeneralKnowledge()

    elif choice == 2:
        Mathematics()

    elif choice == 3:
        Chemistry()
    
    elif choice == 4:
        Physics()
    
    elif choice == 5:
        print("Thankyou for using the Quiz Application, Goodbye!")
        print("x" * 50)
        break

    else:
        print("Enter valid choice")
        print("*" *25)




