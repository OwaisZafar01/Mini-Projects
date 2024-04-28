# FUNCTION FOR GENERAL KNOWLEDGE
def GeneralKnowledge():
    general_knowledge_score = 0
    print("In this topic we have 3 Questions for you!!")
    print ("•" * 45)

    # First Question for General Knowledge
    print("So your first Question is")
    print ("*" * 27)
    print("Q1: What is the Capital of Pakistan? ")
    print ("•" * 40)

    # Show Option for Question 1
    print("Your options are: ")
    print ("*" * 25)
    print("A: lahore     B: Karachi\nC: KPK        D: Islamabad")
    print ("*" * 30)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)
        if choose_option == "a" or choose_option == "b" or choose_option == "c" :
            print("Your answer is incorrect")
            print ("•" * 25)
            break
        else:
            if choose_option == "d":
                print("Your answer is Correct")
                general_knowledge_score += 10
                print ("•" * 30)
                break

            else:
                print("Choose write option")
                print ("*" * 25)

    # Store General Knowledge score in a variable 
    general_knowledge_score += 0

    # 2nd Question for General Knowledge
    print("Your 2nd Question is")
    print ("*" * 27)
    print("Q2: What is the population of Pakistann? ")
    print ("•" * 40)

    # Show Options for Question 2
    print("Your options are: ")
    print ("*" * 25)
    print("A: 22 Crores    B: 30 Crores\nC: 40 Crores    D: 50 Crores")
    print ("*" * 40)
        
    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "b" or choose_option ==  "c" or choose_option == "d" :
            print("Your answer is incorrect")
            print ("•" * 25)
            break
        
        else:
            if choose_option == "a" :
                print("Your answer is Correct")
                general_knowledge_score += 10
                print ("•" * 25)
                break

            else:
                print("Choose write option")
                print ("*" * 25)

    # Store General Knowledge score in a variable 
    general_knowledge_score += 0

    # 3rd Question for General Knowledge
    print("Your last Question is")
    print ("*" * 27)
    print("Q3: What is the national flower of Pakistan? ")
    print ("•" * 50)

    # Show Options for Question 3
    print("Your options are: ")
    print ("*" * 25)
    print("A: Jasmine      B: Rose\nC: Sunflower    D: Lotus")
    print ("*" * 30)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "b" or choose_option == "c" or choose_option == "d" :
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "a" :
                print("Your answer is Correct")
                general_knowledge_score += 10
                print ("•" * 25)
                break

            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store general_knowledge score in a variable 
    general_knowledge_score += 0

    # Show your general_knowledge score           
    print(f"Your score for this topic is {general_knowledge_score}")
    print ("x" * 30)
   
# FUNCTION FOR MATHEMATICS
def Mathematics():
    mathematics_score = 0
    print("In this topic we have 3 Questions for you!!")
    print ("•" * 45)

    # First Question for Mathematics
    print("So your first Question is")
    print ("*" * 27)
    print("Q1: What is the square root of 5? ")
    print ("•" * 40)

    # Show Options for Question 1
    print("Your options are: ")
    print ("*" * 25)
    print("A: 15     B: 10\nC: 25     D: 50")
    print ("*" * 30)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "a" or choose_option == "b" or choose_option == "d" :
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "c" :
                print("Your answer is Correct")
                mathematics_score += 10
                print ("•" * 25)
                break
            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store Mathematics score in a variable             
    mathematics_score += 0

    # 2nd Question for Mathematics
    print("Your 2nd Question is")
    print ("*" * 27)
    print("Q2: What is the factorial of 5? ")
    print ("•" * 40)

    # Show Options for Question 2
    print("Your options are: ")
    print ("*" * 25)
    print("A: 120    B: 90 \nC: 30     D: 60")
    print ("*" * 40)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "b" or choose_option == "c" or choose_option == "d":
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "a" :
                print("Your answer is Correct")
                mathematics_score += 10
                print ("•" * 25)
                break

            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store Mathematics score in a variable             
    mathematics_score += 0

    # 3rd Question for Mathematics
    print("Your last Question is")
    print ("*" * 27)
    print("Q3: What is the deravative of x ")
    print ("•" * 40)

    print("Your options are: ")
    print ("*" * 25)
    print("A: 1     B: x\nC: 0     D: infinity")
    print ("*" * 30)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "b" or choose_option == "c" or choose_option == "d" :
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "a" :
                print("Your answer is Correct")
                mathematics_score += 10
                print ("•" * 25)
                break

            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store Mathematics score in a variable             
    mathematics_score += 0

    # Show your Mathematics score
    print(f"Your score for this topic is {mathematics_score}")
    print ("x" * 30)

# FUNCTION FOR CHEMISTRY   
def Chemistry():
   
    chemistry_score = 0
    print("In this topic we have 3 Questions for you!!")
    print ("•" * 45)

    # First Question for Chemistry
    print("So your first Question is")
    print ("*" * 27)
    print("Q1: What is the chemical formula of water? ")
    print ("•" * 40)

    # Show Options for Question 1
    print("Your options are: ")
    print ("*" * 25)
    print("A: CH2    B: H20\nC: NH3    D: CaCl3")
    print ("*" * 30)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "a" or choose_option == "c" or choose_option == "d" :
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "b" :
                print("Your answer is Correct")
                chemistry_score += 10
                print ("•" * 25)
                break

            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store Chemistry score in a variable            
    chemistry_score += 0

    # 2nd Question for Chemistry 
    print("Your 2nd Question is")
    print ("*" * 27)
    print("Q2: What is NH3 stands for? ")
    print ("•" * 40)

    # Show Options for Question 2
    print("Your options are: ")
    print ("*" * 25)
    print("A: Ammonia         B: Nitric oxide \nC: Oxalic Acid     D: Sodium Chloride")
    print ("*" * 40)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "b" or choose_option == "c" or choose_option == "d":
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "a" :
                print("Your answer is Correct")
                chemistry_score+= 10
                print ("•" * 25)
                break

            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store Chemistry score in a variable       
    chemistry_score+= 0

    # 3rd Question for Chemistry
    print("Your last Question is")
    print ("*" * 27)
    print("Q3: Another name of H20? ")
    print ("*" * 40)

    # Show Options for Question 3
    print("Your options are: ")
    print ("*" * 25)
    print("A: Protein     B: Calcium\nC: Liquid      D: Aqua Regia")
    print ("*" * 30)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "a" or choose_option == "b" or choose_option == "c":
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "d" :
                print("Your answer is Correct")
                chemistry_score += 10
                print ("•" * 25)
                break

            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store Chemistry score in a variable         
    chemistry_score += 0

    # Show your Chmistry score
    print(f"Your score for this topic is {chemistry_score}")
    print ("x" * 30)

# FUNCTION FOR PHYSICS
def Physics():
    physics_score = 0
    print("In this topic we have 3 Questions for you!!")
    print ("•" * 45)

    # First Question for Physics 
    print("So your first Question is")
    print ("*" * 27)
    print("Q1: What is the SI unit of force? ")
    print ("•" * 40)

    # Show Options for Question 1
    print("Your options are: ")
    print ("*" * 25)
    print("A: Newton (N)    B: Watt (W)\nC: Joule (J)     D: Pascal (Pa)")
    print ("*" * 30)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "b" or choose_option == "c" or choose_option == "d":
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "a" :
                print("Your answer is Correct")
                physics_score += 10
                print ("•" * 25)
                break

            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store Physics score in a variable     
    physics_score += 0

    # 2nd Question for Physics 
    print("Your 2nd Question is")
    print ("*" * 27)
    print("Q2: Which of the following is a scalar quantity? ")
    print ("•" * 45)

    # Show Options for Question 2
    print("Your options are: ")
    print ("*" * 25)
    print("A: Velocity        B: Force \nC: Speed           D: Acceleration")
    print ("*" * 40)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "a" or choose_option == "b" or choose_option == "d" :
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "c" :
                print("Your answer is Correct")
                physics_score+= 10
                print ("•" * 25)
                break

            else: 
                print("Choose write option")
                print ("*" * 25)

    # Store Physics score in a variable    
    physics_score+= 0

    # 3rd Question for Physics
    print("Your last Question is")
    print ("*" * 27)
    print("Q3: What is the SI unit of power?? ")
    print ("•" * 40)

    # Show Options for Question 3
    print("Your options are: ")
    print ("*" * 25)
    print("A: Watt (W)         B: Joule (J)\nC: Newton (N)       D: Meter per second (m/s)")
    print ("*" * 30)

    while True:
        choose_option = input("Choose your correct option: ")
        choose_option = choose_option.lower()
        print ("*" * 25)

        if choose_option == "b" or choose_option == "c" or choose_option == "d" :
            print("Your answer is incorrect")
            print ("•" * 25)
            break

        else:
            if choose_option == "a" :
                print("Your answer is Correct")
                physics_score += 10
                print ("•" * 25)
                break
            else: 
                print("Choose write option")
                print ("*" * 25) 

    # Store Physics score in a variable 
    physics_score += 0

    # Show your Physics score 
    print(f"Your score for this topic is {physics_score}")
    print ("x" * 30)
           


















