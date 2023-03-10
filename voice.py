import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0")


def text_to_file(text):
   tmp_file_name = "sounds.mp3"
   engine.save_to_file(text, "sounds.mp3")
   engine.runAndWait()
   return tmp_file_name




