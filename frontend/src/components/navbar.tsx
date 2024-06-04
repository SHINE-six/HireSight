'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { useUserInfoStore } from '@/stores/userInfoStore';
import LoginPopup from './Login';


const Navbar: React.FC = () => {
    const { email, aiStage } = useUserInfoStore();
    const [showLogin, setShowLogin] = useState(false);

    useEffect(() => {
        if (email != "") {
            setShowLogin(false);
        }
    }, [email]);

    return (
        <nav>
            <div className='flex justify-between items-center mx-[3rem] cursor-pointer'>
                <div className='text-[2.2rem] font-semibold text-red-700'>
                    <Link href="/">HireSight</Link>
                </div>
                <div className='flex flex-row space-x-12 text-xl'>
                    <Link href="/">Home</Link>
                    <Link href={`/job-opening`}>Job Opening</Link>
                    {email && aiStage && <Link href={`/ai-interview`}>Ai Interview</Link>}
                    {(email=="") && <div onClick={()=>setShowLogin(true)}>Login</div>}
                    {showLogin && <LoginPopup />}
                </div>
            </div>
        </nav>
    );
};

export default Navbar;