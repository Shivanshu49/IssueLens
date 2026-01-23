import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="bg-[#0d3141] text-[#f7fbff]">
      <div className="max-w-7xl mx-auto px-6 py-12">
        <div className="flex flex-col md:flex-row justify-between gap-10">
          {/* Brand */}
          <div className="max-w-md">
            <Link to="/" className="inline-flex items-center gap-2">
              <span className="text-2xl font-extrabold">Issue</span>
              <span className="text-2xl font-extrabold text-[#d5002c]">
                Lens
              </span>
            </Link>
            <p className="mt-3 text-sm text-gray-300">
              Real-time AI platform that monitors open-source GitHub
              repositories and explains what changed, what broke, and what got
              fixed.
            </p>
          </div>

          {/* Links */}
          <div className="flex gap-12">
            <div>
              <h4 className="text-sm font-semibold text-[#f7fbff] mb-3">
                Product
              </h4>
              <ul className="space-y-2 text-sm text-gray-300">
                <li>
                  <Link to="/dashboard" className="hover:text-white transition">
                    Dashboard
                  </Link>
                </li>
                <li>
                  <Link to="/features" className="hover:text-white transition">
                    Features
                  </Link>
                </li>
                <li>
                  <Link to="/about" className="hover:text-white transition">
                    About
                  </Link>
                </li>
              </ul>
            </div>

            <div>
              <h4 className="text-sm font-semibold text-[#f7fbff] mb-3">
                Resources
              </h4>
              <ul className="space-y-2 text-sm text-gray-300">
                <li>
                  <a
                    href="https://github.com/Shivanshu49/IssueLens"
                    className="hover:text-white transition"
                    target="_blank"
                    rel="noreferrer"
                  >
                    GitHub
                  </a>
                </li>
                <li>
                  <Link to="/docs" className="hover:text-white transition">
                    Docs
                  </Link>
                </li>
                <li>
                  <Link to="/api" className="hover:text-white transition">
                    API
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div className="mt-10 pt-6 border-t border-gray-700 flex flex-col md:flex-row items-center justify-between gap-4">
          <p className="text-sm text-gray-300">
            © {new Date().getFullYear()} IssueLens. All rights reserved.
          </p>
          <p className="text-sm text-gray-400">
            Built with React, FastAPI & Pathway
          </p>
        </div>
      </div>
    </footer>
  );
}
