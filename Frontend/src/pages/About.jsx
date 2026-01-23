import React from "react";
import SectionHeading from "../components/SectionHeading";

export default function About() {
  return (
    <div className="min-h-screen">
      <div className="max-w-4xl mx-auto px-6 py-16">
        <SectionHeading
          title="About IssueLens"
          subtitle="Why we built it, and who it's for."
        />

        <div className="mt-8 space-y-6 text-gray-700">
          <p>
            IssueLens was created to reduce the cognitive overhead of
            maintaining active open-source repositories. Instead of scanning
            issues, PRs, and commit diffs manually, maintainers get a
            continuous, AI-powered view of bug resolution and code changes.
          </p>

          <p>
            Our mission is to make bug resolution visible and explainable — so
            maintainers can prioritize, reviewers can focus, and contributors
            can ship with confidence.
          </p>

          <div className="mt-6 bg-[#f7fbff] border border-gray-200 rounded-lg p-6">
            <h4 className="text-sm font-semibold text-[#0d3141]">
              Who it's for
            </h4>
            <ul className="mt-3 list-disc list-inside text-gray-600">
              <li>Open-source maintainers</li>
              <li>Reviewers and triage teams</li>
              <li>Contributors seeking faster feedback</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
