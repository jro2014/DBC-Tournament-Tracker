# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:11:09 2021

@author: JRO20
"""

# The application user is the tournament administrator.
# Since tournaments may have a variable amount of participants, gather that up front.
# The administrator can add participants to a particular starting slot.
# In order to cancel a participant, the administrator needs to enter both the starting slot and participant name.
# The administrator can list participants in their starting slots.
# Participants and their starting slots should be represented by an array.
# Do not put a value for empty in a slot.
# Participant names are a single string. Do not put first and last names in separate values.
# There will be at least 1 loop and at least 1 function.



# Display a welcome message on startup.
# Prompt for a number of participants (n) and display a confimarion message
    ## Create an empty list that is n long to be filled in with names 
    

# Main Menu (function?): (while input() != 4)
    ## 1. Sign up a player
    ## 2. Cancel a players attendance 
    ## 3. View Particpants 
    ## 4. Exit
    ## Prompt for input (number)

# Sign up a player: 
    ## Prompt for a first and last name
    ## Prompt for a desired starting slot (if none pick next available slot)
    ## Present an error message if the desired slot is full 
    ## Add the name to the desired slot if available 
    ## Possibilities:
        ### Player name and no starting position find name.index("") since it will always find the first match
        ### Player name and starting position 
            #### Check to see that the starting position = "" if yes then replace with entered name
            #### If no, return an error message and reprompt 
    
# Cancel a player
    ## Prompt for a name
    ## Prompt for a starting slot
    ## Check to see if the name matches the starting slot input 
    ## Display error message if not
    ## Replace name with nothing if the name and index match
    ## Possibilities:
        ### Name does not match starting slot: return error and reprompt
        ### Name matches starting slot: delete name from that index and return success message
    

# View Participants
    ## Print out full list of participants with starting slots
    ## 5 before and 5 after


# Exit
    ## Break while loop 
    
# Define the sign up function:  
def Sign_Up(List_Of_Names):
    Sign = True # set something to True
    while Sign: # begin while loop 
        Name_Input = input('First and Last Name of participant: ') # Prompt for name input
        Slot = int(input('Desired starting slot (0 if no desired slot): '))-1 # Prompt for desired slot #
        # If no slot is given
        if Slot == -1:
            # If Loop to see if the player is already signed up
            if Name_Input in List_Of_Names:
               print('Sorry, that name is already participating.') # Print error message if name already exists
            else: 
                index = List_Of_Names.index('') # index first available slot
                List_Of_Names[index] = Name_Input # Put name input in that slot
                Sign = False # break loop
                print(""" Success: 
        {n} is now signed up in starting slot #{s}
                      """.format(n=Name_Input, s = List_Of_Names.index(Name_Input)+1)) # Print success message
        # If slot is outside range of list              
        elif Slot - 1 > len(List_Of_Names):
            print('Sorry, there aren\'t that many slots available') # print error message
        # If slot is given and is in range of list  
        else:
            # If Name is already in the list -- Must have differentiator for same name people
            if Name_Input in List_Of_Names:
                print('Sorry, that name is already participating.')
            # If Slot is already taken    
            elif List_Of_Names[(Slot-1)] != '':
                print('Sorry, that position is filled by {n}'.format(n=List_Of_Names[(Slot)]))
            # If name is not in list and slot is available
            else:
                List_Of_Names[(Slot)] = Name_Input # assign name input to that index
                Sign = False # break loop
                print(""" Success: 
         {n} is now signed up in starting slot #{s}
                      """.format(n=Name_Input, s = List_Of_Names.index(Name_Input)+1)) # Success message
        



# Define the Cancel Player function 
def Cancel_Player(List_Of_Names):
    Sign = True # set sign to True 
    while Sign: # start while loop
        ## Prompt for a first and last name
        Name_Input = input('First and Last Name of participant: ')
        ## Prompt for Slot #
        Slot = int(input('Desired starting slot: '))-1
        ## Check to see if the name matches the starting slot input 
        # If name does not match in specified slot:
        if List_Of_Names[Slot] != Name_Input:
            print('Sorry, {n} is not located in {s}'.format(n = Name_Input, s = Slot))
        # If name matches name in slot
        elif List_Of_Names[Slot] == Name_Input:
            List_Of_Names[Slot] = '' # Set '' to Slot
            print(""" Success
        {n} has been removed from starting slot #{s}""".format(n = Name_Input, s = Slot)) # Success message
            Sign = False # Break loop

# Define View Participants 
def View_Participants(List_Of_Names):
    Slot = int(input("Starting Slot: "))+1 # Prompt for starting slot 
    # If slot is < 6 adjsut range to only show list starting at 1
    if Slot < 6:
        Index = range(0, Slot + 5)
        for i in Index:
            print(i+1,": ", List_Of_Names[i])
    # If slot + 5 is outside upper range of List only show to len(list)
    elif Slot +5 > len(List_Of_Names):
        Index = range(Slot-6, len(List_Of_Names))
        for i in Index:
            print(i+1,": ", List_Of_Names[i]) 
    # If the list is super small
    elif Slot + 5 > len(List_Of_Names) and Slot > 6:
        Index = range(0, len(List_Of_Names))
        for i in Index:
            print(i+1,": ", List_Of_Names[i]) 
    # If everything checks out 
    else:
        Index = range(Slot -6, Slot + 5)
        for i in Index:
            print(i+1,": ", List_Of_Names[i]) 
    
    
    


# Define a main menu function
def Main_Menu():
    print('Welcome to the Tournament Tracker!')
    print('\n')
    print('=======================')
    Number_Of_Participants = int(input('How many participants in this event? '))
    print('\n')
    print('Ok, there will be {num} participants in this event'.format(num=Number_Of_Participants))
    List_Of_Names = ['']*Number_Of_Participants
    Menu = True # Set value to True
    while Menu: # Start While loop
        print("""
              Main Menu:
                  
              1. Sign up a player
              2. Cancel a player
              3. View participants
              4. Exit""") # Print out options
        Menu_Input = int(input('Choose an option: ')) # Prompt for input
        if Menu_Input == 1: # Loop for what to do based on input
            Sign_Up(List_Of_Names)
        elif Menu_Input == 2:
            Cancel_Player(List_Of_Names)
        elif Menu_Input == 3:
            View_Participants(List_Of_Names)
        else:
            New_Input = input("Are you sure you want to exit? All data will be lost (Y/N): ").upper()
            if New_Input == 'Y':
                Menu = False # Change value to False breaking loop if they want to exit 
  

         
        











































