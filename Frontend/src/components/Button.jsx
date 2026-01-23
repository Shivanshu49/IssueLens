import React from "react";
import { Link } from "react-router-dom";

export default function Button({
  children,
  variant = "primary",
  to,
  ...props
}) {
  const base =
    "inline-flex items-center justify-center rounded-md px-4 py-2 text-sm font-semibold transition";
  const styles = {
    primary: `bg-[#d5002c] text-[#f7fbff] hover:bg-[#b30023]`,
    ghost: `bg-transparent text-[#0d3141] border border-gray-300 hover:bg-gray-50`,
  };

  if (to) {
    return (
      <Link to={to} className={`${base} ${styles[variant]}`} {...props}>
        {children}
      </Link>
    );
  }

  return (
    <button className={`${base} ${styles[variant]}`} {...props}>
      {children}
    </button>
  );
}
