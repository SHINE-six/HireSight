'use client';

import { useUserInfoStore } from "@/stores/userInfoStore";

export default function RootLayout({children} : Readonly<{ children: React.ReactNode }>){
    const { email, aiStage } = useUserInfoStore();
    
    return (
        <div>
            {(email !== "" && aiStage !== false) ? (
                <>
                    <div>Welcome {email}</div>
                    <div>{children}</div>
                </>
            ) 
            : 
            <div>Not authorized</div>}
        </div>
    );
}