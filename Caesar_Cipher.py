# SJ du Plooy	- 12070794
# M  Peroski	- 13242475


# Variable to store text from file (global)
file_String = ""

# Function that reads from a file
def read_File () :
	global file_String
	encoded_txt = open('cipher.txt', 'r')
	file_String = encoded_txt.read()


# Function that deciphers the cipher
def ceaser_Cipher () :
    numbers = 48
    small_Caps = 65
    large_Caps = 97

# Function that prints from a file
def print_File () :


# Main function
def main () :
	global file_String
	print (file_String)


# Run main module
if (__name__ == "__main__") :
    main()
