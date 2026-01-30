import { useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { useTheme } from "../context/ThemeContext";
import { useAuth } from "../context/AuthContext";

function Navbar() {
  const [open, setOpen] = useState(false);
  const { theme, toggleTheme } = useTheme();
  const { isAuthenticated, logout } = useAuth();

  const navClass = ({ isActive }) =>
    `hover:text-white transition ${isActive ? "text-white" : "text-gray-200"}`;

  return (
    <header className="bg-[#0d3141] text-[#f7fbff] shadow-sm">
      <div className="max-w-7xl mx-auto px-6">
        <div className="h-20 flex items-center justify-between">
          {/* Brand */}
          <Link to="/" className="flex items-center">
            <span className="text-2xl font-extrabold leading-none">Issue</span><span className="text-2xl font-extrabold text-[#d5002c] leading-none">Lens</span>
          </Link>

          {/* Desktop nav */}
          <nav className="hidden md:flex items-center gap-8 text-sm font-medium">
            <NavLink to="/" className={navClass} end>
              Home
            </NavLink>
            <NavLink to="/dashboard" className={navClass}>
              Dashboard
            </NavLink>
            <NavLink to="/features" className={navClass}>
              Features
            </NavLink>
            <NavLink to="/about" className={navClass}>
              About
            </NavLink>
            {/* external - keep anchor for github */}
            <a
              href="https://github.com/Shivanshu49/IssueLens"
              className="text-gray-200 hover:text-white transition"
              target="_blank"
              rel="noreferrer"
            >
              GitHub
            </a>
          </nav>

          {/* CTA + Mobile button */}
          <div className="flex items-center gap-4">
            {/* Theme Toggle */}
            <button
              onClick={toggleTheme}
              className="p-2 rounded-full hover:bg-white/10 transition"
              aria-label="Toggle theme"
            >
              {theme === "dark" ? "☀️" : "🌙"}
            </button>

            {isAuthenticated ? (
              <button
                onClick={() => {
                  logout();
                  setOpen(false);
                }}
                className="hidden sm:inline-block px-4 py-2 rounded-md bg-gray-200 text-gray-800 text-sm font-semibold hover:bg-gray-300 transition"
              >
                Logout
              </button>
            ) : (
              <>
                <Link
                  to="/login"
                  className="hidden sm:inline-block px-4 py-2 text-sm font-semibold text-gray-200 hover:text-white transition"
                >
                  Log in
                </Link>
                <Link
                  to="/signup"
                  className="hidden sm:inline-block px-4 py-2 rounded-md bg-[#d5002c] text-[#f7fbff] text-sm font-semibold hover:bg-[#b30023] transition"
                >
                  Sign up
                </Link>
              </>
            )}

            {/* Mobile menu button */}
            <button
              onClick={() => setOpen(!open)}
              className="md:hidden p-2 rounded-md text-gray-200 hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#d5002c]"
              aria-label="Toggle menu"
            >
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                {open ? (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M6 18L18 6M6 6l12 12"
                  />
                ) : (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                )}
              </svg>
            </button>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      <div
        className={`md:hidden bg-[#0d3141] border-t border-gray-700 transition-max-height duration-300 overflow-hidden ${open ? "max-h-65" : "max-h-0"
          }`}
      >
        <div className="px-6 mb-6 pb-6 flex flex-col gap-3 text-gray-200">
          <NavLink
            to="/"
            className="py-2 hover:text-white"
            onClick={() => setOpen(false)}
            end
          >
            Home
          </NavLink>
          <NavLink
            to="/dashboard"
            className="py-2 hover:text-white"
            onClick={() => setOpen(false)}
          >
            Dashboard
          </NavLink>
          <NavLink
            to="/features"
            className="py-2 hover:text-white"
            onClick={() => setOpen(false)}
          >
            Features
          </NavLink>
          <NavLink
            to="/about"
            className="py-2 hover:text-white"
            onClick={() => setOpen(false)}
          >
            About
          </NavLink>
          <a
            href="https://github.com/Shivanshu49/IssueLens"
            className="mb-2 hover:text-white "
            target="_blank"
            rel="noreferrer"
          >
            GitHub
          </a>

          {isAuthenticated ? (
            <button
              onClick={() => {
                logout();
                setOpen(false);
              }}
              className="mt-2 text-left block py-2 hover:text-white w-full"
            >
              Logout
            </button>
          ) : (
            <>
              <Link
                to="/login"
                onClick={() => setOpen(false)}
                className="mt-2 text-left block py-2 hover:text-white"
              >
                Log in
              </Link>
              <Link
                to="/signup"
                onClick={() => setOpen(false)}
                className="mt-2 inline-block px-4 py-2 rounded-md bg-[#d5002c] text-[#f7fbff] text-sm font-semibold hover:bg-[#b30023] transition w-max"
              >
                Sign up
              </Link>
            </>
          )}
        </div>
      </div>
    </header>
  );
}

export default Navbar;
