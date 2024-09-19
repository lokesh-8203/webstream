import streamlit as st
import cv2
import numpy as np

st.title("HTTP Video Stream with OpenCV and Streamlit")

http_stream = "http://192.168.0.100:8080/video.mp4"  # Replace with your HTTP stream URL

# Initialize the video capture
cap = cv2.VideoCapture(http_stream, cv2.CAP_FFMPEG)

if not cap.isOpened():
    st.error("Error: Could not open video stream. Please check the stream URL.")
else:
    st.write("Video stream opened successfully.")
    
    # Stream video frames
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            st.write("Error: No frame received. This may be due to stream issues or end of stream.")
            break
        
        # Convert the frame to RGB (Streamlit uses RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame in Streamlit
        st.image(frame_rgb, channels="RGB", use_column_width=True)
        
        # Optional: Add OpenCV processing here, e.g., add text or overlays
        # frame = cv2.putText(frame, "Streaming from HTTP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
    # Release the capture when done
    cap.release()
    st.write("Video capture released.")
