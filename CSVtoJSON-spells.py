# This is a file converter program that reads a CSV file and creates a JSON file with sublibraries rather than concatenated attribute names
import csv

filename = 'spells.csv'

# initializing the titles and rows list
fields = []
rows = []

print('Reading CSV file . . . ')
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row) 
print('CSV file successfully read!\n')
 
print('Writing JSON file . . . ')
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

print('JSON file successfully written!')