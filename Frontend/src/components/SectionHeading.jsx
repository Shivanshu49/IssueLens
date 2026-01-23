import React from "react";

export default function SectionHeading({ title, subtitle }) {
  return (
    <div>
      <h2 className="text-2xl font-extrabold text-[#0d3141]">{title}</h2>
      {subtitle && (
        <p className="mt-2 text-sm text-gray-600 max-w-xl">{subtitle}</p>
      )}
    </div>
  );
}
