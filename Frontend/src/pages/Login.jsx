import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { Link, useNavigate, useLocation } from "react-router-dom";
import axios from "axios";
import { useAuth } from "../context/AuthContext";

// API URL from env or default
const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api/v1";

export default function Login() {
    const { register, handleSubmit, formState: { errors } } = useForm();
    const [serverError, setServerError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    const location = useLocation();
    const { login } = useAuth();
    const message = location.state?.message;

    const onSubmit = async (data) => {
        setLoading(true);
        setServerError("");
        try {
            const res = await axios.post(`${API_BASE}/auth/login`, {
                email: data.email,
                password: data.password,
            });
            // Store token via context
            login(res.data.access_token);
            navigate("/dashboard");
        } catch (err) {
            setServerError(err.response?.data?.detail || "Login failed. Please check credentials.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex items-center justify-center min-h-[80vh]">
            <div className="w-full max-w-md p-8 bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-lg shadow-sm">
                <h2 className="text-2xl font-bold text-center text-[#0d3141] dark:text-white">Welcome Back</h2>
                <p className="mt-2 text-center text-gray-600 dark:text-gray-300">Log in to IssueLens</p>

                {message && (
                    <div className="mt-4 p-3 text-sm text-green-700 bg-green-50 rounded-md">
                        {message}
                    </div>
                )}

                {serverError && (
                    <div className="mt-4 p-3 text-sm text-red-700 bg-red-50 rounded-md">
                        {serverError}
                    </div>
                )}

                <form onSubmit={handleSubmit(onSubmit)} className="mt-6 space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">Email</label>
                        <input
                            type="email"
                            {...register("email", { required: "Email is required" })}
                            className="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-[#0d3141] focus:border-[#0d3141]"
                        />
                        {errors.email && <p className="mt-1 text-xs text-red-600">{errors.email.message}</p>}
                    </div>

                    <div>
                        <div className="flex justify-between items-center">
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">Password</label>
                            <Link to="/forgot-password" className="text-sm text-[#0d3141] dark:text-[#5ba3c0] hover:underline">
                                Forgot Password?
                            </Link>
                        </div>
                        <input
                            type="password"
                            {...register("password", { required: "Password is required" })}
                            className="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-[#0d3141] focus:border-[#0d3141]"
                        />
                        {errors.password && <p className="mt-1 text-xs text-red-600">{errors.password.message}</p>}
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#0d3141] hover:bg-[#1a4b61] focus:outline-none disabled:opacity-50"
                    >
                        {loading ? "Logging in..." : "Log In"}
                    </button>
                </form>

                <p className="mt-4 text-center text-sm text-gray-600 dark:text-gray-400">
                    Don't have an account?{" "}
                    <Link to="/signup" className="font-medium text-[#0d3141] dark:text-[#5ba3c0] hover:underline">
                        Sign up
                    </Link>
                </p>
            </div>
        </div>
    );
}
