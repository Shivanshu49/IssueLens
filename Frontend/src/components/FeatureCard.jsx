import React from "react";

export default function FeatureCard({ title, children, icon }) {
  return (
    <div className="bg-[#f7fbff] border border-gray-200 rounded-xl p-6 shadow-sm">
      <div className="flex items-start gap-4">
        <div className="flex-shrink-0 w-10 h-10 rounded-md bg-[#0d3141] text-[#f7fbff] flex items-center justify-center">
          {icon ?? (
            <svg
              className="w-5 h-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
            >
              <path
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M3 12h18M12 3v18"
              />
            </svg>
          )}
        </div>
        <div>
          <h3 className="text-base font-semibold text-[#0d3141]">{title}</h3>
          <p className="mt-2 text-sm text-gray-600">{children}</p>
        </div>
      </div>
    </div>
  );
}
