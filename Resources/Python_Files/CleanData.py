import csv
# *********************************** Main Program ************************************* #
# Open our files in read and write modes
original_file = open("../Data_Files/Ice_Melting_Polar_Bears_Effect.csv", "r")
# original_file = open("../Data_Files/Ice_Melting_Polar_Bears_Effect.csv", "r")
clean_file = open("Clean_Data_Ice_Concentration.csv", "w")
clean_file.write("Month=January" + "," + "Year"+","+"Ice Concentration"+"\n")

# Lists to hold our figures efor each year
years = []
iceconcentrations = []

# Loop until we meet a blank row in the original file
while True:
 # Read a line of data from CSV file
    readdata = original_file.readline()
# Split the file into an array based on comma seperator 
    InputList = readdata.split(',')
# Break from while loop when we hit an empty line
    if (InputList[0] == ""):                
         break   
# If we identify the row as 1991...
    if (InputList[1] == "1"):
        # Check if there is a empty entry, skip it if so
        if (InputList[1] != "   " and InputList[3] != "  "):
            # Write just the required rows/ data entries and columns to the cleaned file
            clean_file.write(InputList[0] + "," + InputList[4] + "," + InputList[5]+"\n")
            # Create a lists for each year
clean_file.close()
original_file.close()