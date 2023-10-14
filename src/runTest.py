from itertools import product
from sympy.logic.boolalg import Or, And
from sympy.logic.inference import satisfiable
from sympy.logic.boolalg import to_cnf
from sympy.logic.boolalg import simplify_logic
from sympy.abc import symbols

def perform_main_option_1(choice):
    print(f"You chose option 1, command {choice}. Performing function for Boolean Algebraic Function - MIN SOP.")
    minT = input("Enter the Sum of Product Terms separated by a space: ")
    v_in = input("Enter input variables separated by a space: ")
    
    if choice == 1: 
        print("Canonical SOP: ", minterms_to_expression(list(map(int, minT.split())), v_in.split()))

    elif choice == 2: 
        print("Canonical POS expression: (", minterms_to_pos_expression(list(map(int, minT.split())), v_in.split()), ")")
    
    elif choice == 3:
        print("Inverse as a Canonical SOP: (", calculate_inverse_SOP(list(map(int, minT.split())), v_in.split()), ")")

    elif choice == 4: 
        print("Inverse as a Canonical POS: (", calculate_inverse_POS(list(map(int, minT.split())), v_in.split()), ")")

    elif choice == 5: 
        print("Reduced Literals as SOP: ", reduced_minterms(minterms_to_expression(list(map(int, minT.split())), v_in.split())))
    #elif choice == 6: 
    
    #elif choice == 7: 
    
    #elif choice == 8:
    
    #elif choice == 9:
    
    #elif choice == 10: 
    
    #elif choice == 11:  
    
    else:
        print("Break") 

def perform_main_option_2(choice):
    print(f"You chose option 2, command {choice}. Performing function for Digital Combination Logic Circuit.")
    #if choice == 1: 

    #elif choice == 2: 
    
    #elif choice == 3:

    #elif choice == 4: 

    #elif choice == 5: 
    
    #elif choice == 6: 
    
    #elif choice == 7: 
    
    #elif choice == 8:
    
    #elif choice == 9:
    
    #elif choice == 10: 
    
    #elif choice == 11:  
    
    #else:
        
##bool 
def minterms_to_expression(minterms, variables):
    # Sort and remove duplicates from the list of minterms
    minterms = sorted(set(minterms))

    # Initialize an empty list to store boolean expressions for each minterm
    expressions = []

    # Convert each minterm to a boolean expression
    for minterm in minterms:
        # Convert the minterm to binary and pad with zeros to match the number of variables
        binary_minterm = format(minterm, '0b').zfill(len(variables))

        # Create a boolean expression for the minterm
        expression = ""
        for i, bit in enumerate(binary_minterm):
            if bit == '0':
                expression += f"~{variables[i]} & "
            elif bit == '1':
                expression += f"{variables[i]} & "

        # Remove the trailing "&" and add the expression to the list
        expressions.append(expression[:-2])

    # Combine the boolean expressions using OR operations
    sum_of_minterms = " | ".join(expressions)

    return sum_of_minterms

def minterms_to_pos_expression(minterms, variables):
    # Sort and remove duplicates from the list of minterms
    num_vars = len(variables)
    all_values = list(range(2 ** num_vars - 1, -1 , -1))
    # Remove values that are in minterms to get maxterms
    remaining_values = [value for value in all_values if value not in minterms]
    expressions = []
    # Convert each maxterm to a boolean expression
    for maxterm in remaining_values:
        # Convert the maxter, to binary and pad with zeros to match the number of variables
        binary_maxterm = format(maxterm, '0b').zfill(num_vars)

        # Create a boolean expression for the minterm
        expression = ""
        for i, bit in enumerate(binary_maxterm):
            if bit == '0':
                expression += f"{variables[i]} + "
            elif bit == '1':
                expression += f"~{variables[i]} + "

        # Remove the trailing "|"
        expressions.append(expression[:-2])

    # Combine the boolean expressions using AND operations
    product_of_sums = ") & ( ".join(expressions)

    return product_of_sums

def calculate_inverse_SOP(minterms, variables):
    num_vars = len(variables)
    all_values = list(range(2 ** num_vars))
    # Remove values that are in minterms to get maxterms
    remaining_values = [value for value in all_values if value not in minterms]
    expressions = []
    # Convert each maxterm to a boolean expression
    for minterm in remaining_values:
        # Convert the maxter, to binary and pad with zeros to match the number of variables
        binary_maxterm = format(minterm, '0b').zfill(num_vars)

        # Create a boolean expression for the minterm
        expression = ""
        for i, bit in enumerate(binary_maxterm):
            if bit == '0':
                expression += f"~{variables[i]}  "
            elif bit == '1':
                expression += f"{variables[i]}  "

        # Remove the trailing "+"
        expressions.append(expression[:-2])

    # Combine the boolean expressions using AND operations
    inverse_SOP = ") + ( ".join(expressions)
    return inverse_SOP

def calculate_inverse_POS(minterms, variables):
    
    # Remove values that are in minterms to get maxterms
    remaining_values = minterms[::-1]
    print(remaining_values)
    expressions = []
    # Convert each maxterm to a boolean expression
    for maxterm in remaining_values:
        # Convert the maxter, to binary and pad with zeros to match the number of variables
        binary_maxterm = format(maxterm, '0b').zfill(len(variables))

        # Create a boolean expression for the minterm
        expression = ""
        for i, bit in enumerate(binary_maxterm):
            if bit == '0':
                expression += f"{variables[i]} + "
            elif bit == '1':
                expression += f"~{variables[i]} + "

        # Remove the trailing "+"
        expressions.append(expression[:-2])

    # Combine the boolean expressions using AND operations
    inverse_POS = ") & ( ".join(expressions)
    return inverse_POS

def reduced_minterms(minterms):
    return simplify_logic(to_cnf(minterms))

#Command Line Experience
def main():
    while True:
        print("Input Options:")
        print("1. Boolean Algebraic Function - MIN SOP")
        print("2. Digital Combination Logic Circuit" )
        print("0. Exit \n")

        main_choice = int(input("Enter your input choice: "))

        if main_choice == 0:
            print("Thanks for using our program. Goodbye!")
            break
        
        
        if main_choice == 1 or main_choice == 2:
            print("Commands:")
            print("1. Canonical SOP")
            print("2. Canonocal POS")
            print("3. Inverse as Canonical SOP")
            print("4. Inverse as Canonical POS")
            print("5. Minimized Number of Literals in SOP")
            print("6. Minimized number of literals in POS ")
            print("7. # of Prime Implicants")
            print("8. # of Essential Prime Implcants ")
            print("9. # of ON-Set Minterms")
            print("10. # Of ON-Set Maxterms ")
            print("11. ")
            print("12. \n")

            command = int(input("Enter your command: "))

            if main_choice == 1:
                perform_main_option_1(command)
            elif main_choice == 2:
                perform_main_option_2(command)
            else:
                print("Invalid command. Please enter a valid command.")

        else:
            print("Invalid choice. Please enter a valid main option.")

        another_command = input("Do you want to perform another command? (yes/no): ")
        if another_command.lower() != 'yes':
            print("Thanks for using our program. Goodbye!")
            break

if __name__ == "__main__":
    main()

