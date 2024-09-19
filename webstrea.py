import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av
import cv2

http_stream = "http://192.168.0.100:8080/video"  # Replace with your HTTP stream URL

# Class to handle video frames from the HTTP stream
class VideoProcessor(VideoTransformerBase):
    def __init__(self):
        # Open the HTTP stream with OpenCV
        self.cap = cv2.VideoCapture(http_stream, cv2.CAP_FFMPEG)

    def __del__(self):
        # Release the video capture when done
        if self.cap.isOpened():
            self.cap.release()

    def transform(self, frame):
        # Read a frame from the HTTP stream
        ret, img = self.cap.read()

        if not ret:
            return av.VideoFrame.from_ndarray(frame.to_ndarray(format="bgr24"), format="bgr24")

        # Optionally, apply some OpenCV operations on img here
        img = cv2.putText(img, "Streaming from HTTP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Return the processed frame
        return av.VideoFrame.from_ndarray(img, format="bgr24")


# Set up Streamlit
st.title("HTTP Stream in Streamlit with OpenCV")

# Use the webrtc_streamer to stream the live HTTP feed
webrtc_streamer(
    key="example-http-stream",
    video_transformer_factory=VideoProcessor,
    sendback_audio=False
)
