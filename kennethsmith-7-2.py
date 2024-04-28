#Kenneth Smith 4-26-254 7.2
#This program is intended to acquire a String containing a person’s first, middle, and last names, and then display their first, middle, and last initials.

def displayInitials(name):
    # Split the name into first, middle, and last names
    names = name.split()
    
    # Initialize variables to store initials
    firstInitial = names[0][0].upper() + '.'
    middleInitial = names[1][0].upper() + '.'
    lastInitial = names[-1][0].upper() + '.'
    
    # Display the initials
    print("First Initial:", firstInitial)
    print("Middle Initial:", middleInitial)
    print("Last Initial:", lastInitial)

# Acquire the name from the user
fullName = input("Enter your first, middle, and last names: ")

# Display the initials
displayInitials(fullName)

