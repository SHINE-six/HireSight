'use client';

import { useUserInfoStore } from "@/stores/userInfoStore";
import ConsentPopUp from "@/components/ConsentPopUp";
import { useState } from "react";

export default function RootLayout({children} : Readonly<{ children: React.ReactNode }>){
    const { email, aiStage } = useUserInfoStore();
    const [show, setShow] = useState(true);

    const handleConsent = () => {
        setShow(false);
    }
    
    return (
        <div>
            {(email !== "" && aiStage !== false) ? (
                <>
                {(show) ? <ConsentPopUp handleConsent={handleConsent}/> : (
                    <>
                        <div className="text-lg font-semibold w-full text-center">Welcome <span className="underline">{email}</span></div>
                        <div>{children}</div>
                    </>
                )}
                </>
            ) 
            : 
            <div>Not authorized</div>}
        </div>
    );
}