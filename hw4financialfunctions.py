


"""
# HW 4 - Financial Functions

## Background

In financial calculations, there are some core formulas that are used everyday.
These formulas are:

- Present Value (PV):  The value of an income/expense stream as of right now.
    See also: https://en.wikipedia.org/wiki/Present_value
- Future Value (FV):  The value of an income/expense stream in the future.
    See also: https://en.wikipedia.org/wiki/Future_value
- Payment (PMT):  The calculated payment required to achieve a specific FV.
    This is typically associated with as the "monthly" payment.
    See also: https://en.wikipedia.org/wiki/Mortgage_calculator

FV and PV can be found by using this formula (Note: ^ denotes an exponent):

FV = PV x (1 + r) ^ n

where r = simple interest rate; n = number of payment periods.  Rearranging the
above, PV is easily found:

PV = FV / (1 + r) ^ n

PMT can be found using this formula:

P = (r x PV) / (1 - (1 + r) ^ -n)

Where r = simple interest rate; n = number of payment periods.

## Description

For this assignment, modify the functions "pv" and "fv" to prompt the user for
the appropriate variables needed:

- FV or PV: A floating point number that represents the FV if calculating PV or
    PV if calculating FV.
- r: A floating point number that represents the simple interest rate
- n: An integer number that represents the number of payment periods

Next, assume that for "pmt", these variables have already been prompted for you
and are being passed into the function that your creating and therefore there
is no need to prompt the user for those values.

### Example usage

>>> python3 hw4_fin.py
Would you like to calculate FV [1], PV [2], or PMT [3]?
1
Please enter PV:
100000.00
Please enter r:
0.0375
Please enter n:
30
Your expected Future Value is: $301747.14

## Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

### Requirements
- You *must* use `input` to prompt the user for the values.
- You *must* prompt the user for the inputs in this order:
    - PV or FV
    - r
    - n
- You *must* NOT prompt the user for variables for the function pmt.  Instead
    assume these values have already been given to you as the variables PV, r,
    and n.
- You *must* print out the calculated value to the user without any integer
    rounding.  You may round the decimal values.
"""

def fv():
    # START: Your Code here

    print('Please Enter A PV')
    pv = float(input("PV: "))

    print('Please enter an r value ')
    r = float(input("r: "))

    print('Please enter an n value ')
    n = float(input("n: "))

    user_inputs = [pv, r , n]

    future_value = pv * ((1 + r ) ** n)
    future_value_str = str(future_value).split('.')[0]
    
    print('Your future value is: ', (future_value))
    print('future_value_str: ', future_value_str)



    pass
    # END: Your code here

def pv():
    # START: Your code here

    print('Please Enter A FV ')
    fv = float(input("FV: "))

    print('Please enter an r value ')
    r = float(input("r: "))

    print('Please ente® an n value')
    n = float(input("n: "))

    user_inputs = [fv, r , n]

    present_value = fv / ((1 + r) ** n)
    present_value_str = str(present_value).split('.')[0]

    print('Your present value is:', str(present_value))
    print('present_value_str:', present_value_str)

    pass
    # END: Your code here

def pmt(PV, r, n):
    # START: Your code here
    print(PV, r, n)

    payment = (r * PV) / 1 - (1 + r) ** -n 
    payment_str = str(payment).split('.')[0]

    print('Your payment is:', (payment))
    print('payment_str: ', payment_str)
    
    pass
    # END: Your code here


if __name__ == "__main__":
    # NOTE: Altering this code may result in unexpected behaviors when you run
    # to debug.  Beware.
    funcs = {
        "1": fv,
        "2": pv,
        "3": pmt
    }
    print("Would you like to calculate FV [1], PV [2], or PMT [3]?")
    selection = input("Selection: ")
    func = funcs.get(selection, lambda: print("Invalid selection, quitting"))
    if selection == "3":
        print("Please enter r:")
        r = float(input("r: "))
        print("Please enter PV:")
        PV = float(input("PV:"))
        print("Please enter n:")
        n = int(input("n:"))
        func(PV, r, n)
    else:
        func()