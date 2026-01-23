import React from "react";
import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Features from "./pages/Features";
import About from "./pages/About";
import Dashboard from "./pages/Dashboard";
import Navbar from "./Components/Navbar";
import Footer from "./Components/footer";

export default function App() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f7fbff] text-[#0d3141]">
      <Navbar />
      <main className="flex-grow">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/features" element={<Features />} />
          <Route path="/about" element={<About />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
}
