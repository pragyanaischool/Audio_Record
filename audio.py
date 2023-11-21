import streamlit as st
from audiorecorder import audiorecorder
from IPython.display import Audio
from ipywebrtc import CameraStream, AudioRecorder

st.title("Audio Recorder")


# actually I found this hack in some js code
# just pass mime type =)
camera = CameraStream(constraints={'audio': True,
                                   'video': False},
                      mimeType='audio/wav')
recorder = AudioRecorder(stream=camera)

# turn the recorder on
# still a bit rusty on whether I need to show it 
# in a separate cell later to make it work
recorder.recording = True
# say something
# turn the recorder off
recorder.recording = False
recorder.save('test.wav')
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("audio.wav", format="wav")

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")
