# This is to get the maximum radius or max film thickness ( using plot over line ) 
# For film thickness use "PLOT OVER LINE" for the  Zaxis , and for maximum radius use  use Xaxis  
# Firstly save data using "plot over line" in the extract folder with name "zaxis.0 , zaxis.1 ..." 
# Then run this code "python3 analysis.py" to get the max filmthickness

import csv
import os

def get_max_alpha_from_csv(file_path):
    # max_alpha = float('-inf')
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            alpha_value = float(row['alpha.water'])
            arc_length = float(row['arc_length'])
            # print(alpha_value>0.95)
            if alpha_value > 0.9:
                # print(arc_length)
                temp_length = arc_length 
    return temp_length

# Directory containing the CSV files
csv_directory = './extract'

# Array to store the maximum alpha values from each file
radius_values = []
filenum = len(os.listdir(csv_directory))
print(filenum)
file1 = open("./finalResult_zaxis.csv", "w")  # write mode
file1.write("timestep,radius\n")
for i in range(filenum):
        file_path = os.path.join(csv_directory,f'zaxis.{i}.csv')
        # print(filename)
        radius_eachTimestep = get_max_alpha_from_csv(file_path)
        print(f"data{i}: {radius_eachTimestep}")
        file1.write(f"{i*0.001},{radius_eachTimestep}\n")
file1.close()

print("File made")

