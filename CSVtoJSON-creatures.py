# This is a file converter program that reads a CSV file and creates a JSON file with sublibraries rather than concatenated attribute names
import time
import json
import csv

filename = 'creatures.csv'

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

with open("newCreatures.json", 'w') as f: 
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
        f.write('\t\t\t],\n')


# ======================================================================
# Attribute Library
# ======================================================================
        f.write('\t\t\t"attribute_library" : [\n')

        # Image data
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"img_rehosted" : "')
        f.write(row[1])
        f.write('",\n')
        f.write('\t\t\t\t\t"img_rehosted_source" : "')
        f.write(row[2])
        f.write('",\n')
        f.write('\t\t\t\t\t"img_linked" : "')
        f.write(row[3])
        f.write('",\n')
        f.write('\t\t\t\t\t"img_linked_source" : "')
        f.write(row[4])
        f.write('",\n')
        f.write('\t\t\t\t\t"species" : "')
        f.write(row[5])
        f.write('"\n')
        f.write('\t\t\t\t},\n')

        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "General Information",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Category",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[6])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Type",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[7])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')

        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t},\n')

        
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Associations",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Planescape",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[8])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Alignment",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[9])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Values",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[10])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')
        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t},\n')


        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Physiology",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Breath Weapon",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[11])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Horns",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[12])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Wing Type",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[13])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Coloration",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[14])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')
        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t},\n')


        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Ecology",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Habitat",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[15])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Prey",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[16])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')
        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t},\n')


        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Life Cycle",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Gestation",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[17])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "')
        f.write(row[18])
        f.write('",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[19])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "')
        f.write(row[20])
        f.write('",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[21])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "')
        f.write(row[22])
        f.write('",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[23])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "')
        f.write(row[24])
        f.write('",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[25])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')

        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t}\n')


        # Closing braces
        f.write('\t\t\t],\n')


# ======================================================================
# Description Library
# ======================================================================
        f.write('\t\t\t"description_library" : [\n')

        # Image data
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"overview" : "')
        f.write(row[26])
        f.write('"\n')
        f.write('\t\t\t\t},\n')
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Physiology",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Appearance",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[27])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Anatomy",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[28])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')

        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t},\n')

        
        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Ecology",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Food Chain",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[29])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Habitat",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[30])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Lair",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[31])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')
        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t},\n')


        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Behavior",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Hunting",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[32])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Defense",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[33])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Personality",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[34])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')

        f.write('\t\t\t\t\t]\n')
        f.write('\t\t\t\t},\n')


        f.write('\t\t\t\t{\n')
        f.write('\t\t\t\t\t"heading" : "Society",\n')
        f.write('\t\t\t\t\t"sublibrary" : [\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Individual",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[35])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Intraspeciary",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[36])
        f.write('"\n')
        f.write('\t\t\t\t\t\t},\n')

        f.write('\t\t\t\t\t\t{\n')
        f.write('\t\t\t\t\t\t\t"subheading" : "Intercultural",\n')
        f.write('\t\t\t\t\t\t\t"subcontent" : "')
        f.write(row[37])
        f.write('"\n')
        f.write('\t\t\t\t\t\t}\n')

        f.write('\t\t\t\t\t]\n')
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
