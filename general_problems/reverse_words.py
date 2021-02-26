
def rev_sentence(sentence): 
	words = sentence.split(' ')  
	reverse_sentence = ' '.join(reversed(words)) 

	# finally return the joined string 
	return reverse_sentence 

if __name__ == "__main__": 
	input = 'This is the first python programm'
	print (rev_sentence(input)) 

