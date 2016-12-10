from sense_hat import SenseHat
import sys
import nltk
sense = SenseHat()
words = nltk.word_tokenize(sys.argv[1])
for word in words:
	a = [0, 0, 255]
	b = [0, 255, 0]
	c = [255, 0, 0]
	for ax, bx, cx in zip(a, b, c)
	
		sense.show_message(word, text_colour=[ax, bx, cx])
