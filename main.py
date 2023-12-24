from factorial import fact
from exponantional import exp2, exp3
from root import root2, root3
from logarithm import lg, ln, log

def main():
    print("1. Factorial")
    print("2. Exponentiation")
    print("3. Roots")
    print("4. Logarithms")
    print("-"*50)

    while True:

        choice = input("\nChoose an option or print '0' to finish: ")

        if choice == '1':
            while True:
                try:
                    num = int(input("\nEnter a number to find factorial: "))
                    print("-"*50)
                    result = fact(num)
                    print(f"The factorial is: {result}")
                    break
                except ValueError:
                    print("\nInvalid input.Try again.")

        elif choice == '2':
            while True:
                try:
                    num = float(input("\nInput х:"))
                    exp_choice = input("Choose exponent (2 or 3): ")
                    if exp_choice == '2':
                        result = round(exp2(num), 3)
                        print("-"*50)
                        print(f"Result: {result}")
                        break
                    elif exp_choice == '3':
                        result = round(exp3(num), 3)
                        print("-"*50)
                        print(f"Result: {result}")
                        break
                    else:
                        print("\nInvalid choice.Try again.")
                        continue
                    break
                except ValueError:
                    print("\nInvalid input.Try again.")
            
        elif choice == '3':
            while True: 
                try:
                    num = float(input("\nEnter a number for root: "))
                    root_choice = input("Choose root (2 or 3): ")
                    if root_choice == '2':
                        result = round(root2(num), 3)
                        print("-"*50)
                        print(f"Result: {result}")
                        break
                    elif root_choice == '3':
                        result = round(root3(num), 3)
                        print("-"*50)
                        print(f"Result: {result}")
                        break
                    else:
                        print("\nInvalid choice.Try again.")
                        continue
                    break
                except ValueError:
                    print("\nInvalid input.Try again.")

        elif choice == '4':
            while True:
                try:
                    log_choice = input("Choose logarithm (lg, ln, log): ")
                    num = float(input("\nEnter a number for logarithm: "))
                    if log_choice == 'lg':
                        result = round(lg(num), 3)
                        print("-"*50)
                        print(f"Result: {result}")
                        break
                    elif log_choice == 'ln':
                        result = round(ln(num), 3)
                        print("-"*50)
                        print(f"Result: {result}")
                        break
                    elif log_choice == 'log':
                        base = float(input("Enter base: "))
                        result = round(log(num, base), 3)
                        print("-"*50)
                        print(f"Result: {result}")
                        break
                    else:
                        print("\nInvalid choice.Try again.")
                        continue
                    break 
                except ValueError:
                    print("\nInvalid input.Try again.") 
        elif choice == "0":
            print("Goodbye! PrOgRaM iS oVeR~~~")
            break
    
if __name__ == "__main__":
    main()
