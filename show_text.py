from sense_hat import SenseHat
import sys
import nltk
sense = SenseHat()
words = nltk.word_tokenize(sys.argv[1])
for word in words:
    sense.show_message(word)
