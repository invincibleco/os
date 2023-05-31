with open('oone.txt','r') as firstfile, open('twoo.txt','a') as secondfile:
	
	# read content from first file
	for line in firstfile:
			
			# append content to second file
			secondfile.write(line)

file = open("oone.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))


# Open the file for writing
with open('oone.txt', 'w') as f:
	# Define the data to be written
	data = ['This is the first line', 'This is the second line', 'This is the third line']
	# Use a for loop to write each line of data to the file
	for line in data:
		f.write(line + '\n')
		# Optionally, print the data as it is written to the file
		print(line)