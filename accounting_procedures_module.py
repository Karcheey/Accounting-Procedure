
# define a function for total shift sales
def total_shift_sales():
    morning_shift_sales = float(input('Morning shift sales: '))
    evening_shift_sales = float(input('Evening shift sales: '))

    # Pass the shift sales into a list
    total_shift_sales_list = [morning_shift_sales,evening_shift_sales]
    total_shift_sales = morning_shift_sales + evening_shift_sales
    print('')
    
    a = print(f"The Total shift sales is '{total_shift_sales}'")
    return a


# define a function to calculate worker's salary
def workers_salary():
    try:
        # define hourly rate
        hourly_rate = float(input('Enter pay per hour: '))

        try:
            # define hours worked by worker
            hours_worked_by_worker = int(input('Enter number of hours worked: '))

            # determine worker's salary
            worker_salary = hourly_rate * hours_worked_by_worker
            print('')
            
            a = print(f"Worker's salary is '₦{worker_salary}'")

            return a
        
        except ValueError:
            print('')
            print('Invalid entry!')
            print('Please enter a whole number,try again.')
            
    except ValueError:
        print('')
        print('Invalid entry!')
        print('Please enter an amount,try again.') 


# define a function to calculate Profit
def profit_or_loss():
    try:
        morning_shift_sales = float(input('Morning shift sales: '))
        evening_shift_sales = float(input('Evening shift sales: '))

        # Pass the shift sales into a list
        total_shift_sales_list = [morning_shift_sales,evening_shift_sales]
        total_shift_sales = morning_shift_sales + evening_shift_sales

        # define morning shift cost
        morning_shift_cost = float(input('Morning shift cost: '))

        # define evening shift cost
        evening_shift_cost = float(input('Evening shift cost: '))

        # Pass the shift cost into a list
        total_shift_cost_list = [morning_shift_cost,evening_shift_cost]

        # total shift cost
        total_shift_cost = morning_shift_cost + evening_shift_cost


        # define the profit
        profit = abs(total_shift_sales-total_shift_cost)

        if total_shift_sales < total_shift_cost:
            print('')
            a = print(f"The loss made is '₦{profit}'")
            return a
        else:
            print('')
            b = print(f"The profit made is '₦{profit}'")
            return b
    
    except ValueError:
        print('')
        print('Invalid entry!')
        print('Please enter an amount,try again.')


# define a function to achieve this
def tips():
    try:
        # Define the shift sales
        morning_shift_sales = float(input('Morning shift sales: '))
        evening_shift_sales = float(input('Evening shift sales: '))

        # Pass the shift sales into a list
        total_shift_sales_list = [morning_shift_sales,evening_shift_sales]

        # define tips for a shift into a list
        tips_for_a_shift = [0.02*i for i in total_shift_sales_list]

        try:
            # Create a user-friendly interface that displays a menu of available operations.
            while True:
                print('')
                print(' Calculate tips for a shift')
                print('1. Morning shift')
                print('2. Evening shift')
                print('3. Total tips for the day')
                print('4. Exit')

                calculate_tips = int(input('Please enter shift(1 - 3): '))
                if calculate_tips == 1:
                    print('')
                    print(f"The Tips for Morning shift is '₦{round(tips_for_a_shift[0],2)}'")
                elif calculate_tips == 2:
                    print('')
                    print(f"The Tips for Evening shift is '₦{round(tips_for_a_shift[1],2)}'")
                # Calculate Total tips for the day
                elif calculate_tips == 3:
                    print('')
                    print(f"The Total tips for the day is '₦{round(tips_for_a_shift[0]+tips_for_a_shift[1],2)}'")
                # Provide an option for users to exit the  program.
                elif calculate_tips == 4:
                    break
                # Accept only numbers from 1 to 4
                else:
                    print('')
                    print('Invalid choice. Please enter a number between 1 and 4.')
        except ValueError:
                print('')
                print('Invalid entry!')
                print('Please enter a valid entry,try again.')
    except ValueError:
        print('')
        print('Invalid entry!')
        print('Please enter an amount,try again.')


# define the absolute function for the accounting procedures
def accounting_procedures():
     # Create a user-friendly interface that displays a menu of available operations.
            while True:
                print('')
                print(' Accounting procedures')
                print('1. Calculate Total sales for the day')
                print('2. Calculate workers salary')
                print('3. Calculate Profit or Loss')
                print('4. Calculate Total Tips and Tips for a shift')
                print('5. Exit')
                
                accounting_procedures = int(input('Please enter a number(1 - 5): '))
                if accounting_procedures == 1:
                    total_shift_sales()
                elif accounting_procedures == 2:
                    workers_salary()
                # Calculate Total tips for the day
                elif accounting_procedures == 3:
                    profit_or_loss()
                elif accounting_procedures == 4:
                    tips()
                # Provide an option for users to exit the  program.
                elif accounting_procedures == 5:
                    break
                # Accept only numbers from 1 to 5
                else:
                    print('')
                    print('Invalid choice. Please enter a number between 1 and 5.')
                    
