# Algorithm Document
1) Output 'Hi friend, how are you? Need help calculating your house costs?'
2) set cost equal to zero 

- Purpose: get floor type
- Name: floor_type
- Parameter: tile, hardwood, or carpet
- Return: type of flooring
###
- Purpose: get length  of room
- Name: length
- Parameter: none
- Return: length 
###
- Purpose: get width of room
- Name: width
- Parameter: none
- Return: width
### 
- Purpose: calculates the square feet in each room
- Name: area
- Parameter: length and width
- Return: area of room  
###
- Purpose: Calculate room cost
- Name: room_cost
- Parameter: none
- Return: price of room
###
- Purpose: Calculate total cost of the five rooms by adding up the 5 room costs
- Name: total_room_cost
- Parameter: none
- Return: cost of five rooms 
###
- Purpose: calculating the total cost of the flooring given the length and width
- Name: main
- Parameter: none
- Return: costs of each room and total cost of flooring

room_count = 0
while room_count does not equal 5: 
call length function
call width function
call area function
call floor_type function 
call room_cost function
call total_room_cost

Output floor options to the user
3) Make each room their own variable
4) Make variables for carpet, hardwood, and tile
5) name in feet 
5) call 'area' function
5) Reprompt user to enter a float if anything other than a float is entered
6) Prompt user for flooring type for each room 
7) Remove spaces and change flooring type to lower case
8) Reprompt user to enter a choice from step one if not inputted 
9) call room_cost function 
10) Output cost of each room
11) Output total cost of rooms combined by adding cost of each room together
12) Output 'Thank you!'

