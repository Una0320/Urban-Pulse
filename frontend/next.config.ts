import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  transpilePackages: ['@deck.gl/layers', '@deck.gl/react', '@deck.gl/core'],
};

export default nextConfig;
