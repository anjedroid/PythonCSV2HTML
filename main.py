
import csv
import pandas as pd


print("this is a simple text-based csv-to-html converter \n")
menuChoice=True
while menuChoice:
    menuChoice = input("1. type 'open' or '1' to open csv \n2. type 'credits' or '2' for credits\n3. quit")
    if menuChoice== '1' or menuChoice=='open':
        while True:

            csvChoice= input("What kind of csv are you converting? \n1.contacts/typical csv \n2.simple comma-separated values \n3.go back")
    #elif menuChoice== '2':
       # csvChoice = input("What kind of csv are you converting? \n 1.contacts \n 2.just values with commas")
            if csvChoice=="2":

                filename = input("Enter filename with '.csv' extension")

                newFilename = filename.replace(".csv", "")

                originalFile = open(filename, "r")

                print("opening file...")
                try:

                    line = str(originalFile.readlines())
                    print (line)
                    convFile = open(newFilename + ".html", "w")
                    convFile.write(line.replace(","," "+"\n"))
                    convFile.write(line)

                    print("Done!")




                except FileNotFoundError:
                    print("File not found! Please check name entered.")

            elif csvChoice =='1':

                filename = input("Enter filename with '.csv' extension")
                newFilename = filename.replace(".csv", "")

                openCsv=pd.read_csv(filename)
                openCsv.to_html(newFilename+".html")
                html_file = openCsv.to_html()
                print("Done!")
            elif csvChoice == '3':
                break


    elif menuChoice== 'credits' or menuChoice=='2':
        print("Creator:MishoV, Pandas Package Team github.com/pandas-dev/pandas, 2022")
    elif menuChoice == 'quit'or menuChoice=='3':

        print("exiting")
        menuChoice=None
        break
    else:
        print("Please enter a valid command")

        print(" 1.type open to open csv \n2. credits:\n3. quit ")
