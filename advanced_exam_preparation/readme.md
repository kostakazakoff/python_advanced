## Stewards
"It's only when you are flying above that you realize how incredible the Earth really is."
As you know, stewards are needed for every single flight. Today you will be that one steward, and you will be assisting the passengers in finding their seats.

You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}". You will also be given two more sequences of numbers only.
- First, you have to take the first number of the first sequence and the last number of the second sequence.
- Next, take the sum of those two numbers and find its ASCII character.
- Compare each of the two taken numbers and the found character with the seats. If you find a match, the passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
* If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last becomes first).
* If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of all rotations made.

The program should end under the following circumstances:
- You have found 3 (three) seat matches 
- You have made a total of 10 rotations
### Input
- On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
- On the second and the third line, you will be given two more sequences - integers separated by a comma and a space ", "
### Output
When the program ends, print the following on two different lines:
- Seat matches: {matches separated by comma and space}
- Rotations count: {total rotations made}
### Constraints
- All integers will be in the range [1, 100]
- All letters will be in the range [A-Z]
- You will never run out of numbers in your sequences before the program ends
- You will never have more than one match at a time

## CRUD
The abbreviation CRUD expands to Create, Read, Update and Delete.
These are the four fundamental operations in a database.

In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information. 

It consists of:
- Letters - on one or many positions in the table
- Numbers - on one or many positions in the table
- Empty positions - marked with "."

Next, you will receive your first position on the table in the format "({row}, {column})"

On the following lines, until you receive "Stop" you will be receiving commands in the format:
- "Create, {direction}, {value}"
* The direction could be "up", "down", "left" or "right"
* If you step in an empty position, create the given value on that position. E.g., if the given value is "A", and the position is empty (".") - change it to "A"
* If the position is NOT empty, do NOT create a value on that position

- "Update, {direction}, {value}"
* The direction could be "up", "down", "left" or "right"
* If you step on a letter or number, update the position with the given value. E.g., if the given value is "h", and the position's value is "12" - change it to "h"
* If the position is empty, do NOT update the value on that position

- "Delete, {direction}"
* The direction could be "up", "down", "left" or "right"
* If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."
* If the position is already empty, do NOT delete it

- "Read, {direction}"
* The direction could be "up", "down", "left" or "right"
* If you step on a letter or number, print it on the console
* If the position is empty, do NOT read it

> You can make only ONE move at a time in the given direction for each command given.
> In the end, print the final matrix.

### Input
- On the first 6 lines - a matrix with positions separated by a single space
* Letters are in the range [a-zA-Z]
* Numbers are in the range [-100, 100]
- On the next line - your first position in the format: "({row}, {column})"
- On the following lines until you receive the command "Stop" - commands in the format shown above
### Output
- In the end, print the final matrix, each row on a new line, each position separated by a single space.
### Constraints
- You will always receive valid coordinates
- You will always receive directions in the range of the table
- You will always receive letters or numbers