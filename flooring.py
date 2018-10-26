# Describe Program to user
print("Welcome friend!")
print("")
print("I see you've bought a new house, but all of the rooms have carpet or laminate that is"
      "\nhorribly dirty and gross. I'm sure you need help in calculating how much it will "
      "\ncost to re-do all of the rooms in your house. "
      "\nLucky for you, I've designed this program to help expedite the calculation process!")
print("")
print("Lets get started!")
print("")

# Initialize variable names
room = 0
sum = 0
add_room = 0

# There are 3 while loops. The first one encases a lot of information
# This loop continues to run as long as the user needs to add more rooms to the
# calculations.
while add_room != "NO" :
    # To seperate each room we will add 1 to the count of each room and each room
    # will be labeled as ROOM , ROOM 2 , and so on.
    print("")
    room +=1
    print("ROOM" , room)
    print("")
    # This second loop is just to make sure that the value entered is valid
    while True:
        try:
            length = int (input("Please enter length (in feet): "))
        except ValueError:
            print("The value you have entered is not valid."
                  "\nPlease enter a numerical value.")
            # if the value is valid it will continue
            # Otherwise the user will be prompted to enter a new value
            continue

        else:
            # This just ends the while loop
            break
    # This third loop is to once again make sure that the value entered is valid
    while True:
        try:
            width = int (input("Please enter width(in feet): "))
        except ValueError:
            print("The value you have entered is not valid."
                  "\nPlease enter a numerical value.")
            # If the value is valid it will continue
            # Otherwise the user will be prompted to enter a new value
            continue
        else:
            break

    # The size calculation is simply the area times the width
    dimension = length * width
    # Assuming the cost per square foot is $1.39 we multiply this by the decision to
    # find the total cost of re-doing that specfic room.
    print("")
    cost = dimension * 1.39
    print("The total dimension of room " , room , " is " , dimension , " square feet")
    print("The cost for room " , room , " is $" , cost)

    # The sum of each cost per room is added
    sum += cost

    # This allows the loop to continue until the user decides to end it
    add_room = input("Do you wish to add room? "
                         "\nPlease enter 'YES' or 'NO': ")

# Lastly, we print the total of the sum cost and dimensions for the user
print("")
print("The total cost for all rooms is $" , sum)
print("Width= ", width, "\tLength=", length)
