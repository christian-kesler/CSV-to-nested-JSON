# This is a file converter program that reads a CSV file and creates a JSON file with sublibraries rather than concatenated attribute names
import keyboard
import time
import json
import csv

filename = 'spells.csv'

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 
#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')

with open("newSpells.json", 'w') as f: 
    f.write('{\n\t"entries" : [\n')
    for row in rows:
        # entry name
        f.write('\t\t{\n\t\t\t"entry_name" : "')
        f.write(row[0])
        f.write('",\n')


# ======================================================================
# Title Library
# ======================================================================
        f.write('\t\t\t"title_library" : [\n')
        
        # Table Row One
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"table_row" : [\n')

        # Spell Level
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Level",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[2])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')
        
        # Spell Casting Time
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Casting Time",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[4])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        # Spell Range/Area
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Range/Area",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[6])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        # Spell Components
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Components",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[8])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        # Spell Source
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Source",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[10])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')

        # Table Row Two
        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t},\n')
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"table_row" : [\n')

        # Spell Duration
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Duration",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[12])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        # Spell School
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "School",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[14])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        # Spell Attack/Save
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Attack/Save",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[16])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        # Spell Damage/Effect
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Damage/Effect",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[18])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        # Spell Classes
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"heading" : "Classes",\n')
        f.write('\t\t\t\t\t\t\t"content" : "')
        f.write(row[20])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')

        # # Spell Materials
        # f.write('\t\t\t\t\t\t{\n')
        # f.write('\t\t\t\t\t\t\t"heading" : "Materials",\n')
        # f.write('\t\t\t\t\t\t\t"content" : "')
        # f.write(row[6])
        # f.write('"\n')
        # f.write('\t\t\t\t\t\t},\n')




        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t}\n')
        f.write('\t\t\t],\n')


# ======================================================================
# Attribute Library
# ======================================================================
        f.write('\t\t\t"attribute_library" : [\n')

        # Image data
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"img_rehosted" : "')
        f.write(row[21])
        f.write('",\n')
        f.write('\t\t\t\t\t"img_rehosted_source" : "https://www.deviantart.com/dryoshiyahu/art/Schools-of-Magic-811154835"\n')
        f.write('\t\t\t\t}\n')

        # Closing braces
        f.write('\t\t\t],\n')


# ======================================================================
# Description Library
# ======================================================================
        f.write('\t\t\t"description_library" : [\n')

        # Image data
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Mechanics",\n')
        f.write('\t\t\t\t\t"content" : "')
        f.write(row[24])
        f.write('",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')
        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Components",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[27])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')
        f.write('\t\t\t\t\t]\n')

        f.write('\t\t\t\t},\n')

        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "At Higher Levels",\n')
        f.write('\t\t\t\t\t"content" : "')
        f.write(row[26])
        f.write('"\n')



        f.write('\t\t\t\t}\n')

        # Closing braces
        f.write('\t\t\t]\n')

        # Closing braces
        f.write('\t\t},\n')

    f.write('\t]\n}')



# # Opening JSON file
# f = open('D:/_workspaces/HTML/KnowOnesWebsiteOfEverything/caped-crusaders/spells.json')
 
# # returns JSON object as a dictionary
# data = json.load(f)
 

# # Iterating through the json list
# for i in data['entries']:
#     print(i)
#     print('\n\n\n')

# with open("myfile.txt", 'w') as f: 
#     for key, value in data.items(): 
#         f.write('%s:%s\n' % (key, value))
#         f.write('\n\n\n')

# # Closing file
# f.close()


# some sample JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# Sample print
print ('Testing 123')
