import React from "react";
import StatCard from "../components/StatCard";
import FeatureCard from "../components/FeatureCard";

export default function Dashboard() {
  // demo data -- replace with API calls later
  const stats = [
    { label: "Bugs fixed (30d)", value: "128", delta: "+12%" },
    { label: "Open bugs", value: "42", delta: "-3%" },
    { label: "Potential regressions", value: "3", delta: "+1" },
  ];

  const recent = [
    {
      id: 1,
      title: "Fix state leak in Navbar",
      status: "fixed",
      summary: "Removed stale state causing re-renders.",
    },
    {
      id: 2,
      title: "Auth token expiration bug",
      status: "open",
      summary: "Tokens not refreshed on expiry.",
    },
  ];

  return (
    <div className="min-h-screen">
      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-extrabold text-[#0d3141]">Dashboard</h1>
          <div className="text-sm text-gray-600">Overview of repo health</div>
        </div>

        <div className="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-4">
          {stats.map((s) => (
            <StatCard
              key={s.label}
              label={s.label}
              value={s.value}
              delta={s.delta}
            />
          ))}
        </div>

        <div className="mt-8 grid md:grid-cols-3 gap-6">
          <div className="md:col-span-2 bg-[#f7fbff] border border-gray-200 rounded-lg p-6">
            <h3 className="text-lg font-semibold text-[#0d3141]">
              Recent activity
            </h3>
            <ul className="mt-4 space-y-4">
              {recent.map((r) => (
                <li
                  key={r.id}
                  className="p-4 border border-gray-100 rounded-md"
                >
                  <div className="flex items-start justify-between gap-4">
                    <div>
                      <h4 className="text-sm font-semibold text-[#0d3141]">
                        {r.title}
                      </h4>
                      <p className="mt-1 text-sm text-gray-600">{r.summary}</p>
                    </div>
                    <div>
                      <span
                        className={`px-3 py-1 rounded-full text-xs font-medium ${
                          r.status === "fixed"
                            ? "bg-green-100 text-green-800"
                            : "bg-yellow-100 text-yellow-800"
                        }`}
                      >
                        {r.status}
                      </span>
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          </div>

          <div className="bg-[#f7fbff] border border-gray-200 rounded-lg p-6">
            <h3 className="text-lg font-semibold text-[#0d3141]">
              Quick actions
            </h3>
            <div className="mt-4 space-y-3">
              <FeatureCard title="Run analysis now">
                Trigger an on-demand analysis of a recent PR or commit.
              </FeatureCard>
              <FeatureCard title="Create alert">
                Create a notification for risky changes or regressions.
              </FeatureCard>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
