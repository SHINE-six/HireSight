'use client';

import React, { useState } from "react";
import WebcamStream from "@/components/WebcamStream";
import MicStream from "@/components/MicStream";
import { CiMicrophoneOn, CiMicrophoneOff } from "react-icons/ci";

export default function AiInterviewPage() {
    const [isRecording, setIsRecording] = useState(false);

    const handleRecord = () => {
        setIsRecording(!isRecording);
    }

    return (
        <div className="border-2 m-24">
            <div className="text-4xl font-bold">AI giua.</div>
            <WebcamStream isRecording={isRecording}/>
            <MicStream isRecording={isRecording}/>
            <button onClick={handleRecord}>
                <div className="text-6xl">
                    {isRecording ? <CiMicrophoneOn /> : <CiMicrophoneOff />}
                </div>
            </button>
        </div>
    );
}