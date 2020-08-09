#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# BWayward, 2020-Aug-07, Created File
# BWayward, 2020-Aug-07, Added Load Data functionality
# Bwayward, 2020-Aug-09, Added and corrected delete functionality
# BWayward, 2020-Aug-09, Modified delete functionality to work correctly
# with pop instead of delete, as it wouldn't delete every line, just 1st
# BWayward, 2020-Aug-09 Cleaned up scraps, removed debug print statements, published
# to github
#------------------------------------------#

# Declare variables

dictRow = {}
strChoice = '' #User Input
lstTbl = [] # List of lists to hold data
lstRow = [] # List of data row
strFileName = 'CDInventory.txt' #Data Storage File
objFile = None #File Object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.split(',')
            dictRow = {'id': lstRow[0], 'Artist': lstRow[1], 'Title': lstRow[2]}
            lstTbl.append(dictRow)
        objFile.close()
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {'id': intID, 'Title': strTitle, 'Artist': strArtist, }
        lstTbl.append(dictRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        # Crashes if pressed before l for load. not sure how to check for 
        # validity of data prior to execution
        print('ID, Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        remInput=input('What ID would you like to remove from the system?')
        for i in range(len(lstTbl) - 1, -1, -1):
            if lstTbl[i]['id'] == remInput:
                lstTbl.pop(i)     
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for items in row.values():
                strRow += str(items) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

