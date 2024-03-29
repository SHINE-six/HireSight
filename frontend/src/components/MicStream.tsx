import React, { use, useEffect, useRef, useState, } from 'react';

const MicStream = ({ isRecording }: { isRecording: boolean }) => {
  const [audioStream, setaudioStream] = useState<MediaStream | null>(null);
  const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
  const recordedChunksRef = useRef<Blob[]>([]);
  let recorder: MediaRecorder | null;

  useEffect(() => {
    // Access the Mic
    const accessMic = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        setaudioStream(stream);
      } catch (error) {
        console.error("Error accessing the mic", error);
      }
    };

    accessMic();

    return () => {
      // Cleanup
      audioStream?.getTracks().forEach(track => track.stop());
    };
  }, []);

  const startRecording = () => {
    if (!audioStream) {
      console.error('No audio stream available');
      return;
    }

    recorder = new MediaRecorder(audioStream, { mimeType: 'audio/webm' });
    recorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        recordedChunksRef.current.push(event.data);
        console.log(event.data);
      }
    };
    recorder.start();
    setMediaRecorder(recorder);
    console.log(recorder)
  };

  const stopRecording = () => {
    if (!mediaRecorder) {
      console.error('No media recorder available');
      return;
    }

    mediaRecorder.stop();
    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(recordedChunksRef.current, { type: 'audio/webm' });
      console.log(recordedChunksRef)
      sendVideoToBackend(audioBlob);
      recordedChunksRef.current = [];
    };
  };

  const sendVideoToBackend = async (blob: Blob | null) => {
    if (blob === null) {
      console.error('No audio blob available');
      return;
    }
    const formData = new FormData();
    formData.append('audio', blob, 'mic-audio.webm');
    console.log(formData)

    try {
      const response = await fetch('https://ddncl8rd-8000.asse.devtunnels.ms/audio', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      console.log('Audio uploaded successfully');
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
    </div>
  );
};

export default MicStream;
