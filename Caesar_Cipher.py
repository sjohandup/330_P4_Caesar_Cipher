# SJ du Plooy	- 12070794
# M  Peroski	- 13242475

# Variable to store text from file (global)
file_String = ""

# Function that reads from a file
def read_File () :
	global file_String
	encoded_txt = open("cipher.txt", "r")
	file_String = encoded_txt.read()
	encoded_txt.close()

# Function that writes to the file
def write_File (decodedArray) :
	size = len(decodedArray)
	decoded_txt = open("decoded.txt", "w")
	for i in range(0, size) :
		decoded_txt.write(decodedArray[i])
		decoded_txt.write("\n")
		decoded_txt.write("\n")
	decoded_txt.close()

# Function that deciphers the cipher
def ceaser_Cipher () :
    # Call variable that stores cipher
	global file_String
    # Variables that store point breaks in ascii table
	numbers = 57
	large_Caps = 90
	small_Caps = 122
    # Counter variable
	count = 62
    # String array to store all of the iterations
	iterations = []
	# Array for strings
	to_File = []
	# Store each character
	for x in range (0, len (file_String) - 1) :
		iterations.append (file_String[x])

	# Loop through the counter
	for i in range (1, count) :
		# Loop through each of the characters
		for c in range (0, len (iterations)) :
			# Check if the max number ascii value has been reached
			if (ord (iterations[c]) == numbers) :
				 iterations[c] = (chr (ord (iterations[c]) + 8))
			# Check if the max large caps ascii value has been reached
			elif (ord (iterations[c]) == large_Caps) :
				 iterations[c] =  (chr (ord (iterations[c]) + 7))
			# Check if the max small caps ascii value has been reached
			elif (ord (iterations[c]) == small_Caps) :
				 iterations[c] =  (chr (ord (iterations[c]) - 74))
			else :
				 iterations[c] =  (chr (ord (iterations[c]) + 1))
		# Print the iteration count
		print ("Iteration: ", str (i))
		# Print the cipher
		print (''.join (iterations), "\n")
		# Append to the array of strings
		to_File.append (''.join (iterations))
	# Call write file function
	write_File (to_File)

# Function that prints from a file
def print_File () :
	decoded_file_String = ""
	encoded_txt = open('decoded.txt', 'r')
	decoded_file_String = encoded_txt.read()
	encoded_txt.close()
	print (decoded_file_String, "\n")

# Main function
def main () :
	read_File ()
	ceaser_Cipher ()

# Run main module
if (__name__ == "__main__") :
    main()
