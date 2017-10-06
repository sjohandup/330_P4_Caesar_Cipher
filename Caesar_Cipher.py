# SJ du Plooy	- 12070794
# M  Peroski	- 13242475


# Variable to store text from file (global)
file_String = ""

# Function that reads from a file
def read_File () :
	global file_String
	encoded_txt = open('cipher.txt', 'r')
	file_String = encoded_txt.read()
	encoded_txt.close()

def write_File (decodedArray) :
	size = len(decodedArray)
	decoded_txt = open('decoded.txt', 'w')
	for i in range(0..size) :
		decoded_txt.write(decodedArray[i])
		decoded_txt.write('\n')
	decoded_txt.close()


# Function that deciphers the cipher
def ceaser_Cipher () :
    # Call variable that stores cipher
    global file_Sting
    # Variables that store point breaks in ascii table
    numbers = 48
    small_Caps = 65
    large_Caps = 97
    # Counter variable
    count = 61

    for i in range (0, count) :
        for c in range (0, len (file_Sting)) :
            print ("DUMMY")

# Function that prints from a file
def print_File () :
	decoded_file_String = ""
	encoded_txt = open('decoded.txt', 'r')
	decoded_file_String = encoded_txt.read()
	encoded_txt.close()
	print (decoded_file_String)


# Main function
def main () :
	global file_String
	print (file_String)


# Run main module
if (__name__ == "__main__") :
    main()
