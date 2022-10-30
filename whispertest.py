import whisper
import os


audiofile = "audio.mp3"
fileexists = os.path.isfile(audiofile) 
print(fileexists)

if(fileexists):
    model = whisper.load_model("base")
    result = model.transcribe(audiofile, fp16=False, language="es")
    # result = model.transcribe(audiofile)
    print(result["text"])
else:
    print(f"El archivo {audiofile} no existe")