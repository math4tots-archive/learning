def is_even(numb):
    """
    When a user inputs a number, the function will check to see if the
    number is an odd or even number

    """
    if numb % 2 == 0:
        print("Yes, it's even")
        return True
    else:
        print("No. It's odd.")
    return #Why did this work?

is_even(int(input()))
#When I tried to implenent the doc spring the program didn't work
#Doing 3 ' "" ' worked!
# So return (or absent of return) means return nothing
#This is ok when just printing but not ok if I wanted to manipulate data outside
#Because...nothing was returned.
