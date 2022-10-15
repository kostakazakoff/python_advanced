# Stewards
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

# CRUD
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
> The direction could be "up", "down", "left" or "right"

> If you step in an empty position, create the given value on that position. E.g., if the given value is "A", and the position is empty (".") - change it to "A"

> If the position is NOT empty, do NOT create a value on that position

- "Update, {direction}, {value}"
> The direction could be "up", "down", "left" or "right"

> If you step on a letter or number, update the position with the given value. E.g., if the given value is "h", and the position's value is "12" - change it to "h"

> If the position is empty, do NOT update the value on that position

- "Delete, {direction}"
> The direction could be "up", "down", "left" or "right"

> If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."

> If the position is already empty, do NOT delete it

- "Read, {direction}"
> The direction could be "up", "down", "left" or "right"

> If you step on a letter or number, print it on the console

> If the position is empty, do NOT read it

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

# Song Creator
Create a function called add_songs().
It receives one or many tuples.
Each tuple consists of exactly two elements - the song's title in the first position and a list in the second position.
The list can consist of one, many, or no strings - each representing a line of the lyrics of the song. 
The function collects the information and concatenates the lyrics for each song (each string on a different line). If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.

In the end, it should return a string for each song with its lyrics in the format:
"- {song_title}"
"{first_line_of_lyrics}"
"{second_line_of_lyrics}"
…
"{nth_line_of_lyrics}"

If there are no lyrics given for a song, return just its title in the format shown above.
For more clarification, see the examples below.

### Input:
There will be no input, just tuples passed to your function.
### Output:
Return the desired result as described above.
### Constraints:
You will always have a song's name on the first position of the tuple.

# Collecting Eggs
Old MacDonald wants to fill some boxes with eggs. But he has a big farm, and he will need some help.

On the first line, you will receive a sequence of numbers, each representing an egg with its size.
On the second line, you will receive another sequence of numbers, each representing a piece of paper with its size. 

You should take the first egg and wrap it with the last piece of paper. Then, try to put it in a box with a size of 50. Each wrapped-in-a-paper egg fills one box if it fits in it. Your task is to check whether you have filled at least one box.

You should comply with the following conditions:
- If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it from the sequence before it is wrapped with a piece of paper.
- If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), put the wrapped egg in the box and remove both from the sequences.
- Otherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without putting them in a box.

During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 it brings bad luck to him. You should remove this egg from the sequence before it is wrapped with a piece of paper. 
Furthermore, each time you take an egg with a size of 13, it will be best to swap the first and last pieces of paper positions to bring the good luck back to Old MacDonald.

Note: There will be NO case where there will be just one piece of paper left.
For more clarification see the examples below.

### Input
- In the first line, you will be given a sequence of eggs with their sizes - integers separated by comma and space ", " in the range [-100, 100]
- In the second line, you will be given a sequence of pieces of paper with their sizes - integers separated by comma and space ", " in the range [1, 100]

### Output
- On the first line:

> If you have at least one box filled, print: 
"Great! You filled {total count} boxes."
> If you couldn't fill any boxes, print:
"Sorry! You couldn't fill any boxes!"

- On the following lines, print the eggs left or pieces of paper left if there are any:

> Eggs left: {left eggs joined by ", "}
> Pieces of paper left: {left pieces of paper joined by ", "}

### Constraints
You will always have at least one egg and at least one piece of paper.