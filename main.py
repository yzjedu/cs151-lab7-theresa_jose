# your codeprint("Hi friend, how are you? Need help calculating your house costs?")

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
    while True:
        room_length = input("Enter the length of the room in feet: ")
        if room_length.replace('.', '', 1).isdigit() and float(room_length) > 0:
            return float(room_length)
        print("Invalid input. Please enter a positive numeric value.")


# Function to get width of the room
def width():
    while True:
        room_width = input("Enter the width of the room in feet: ")
        if room_width.replace('.', '', 1).isdigit() and float(room_width) > 0:
            return float(room_width)
        print("Invalid input. Please enter a positive numeric value.")


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
