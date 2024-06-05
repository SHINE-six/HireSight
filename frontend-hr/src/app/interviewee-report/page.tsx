import React from "react";
import View from "./PDFView";

// const Template = dynamic(() => import("./PDFFileTSX"), {
//   loading: () => <p>Loading...</p>,
//   ssr: false,
//   });

const MyPage = () => {

  return (
    <main className="flex h-fit flex-col items-center justify-between p-0  overflow-hidden">
      <View />
    {/* <MyRadarChart /> */}
    </main>
  );
};

export default MyPage;
