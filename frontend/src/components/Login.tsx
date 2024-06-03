'use client';

import React, { useState } from 'react';
import { useUserInfoStore } from '@/stores/userInfoStore';


const PostLoginInfo = async (email: string, password: string) => {
    const res = await fetch('http://localhost:8000/login', {
        method: 'POST',
        // body: formData,
        headers: {
            Authorization: 'Basic ' + btoa(email + ':' + password),
        },
        credentials: 'include'  // Include credentials in the request
    });
    const data = await res.json();
    console.log(data);
    return data;
}

const LoginPopup = () => {
    const [email, setLocalEmail] = useState('');
    const [password, setPassword] = useState('');
    const { setEmail, setAiStage } = useUserInfoStore();

    async function handleLocalSubmit(e: React.FormEvent) {
        e.preventDefault();
        // const formData = new FormData();
        // formData.append('email', email);
        // formData.append('password', password);
        const response = await PostLoginInfo(email, password); // Await the response
        if (response.status === 200) { // Access the status property
            setEmail(email);
            setAiStage(response.aiStage);
        }
        else {
            console.log('Login failed');
        }
    }
    
    return (
        <div className="absolute top-0 left-0 w-screen h-full bg-black bg-opacity-50 z-50">
            <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-[2rem] rounded-lg shadow-lg">
                <div className="text-2xl font-bold text-red-700">Login</div>
                <form className="mt-[1rem]" onSubmit={(e)=>handleLocalSubmit(e)}>
                    <div className="flex flex-col space-y-4">
                        <input className="border border-gray-300 p-[0.5rem] rounded-md" type="text" placeholder="Email" onChange={(e) => setLocalEmail(e.target.value)} />
                        <input className="border border-gray-300 p-[0.5rem] rounded-md" type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
                        <button className="bg-red-700 text-white p-[0.5rem] rounded-md" type='submit'>Login</button>
                    </div>
                </form>
            </div>
        </div>
    );
}


export default LoginPopup;