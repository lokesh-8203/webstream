import streamlit as st
import ffmpeg
import numpy as np
import io
from PIL import Image

st.title("HTTP Video Stream with ffmpeg-python and Streamlit")

http_stream = "http://192.168.0.100:8080/video"  # Replace with your HTTP stream URL

def get_frame_from_stream(stream_url):
    # Create a pipe to read video frames from ffmpeg
    process = (
        ffmpeg
        .input(stream_url)
        .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        .run_async(pipe_stdout=True, pipe_stderr=True)
    )
    return process

def stream_video():
    # Start ffmpeg process
    process = get_frame_from_stream(http_stream)
    
    while True:
        # Read raw video frame data from ffmpeg
        in_bytes = process.stdout.read(640 * 480 * 3)  # Adjust widthheightchannels as needed

        if not in_bytes:
            st.write("Error: No frame received.")
            break
        
        # Convert raw bytes to numpy array
        frame = np.frombuffer(in_bytes, np.uint8).reshape((480, 640, 3))  # Adjust height and width as needed

        # Convert numpy array to PIL Image for Streamlit
        image = Image.fromarray(frame)
        
        # Display the image
        st.image(image, channels="RGB", use_column_width=True)

    process.terminate()

# Stream video frames
stream_video()
