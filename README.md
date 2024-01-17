# Scramble Machine Simulator

This project simulates a computational machine known as a Scramble Machine. Similarly to a Turing Machine, it has only a few simple operations but can perform a variety of calculations.

## Properties of the machine:
- There are an infinite number of rows in the machine, and in each row there can be any number of balls.
- The machine is initiallized with any number of balls in the first row, and the rest of the rows are empty.
- There is also a lever or pointer to a row.
- The lever is initially pointing at the first row.
- The machine has one bit of memory. (MEM = false,true)

## The operations available in the machine:
- LOWER_LEVER: Move the lever one space down.
- RAISE_LEVER: Move the lever one space up. If in the top row already do nothing.
- CHECK_EMPTY: Checks if the current row pointed at by the lever is empty. If it is empty, set MEM to true, otherwise set MEM to false.
- RESET: Put all the balls in the first row.
- SCRAMBLE_DOWN: One at a time the balls above the lever start to fall to their next rows until no row (above the lever) has more balls than the one below it. Sets memory to whether any balls have moved.
- SCRAMBLE_UP: Similar but reversed scramble down. Move balls up until no row above and including the lever row has more balls than the one above it.
- RETURN_(TRUE/FALSE)_IF_MEM_(TRUE/FALSE): The program terminates only if the condition is satisfied.
- Loop: Loops forever.

The simulator comes with two programs: one that calculates if a number is even and another that calculates if a number is prime.
