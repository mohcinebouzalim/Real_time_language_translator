import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

r1 = sr.Recognizer()
r2 = sr.Recognizer()

mic = sr.Microphone(device_index = 0)

with mic as source:
	print("say Hello to initiate the translation")
	print("-------------------------------------")
	audio = r1.listen(source)

result = r1.recognize_google(audio)

if "hello" in result:
	transtlator = Translator()
	with mic as source:
		print("Speak sentence ...")
		audio2 = r2.listen(source)

	result2 = r2.recognize_google(audio2)
	try:
		text_translation = transtlator.translate(result2, src="en", dest="fr")
		translated_text = text_translation.text
		speak = gTTS(text=translated_text, lang="fr", slow=False)
		speak.save("transaltion.mp3")
		os.system("start transaltion.mp3")
	except sr.UnknownValueError:
		print("I don't understand the sentence")
	except sr.RequestError as e:
		print("I can't provide required output".format(e))
