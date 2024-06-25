

# import whisper

# model = whisper.load_model("small")  # other models are "tiny", "base", "medium", "large" based on your needs

# result = model.transcribe("presentation.mp4")

# print(result["text"])



import requests
import json

def send(query):
    try:
        url = "https://mixtral.k8s-gosha.atlas.illinois.edu/completion"

        myobj = {
            "prompt": "<s>[INST]" + query + "[/INST]",
            "n_predict": -1  # No limit on tokens for output
        }

        headers = {
            "Content-Type": "application/json",
            #"Authorization": "Basic YXRsYXNhaXRlYW06anhAVTJXUzhCR1Nxd3U=" #--what is this for?
        }

        response = requests.post(url, data=json.dumps(myobj), headers=headers,
                                 auth=('atlasaiteam', 'jx@U2WS8BGSqwu'), timeout=1000)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response in JSON format
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Testing query
query = "Building a website can be done in 10 simple steps:"
result = send(query)
print(result)



# import assemblyai as aai

# # Replace with your API key
# aai.settings.api_key = "9cd5039fa6a54090a638e389ce52b772"

# # URL of the file to transcribe
# FILE_URL = "presentation.mp4"

# # You can also transcribe a local file by passing in a file path
# # FILE_URL = './path/to/file.mp3'

# transcriber = aai.Transcriber()
# transcript = transcriber.transcribe(FILE_URL)

# if transcript.status == aai.TranscriptStatus.error:
#     print(transcript.error)
# else:
#     print(transcript.text)
