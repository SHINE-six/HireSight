'use client'
import React, {useEffect, useState} from "react";
import View from "./PDFView";

// const Template = dynamic(() => import("./PDFFileTSX"), {
//   loading: () => <p>Loading...</p>,
//   ssr: false,
//   });

const MyPage = () => {
  const [isLoading, setIsLoading] = useState(true)
  useEffect(() => {
    const getReportGeneratingStatus = async () => {
      const response = await fetch('http://localhost:8000/get-report-loading')
      const data = await response.json()
      if(data.message === 'False'){
        setIsLoading(false)
      }
    }

    getReportGeneratingStatus()
  }, [])

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-0">
      {isLoading ? <p>Loading...</p>: <View />}
      {/* <View /> */}
    {/* <MyRadarChart /> */}
    </main>
  );
};

export default MyPage;
