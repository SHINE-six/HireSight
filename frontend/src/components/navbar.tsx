import React from 'react';
import Link from 'next/link';

const Navbar: React.FC = () => {
    return (
        <nav>
            <div className='flex justify-between items-center'>
                <div className='text-3xl font-medium'>HireSight</div>
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