#Scramble Machine Simulator
"""
There are several rows in the machine, and in each row there are balls.
There is also a pointer to a row.
The machine has an infinite number of rows and a lever.
The lever is initially pointing at the first row.
The machine has one bit of memory. (MEM = false,true)

Operations:
LOWER_LEVER: Move the lever one space down
RAISE_LEVER: Move the lever one space up. If in the top row already do nothing.
CHECK_EMPTY: Checks if the current row is empty. If it is empty, MEM is true, otherwise MEM is false.
RESET: Put all the balls in the first row.
SCRAMBLE_DOWN: The balls above the lever start to fall to their next rows until no row (above the lever) has more balls than the one below it. Sets memory to whether any balls have moved.
SCRAMBLE_UP: Similar but reversed scramble down. Move balls up until no row above and including the lever row has more balls than the one above it.
RETURN_(TRUE/FALSE)_IF_MEM_(TRUE/FALSE): The program terminates only if the condition is satisfied.
Loop: Loops forever.
"""

import math

# Main program
# User enters the number of balls to put in the machine
rows = [0]
try:
    total_balls = abs(int(input("How many balls in the first row?: ")))
    rows[0] = total_balls
except:
    valid_input = False
    while not valid_input:
        try:
            total_balls = abs(int(input("Invalid input. How many balls in the first row?: ")))
            rows[0] = total_balls
            valid_input = True
        except:
            pass

mem = False
pointed_row = 0

def print_rows():
    print("Rows:")
    for row in rows:
        print(str(row))
    

# Operation implementations
def LOWER_LEVER():
    global pointed_row
    pointed_row += 1

def RAISE_LEVER():
    global pointed_row
    if pointed_row > 0:
        pointed_row -= 1

def CHECK_EMPTY():
    global mem
    if len(rows)-1 < pointed_row:
        mem = True
        return
    if rows[pointed_row] == 0:
        mem = True
    else:
        mem = False

def RESET():
    global rows
    rows = [total_balls]

def SCRAMBLE_DOWN():
    global rows
    global mem
    while len(rows)-1 < pointed_row:
        rows.append(0)

    balls_moved = False
    balls_moved_loop = True
    while balls_moved_loop:
        balls_moved_loop = False
        for i in range(pointed_row+1):
            if not i == 0:
                if rows[i-1] > rows[i]:
                    rows[i-1] -= 1
                    rows[i] += 1
                    balls_moved = True
                    balls_moved_loop = True
    mem = balls_moved

def SCRAMBLE_UP():
    global rows
    global mem
    while len(rows)-1 < pointed_row:
        rows.append(0)

    balls_moved = False
    balls_moved_loop = True
    while balls_moved_loop:
        balls_moved_loop = False
        for i in range(pointed_row+1):
            if not i == 0:
                if rows[i-1] < rows[i]:
                    rows[i-1] += 1
                    rows[i] -= 1
                    balls_moved = True
                    balls_moved_loop = True
    mem = balls_moved

def RETURN_X_IF_MEM_Y(X, Y):
    if mem == Y:
        print("Program ended, returned " + str(X))
        exit()


#----------------------------------------------------------

# Program: (write scramble machine programs here using the available functions)
"""
LOWER_LEVER: Move the lever one space down. The lever starts in the first row.
RAISE_LEVER: Move the lever one space up. If in the top row already do nothing.
CHECK_EMPTY: Checks if the current row is empty. If it is empty, MEM is set to true, otherwise MEM is set to false.
RESET: Put all the balls in the first row.
SCRAMBLE_DOWN: The balls above the lever start to fall to their next rows until no row (above the lever) has more balls than the one below it. Sets memory to whether any balls have moved.
SCRAMBLE_UP: Similar but reversed scramble down. Move balls up until no row above and including the lever row has more balls than the one above it.
RETURN_(TRUE/FALSE)_IF_MEM_(TRUE/FALSE): The program terminates only if the condition is satisfied.
Loop: While true loop.

print_rows() can be used to debug your program.
"""

# Sample program that calculates if a number is even
"""
LOWER_LEVER()
SCRAMBLE_DOWN()
SCRAMBLE_UP()
RETURN_X_IF_MEM_Y(True, False)
RETURN_X_IF_MEM_Y(False, True)
"""

# Sample program that calculates if a number is prime

#Check for 0
CHECK_EMPTY()
RETURN_X_IF_MEM_Y(False, True)

#Check for 1
LOWER_LEVER()
SCRAMBLE_DOWN()
SCRAMBLE_UP()
CHECK_EMPTY()
RETURN_X_IF_MEM_Y(False, True)
RESET()


while True:
    LOWER_LEVER()
    SCRAMBLE_DOWN()
    SCRAMBLE_UP()
    CHECK_EMPTY()
    RETURN_X_IF_MEM_Y(True, True)
    RESET()
    RAISE_LEVER()

    SCRAMBLE_DOWN()
    SCRAMBLE_UP()
    RETURN_X_IF_MEM_Y(False, False)
    RESET()

    LOWER_LEVER()