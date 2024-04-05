import type { Metadata } from "next";
import Navbar from "@/components/navbar";
import "./globals.css";

export const metadata: Metadata = {
  title: "HireSight - prototype",
  description: "The prototype of HireSight by team HireMe",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className="bg-white py-[1rem] font-work-sans">
        <Navbar />
        <main>{children}</main>
      </body>
    </html>
  );
}
