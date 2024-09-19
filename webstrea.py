import streamlit as st
import cv2
import numpy as np

st.title("HTTP Stream with OpenCV")

http_stream = "http://your-stream-url"

# Capture video
cap = cv2.VideoCapture(http_stream, cv2.CAP_FFMPEG)

while True:
    ret, frame = cap.read()
    if not ret:
        st.write("Failed to capture frame.")
        break

    # Apply any OpenCV processing here
    # Example: Adding a text overlay
    frame = cv2.putText(frame, "Streaming from HTTP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame
    st.image(frame_rgb, channels="RGB")

# Release the capture when done
cap.release()
