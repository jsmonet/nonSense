from sense_hat import SenseHat
import sys
import nltk
sense = SenseHat()
words = nltk.word_tokenize(sys.argv[1])
rotayshun = sys.argv[2]
if any(nu in rotayshun for nu in ('0', '90', '180', '270')):
    sense.set_rotation(rotayshun)
elif rotayshun is None:
    sense.set_rotation(180)
else:
    print "Figure your shit out, jerky"
    exit 1
for word in words:
    sense.show_message(word)
