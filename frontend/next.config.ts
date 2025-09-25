import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */

  turbopack: {
    root: __dirname, // explicitly sets the correct root to avoid waring about multiple package-lock.josn files
  },
};

export default nextConfig;
