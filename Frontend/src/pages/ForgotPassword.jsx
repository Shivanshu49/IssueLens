import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api/v1";

export default function ForgotPassword() {
    const [email, setEmail] = useState("");
    const [status, setStatus] = useState("idle"); // idle, loading, success, error
    const [message, setMessage] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        setStatus("loading");
        setMessage("");

        try {
            await axios.post(`${API_BASE}/auth/forgot-password`, {
                email: email,
            });
            setStatus("success");
            setMessage("If an account exists for " + email + ", we have sent a reset link.");
        } catch (err) {
            console.error(err);
            setStatus("error");
            setMessage("Something went wrong. Please try again.");
        }
    };

    return (
        <div className="flex items-center justify-center min-h-[80vh]">
            <div className="w-full max-w-md p-8 bg-white dark:bg-slate-800 border border-gray-100 dark:border-slate-700 rounded-lg shadow-sm">
                <h2 className="text-2xl font-bold text-center text-[#0d3141] dark:text-white">Reset Password</h2>
                <p className="mt-2 text-center text-gray-600 dark:text-gray-300">
                    Enter your email to receive a reset link.
                </p>

                {status === "success" && (
                    <div className="mt-4 p-3 text-sm text-green-700 bg-green-50 rounded-md">
                        {message}
                    </div>
                )}

                {status === "error" && (
                    <div className="mt-4 p-3 text-sm text-red-700 bg-red-50 rounded-md">
                        {message}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="mt-6 space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-200">Email Address</label>
                        <input
                            type="email"
                            required
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-slate-600 rounded-md shadow-sm focus:outline-none focus:ring-[#0d3141] focus:border-[#0d3141] dark:bg-slate-700 dark:text-white"
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={status === "loading" || status === "success"}
                        className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#0d3141] hover:bg-[#1a4b61] focus:outline-none disabled:opacity-50"
                    >
                        {status === "loading" ? "Sending..." : "Send Reset Link"}
                    </button>
                </form>

                <p className="mt-4 text-center text-sm text-gray-600 dark:text-gray-400">
                    Remembered it?{" "}
                    <Link to="/login" className="font-medium text-[#0d3141] hover:underline dark:text-blue-400">
                        Back to Login
                    </Link>
                </p>
            </div>
        </div>
    );
}
