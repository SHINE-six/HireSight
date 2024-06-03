import React from "react";
import View from "./PDFView";

// const Template = dynamic(() => import("./PDFFileTSX"), {
//   loading: () => <p>Loading...</p>,
//   ssr: false,
//   });

const MyPage = () => {

  return (

    <main className="flex min-h-screen flex-col items-center justify-between p-0 h-full">
      <View />
    {/* <MyRadarChart /> */}
    </main>
  );
};

export default MyPage;
