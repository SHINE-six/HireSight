import { create } from 'zustand';


type UserInfoStore = {
    email: string,
    aiStage: boolean,
    setEmail: (email: string) => void,
    setAiStage: (aiStage: boolean) => void
}

export const useUserInfoStore = create<UserInfoStore>((set) => ({
    email: '',
    aiStage: false,
    setEmail : (email) => set({ email }),
    setAiStage : (aiStage) => set({ aiStage }),
}));