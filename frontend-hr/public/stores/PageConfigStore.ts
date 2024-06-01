import { create } from 'zustand';

type ResumeCount = {
    Ai_detection: number,
    Resume_suitability: number,
    Interview: number
}

type PageConfigStore = {
    currentAvailableJob: string,
    resumeCount: ResumeCount,
    setCurrentAvailableJob: (job: string) => void,
    setResumeCount_Ai_detection: (count: number) => void,
    setResumeCount_Resume_suitability: (count: number) => void,
    setResumeCount_Interview: (count: number) => void
}

export const usePageConfigStore = create<PageConfigStore>((set) => ({
    currentAvailableJob: '',
    resumeCount: {
        Ai_detection: 0,
        Resume_suitability: 0,
        Interview: 0
    },
    setCurrentAvailableJob: (job) => set({ currentAvailableJob: job }),
    setResumeCount_Ai_detection: (count) => set((state) => ({ resumeCount: { ...state.resumeCount, Ai_detection: count } })),
    setResumeCount_Resume_suitability: (count) => set((state) => ({ resumeCount: { ...state.resumeCount, Resume_suitability: count } })),
    setResumeCount_Interview: (count) => set((state) => ({ resumeCount: { ...state.resumeCount, Interview: count } }))
}));