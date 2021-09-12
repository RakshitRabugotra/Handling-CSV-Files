import csv

FileName = "Sample.csv"

# Data (to be extracted from the file)
Fields = []
Content = []

with open(FileName, mode='r+') as csvFile:
	# Creating a csv 'reader' instance
	csvReader = csv.reader(csvFile)

	# Extracting Field Names from first row
	Fields = next(csvReader)

	# Iterating through
	for row in csvReader:
		Content.append(row)

	# Get the total number of lines parsed
	print("\nParsed {} lines from {}".format(csvReader.line_num, FileName))

# Displaying the Fields
print("Fields => " + ", ".join(field for field in Fields))

# Displaying the Content
print("\nContent => ")
for row in Content:
	# Displaying every Column
	for col in row:
		print("%5s"%col, end='')
	print()
