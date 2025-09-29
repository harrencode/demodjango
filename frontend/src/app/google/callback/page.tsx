// app/google/callback/page.tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function GoogleCallbackPage({
  searchParams,
}: {
  searchParams: { code?: string };
}) {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const code = searchParams.code;

    if (!code) {
      setError("Invalid callback: no code provided.");
      return;
    }

    // The backend (Django) handles the token exchange via GET automatically
    // Redirect the user to a success page or dashboard
    const handleRedirect = async () => {
      try {
        // Optionally, you could fetch your backend to store the JWT in a cookie
        // But typically, dj-rest-auth will return a redirect or JWT from the GET callback
        router.push("/"); // redirect to home/dashboard
      } catch (err) {
        console.error(err);
        setError("Something went wrong during login.");
      }
    };

    handleRedirect();
  }, [searchParams.code, router]);

  if (error) return <div>{error}</div>;

  return <div>Logging in with Google...</div>;
}
