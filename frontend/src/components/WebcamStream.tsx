import React, { useEffect, useRef, useState, } from 'react';

const WebcamRecorder: React.FC<{isRecording: boolean}> = ({ isRecording }: { isRecording: boolean }) => {
  // const [videoStream, setVideoStream] = useState<MediaStream | null>(null);
  const videoStream = useRef<MediaStream | null>(null);
  // const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
  const mediaRecorder = useRef<MediaRecorder | null>(null);
  const recordedChunksRef = useRef<Blob[]>([]);
  let recorder: MediaRecorder | null;

  useEffect(() => {
    // Access the webcam
    const accessWebcam = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        // setVideoStream(stream);
        videoStream.current = stream;
        const videoElement = document.querySelector('video');
        if (videoElement) videoElement.srcObject = stream;
      } catch (error) {
        console.error("Error accessing the camera", error);
      }
    };

    accessWebcam();

    return () => {
      // Cleanup
      if (videoStream.current) {
        videoStream.current.getTracks().forEach(track => track.stop());
      }

      if (mediaRecorder.current) {
        mediaRecorder.current.stop();
      }
    };
  }, []);

  const startRecording = () => {
    if (!videoStream.current) {
      console.error('No video stream available');
      return;
    }

    recorder = new MediaRecorder(videoStream.current, { mimeType: 'video/webm; codecs=vp9' });
    recorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        recordedChunksRef.current.push(event.data);
        console.log(event.data);
      }
    };
    recorder.start();
    // setMediaRecorder(recorder);
    mediaRecorder.current = recorder;
    console.log(recorder)
  };

  const stopRecording = () => {
    if (!mediaRecorder.current) {
      console.error('No media recorder available');
      return;
    }

    mediaRecorder.current.stop();
    mediaRecorder.current.onstop = () => {
      const videoBlob = new Blob(recordedChunksRef.current, { type: 'video/webm' });
      console.log(recordedChunksRef)
      sendVideoToBackend(videoBlob);
      recordedChunksRef.current = [];
    };
  };

  const sendVideoToBackend = async (blob: Blob | null) => {
    if (blob === null) {
      console.error('No video blob available');
      return;
    }
    const formData = new FormData();
    formData.append('video', blob, 'webcam-video.mp4');
    console.log(formData)

    try {
      const response = await fetch('http://localhost:8000/video', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      console.log('Video uploaded successfully');
    } catch (error) {
      console.error('Error uploading the video:', error);
    }
  };

  useEffect(() => {
    if (isRecording) {
      startRecording();
    } else {
      stopRecording();
    }
  }, [isRecording]);


  return (
    <div>
      <video autoPlay playsInline muted className="transform scale-x-[-1] filter contrast-[1.4] saturate-[1.3] brightness-[1.5] relative top-[-4.5rem]"></video>
    </div>
  );
};

export default WebcamRecorder;
