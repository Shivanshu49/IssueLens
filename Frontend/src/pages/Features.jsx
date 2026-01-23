import React from "react";
import SectionHeading from "../components/SectionHeading";
import FeatureCard from "../components/FeatureCard";

export default function Features() {
  return (
    <div className="min-h-screen">
      <div className="max-w-6xl mx-auto px-6 py-16">
        <SectionHeading
          title="Features"
          subtitle="Everything IssueLens gives you to keep your repository healthy."
        />

        <div className="mt-8 grid md:grid-cols-2 gap-6">
          <FeatureCard title="Real-time GitHub monitoring">
            Capture issues, PRs and commits as events and stream to Pathway.
          </FeatureCard>
          <FeatureCard title="Diff analysis & explanations">
            AI analyzes diffs and returns human-friendly explanations that map
            to issues.
          </FeatureCard>
          <FeatureCard title="Bug lifecycle tracking">
            Auto-detect bug status changes and compute bug health score across
            time.
          </FeatureCard>
          <FeatureCard title="Alerts & regressions">
            Notify maintainers about possible regressions and risky changes.
          </FeatureCard>
        </div>
      </div>
    </div>
  );
}
