import React, { createContext, useContext, useEffect, useState } from "react";

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
    const [theme, setTheme] = useState(() => {
        // Check local storage first, default to light mode
        const stored = localStorage.getItem("theme");
        if (stored) {
            return stored;
        }
        return "light"; // Default to light mode
    });

    useEffect(() => {
        const root = window.document.documentElement;
        // Remove both classes first
        root.classList.remove("light", "dark");
        // Add current theme class
        root.classList.add(theme);
        // Save to localStorage
        localStorage.setItem("theme", theme);
    }, [theme]);

    const toggleTheme = () => {
        setTheme((prev) => {
            const newTheme = prev === "dark" ? "light" : "dark";
            return newTheme;
        });
    };

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

export function useTheme() {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error("useTheme must be used within a ThemeProvider");
    }
    return context;
}
