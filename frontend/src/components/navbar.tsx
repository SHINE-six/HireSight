'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import LoginPopup from './Login';


const Navbar: React.FC = () => {
    const [login, setLogin] = useState(false);

    function handleLogin() {
        setLogin(true);
    }

    return (
        <nav>
            <div className='flex justify-between items-center mx-[3rem]'>
                <div className='text-[2.2rem] font-semibold text-red-700'>
                    <Link href="/">HireSight</Link>
                </div>
                <div className='flex flex-row space-x-12 text-xl'>
                    <Link href="/">Home</Link>
                    <Link href="/job-opening">Job Opening</Link>
                    {login && <Link href="/ai-interview">Ai Interview</Link>}
                </div>
            </div>
            {!login && <LoginPopup handleLogin={handleLogin}/>}
        </nav>
    );
};

export default Navbar;