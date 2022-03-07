# This is a file converter program that reads a CSV file and creates a JSON file with sublibraries rather than concatenated attribute names
import csv
from pickle import FALSE, TRUE

filename = 'sample.csv'

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
with open("nested.json", 'w') as f: 

	# file opening braces
	f.write('{\n\t"entries" : [')

	firstentry = TRUE
	for row in rows:
		# inserting a comma if this is not the first entry
		try:
			if firstentry == FALSE:
				f.write(',\n')
			else:
				f.write('\n')
			
			# entry opening braces
			f.write('\t\t{')

			firstline = TRUE
			for i in range(len(fields)):
				# ensuring the values are not an empty column
				if not fields[i] == "":

					# inserting a comma if this is not the first entry
					try:
						if firstline == FALSE:
							f.write(',\n')
						else:
							f.write('\n')

						# writing the fields and values
						f.write('\t\t\t"')
						f.write(fields[i])
						f.write('" : "')
						f.write(row[i])
						f.write('"')

						firstline = FALSE
					except:
						pass

			# entry closing braces
			f.write('\n\t\t}')
			firstentry = FALSE
		except:
			pass

	# file closing braces
	f.write('\n\t]\n}')

print('JSON file successfully written!')