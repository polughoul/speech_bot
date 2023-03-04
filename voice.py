import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0")


def text_to_file(text):
   tmp_file_name = "sounds"
   engine.save_to_file(text, f"data/{tmp_file_name}.mp3")
   engine.runAndWait()
   return f"data/{tmp_file_name}.mp3"




