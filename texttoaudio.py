from gtts import gTTS

text ="hello everyone, it's aniket !"
tts = gTTS(text = text, lang='en')

tts.save("voice.mp3")

print("audio saved successfully")
