# This is a file converter program that reads a CSV file and creates a JSON file with sublibraries rather than concatenated attribute names
import csv
from pickle import FALSE, TRUE
from tkinter import FIRST

filename = 'sample.csv'

# initializing the titles and rows list
fields = []
rows = []

def recursiveDict(field, tabCount, row):

	# TO DO:  Implement check of prior dictionary titles
	for z in range(len(field)):
		if z == 0:
			for a in range(tabCount):
				f.write('\t')
			f.write('"')
			f.write(field[z])
			f.write('" : [\n')
			tabCount = tabCount + 1
			for a in range(tabCount):
				f.write('\t')
			f.write('{\n')
		else:
			for a in range(tabCount + 1):
				f.write('\t')
			f.write('"')
			f.write(field[z])
			f.write('" : ')
			if z == (len(field) - 1):
				f.write('"')
				f.write(row[z])
				f.write('"')
			else:
				pass

		if z == (len(field) - 1):
			f.write('\n')
			for a in range(tabCount):
				f.write('\t')
			f.write('}\n')
			tabCount = tabCount - 1
			for a in range(tabCount):
				f.write('\t')
			f.write(']')




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
with open("nested.json", 'w') as f: 

# ================================================================================
# File dict opening braces
# ================================================================================
	f.write('{\n\t"entries" : [')
	# first loop iteration variable
	firstEntry = TRUE
	for row in rows:
		# inserting a comma if this is not the first entry
		try:
			if firstEntry == FALSE:
				f.write(',\n')
			else:
				f.write('\n')

# ================================================================================
# Entry Opening braces
# ================================================================================
			f.write('\t\t{')
			# first loop iteration variable
			firstLine = TRUE
			for i in range(len(fields)):
				# ensuring the values are not an empty column
				if not fields[i] == "":
					# inserting a comma if this is not the first entry
					try:
						if firstLine == FALSE:
							f.write(',\n')
						else:
							f.write('\n')

# ================================================================================
# Generating Nested Dictionaries within an entry
# ================================================================================
						if "/" in fields[i]:
							parsedField = fields[i].split("/")
							print(parsedField)
							# calling recursive function to print dictionary
							recursiveDict(parsedField, 3, row)
							firstSubentry = TRUE

# ================================================================================
# Generating Nominal Key/Value attributes within an entry
# ================================================================================
						else:
							f.write('\t\t\t"')
							f.write(fields[i])
							f.write('" : "')
							f.write(row[i])
							f.write('"')

						firstLine = FALSE
					except:
						pass

# ================================================================================
# Entry closing braces
# ================================================================================
			f.write('\n\t\t}')
			firstEntry = FALSE
		except:
			pass

# ================================================================================
# File dict closing braces
# ================================================================================
	f.write('\n\t]\n}')

print('JSON file successfully written!')