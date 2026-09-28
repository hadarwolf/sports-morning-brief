import type { MetadataRoute } from "next";

export const dynamic = "force-static";

// Makes the site installable: "Add to Home Screen" opens it full-screen like an app.
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Daily Brief",
    short_name: "Brief",
    description: "Sports, world affairs and ideas: read in 30 seconds, 3 minutes or 10.",
    start_url: "/",
    display: "standalone",
    orientation: "portrait",
    background_color: "#f6f4ef",
    theme_color: "#f6f4ef",
    icons: [
      { src: "/icon-192.png", sizes: "192x192", type: "image/png" },
      { src: "/icon-512.png", sizes: "512x512", type: "image/png" },
      { src: "/icon-maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
  };
}
