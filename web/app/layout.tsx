import type { Metadata, Viewport } from "next";
import { Heebo, Inter } from "next/font/google";

import "./globals.css";

const inter = Inter({ variable: "--font-inter", subsets: ["latin"] });
const heebo = Heebo({ variable: "--font-heebo", subsets: ["hebrew", "latin"] });

export const metadata: Metadata = {
  title: "Daily Brief",
  description: "Sports, world affairs and ideas: read in 30 seconds, 3 minutes or 10.",
  appleWebApp: { capable: true, title: "Brief", statusBarStyle: "default" },
  icons: {
    icon: [{ url: "/icon-192.png", sizes: "192x192", type: "image/png" }],
    apple: [{ url: "/apple-touch-icon.png", sizes: "180x180" }],
  },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#f6f4ef" },
    { media: "(prefers-color-scheme: dark)", color: "#131210" },
  ],
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className={`${inter.variable} ${heebo.variable} antialiased`}>
      <body className="min-h-dvh">{children}</body>
    </html>
  );
}
