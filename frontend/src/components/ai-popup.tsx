'use client';

import { useState } from "react";
import { IoChatboxEllipses } from "react-icons/io5";
import { FaWindowClose } from "react-icons/fa";
import { IoSend } from "react-icons/io5";

interface Message {
    user: string;
    content: string;
}

// Function to Connect to backend API to get the response
const getResponse = async (message: string) => {
    const res = await fetch('http://localhost:11434/api/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(
            { 
                "model": "llama3",
                "prompt": message,
                "stream": false,
            }
        ),
    });
    const data = await res.json();
    return data;
}


const AiPopup = () => {
    const [isOpen, setIsOpen] = useState(false);

    const handleOnClick = () => {
        setIsOpen(!isOpen);
    }

    const [message, setMessage] = useState("");
    const [response, setResponse] = useState("");

    const [messageHistory, setMessageHistory] = useState<Message[]>([]);

    const handleOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setMessage(e.target.value);
    }

    const handleOnSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        // Call your API or perform any logic here to get the response
        // For now, let's just set a dummy response
        const formatMessage = { user: "You", content: message };
        setMessageHistory((prevMessageHistory) => [...prevMessageHistory, formatMessage]);

        getResponse(message).then((data) => {
            setResponse(data.response);
            const formatResponse = { user: "System", content: data.response };
            setMessageHistory((prevMessageHistory) => [...prevMessageHistory, formatResponse]);
        });
        setMessage("");
    }

    return (
        <div className='fixed top-0 left-0 w-full h-full flex justify-end items-end z-40'>
            <div onClick={handleOnClick} className='bg-gray-200 p-[0.8rem] rounded-full aspect-square mr-[1rem] mb-[1rem] text-3xl border-black border-[0.01rem]'>
                {isOpen ? <FaWindowClose /> : <IoChatboxEllipses />}
            </div>
            {isOpen && (
                <div className='fixed bottom-[6rem] right-0 w-[17rem] h-[20rem] bg-white border p-4 transition-all transform ease-in-out duration-500'>
                    <div className="sticky top-0">Chat Panel</div>
                    <div className="flex flex-col h-full justify-stretch overflow-auto">
                        <div className="h-fit mb-[3rem]">
                            {messageHistory && messageHistory.map((msg, index) => {
                                const style = msg.user === "You" ? "bg-gray-200 ml-auto" : "bg-gray-300";
                                return (
                                    <div key={index} className={`p-[0.5rem] rounded-md ${style} mb-[0.5rem] w-fit`}>
                                        <div>{msg.user}</div>
                                        <div>{msg.content}</div>
                                    </div>
                                )
                            })}
                        </div>
                        <div className="fixed bottom-0">
                            <form onSubmit={handleOnSubmit}>
                                <input type="text" value={message} onChange={handleOnChange} className="border-2 border-black"/>
                                    <button type="submit">
                                        <div className="ml-[0.5rem] text-lg">
                                            <IoSend />
                                        </div>
                                    </button>
                            </form>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}
export default AiPopup;