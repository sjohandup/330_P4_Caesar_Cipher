# SJ du Plooy	- 12070794
# M  Peroski	- 13242475

# Main function
def main () :
	# Variable to store entire text file as string
	dictionary_txt = ""

	# Open and retrieve file text, and close file when done
	file_dictionary = open("words.txt", "r")
	dictionary_txt = file_dictionary.read()
	file_dictionary.close()

	# make all words in collection lower case
	dictionary_txt = str.lower(dictionary_txt)

	# Split string into array of words
	words = dictionary_txt.split("\n")

	#Alphabet arrays
	aWords = []
	bWords = []
	cWords = []
	dWords = []
	eWords = []
	fWords = []
	gWords = []
	hWords = []
	iWords = []
	jWords = []
	kWords = []
	lWords = []
	mWords = []
	nWords = []
	oWords = []
	pWords = []
	qWords = []
	rWords = []
	sWords = []
	tWords = []
	uWords = []
	vWords = []
	wWords = []
	xWords = []
	yWords = []
	zWords = []

	# Split words array
	for i in range(1, len(words)) :
		if (words[i][0] == "a") :
			aWords.append(words[i])
		elif (words[i][0] == "b") :
			bWords.append(words[i])
		elif (words[i][0] == "c") :
			cWords.append(words[i])
		elif (words[i][0] == "d") :
			dWords.append(words[i])
		elif (words[i][0] == "e") :
			eWords.append(words[i])
		elif (words[i][0] == "f") :
			fWords.append(words[i])
		elif (words[i][0] == "g") :
			gWords.append(words[i])
		elif (words[i][0] == "h") :
			hWords.append(words[i])
		elif (words[i][0] == "i") :
			iWords.append(words[i])
		elif (words[i][0] == "j") :
			jWords.append(words[i])
		elif (words[i][0] == "k") :
			kWords.append(words[i])
		elif (words[i][0] == "l") :
			lWords.append(words[i])
		elif (words[i][0] == "m") :
			mWords.append(words[i])
		elif (words[i][0] == "n") :
			nWords.append(words[i])
		elif (words[i][0] == "o") :
			oWords.append(words[i])
		elif (words[i][0] == "p") :
			pWords.append(words[i])
		elif (words[i][0] == "q") :
			qWords.append(words[i])
		elif (words[i][0] == "r") :
			rWords.append(words[i])
		elif (words[i][0] == "s") :
			sWords.append(words[i])
		elif (words[i][0] == "t") :
			tWords.append(words[i])
		elif (words[i][0] == "u") :
			uWords.append(words[i])
		elif (words[i][0] == "v") :
			vWords.append(words[i])
		elif (words[i][0] == "w") :
			wWords.append(words[i])
		elif (words[i][0] == "x") :
			xWords.append(words[i])
		elif (words[i][0] == "y") :
			yWords.append(words[i])
		elif (words[i][0] == "z") :
			zWords.append(words[i])

	# Sort alphabet arrays from longest word to shortest
	aWords.sort(key=len, reverse=True)
	bWords.sort(key=len, reverse=True)
	cWords.sort(key=len, reverse=True)
	dWords.sort(key=len, reverse=True)
	eWords.sort(key=len, reverse=True)
	fWords.sort(key=len, reverse=True)
	gWords.sort(key=len, reverse=True)
	hWords.sort(key=len, reverse=True)
	iWords.sort(key=len, reverse=True)
	jWords.sort(key=len, reverse=True)
	kWords.sort(key=len, reverse=True)
	lWords.sort(key=len, reverse=True)
	mWords.sort(key=len, reverse=True)
	nWords.sort(key=len, reverse=True)
	oWords.sort(key=len, reverse=True)
	pWords.sort(key=len, reverse=True)
	qWords.sort(key=len, reverse=True)
	rWords.sort(key=len, reverse=True)
	sWords.sort(key=len, reverse=True)
	tWords.sort(key=len, reverse=True)
	uWords.sort(key=len, reverse=True)
	vWords.sort(key=len, reverse=True)
	wWords.sort(key=len, reverse=True)
	xWords.sort(key=len, reverse=True)
	yWords.sort(key=len, reverse=True)
	zWords.sort(key=len, reverse=True)


	# export files
	a_file = open("Seperated\\a.txt", "w")
	for i in range(0, len(aWords)) :
		a_file.write(aWords[i] + "\n")
	a_file.close()

	b_file = open("Seperated\\b.txt", "w")
	for i in range(0, len(bWords)) :
		b_file.write(bWords[i] + "\n")
	b_file.close()

	c_file = open("Seperated\\c.txt", "w")
	for i in range(0, len(cWords)) :
		c_file.write(cWords[i] + "\n")
	c_file.close()

	d_file = open("Seperated\\d.txt", "w")
	for i in range(0, len(dWords)) :
		d_file.write(dWords[i] + "\n")
	d_file.close()

	e_file = open("Seperated\\e.txt", "w")
	for i in range(0, len(eWords)) :
		e_file.write(eWords[i] + "\n")
	e_file.close()

	f_file = open("Seperated\\f.txt", "w")
	for i in range(0, len(fWords)) :
		f_file.write(fWords[i] + "\n")
	f_file.close()

	g_file = open("Seperated\\g.txt", "w")
	for i in range(0, len(gWords)) :
		g_file.write(gWords[i] + "\n")
	g_file.close()

	h_file = open("Seperated\\h.txt", "w")
	for i in range(0, len(hWords)) :
		h_file.write(hWords[i] + "\n")
	h_file.close()

	i_file = open("Seperated\\i.txt", "w")
	for i in range(0, len(iWords)) :
		i_file.write(iWords[i] + "\n")
	i_file.close()

	j_file = open("Seperated\\j.txt", "w")
	for i in range(0, len(jWords)) :
		j_file.write(jWords[i] + "\n")
	j_file.close()

	k_file = open("Seperated\\k.txt", "w")
	for i in range(0, len(kWords)) :
		k_file.write(kWords[i] + "\n")
	k_file.close()

	l_file = open("Seperated\\l.txt", "w")
	for i in range(0, len(lWords)) :
		l_file.write(lWords[i] + "\n")
	l_file.close()

	m_file = open("Seperated\\m.txt", "w")
	for i in range(0, len(mWords)) :
		m_file.write(mWords[i] + "\n")
	m_file.close()

	n_file = open("Seperated\\n.txt", "w")
	for i in range(0, len(nWords)) :
		n_file.write(nWords[i] + "\n")
	n_file.close()

	o_file = open("Seperated\\o.txt", "w")
	for i in range(0, len(oWords)) :
		o_file.write(oWords[i] + "\n")
	o_file.close()

	p_file = open("Seperated\\p.txt", "w")
	for i in range(0, len(pWords)) :
		p_file.write(pWords[i] + "\n")
	p_file.close()

	q_file = open("Seperated\\q.txt", "w")
	for i in range(0, len(qWords)) :
		q_file.write(qWords[i] + "\n")
	q_file.close()

	r_file = open("Seperated\\r.txt", "w")
	for i in range(0, len(rWords)) :
		r_file.write(rWords[i] + "\n")
	r_file.close()

	s_file = open("Seperated\\s.txt", "w")
	for i in range(0, len(sWords)) :
		s_file.write(sWords[i] + "\n")
	s_file.close()

	t_file = open("Seperated\\t.txt", "w")
	for i in range(0, len(tWords)) :
		t_file.write(tWords[i] + "\n")
	t_file.close()

	u_file = open("Seperated\\u.txt", "w")
	for i in range(0, len(uWords)) :
		u_file.write(uWords[i] + "\n")
	u_file.close()

	v_file = open("Seperated\\v.txt", "w")
	for i in range(0, len(vWords)) :
		v_file.write(vWords[i] + "\n")
	v_file.close()

	w_file = open("Seperated\\w.txt", "w")
	for i in range(0, len(wWords)) :
		w_file.write(wWords[i] + "\n")
	w_file.close()

	x_file = open("Seperated\\x.txt", "w")
	for i in range(0, len(xWords)) :
		x_file.write(xWords[i] + "\n")
	x_file.close()

	y_file = open("Seperated\\y.txt", "w")
	for i in range(0, len(yWords)) :
		y_file.write(yWords[i] + "\n")
	y_file.close()

	z_file = open("Seperated\\z.txt", "w")
	for i in range(0, len(zWords)) :
		z_file.write(zWords[i] + "\n")
	z_file.close()

	print ("Finished...\n")

# Run main module
if (__name__ == "__main__") :
    main()
