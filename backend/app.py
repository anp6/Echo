

import assemblyai as aai

aai.settings.api_key = "9cd5039fa6a54090a638e389ce52b772"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)