# SJ du Plooy	- 12070794
# M  Peroski	- 13242475

# Import libraries
import os

# Main function
def main () :
	# Remove the denk
	if (os.path.isfile('./human_Readable.txt')) :
		os.remove("human_Readable.txt")

	# Variable to store entire text file as string
	decoded_str = ""
	end_result_str = ""
	dictionary_str = ""
	dictionary_arr = []
	next_word_index = 0

	# Open and retrieve decoded file text, and close file when done
	decoded_file = open("decoded.txt", "r")
	decoded_str = decoded_file.read().splitlines()
	decoded_file.close()

	output = open("human_Readable.txt", "a")

	for x in range (0, len(decoded_str)) :
		decoded_Line = decoded_str[x]
		next_word_index = 0
		end_result_str = ""
		while (next_word_index < len(decoded_Line)) :
			if (ord(decoded_Line[next_word_index]) >= 97 and ord(decoded_Line[next_word_index]) <= 122) :

				dictionary_str = ""
				dictionary_arr = []

				if ((decoded_Line[next_word_index]) == "\n") :
					break

				dictionary_file = open("Seperated/"+decoded_Line[next_word_index]+".txt", "r+")
				dictionary_str = dictionary_file.read()
				dictionary_file.close()
				dictionary_arr = dictionary_str.split("\n")

				temp = decoded_Line[next_word_index : len(decoded_Line)]

				match_index = 0
				match_found = 0
				j = 0
				while (j < len(dictionary_arr) and match_found == 0) :
					if ((len(temp) - next_word_index) < len(dictionary_arr[j])) :
						match_found = 0
					if (dictionary_arr[j] == temp[0 : len(dictionary_arr[j])]) :
						end_result_str = end_result_str + dictionary_arr[j] + " "
						match_index = j
						match_found = -1
					else :
						j = j+1
				next_word_index = next_word_index + len(dictionary_arr[match_index])
			else :
				end_result_str = end_result_str + decoded_Line[next_word_index]

				if (next_word_index + 1 < len (decoded_Line)) :
					if (ord(decoded_Line[next_word_index + 1]) >= 97 and ord(decoded_Line[next_word_index + 1]) <= 122) :
						end_result_str = end_result_str + " "

				next_word_index = next_word_index + 1

		print (end_result_str)
		output.write(end_result_str)
		output.write("\n")
	output.close()

# Run main module
if (__name__ == "__main__") :
    main()
