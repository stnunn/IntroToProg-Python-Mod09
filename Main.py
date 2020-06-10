# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Started script
# RRoot,1.1.2020,Added pseudo-code to start assignment 9
# SNunn,6.10.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules # DONE

if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as IO # IO classes
else:
    raise Exception("This file was not created to be imported")

STR_FILE_PERS_DATA = 'C:\\_PythonClass\\Assignment09\\PersonData.txt'
STR_FILE_EMPL_DATA = 'C:\\_PythonClass\\Assignment09\\EmployeeData.txt'

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body # DONE
# Load data from file into a list of employee objects when script starts
lstFileData = []
lstFileData = P.FileProcessor.read_data_from_file(STR_FILE_PERS_DATA)
while True:
    # Show user a menu of options
    IO.EmployeeIO.print_menu_items()
    # Get user's menu option choice
    strChoice = IO.EmployeeIO.input_menu_options()
    # Show user current data in the list of employee objects
    if strChoice.strip() == '1':
        IO.EmployeeIO.print_current_list_items(lstFileData)
    # Let user add data to the list of employee objects
    if strChoice.strip() == '2':
        IO.EmployeeIO.input_employee_data(lstFileData)
    # let user save current data to file
    if strChoice.strip() == '3':
        P.FileProcessor.save_data_to_file(STR_FILE_EMPL_DATA, lstFileData)
    # Let user exit program
    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #
