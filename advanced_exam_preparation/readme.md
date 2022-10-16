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
- If the rover goes out of the field, it should continue from the opposite side in the same direction.
Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position (3, 5).

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

# Pawn Wars

![image](https://user-images.githubusercontent.com/104040753/196009575-fe760361-a228-4cbf-aa24-52a6bb4da868.png)


A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a number (a1, b1, c1, etc.). In this problem colors of the board will be ignored.

We will play the game with two pawns, white (w) and black (b), where they can:
- Only move forward in a straight line:
    - White (w) moves from the 1st rank to the 8th rank direction.
    - Black (b) moves from 8th rank to the 1st rank direction.
- Can move only 1 square at a time.
- Can capture another pawn in from of them only diagonally:

![image](https://user-images.githubusercontent.com/104040753/196009595-00ea4b81-18e1-4420-8e8f-669b7968c275.png)


When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st rank), can be promoted to a queen.

Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on. 


### Some rules apply when moving paws:
- If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn, the game is over.
- If no capture is possible, the pawns keep on moving until one of them reaches the last rank.

### Input
- On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
    - Empty positions are marked with "-".
    - White pawn is marked with "w"
    - Black pawn is marked with "b"

### Output
Print either one of the following:
- If a pawn captures the other, print:
    - "Game over! {White/Black} win, capture on {square}."
- If a pawn reaches the last rank, print:
    - "Game over! {White/Black} pawn is promoted to a queen at {square}."

### Constraints
- The input will always be valid.
- The matrix will always be 8x8.
- There will be no case where two pawns are placed on the same square.
- There will be no case where two pawns are placed on the same column.
- There will be no case where black/white will be placed on the last rank.

# Springtime
Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the earth seems to come to life again. Farmers and gardeners plant their seeds and temperatures slowly rise.
Write a function called start_spring which will receive a different number of keyword arguments.
Each keyword holds a key with a name of the spring object (string), and each value holds its type (string).

For example, dahlia="flower", shrikes="bird", dogwood="tree".

The function should sort the given spring objects in collections by their type:
- The collections sorted by their number of elements in descending order. If two or more collections have the same number of elements in them, return them in ascending order (alphabetically) by the type's name. 
- Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.

Note: Submit only the function in the judge system

### Input
- There will be no input. Just parameters passed to your function.
### Output
- Return the result, sorted as described above in the format:

"{type_one}:

-{spring_object_of_this_type_one}

-{spring_object_of_this_type_two}

…

-{spring_object_of_this_type_N}

{type_two}:

…

{type_N}:

…

-{last_spring_object_of_typeN}"


# Christmas Elves

Everything in the Satna Claus' workshop was going well until, on one freezing Sunday, a dangerous storm destroyed almost all toys. Now Santa's elves fear they won't be able to meet their December deadline. It could be a disaster, and some children around the world may not get their Christmas toys. Luckily, you've come up with an idea, and you just need to write a program that manages your plan.

The Christmas elves have special toy-making skills - еach elf can make a toy from a given number of materials.

First, you will receive a sequence of integers representing each elf's energy. On the following line, you will be given another sequence of integers, each representing a number of materials in a box.

Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.

You are very clever and have immediately recognized the pros and cons of the work process - the first elf takes the last box of materials and tries to create the toy:
- Usually, the elf needs energy equal to the number of materials. If he has enough energy, he makes the toy. His energy decreases by the used energy, and the toy goes straight to Santa's bag. Then, the elf eats a cookie reward which increases his energy by 1, and goes to the end of the line, preparing for the upcoming boxes.
- Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as much energy as usual. If he has enough, he manages to create 2 toys. Then, his energy decreases; he eats a cookie reward and goes to the end of the line, similar to the first bullet.
- Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy when he just made it (if he made it). The toy is thrown away, and the elf doesn't get a cookie reward. However, his energy is already spent, and it needs to be added to the total elves' energy.
    - If an elf creates 2 toys, but he is clumsy, he breaks them.
- If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the toy, the elf drinks a hot chocolate which doubles his energy, and goes to the end of the line, preparing for the upcoming boxes.

Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units, he does NOT TAKE a box, but he takes a day off. Remove the elf from the collection.

Stop crafting toys when you are out of materials or elves.

### Input
- The first line of input will represent each elf's energy - integers, separated by a single space
- On the second line, you will be given the number of materials in each box - integers, separated by a single space

### Output
- On the first line, print the number of created toys:
"Toys: {total_number_of_toys}"

- On the second line, print the total used energy:
"Energy: {total_used_energy}"

- On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:

"Elves left: {elf1}, {elf2}, … {elfN}"

"Boxes left: {box1}, {box2}, … {boxN}"

### Constraints
- All the elves' values will be integers in the range [1, 100]
- All the boxes' values will be integers in the range [1, 100]

# North Pole Challenge

You are visiting Santa Claus' workshop, and it is complete chaos. You will need to help Santa find all items scattered around the workshop.

You will be given the size of the matrix in the format "{rows}, {columns}".

It is the Santa's workshop represented as some symbols separated by a single space:
- Your position is marked with the symbol "Y"
- Christmas decorations are marked with the symbol "D"
- Gifts are marked with the symbol "G"
- Cookies are marked with the symbol "C"
- All of the empty positions will be marked with "."

After the field state, you will be given commands until you receive the command "End".
The commands will be in the format "right/left/up/down-{steps}".
You should move in the given direction with the given steps and collect all the items that come across. If you go out of the field, you should continue to traverse the field from the opposite side in the same direction.
You should mark your path with "x". Your current position should always be marked with "Y".
Keep track of all collected items.
If you've collected all items at any point, end the program and print: "Merry Christmas!".

### Input
- On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
- On the next lines, you will receive each row with its columns - symbols, separated by a single space.
- On the following lines, you will receive commands in the format described above until you receive the command "End" or until you collect all items.

### Output
- On the first line, if you have collected all items, print:
"Merry Christmas!"
- Otherwise, skip the line
- Next, print the number of collected items in the format:

>    "You've collected:
>    - {number_of_decoration} Christmas decorations
>    - {number_of_gifts} Gifts
>    - {number_of_cookies} Cookies"

Finally, print the field, as shown in the examples.

### Constrains
- All the commands will be valid
- There will always be at least one item
- The dimensions of the matrix will be integers in the range [1, 20]
- The field will always have only one "Y"
- On the field, there will always be only the symbols shown above.

# Naughty or Nice

Santa Claus is always watching and seeing if children are good or bad. Only the nice children get Christmas presents, so Santa Claus is preparing his list this year to check which child has been good or bad.

Write a function called naughty_or_nice_list which will receive
- A list representing Santa Claus' "Naughty or Nice" list full of kids' names
- A different number of arguments (strings) and/or keywords representing commands

The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
The list holds a different number of kids - tuples containing two elements: a counting number (integer) at the first position and a name (string) at the second position.
For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
Next, the function could receive arguments and/or keywords. 
Each argument is a command. The commands could be the following:

"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to a list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.

"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
    
Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"): 
If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids depending on the value in the keyword. Then, remove it from the Santa list.

Otherwise, ignore the command.

All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
In the end, return the final lists, each on a new line as described below.

Note: Submit only the function in the judge system

### Input
There will be no input. Just parameters passed to your function.

### Output
The function should return strings with the names on each list on separate lines, if there are any, otherwise skip the line:
    "Nice: {name1}, {name2} … {nameN}"
    "Naughty: {name1}, {name2} … {nameN}"
    "Not found: {name1}, {name2} … {nameN}"


# Aladdin's Gifts

Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine. He asks Genie for help to prepare the wedding presents.
First, you will receive a sequence of integers representing the materials for every wedding present. After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.


| Gift | Magic needed |
| ---- | ------------ |
| Gemstone | 100 to 199 |
| Porcelain Sculpture | 200 to 299 |
| Gold | 300 to 399 |
| Diamond Jewellery | 400 to 499 |


To make a present, you should take the last integer of materials and sum it with the first magic level value. If the result is between or equal to the numbers described in the table above, you make the corresponding gift and remove both materials and magic value. Otherwise:
- If the product of the operation is under 100:
    - And if it is an even number, double the materials, and triple the magic, then sum it again. 
    - And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between or equal to any of the numbers in the table above.
- If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. Then, check again if it is between or equal to any of the numbers in the table above.
- If, however, the result is not between or equal to any of the numbers in the table above after performing the calculation, remove both the materials and the magic level.

Stop crafting gifts when you are out of materials or magic level.

You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture or gold and jewellery.

### Input
- The first line of input will represent the values of materials - integers, separated by a single space
- On the second line, you will be given the magic levels - integers, separated by a single space

### Output
- On the first line - print whether you have succeeded in crafting the presents:

"The wedding presents are made!"

"Aladdin does not have enough wedding presents."

- On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:

"Materials left: {material1}, {material2}, …"

"Magic left: {magicValue1}, {magicValue2}, …

- On the next lines, print the gifts alphabetically that the Genie has crafted at least once:

"{present1}: {amount}

{present2}: {amount}

…

{presentN}: {amount}"

### Constraints
All the materials values will be integers in the range [1, 1000]
Magic level values will be integers in the range [1, 1000]


# Ball in the Bucket

You are at the funfair to play different games and test your skills. Now you are playing ball in the bucket game.
You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be points (integers) and buckets marked with the letter "B". 

Rules of the game:
- You can throw a ball only 3 times.
- When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
- You can hit a bucket only once. If you hit the same bucket again, you do not score any points. 
- If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points. 

After the board state, you are going to receive the information for every throw on a separate line. The coordinates’ information of a hit will be in the format: "({row}, {column})".

Depending on how many points you have collected, you win one of the following:

| -------- | ----------------- |
| Football | 100 to 199 points |
| Teddy Bear | 200 to 299 points |
| Lego Construction Set | 300 and more points |

Your job is to keep track of the scored points and to check if you won a prize. 
For more clarifications, see the examples below.

### Input
- 6 lines – matrix representing the board (each position separated by a single space)
- On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"

### Output
-On the first line:
-If you won a prize, print: 

"Good job! You scored {points} points, and you've won {prize}."

- If you did not win any prize, print the points you need to get at least the first prize: 

"Sorry! You need {points} points more to win a prize."

### Constraints
- All of the given points will be integers in the range [1, 30]
- All the given indexes will be integers in the range [0, 30]
- There always will be exactly 6 buckets - 1 on each column