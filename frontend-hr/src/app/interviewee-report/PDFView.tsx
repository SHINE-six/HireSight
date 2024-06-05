'use client'
import dynamic from "next/dynamic";
import { useEffect, useState } from "react"


const InvoicePDF = dynamic(() => import("./PDFFileTSX"), {
    ssr: false,
  });


const View = () => {

    const [client, setClient] = useState(false)

    useEffect(() => {
        setClient(true)
    }, [])

    return(
        <div className="absolute top-0 h-fit w-screen">
            <InvoicePDF/>
        </div>
    )
}


export default View