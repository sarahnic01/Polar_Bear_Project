import csv
clean_file = open("../Data_Files/Clean_Data_Ice_Concentration.csv", "w")
clean_file.write("January of Years" + "," + "NE Shelf"+","+"NE Deep"+"\n")

with open ("../Data_Files/Original_Ice_Concentration_Dataset.csv","r") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        # print(row)
        if(row["year"] == "" or row[' NE shelf'] == "" or row[' NE deep'] == ""):
            break
        if(row["month"] == " 1"):
            clean_file.write(row['year'] + "," + row[' NE shelf'] + "," + row[' NE deep']+"\n")

