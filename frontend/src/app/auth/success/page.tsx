"use client";
export const dynamic = "force-dynamic"; 

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function AuthRedirect() {
  const router = useRouter();

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const accessToken = params.get("access_token");
    if (accessToken) {
      localStorage.setItem("access_token", accessToken);
      router.replace("/");
    }
  }, [router]);

  return <div>Logging you in...</div>;
}
