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
def write_File (decodedArray, count, perm) :
	size = len(decodedArray)
	decoded_txt = open("decoded.txt", "a")
	#decoded_txt.write ("Alphabet size: ")
	#decoded_txt.write (str (count))
	#decoded_txt.write (str (" >< Permutation: "))
	#decoded_txt.write (str (perm))
	#decoded_txt.write("\n")
	for i in range(0, size) :
		decoded_txt.write(decodedArray[i])
		decoded_txt.write("\n")
	#decoded_txt.write("\n")
	decoded_txt.close()

# Permutation one
def decypher_Alphabet (iterations, small_Caps, cut_Alphabet, char_Only) :
	# If the character is no longer part of the alphabet
	if (ord (iterations) > (small_Caps - cut_Alphabet)) :
		return (chr (ord (iterations)))
	# Check if the max small caps ascii value has been reached
	if (ord (iterations) == (small_Caps - cut_Alphabet) and cut_Alphabet < 26 and char_Only == 0) :
		# Lower case to numbers
		return (chr (ord (iterations) - (74 - cut_Alphabet)))
	# Only use letters
	elif (ord (iterations) == (small_Caps - cut_Alphabet) and char_Only == 1) :
		return (chr (97))
	# Otherwise incriment
	return (chr (ord (iterations) + 1))

# Permutation two
def decypher_Numbers (iterations, numbers, cut_Numbers, cut_Alphabet) :
	# If the number is no longer part of the alphabet
	if (ord (iterations) > (numbers - cut_Numbers)) :
		return (chr (ord (iterations)))
	# Check if the max number ascii value has been reached
	if (ord (iterations) == (numbers - cut_Numbers) and cut_Numbers < 10 and cut_Alphabet < 26) :
		# Numbers to lower case
		return (chr (ord (iterations) + (40 + cut_Numbers)))
	# Only use numbers
	elif (ord (iterations) == (numbers - cut_Numbers)) :
		return (chr (48))
	# Otherwise incriment
	return (chr (ord (iterations) + 1))

# Function that deciphers the cipher
def ceaser_Cipher (perm ,count, cut_Alphabet, cut_Numbers) :
    # Call variable that stores cipher
	global file_String
    # Variables that store point breaks in ascii table
	numbers = 57
	small_Caps = 122
    # String array to store all of the iterations
	iterations = []
	# Array for strings
	to_File = []
	# Store each character
	for x in range (0, len (file_String) - 1) :
		iterations.append (str.lower(file_String[x]))

	# Loop through counter
	for i in range (0, count) :
		# Loop through each of the characters
		for c in range (0, len (iterations)) :
			# Numbers and alphabet + numbers only
			if (perm == 1) :
				# If the character is a number
				if (ord (iterations[c]) <= (numbers) and ord (iterations[c]) >= (48)) :
					iterations[c] = decypher_Numbers (iterations[c], numbers, cut_Numbers, cut_Alphabet)
				# If the character is a letter
				elif (ord (iterations[c]) <= (small_Caps) and ord (iterations[c]) >= (97)) :
					iterations[c] = decypher_Alphabet (iterations[c], small_Caps, cut_Alphabet, 0)
			# Only alphabet
			elif (perm == 2) :
				# If the character is a letter
				if (ord (iterations[c]) <= (small_Caps) and ord (iterations[c]) >= (97)) :
					iterations[c] = decypher_Alphabet (iterations[c], small_Caps, cut_Alphabet, 1)
		# Append to the array of strings
		to_File.append (''.join (iterations))
	# Call write file function
	write_File (to_File, count, perm)

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
	print ("Reading the cypher from the file \n")
	read_File ()
	print ("Decyphering \n")

	# Counter variable for alphabet
	count = 36
	# Variables responsible for lowering alphabet
	cut_Alphabet = 0
	cut_Numbers = 0

	# Loop though alphabet
	while count > 0:
		# Call decyphering function
		ceaser_Cipher (1, count, cut_Alphabet, cut_Numbers)
		count = count - 1
		# Incriment alphabetical cut off point
		if (count >= 10) :
			cut_Alphabet = cut_Alphabet + 1
		# Incriment numerical cut off point
		else :
			cut_Numbers = cut_Numbers + 1

	print ("Decyphered possible combinations with numbers + letters and numbers only \n")

	# Reset counter and cut value
	count = 26
	cut_Alphabet = 0
	# Loop though all of the permutations
	while count > 0:
		# Call decyphering function
		ceaser_Cipher (2, count, cut_Alphabet, 0)
		count = count - 1
		cut_Alphabet = cut_Alphabet + 1

	print ("Decyphered possible combinations with letters only \n")

# Run main module
if (__name__ == "__main__") :
    main()
