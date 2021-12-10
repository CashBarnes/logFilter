import csv
import os

directory = '' # location of raw data files to search for relevant databases used (or any column containing relevant data)
for filename in os.listdir(directory):
    # check that we're only searching csv files in case there are other files in the directory
    if filename.endswith('.csv'): 
        # create a new file named according to the current file being filtered
        open(directory + filename + 'Filtered.csv', 'w'). close()
        # open the file to be filtered
        with open(directory + filename, 'r') as filePath:
            reader = csv.reader(filePath)
            # open the new file created above to append resultst to
            with open(directory + filename + 'Filtered.csv', 'a', newline='') as newFile:
                # search rows in raw file for relevant data
                for row in reader:
                    # add conditions to find rows containing relevant data
                    if '' == row[2].lower() \ 
                            or '' in row[5].lower():
                    writer = csv.writer(newFile)
                    # write row containing relevant data to new file
                    write.writerow(row)