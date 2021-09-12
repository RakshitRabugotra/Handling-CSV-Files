import csv

FileName = "Sample.csv"

# Data (can be anything)
Fields = ["Name", "Age", "Blood-Group"]
Content = [
		["Kyle", "14", "A+"],
		["Rick", "65", "O-"],
		["Morty", "14", "AB+"],
		["Jerry", "45", "B+"]
	]

# Opening a CSV file using inbuilt 'open()' function
with open(FileName, mode='w+') as csvFile:	

	# Creating a csv writer instance
	csvWriter = csv.writer(csvFile)

	# Writing a Header
	csvWriter.writerow(Fields)

	# Writing contents
	csvWriter.writerows(Content)


"""
	writerow() -> Takes a single iterable instance like 'list' or 'tuple'.
	writerows() -> Takes a single nested iterable instace like 'lists in list' or 'tuples in tuple'... etc.
"""
