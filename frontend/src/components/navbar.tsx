import React from 'react';
import Link from 'next/link';

const Navbar: React.FC = () => {
    return (
        <nav>
            <div className='flex justify-between items-center mx-[3rem]'>
                <div className='text-[2.2rem] font-semibold text-red-700'>
                    <Link href="/">HireSight</Link>
                </div>
                <div className='flex flex-row space-x-12 text-xl'>
                    <Link href="/">Home</Link>
                    <Link href="/job-opening">Job Opening</Link>
                    <Link href="/ai-interview">Ai Interview</Link>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;