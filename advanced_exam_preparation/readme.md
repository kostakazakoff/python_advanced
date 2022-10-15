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
    - The direction could be "up", "down", "left" or "right"

    - If you step in an empty position, create the given value on that position. E.g., if the given value is "A", and the position is empty (".") - change it to "A"

    - If the position is NOT empty, do NOT create a value on that position

- "Update, {direction}, {value}"
    - The direction could be "up", "down", "left" or "right"

    - If you step on a letter or number, update the position with the given value. E.g., if the given value is "h", and the position's value is "12" - change it to "h"

    - If the position is empty, do NOT update the value on that position

- "Delete, {direction}"
    - The direction could be "up", "down", "left" or "right"

    - If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."

    - If the position is already empty, do NOT delete it

- "Read, {direction}"
    - The direction could be "up", "down", "left" or "right"

    - If you step on a letter or number, print it on the console

    - If the position is empty, do NOT read it

    - You can make only ONE move at a time in the given direction for each command given.

    - In the end, print the final matrix.

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

    - If you have at least one box filled, print: 
    "Great! You filled {total count} boxes."
    - If you couldn't fill any boxes, print:
    "Sorry! You couldn't fill any boxes!"

- On the following lines, print the eggs left or pieces of paper left if there are any:

    - Eggs left: {left eggs joined by ", "}
    - Pieces of paper left: {left pieces of paper joined by ", "}

### Constraints
You will always have at least one egg and at least one piece of paper.

# Exit Founder

Tom and Jerry decided to play a game together. The game is a maze of which they need to find a way out. Monitor their moves closely and find out who the winner will be!

First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in which they are received determines the order in which they will take turns. The first player starts first.

Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
- Only one Exit - marked with the "E" letter
- Trap (one, many, or none) - marked with the "T" letter
- Wall (one, many, or none) - marked with the "W" letter
- Empty positions will be marked with "."

In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving coordinates for each of the players. They will be taking turns and stepping on different positions on the board until one of them find the Exit or falls into a Trap. Here are the rules:
- If a player hits the letter "E", he escapes the maze and wins the game.
Print "{player} found the Exit and wins the game!" and end the program.
- If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
Print "{player} is out of the game! The winner is {winner}." and end the program.
- If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
Print "{player} hits a wall and needs to rest."
- If a player steps on an empty position ".", nothing happens. 

Both players can step in the same position at the same time.

### Input
- On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
- On the following 6 lines, you will receive the maze board (elements will be separated by a space)
- On the following lines, you will be receiving coordinates in the format: "({row}, {column})"

### Output
- You should print the output as described above.
- The input coordinates will always be valid.

# Shopping Cart
Peter has decided to invite some guests. He should go shopping, but he will need help because 
there are too many things he needs to remember. Would you assist him?

Write a function called shopping_cart that adds products to a shopping cart for the following three types of meals:  "Soup", "Pizza", and "Dessert". Every meal has a limit of products that can be added to it:
- Soup: 3
- Pizza: 4
- Dessert: 2

Once you reach the limit of a meal, you should stop adding products to that meal.
The function will receive a different number of arguments. The arguments will be passed as tuples with two elements - the first one is the type of meal, and the second is the product for the meal. You need to take each argument and make a dictionary with the meal's name as a key and the products as a value of the corresponding key.

There are some additional requirements:
- If you receive the same product for the same meal more than once, you must not add it again.
- If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding products to the cart - just sort and return the desired result as described below.
In the end, sort the meals by the number of bought products in descending order. If there are meals with an equal number of products, sort them (the meals) by their name in ascending order (alphabetically). For each meal sort its products in ascending order (alphabetically).
Return an output as described below.

Note: Submit only the function in the judge system

### Input
- There will be no input, just parameters passed to your function
### Output
- Return a string for each of the 3 types of a meal of the sorted result in the format:

"{meal_type}:"

" - {first_product_added}"

" - {second_product_added}"

…

" - {Nth_product_added}"

- If there are no products given for a meal, return just its name in the format shown above.
- If there are NO products in the cart (at all), return the message: "No products in the cart!"
### Constrains
- Each tuple given will always contain the type of meal in the first position and a product in the second.
- There will be no other meals passed than "Soup", "Pizza", and "Dessert".

# Ramen Shop
You will be given two sequences of integers representing bowls of ramen and customers. Your task is to find out if you can serve all the customers.

Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen until we have no more ramen or customers left:
- Each time the value of the ramen is equal to the value of the customer, remove them both and continue with the next bowl of ramen and the next customer.
- Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with the value of that customer and remove the customer. Then try to match the same bowl of ramen (which has been decreased) with the next customer.
- Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer with the value of the ramen bowl and remove the bowl. Then try to match the same customer (which has been decreased) with the next bowl of ramen.

### Input
- On the first line, you will receive integers representing the bowls of ramen, separated by a single space and a comma ", ".
- On the second line, you will receive integers representing the customers, separated by a single space and a comma ", ".
### Output
- If all customers are served, print: "Great job! You served all the customers."
- Print all of the left ramen bowls (if any) separated by comma and space in the format: "Bowls of ramen left: {bowls of ramen left}"
- Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
- Print all customers left separated by comma and space in the format "Customers left: {customers left}"

# Martian Explorer
Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:
- One rover - marked with the letter "E"
- Water deposit (one or many) - marked with the letter "W"
- Metal deposit (one or many) - marked with the letter "M"
- Concrete deposit (one or many) - marked with the letter "C"
- Rock (one or many) - marked with the letter "R"
- Empty positions will be marked with "-"

After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", ").
Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of the given types of deposit or a rock:
- When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase its value by 1.
- If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below, and the program ends.
- If the rover goes out of the field, it should continue from the opposite side in the same direction. Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position (3, 5).

The rover needs to find at least one of each deposit to consider the area suitable to start our colony. 
Stop the program if you run out of commands or the rover gets broken.

### Input
- On the first 6 lines, you will receive the matrix.
- On the following line, you will receive the commands for the rover separated by a comma and a space.
### Output
- For each deposit found while you go through the commands, print out on the console: "{Water, Metal or Concrete} deposit found at ({row}, {col})"
- If the rover hits a rock, print the coordinates where it got broken in the format: "Rover got broken at ({row}, {col})"
- After you go through all the commands or the rover gets broken, print out on the console:

    - If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
    - Otherwise, print on the console: "Area not suitable to start the colony."

# Words Sorting
Write a function words_sorting which receives a different number of words.

Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is the sum of all ASCII values of that key.

Then, sort the dictionary:
- By values in descending order, if the sum of all values of the dictionary is odd
- By keys in ascending order, if the sum of all values of the dictionary is even

Note: Submit only the function in the judge system

### Input
- There will be no input, just any number of words passed to your function
### Output
- The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
### Constraints:
- There will be no case with capital letters.
- There will be no case with a string consisting of other than letters.

# Flower Finder
You will be given two sequences of characters, representing vowels and consonants. Your task is to start checking if the following words could be found:
- "rose"
- "tulip"
- "lotus"
- "daffodil"

Start by taking the first character of the vowels collection and the last character from the consonants collection. Then check if these letters are present in one or more of the given words. If a letter is present, that part of the word is considered found. The word is gradually revealed with each letter found. Continue processing the next couple of letters until you find one of the given words above.

A letter (vowels or consonants) could participate in more than one word or more than one time in a word, for example:
- The letter "o" is present in "rose", "lotus", and "daffodil". 
- The letter "l" is present in "tulip", "lotus", and "daffodil".
- The letter "f" is present in the word "daffodil" twice.
- The consonant and the vowel are always removed from the collection after trying to match them with the letters in the given words (whether successful or not). In the end, the program stops when a word is found, or there are no more vowels or consonants.

As a result, if you found a word, print it and the remaining letters in each collection in the format described below. Otherwise, print "Cannot find any word!" on the first line and the remaining letters in each sequence in the format described below.

### Input
- On the first line, you will receive vowels, separated by a single space (" ").
- On the second line, you will receive consonants, separated by a single space (" ").

### Output
- On the first line:
    - If a word is found, print it in the format: "Word found: {word_found}"
    - Otherwise, print: "Cannot find any word!"
- On the next lines, print the remaining letters in each collection (if there are any left):
    - "Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
    - "Consonants left: {consonants_one} {consonants_two} … {consonants_N}"

### Constraints
- All letters will be lowercase.
- The letter 'y' will always be a vowel.
- The letter 'w' will always be a consonant.