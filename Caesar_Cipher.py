# SJ du Plooy	- 12070794
# M  Peroski	- 13242475

# Import libraries
import os

# Variable to store text from file (global)
file_String = ""

# Function that reads from a file
def read_File () :
	global file_String
	encoded_txt = open("cipher.txt", "r")
	file_String = encoded_txt.read()
	encoded_txt.close()

# Function that writes to the file
def write_File (decodedArray, perm) :
	size = len(decodedArray)
	decoded_txt = open("decoded.txt", "a")
	decoded_txt.write ("Permutation: ")
	decoded_txt.write (str (perm))
	decoded_txt.write("\n")
	decoded_txt.write("\n")
	for i in range(0, size) :
		decoded_txt.write(decodedArray[i])
		decoded_txt.write("\n")
		decoded_txt.write("\n")
	decoded_txt.close()

# Permutation one
def perm_1 (iterations, numbers, large_Caps, small_Caps) :
	# Check if the max number ascii value has been reached
	if (ord (iterations) == numbers) :
		# Numbers to caps
		return (chr (ord (iterations) + 8))
	# Check if the max large caps ascii value has been reached
	elif (ord (iterations) == large_Caps) :
		# Caps to lower case
		return (chr (ord (iterations) + 7))
	# Check if the max small caps ascii value has been reached
	elif (ord (iterations) == small_Caps) :
		# Lower case to numbers
		return (chr (ord (iterations) - 74))
	else :
		# Otherwise incriment
		return (chr (ord (iterations) + 1))

# Permutation two
def perm_2 (iterations, numbers, large_Caps, small_Caps) :
	# Check if the max number ascii value has been reached
	if (ord (iterations) == numbers) :
		# Numbers to lower case
		return (chr (ord (iterations) + 40))
	# Check if the max large caps ascii value has been reached
	elif (ord (iterations) == large_Caps) :
		# Caps to numbers
		return (chr (ord (iterations) - 42))
	# Check if the max small caps ascii value has been reached
	elif (ord (iterations) == small_Caps) :
		# Lower case to caps
		return (chr (ord (iterations) - 57))
	else :
		# Otherwise incriment
		return (chr (ord (iterations) + 1))

# Function that deciphers the cipher
def ceaser_Cipher (perm) :
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
			# Check permutation counter
			if (perm == 1) :
				iterations[c] = perm_1 (iterations[c], numbers, large_Caps, small_Caps)
			elif (perm == 2) :
				iterations[c] = perm_2 (iterations[c], numbers, large_Caps, small_Caps)
		# Print the iteration count
		#print ("Iteration: ", str (i))
		# Print the cipher
		#print (''.join (iterations), "\n")
		# Append to the array of strings
		to_File.append (''.join (iterations))
	# Call write file function
	write_File (to_File, perm)

# Function that prints from a file
def print_File () :
	decoded_file_String = ""
	encoded_txt = open('decoded.txt', 'r')
	decoded_file_String = encoded_txt.read()
	encoded_txt.close()
	print (decoded_file_String, "\n")

# Main function
def main () :
	# Remove decoded file if it is present
	if (os.path.isfile('./decoded.txt')) :
		os.remove("decoded.txt")
	print ("Reading the cypher from the file")
	read_File ()
	print ("Decyphering")
	# Loop though all of the permutations
	for i in range (1, 3) :
		ceaser_Cipher (i)
	print ("Decyphered possible combinations")

# Run main module
if (__name__ == "__main__") :
    main()
