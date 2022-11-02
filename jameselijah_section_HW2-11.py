"""
Starter code by: Elijah James
#Finished code by: Elijah James
#Description: Starter code for Homework 2 # change the line below
"""
floor = 0  # change to starting state according to diagram

while floor <= 6:  # what should this be to keep looping
    # while elevator is not off
    print("At floor {}, Waiting button press ".format(floor))
    button = input("\tU(p) or D(own) or O(ff) or X(press):\n\tSingle letters please! ")
    if button == 'x' or button == 'X':
        if floor == 4:
            floor = 4
        else:
            floor = 0

    if button == 'U' or button == 'u':
        if floor == 5:
            floor = 5
        elif floor == 6:
            floor = 6
        elif floor == -1:
            floor = -1
        else:
            floor += 2
    if button == 'D' or button == 'd':
        if floor == -1:
            floor = -1
        else: floor = round(floor / 2)
    if floor == 0:
        if button == 'o' or button == 'O':
            floor = -1
""" 
Answer the following questions inside this Doc-string
Use 'U', 'D', 'X' for up, down and express 
1.  From the initial state, using  less than 7 button presses, how does
one get to the '5' floor?( u,u,u,d,u)
2.  From the '4' floor, what are the button pushes that get you to the '0' 
floor with the fewest buttons pushed? (d,x)
"""
