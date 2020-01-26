 
import plotly.graph_objects as go
import plotly.io as pio

#*********************************** Function ************************************* #

# Function that takes a list of integers and returns the mean value
def mean_calc(datalist):
    total_value = 0
    for i in datalist:
        total_value = total_value + i
    
    # returns the total of adding all values in the list
    # and dividing that number by the number of items in the list
    return round(total_value/len(datalist),1)
    
# *********************************** Function ************************************* #

# Function that takes a list of integers and returns the most common value                   
def mode_calc(datalist):
    # Variables to track the most common value in the list and a count of the value
    highest_value = 0
    highest_count = 0
    # The flag variable is used to flag situations where 2 variables share the highest count
    flag = 0
    
    for i in datalist:
        # if the current item is already the highest value, skip looking at it
        if highest_value != i:
            
            # if the current value appears more than the previous highest count
            if datalist.count(i) > highest_count:
                
                # replace the highest value with the new value...
                highest_value = i
                # ... and the highest count with the new value's count.
                highest_count = datalist.count(i)
                # Set the flag to 0 indicating no issues, we have a new highest value
                flag=0
            
            # if the current value matches the highest value found so far we flag it
            # as a potential issue - i.e. there may be no mode
            elif datalist.count(i) ==  highest_count:
                flag=1
        
    
    # Once the process has completed, we check if there is an outstanding flag, if so
    # there is no mode in the data, otherwise we return the highest value we found
    if flag == 1:
        return ("N/A")
    else:
        return (highest_value)

# *********************************** Function ************************************* #

# Function that takes a list and returns the median value of the list
def median_calc(datalist):
    # Sort the list in acsending order
    datalist.sort()
  
    # If there is an odd number of items in the list...
    if (len(datalist)%2 == 1):
        # take one from the list length and half it you'll get the middle position of the list
        # REMEMBER : if you want the 3rd item on the list, in python lists that's item number 2!
        middlevalue = int((len(datalist)-1)/2)
        return(datalist[middlevalue])
    
    # If there is an even number of items in the list...
    else:
        # Find the two middle values and calculate their mean
        mid_val1 = int(len(datalist)/2)
        mid_val2 = int(mid_val1 - 1)
        median = (datalist[mid_val1] + datalist[mid_val2])/2
        return median

# *********************************** Main Program ************************************* #
# Open our files in read and write modes
original_file = open("Ice_Melting_Polar_Bears_Effect.csv", "r")

Temp1991_file = open("Clean_Data_Polar_Bear_Effect.csv", "w")
Temp1991_file.write("Month=January" + "," + "year"+","+"Amount of sighting"+"\n")

Temp2016_file = open("Temp2016_cleaneddata.csv", "w")
Temp2016_file.write("Year = 2016" + "," + "Temperature"+","+"Month"+"\n")


# Lists to hold our figures efor each year

Temp1991 = []
Months1991 = []
Temp2016 = []
Months2016 = []

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
    if (InputList[1] == "1991"):
        # Check if there is a empty entry, skip it if so
        if (InputList[1] != "   " and InputList[3] != "  "):
            # Write just the 1st Column (Temperature) and 3rd Column(Month) columns to the cleaned file
            Temp1991_file.write ("" + "," + str(InputList[0] + "," + InputList[2])+"\n")
            # Create a lists for each year
            Temp1991.append(float(InputList[0]))
            Months1991.append(InputList[2])
            
    elif (InputList[1] == "2016"):
              if (InputList[1] != "   " and InputList[3] != "  "):
            # Write just the 1st Column (Temperature) and 2nd Column(Year) columns to the cleaned file
                Temp2016_file.write ("" + "," + str(InputList[0] + "," + InputList[2])+"\n")
            # Create alists for each year
                Temp2016.append(float(InputList[0]))
                Months2016.append(InputList[2])
                   
Temp1991mean = mean_calc(Temp1991)
Temp1991mode = mode_calc(Temp1991)
Temp1991median = median_calc(Temp1991)
Temp2016mean = mean_calc(Temp2016)
Temp2016mode = mode_calc(Temp2016)
Temp2016median = median_calc(Temp2016)

Temp1991_file.write("Mean:" + "," + str(Temp1991mean) + "," + str(Temp1991mode) + "\n")

print("Processing Complete!\n")
print(Temp1991)  #prints list Temp1991 (all the temps from 1991)
print(Temp2016)
print(Months1991)
print(Temp1991mean) #prints the mean of 1991 temps
print(Temp1991mode)
print(Temp1991median)


Temp1991_file.close()
Temp2016_file.close()
original_file.close()


# See https://plot.ly/python/getting-started-with-chart-studio/#initialization-for-offline-plotting
fig = go.Figure(go.Scatter(x=Months1991, y=Temp1991, name = '1991'))
fig.add_trace(go.Scatter(x=Months2016, y=Temp2016, name = '2016'))
# Possible to add further traces for more countries
fig.update_layout(title_text='Comparison of Temperatures between 1991 and 2016 in Ireland', xaxis_title = 'Year by Month', yaxis_title = 'Temperature')
pio.write_html(fig, file='TemperatureComparisonsIreland.html', auto_open=True)
