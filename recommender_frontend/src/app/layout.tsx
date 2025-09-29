import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Sistema de Recomendación Académico",
  description:
    "Encuentra recursos de estudio personalizados basados en tu carrera, semestre y curso",
  icons: {
    icon: [
      { url: "/favicon-Recocurso.png", sizes: "32x32", type: "image/png" },
      { url: "/Imagen-Recocurso.png", sizes: "192x192", type: "image/png" },
    ],
    apple: [
      { url: "/Imagen-Recocurso.png", sizes: "180x180", type: "image/png" },
    ],
    shortcut: "/favicon-Recocurso.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
