from google.cloud import storage
from google.cloud import texttospeech


def text_to_speech(event, context):
    """
    This function is triggered by uploading / updating a '.txt' file
    in a GCS bucket.
    
    An '.mp3' file with the same name will appear in the specified bucket.
    """


    # Check if the uploaded file has '.txt' format
    if event['name'][-4:] != ".txt":
        print("Wrong file provided: provided file must have '.txt' extension")
        return ""
    

    # Instantiate a storage client
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(event['bucket'])
    blob = bucket.get_blob(event['name'])
    

    # Instantiate a text-to-speech client
    tts_client = texttospeech.TextToSpeechClient()
    #tts_client.from_service_account_json("credentials.json")

    
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=blob.download_as_string())


    # Build the voice request, select the language code ("en-US") and the ssml
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Wavenet-B',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

    
    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3, speaking_rate=1.2, pitch=-2.0)

    
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = tts_client.synthesize_speech(synthesis_input, voice, audio_config)

    
    # The response's audio_content is binary.
    with open('/tmp/output.mp3', 'wb') as out:
        out.write(response.audio_content)
        audio_file = event['name'][:-4] + '.mp3'
        print("Audio content written to file '{}'".format(audio_file))
        blob = bucket.blob(audio_file)
        blob.upload_from_filename("/tmp/output.mp3")
        
