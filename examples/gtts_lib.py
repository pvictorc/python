# Import the required module for text to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

# The text that you want to convert to audio
# mytext = 'Welcome to geeksforgeeks Joe!'
file = open('convertido.md','r') 
mytext = ''.join(file.readlines())
# mytext = "agora eu tenho meu próprio gerador de voz"

print(mytext) # debug 

# Language in which you want to convert
# language = 'en'
language = 'pt-BR'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
# myobj.save("welcome.mp3")
output = "output.mp3"
myobj.save(output)

# Playing the converted file
os.system("ffplay ${output}")
