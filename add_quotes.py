import csv 

""" Python program to demonstrate to add more quotes to random-quotes. """ 
    
# A user can add rows of quotes and their authors to this list
rows = [ ['A random quote', 'Author Name'], 
         ['Another random quote', 'Author Name'] 
        ] 

# name of csv file 
filename = "random-quotes.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the data rows 
    csvwriter.writerows(rows)