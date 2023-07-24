import csv
import pandas as pd

# Greeting
print("this is a simple text-based csv-to-html converter \n")

# Variable to keep track of the menu choice
menuChoice = True

# Start of the main loop
while menuChoice:
    # Display the menu options and get user's choice
    menuChoice = input("1. type 'open' or '1' to open csv \n2. type 'credits' or '2' for credits\n3. quit")

    # Check if the user wants to open a CSV
    if menuChoice == '1' or menuChoice == 'open':
        while True:
            # Get user's choice for the type of CSV conversion
            csvChoice = input("What kind of csv are you converting? \n1.contacts/typical csv \n2.simple comma-separated values \n3.go back")

            # choice 2: Simple comma-separated values conversion
            if csvChoice == "2":
                filename = input("Enter filename with '.csv' extension")

                # Create a new filename without the ".csv" extension
                newFilename = filename.replace(".csv", "")

                # Open the original CSV file in read mode
                originalFile = open(filename, "r")
                print("opening file...")

                try:
                    # Read all lines from the file as a single string
                    line = str(originalFile.readlines())
                    print(line)

                    # Create a new HTML file and write the contents of the CSV file into it, replacing commas with spaces and newlines
                    convFile = open(newFilename + ".html", "w")
                    convFile.write(line.replace(",", " " + "\n"))
                    convFile.write(line)

                    print("Done!")

                except FileNotFoundError:
                    print("File not found! Please check the name entered.")

            #choice 1: Contacts/Typical CSV conversion using pandas
            elif csvChoice == '1':
                filename = input("Enter filename with '.csv' extension")
                newFilename = filename.replace(".csv", "")

                # Read the CSV file using pandas and convert it to an HTML file
                openCsv = pd.read_csv(filename)
                openCsv.to_html(newFilename + ".html")
                html_file = openCsv.to_html()

                print("Done!")

            # choice 3: Go back to the main menu
            elif csvChoice == '3':
                break

    # Check if the user wants to view credits
    elif menuChoice == 'credits' or menuChoice == '2':
        print("Creator: MishoV, Pandas Package Team github.com/pandas-dev/pandas, 2022")

    # Check if the user wants to quit the program
    elif menuChoice == 'quit' or menuChoice == '3':
        print("exiting")
        menuChoice = None
        break

    # If the user entered an invalid command, display an error message
    else:
        print("Please enter a valid command")
        print("1. type open to open csv \n2. credits:\n3. quit ")
