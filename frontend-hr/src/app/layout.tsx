import type { Metadata } from "next";
import "./globals.css";
import Header from "@/components/header";

export const metadata: Metadata = {
  title: "HireSight - prototype",
  description: "The prototype of HireSight by team HireMe",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className="bg-white p-[1rem] font-work-sans">
        <main>
          <Header />
          {children}
        </main>
      </body>
    </html>
  );
}
