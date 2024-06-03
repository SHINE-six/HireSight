'use client'
import dynamic from "next/dynamic";
import { useEffect, useState } from "react"


const InvoicePDF = dynamic(() => import("./PDFFileTSX"), {
    
    ssr: false,
  });


const View = ({info} : any) => {

    const [client, setClient] = useState(false)

    useEffect(() => {
        setClient(true)
    }, [])

    return(
        <InvoicePDF/>
    )
}


export default View