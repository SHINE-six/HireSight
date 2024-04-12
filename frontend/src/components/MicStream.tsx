import React, { useEffect, useRef, useState, } from 'react';


interface ChildProps {
  isRecording: any;
  onAudioUrlChange: (newAudioUrl: string | null) => void;
  onJsonDataChange: (newJsonData: any | null) => void;
}

const MicStream: React.FC<ChildProps> = (props) => {
  const [audioStream, setaudioStream] = useState<MediaStream | null>(null);
  const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
  const recordedChunksRef = useRef<Blob[]>([]);
  let recorder: MediaRecorder | null;

  const { onAudioUrlChange, onJsonDataChange } = props;

  useEffect(() => {
    // Access the Mic
    const accessMic = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        setaudioStream(stream);
        return () => stream.getTracks().forEach(track => track.stop());  // Cleanup
      } catch (error) {
        console.error("Error accessing the mic", error);
      }
    };

    accessMic();

    return () => {
      // Cleanup
      if (audioStream) {
        audioStream.getTracks().forEach(track => track.stop());
      }
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

    const response = await fetch('http://localhost:8000/audio', {
      method: 'POST',
      body: formData,
    });

    console.log(response);

    get_fromAI_fromBackend();

  };

  const get_fromAI_fromBackend = async () => {
    let intervalId: NodeJS.Timeout;
    const fetchData = async () => {
      try {
          const response = await fetch('http://localhost:8000/task-status', { method: 'GET' });
          const data = await response.json();
          console.log("status: ", data.status);
          if (data.status) {
              clearInterval(intervalId);

              const responseAudio = await fetch('http://localhost:8000/get-fromAI-wav', { method: 'GET' });
              const blob = await responseAudio.blob();
              const url = URL.createObjectURL(blob);
              onAudioUrlChange(url);

              const responseJson = await fetch('http://localhost:8000/get-fromAI-json', { method: 'GET' });
              const jsonData = await responseJson.json();
              onJsonDataChange(jsonData);
          }
      } catch (error) {
          console.error('Error getting fromAI from backend:', error);
          clearInterval(intervalId);
          setTimeout(get_fromAI_fromBackend, 10000);
      }
    };
    intervalId = setInterval(fetchData, 6000);
  };

  // const get_fromAI_fromBackend: () => Promise<void> = async () => {
  //   let data = {status: false};
  //   while (!data.status) {
  //     try {
  //       const response = await fetch('http://localhost:8000/task-status', { method: 'GET' });
  //       const data = await response.json();
  //       console.log("status: ", data.status);
  //       if (!data.status) {
  //         await new Promise(resolve => setTimeout(resolve, 6000));
  //       } else {
  //         const response = await fetch('http://localhost:8000/get-fromAI-wav', { method: 'GET' });
  //         const blob = await response.blob();
  //         const url = URL.createObjectURL(blob);
  //         onAudioUrlChange(url);

  //         const responseJson = await fetch('http://localhost:8000/get-fromAI-json', { method: 'GET' });
  //         const jsonData = await responseJson.json();
  //         onJsonDataChange(jsonData);
  //       }            
  //     } catch (error) {
  //       console.error('Error getting fromAI from backend:', error);
  //       setTimeout(get_fromAI_fromBackend, 10000);
  //     }
  //   }
  // }

  useEffect(() => {
    if (props.isRecording) {
      startRecording();
    } else {
      stopRecording();
    }
  }, [props.isRecording]);


  return (
    <div>
    </div>
  );
};

export default MicStream;
