'use client'
import React, { useEffect, useState } from "react";
import View from "./PDFView";

// const Template = dynamic(() => import("./PDFFileTSX"), {
//   loading: () => <p>Loading...</p>,
//   ssr: false,
//   });

const MyPage = () => {
  // const [isGettingReportData, setIsGettingReportData] = useState("True")

  // useEffect(() => {
  //   const fetchData = async () => {
  //     const response = await fetch('http://localhost:8000/get-report-loading')
  //     const data = await response.json()
  //     setIsGettingReportData(data.message)
  //   }
  //   fetchData()
  // }, [])

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-0">
      {/* {(isGettingReportData === "False") ? <View /> : <p>Loading...</p>} */}
      <View />
    {/* <MyRadarChart /> */}
    </main>
  );
};

export default MyPage;
