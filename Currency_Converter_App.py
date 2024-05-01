# Define a function to display the currency conversion options
def converter():                                    
# Welcome message and menu
    print("Welcome to Money Converter App")
    print("*" * 40)

    print("1: PKR_TO_USD")
    print("2: USD_TO PKR")
    print("3: PKR_TO_EURO")
    print("4: EURO_TO_PKR")
    print("5: PKR_TO_GBP")
    print("6: GBP_TO_PKR")
    print("7: PKR_TO_AED")
    print("8: AED_TO_PKR")
    print("9: EXIT")
    print("*" * 25)

# Define conversion rates for different currency pairs                          
PKR_TO_USD = 280                                
PKR_TO_USD = 280
PKR_TO_EURO = 305
PKR_TO_GBP = 355                                           
PKR_TO_AED = 75

# Define the function to perform currency conversion
def exchange_currecy():                         
    while True:
        # Loop for continuous operation until the user exits
        choice = (input("Enter your choice: "))             
        print("*" * 25)
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice,Enter a Number")
            print("*" * 25)
            continue

        # Perform the selected currency conversion based on user input
        if choice == 1:
            while True:
                pkr_choice = input("Enter amount in Pkr: ")
                try:
                    pkr_choice = float(pkr_choice)
                    break
                except ValueError:
                    print("Enter amount in digits")
                    print("*" * 25)
                    continue
            # Perform the currency conversion and display the result
            print(f"{round(pkr_choice / PKR_TO_USD, 3)}$")
            print("*" * 25)

        elif choice == 2:
            while True:
                usd_choice = input("Enter amount in Dollar: ")
                try:
                    usd_choice = float(usd_choice)
                    break
                except ValueError:
                    print("Enter amount in digits")
                    print("*" * 25)
                    continue
            # Perform the currency conversion and display the result
            print(f"{round(usd_choice * PKR_TO_USD, 3)}pkr")
            print("*" * 25)

        elif choice == 3:
            while True:
                pkr_choice = input("Enter amount in Pkr: ")
                try:
                    pkr_choice = float(pkr_choice)
                    break
                except ValueError:
                    print("Enter amount in digits")
                    print("*" * 25)
                    continue

            # Perform the currency conversion and display the result
            print(f"{round(pkr_choice / PKR_TO_EURO, 3)}euro")
            print("*" * 25)

        elif choice == 4:
            while True:

                euro_choice = input("Enter amount in Euro: ")
                try:
                    euro_choice = float(euro_choice)
                    break
                except ValueError:
                    print("Enter amount in digits")
                    print("*" * 25)
                    continue

            # Perform the currency conversion and display the result
            print((f"{round(euro_choice * PKR_TO_EURO, 3)}pkr"))
            print("*" * 25)

        elif choice == 5:
            while True:
                pkr_choice = input("Enter amount in Pkr: ")
                try:
                    pkr_choice = float(pkr_choice)
                    break
                except ValueError:
                    print("Enter amount in digits")
                    print("*" * 25)
                    continue

            # Perform the currency conversion and display the result
            print((f"{round(pkr_choice / PKR_TO_GBP, 3)}GBP"))
            print("*" * 25)

        elif choice == 6:
            while True:
                gbp_choice = int(input("Enter amount in GBP: "))
                try:
                    gbp_choice = float(gbp_choice)
                    break
                except ValueError:
                    print("Enter amount in digits")
                    print("*" * 25)
                    continue

            # Perform the currency conversion and display the result
            print((f"{round(gbp_choice * PKR_TO_GBP, 3)}pkr"))
            print("*" * 25)

        elif choice == 7:
            while True:
                pkr_choice = int(input("Enter amount in Pkr: "))
                try:
                    pkr_choice = float(pkr_choice)
                    break
                except ValueError:
                    print("Enter amount in digits")
                    print("*" * 25)
                    continue

            # Perform the currency conversion and display the result
            print(f"{round(pkr_choice / PKR_TO_AED, 3)}AED")
            print("*" * 25)
        
        elif choice == 8:
            while True:
                aed_choice = int(input("Enter amount in AED: "))
                try:
                    aed_choice = float(aed_choice)
                    break
                except ValueError:
                    print("Enter amount in digits")
                    print("*" * 25)
                    continue

            # Perform the currency conversion and display the result
            print(f"{round(aed_choice * PKR_TO_AED, 3)}pkr")
            print("*" * 25)

        # Handle the exit option
        elif choice == 9 :
            print("Thankyou for using Converter App")
            print("x" * 35)
            break

        else:
            print("Invalid Choice,Enter Choice between 1 to 9")
            print("*" * 47)

# Call the converter function to display the menu
converter()    
#Call the exchange_currency function to perform currency conversions                      
exchange_currecy()






































