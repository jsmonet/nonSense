from sense_hat import SenseHat
import sys
import nltk
# So, nltk first use will likely return this error
# Resource u'tokenizers/punkt/english.pickle' not found.
# open an interactive python session and type:
# nltk.download('punkt')
# All set. run in peace.

sense = SenseHat()
words = nltk.word_tokenize(sys.argv[1])
# breaking this up into individual words so that later on I
# can screw with color-swapping each word.
# this is literally useless in this script as it currently stands.
# remove it and I will dislike you, but I'll understand.
rotayshun = int(sys.argv[2])
# you enter this number bare, but python treats all argv as string
# Let's retype it to int, because that's what sense.set_rotation requires
if rotayshun == 0 or rotayshun % 90 == 0:
    sense.set_rotation(rotayshun)
elif rotayshun is None:
    sense.set_rotation(180)
else:
    print "Figure your shit out, jerky"
# this isn't currently handling null argv[2]. I also haven't
# controlls for > 270 yet. I'll get on it.

for word in words:
    sense.show_message(word)
# YEEEEE display it on the LCD. I want to feed it more than just a quote-wrapped text.
