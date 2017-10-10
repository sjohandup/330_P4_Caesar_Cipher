# SJ du Plooy	- 12070794
# M  Peroski	- 13242475

# Main function
def main () :
	# Variable to store entire text file as string
	decoded_str = ""
	end_result_str = ""
	dictionary_str = ""
	dictionary_arr = []
	next_word_index = 0

	# Open and retrieve decoded file text, and close file when done
	decoded_file = open("temp_decoded.txt", "r")
	decoded_str = decoded_file.read()
	decoded_file.close()

	while (next_word_index < len(decoded_str)) :
		print ("next_word_index =", next_word_index)
		print (decoded_str[next_word_index]+".txt")

		dictionary_str = ""
		dictionary_arr = []

		if ((decoded_str[next_word_index]) == "\n") :
			break

		dictionary_file = open("Seperated/"+decoded_str[next_word_index]+".txt", "r+")
		dictionary_str = dictionary_file.read()
		dictionary_file.close()
		dictionary_arr = dictionary_str.split("\n")

		print ("length of dictionary_arr", len(dictionary_arr))

		temp = decoded_str[next_word_index : len(decoded_str)]

		match_index = 0
		match_found = 0
		j = 0
		while (j < len(dictionary_arr) and match_found == 0) :
			if ((len(temp) - next_word_index) < len(dictionary_arr[j])) :
				match_found = 0
			if (dictionary_arr[j] == temp[0 : len(dictionary_arr[j])]) :
				print (dictionary_arr[j])
				print (decoded_str[next_word_index : ])
				end_result_str = end_result_str + dictionary_arr[j] + " "
				match_index = j
				match_found = -1
			else :
				j = j+1
		next_word_index = next_word_index + len(dictionary_arr[match_index])

	print (end_result_str)

# Run main module
if (__name__ == "__main__") :
    main()
