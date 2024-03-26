'use client';

import React from "react";
import WebcamStream from "@/components/WebcamStream";

export default function AiInterviewPage() {
    return (
        <div className="border-2 m-24">
            <div className="text-4xl font-bold">AI giua.</div>
            <WebcamStream />
        </div>
    );
}