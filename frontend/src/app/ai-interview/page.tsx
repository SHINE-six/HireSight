'use client';

import React, { useEffect, useRef, useState } from "react";
import WebcamStream from "@/components/WebcamStream";
import MicStream from "@/components/MicStream";
import Experience from "@/components/Experience";
import { CiMicrophoneOn, CiMicrophoneOff } from "react-icons/ci";
import { Canvas } from "@react-three/fiber";

export default function AiInterviewPage() {
    const isLogin = useRef<boolean>(false);
    const [isRecording, setIsRecording] = useState(false);
    const [audioUrl, setAudioUrl] = useState<string | null>('/audios/fromAI.wav');
    const [jsonData, setJsonData] = useState<any | null>('/audios/fromAI.json');
    const [loading, setLoading] = useState(false);

    // const wav_file = ['/audios/fromAI(1).wav', '/audios/fromAI(1r).wav', '/audios/fromAI(2).wav', '/audios/fromAI(3).wav', '/audios/fromAI(4).wav', '/audios/fromAI(5).wav', '/audios/fromAI(6).wav', '/audios/fromAI(7).wav', '/audios/fromAI(8).wav'];
    // const json_file = ['/audios/fromAI(1).json', '/audios/fromAI(1r).json', '/audios/fromAI(2).json', '/audios/fromAI(3).json', '/audios/fromAI(4).json', '/audios/fromAI(5).json', '/audios/fromAI(6).json', '/audios/fromAI(7).json', '/audios/fromAI(8).json'];
    // const [counter, setCounter] = useState(0);

    const handleRecord = () => {
        if (isRecording) {
            setIsRecording(false);
            setLoading(true);
            // setCounter((counter + 1));
            // setAudioUrl(wav_file[counter]);
            // setJsonData(json_file[counter]);
        }
        else {
            setIsRecording(true);
        }
    }

    const handleAudioUrlChange = (newAudioUrl: string | null) => {
        console.log("this is ", newAudioUrl);
        if (!newAudioUrl) return;
        console.log("playing audio")
        setAudioUrl(newAudioUrl);
        setLoading(false);
    }

    const handleJsonDataChange = (newJsonData: any | null) => {
        console.log(newJsonData);
        setJsonData(newJsonData);
    }

    useEffect(() => {
        if (!isLogin.current) {
            console.log("FFFFFFFFFFFFFFF");
        }
        isLogin.current = true;
    }, []);

    return (
        <div className="mx-24">
            <div className="text-4xl font-bold my-[2rem] text-center">AI Interview Session - EVA</div>
            <div className="flex flex-row justify-around">
                <div className={`w-[30rem] h-[18rem] overflow-hidden rounded-md border-2 ${isRecording? 'border-red-600 shadow-red-600' : 'border-black shadow-black'} shadow-md`}>
                    <WebcamStream isRecording={isRecording}/>
                </div>
                <div className={`bg-blue-200 relative w-[30rem] h-[18rem] rounded-md border-2 overflow-visible ${isRecording? 'border-black shadow-black' : 'border-red-600 shadow-red-600'} shadow-md`}>
                    <div className="absolute z-30 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                        {loading && <img className="w-[4rem]" src="/loading.gif" alt="Loading" />}
                    </div>
                    <Canvas shadows camera={{ position: [0, 0.3, 6], fov: 20 }}>
                        <Experience newAudioURL={audioUrl} newJsonData={jsonData}/>
                    </Canvas>
                </div>
            </div>

            <MicStream 
                isRecording={isRecording}
                onAudioUrlChange={handleAudioUrlChange}
                onJsonDataChange={handleJsonDataChange}
            />
            <button onClick={handleRecord} className="w-full flex justify-center mt-[3rem]">
                <div className="text-[6rem] ">
                    {isRecording ? <CiMicrophoneOn /> : <CiMicrophoneOff />}
                </div>
            </button>
        </div>
    );
}