from sense_hat import SenseHat
import sys
import nltk
sense = SenseHat()
words = nltk.word_tokenize(sys.argv[1])
rotayshun = int(sys.argv[2])
if rotayshun == 0 or rotayshun % 90 == 0:
    sense.set_rotation(rotayshun)
elif rotayshun is None:
    sense.set_rotation(180)
else:
    print "Figure your shit out, jerky"
for word in words:
    sense.show_message(word)
