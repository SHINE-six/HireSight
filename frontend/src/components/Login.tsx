'use client';

import React, { useState } from 'react';
// import { handleSubmit } from './LoginClass';

interface LoginPopupProps {
    handleLogin: () => void;
}

const PostLoginInfo = async (formData: FormData) => {
    const res = await fetch('http://localhost:8000/login', {
        method: 'POST',
        body: formData
    });
    const data = await res.json();
    console.log(data);
}

const LoginPopup:React.FC<LoginPopupProps> = ({ handleLogin }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    function handleLocalSubmit(e: React.FormEvent) {
        e.preventDefault();
        const formData = new FormData();
        formData.append('email', email);
        formData.append('password', password);
        PostLoginInfo(formData);
        handleLogin();
    }
    
    return (
        <div className="absolute top-0 left-0 w-screen h-full bg-black bg-opacity-50 z-50">
            <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-[2rem] rounded-lg shadow-lg">
                <div className="text-2xl font-bold text-red-700">Login</div>
                <form className="mt-[1rem]" onSubmit={(e)=>handleLocalSubmit(e)}>
                    <div className="flex flex-col space-y-4">
                        <input className="border border-gray-300 p-[0.5rem] rounded-md" type="text" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
                        <input className="border border-gray-300 p-[0.5rem] rounded-md" type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
                        <button className="bg-red-700 text-white p-[0.5rem] rounded-md" type='submit'>Login</button>
                    </div>
                </form>
            </div>
        </div>
    );
}


export default LoginPopup;