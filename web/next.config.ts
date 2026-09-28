import type { NextConfig } from "next";

// Static export: the app is plain files on a CDN. Today's brief is copied into
// public/briefs at build time (scripts/copy-briefs.mjs), and every commit of a new
// brief triggers a rebuild on Vercel.
const nextConfig: NextConfig = {
  output: "export",
  images: { unoptimized: true },
};

export default nextConfig;
