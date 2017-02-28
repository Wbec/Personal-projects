#The quit error is designed to allow the user to quit a program from any input prompt
#it is less efficent than having each prompt have a quit option,
#using this error quitting can be handled by a single try-except block in the main method
class QuitError (Exception):
    "Error allowing for the exit of a program by a user."
    pass
