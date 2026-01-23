import React from "react";

export default function StatCard({ label, value, delta }) {
  return (
    <div className="bg-[#f7fbff] border border-gray-200 rounded-lg p-4">
      <p className="text-sm text-gray-600">{label}</p>
      <div className="mt-2 flex items-baseline gap-3">
        <span className="text-2xl font-extrabold text-[#0d3141]">{value}</span>
        {delta && (
          <span
            className={`text-sm font-medium ${String(delta).startsWith("-") ? "text-red-600" : "text-green-600"}`}
          >
            {delta}
          </span>
        )}
      </div>
    </div>
  );
}
