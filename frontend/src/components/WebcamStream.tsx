import React, { useEffect, useRef } from 'react';

const WebcamStream: React.FC = () => {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
          if (videoRef.current) {
            videoRef.current.srcObject = stream;
          }

          // Cleanup
          return () => {
            stream.getTracks().forEach((track) => {
              track.stop();
            });

            if (videoRef.current) {
              videoRef.current.srcObject = null;
            }
          };
        })
        .catch((err) => {
          console.error("Error accessing the webcam:", err);
        });
    }
  }, []);

  return <video ref={videoRef} autoPlay playsInline style={{ transform: 'scaleX(-1)' }}/>;
};

export default WebcamStream;
