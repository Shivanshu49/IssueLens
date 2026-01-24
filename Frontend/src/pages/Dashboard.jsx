import React, { useState, useEffect } from "react";
import StatCard from "../components/StatCard";
import FeatureCard from "../components/FeatureCard";

// API base URL - configurable via environment variable
const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api/v1";

export default function Dashboard() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch activity feed
  useEffect(() => {
    const fetchActivity = async () => {
      try {
        setLoading(true);
        const res = await fetch(`${API_BASE}/activity`);
        if (!res.ok) throw new Error("Failed to fetch activity");
        const data = await res.json();
        setActivities(data.slice(0, 5)); // Last 5 events
        setError(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchActivity();
    // Refresh every 30 seconds
    const interval = setInterval(fetchActivity, 30000);
    return () => clearInterval(interval);
  }, []);

  // demo data -- replace with API calls later
  const stats = [
    { label: "Bugs fixed (30d)", value: "128", delta: "+12%" },
    { label: "Open bugs", value: "42", delta: "-3%" },
    { label: "Potential regressions", value: "3", delta: "+1" },
  ];

  const getStatusBadge = (status) => {
    const styles = {
      fixed: "bg-green-100 text-green-800",
      completed: "bg-green-100 text-green-800",
      open: "bg-yellow-100 text-yellow-800",
      pending: "bg-blue-100 text-blue-800",
      error: "bg-red-100 text-red-800",
    };
    return styles[status] || "bg-gray-100 text-gray-800";
  };

  const getTypeIcon = (type) => {
    const icons = {
      push: "🔄",
      issue: "🐛",
      pull_request: "📥",
      commit: "📝",
    };
    return icons[type] || "📌";
  };

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
              Live Activity Feed
            </h3>
            
            {loading && (
              <div className="mt-4 flex items-center justify-center py-8">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[#0d3141]"></div>
                <span className="ml-3 text-gray-600">Loading activity...</span>
              </div>
            )}

            {error && (
              <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-md">
                <p className="text-sm text-red-600">Error: {error}</p>
              </div>
            )}

            {!loading && !error && activities.length === 0 && (
              <div className="mt-4 p-8 text-center">
                <p className="text-gray-500">No recent activity</p>
              </div>
            )}

            {!loading && !error && activities.length > 0 && (
              <ul className="mt-4 space-y-4">
                {activities.map((activity, idx) => (
                  <li
                    key={idx}
                    className="p-4 border border-gray-100 rounded-md bg-white hover:shadow-sm transition-shadow"
                  >
                    <div className="flex items-start justify-between gap-4">
                      <div className="flex items-start gap-3">
                        <span className="text-xl">{getTypeIcon(activity.type)}</span>
                        <div>
                          <h4 className="text-sm font-semibold text-[#0d3141]">
                            {activity.message}
                          </h4>
                          <p className="mt-1 text-xs text-gray-500">
                            {activity.repo} • {activity.type}
                          </p>
                        </div>
                      </div>
                      <span
                        className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusBadge(activity.status)}`}
                      >
                        {activity.status}
                      </span>
                    </div>
                  </li>
                ))}
              </ul>
            )}
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
