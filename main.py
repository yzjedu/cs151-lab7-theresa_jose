# Programmers: Theresa and Jose
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/16/2024
# Lab Assignment: 7
# Problem Statement: Our friend just bought a new house, but all of the rooms have carpet or laminate that is horribly
# dirty and gross.
#You need to design, write, and test a program that calculates the cost of buying flooring for your friend’s house.
# Your friend may need to test the cost with different designs, so your program should ask your friend if they want to check the cost of another design.
# Data In: Length and width of flooring in each room, and type of flooring being installed
# Data Out:  Total balance of all the rooms combined
# Credits: In Class

# print("Hi friend, how are you? Need help calculating your house costs?")
print('Hi friend, how are you? Need help calculating your house costs?')
print('Your floor options are hardwood at $1.39 per square foot, carpet at $3.99 per square foot, or tile at $4.99 per square foot. ')

# Initial total cost to zero
total_cost = 0


# Function to get flooring type
def floor_type():
    flooring = input("Enter the type of flooring (hardwood, carpet, or tile): ").lower().strip()
    while flooring != "hardwood" and flooring != "carpet" and flooring != "tile":
        print("Invalid input. Please enter 'hardwood', 'carpet', or 'tile'.")
        flooring = input("Enter the type of flooring (hardwood, carpet, or tile): ").lower().strip()
    return flooring


# Function to get length of the room
def length():
    room_length = input("Enter the length of the room in feet: ")

    # while not room_length:
    #room_length = input("Enter the length of the room in feet: ")
    #if room_length.replace('.', '', 1).isdigit() and float(room_length) > 0:
    # return float(room_length)
    #print("Invalid input. Please enter a positive numeric value.")
    while not (room_length.replace('.', '', 1).isdigit() and float(room_length) > 0):
        print("Invalid input. Please enter a positive numeric value.")
        room_length = input("Enter the length of the room in feet: ")
    return float(room_length)


# Function to get width of the room
def width():
    room_width: str = input("Enter the width of the room in feet: ")

    while not room_width.replace('.', '', 1).isdigit() and float(room_width) > 0:
        print("Invalid input. Please enter a positive numeric value.")
        room_width = input("Enter the width of the room in feet: ")
    return float(room_width)


# Function to calculate area of the room
def area(room_length, room_width):
    return room_length * room_width


# Function to calculate cost of flooring for a room based on area and flooring type
def room_cost(area, flooring_type):
    if flooring_type == "hardwood":
        return area * 1.39
    elif flooring_type == "carpet":
        return area * 3.99
    elif flooring_type == "tile":
        return area * 4.99


# Main function to calculate and display the total cost for five rooms
def main():
    total_cost = 0
    room_count = 0
    while room_count != 5:
        print("Room", room_count + 1)

        # Get room dimensions and flooring type
        room_length = length()
        room_width = width()
        flooring_type = floor_type()

        # Calculate area and room cost
        room_area = area(room_length, room_width)
        room_price = room_cost(room_area, flooring_type)

        # Display cost for the current room
        print("Cost of Room", room_count + 1, "with", flooring_type, "flooring: $", "%.2f" % room_price)

        # Add to total cost and room count
        total_cost += room_price
        room_count += 1

    # Output total cost of all rooms
    print("Total cost for all rooms: $", "%.2f" % total_cost)
    print("Thank you!")


# Call the main function to start the program
main()
