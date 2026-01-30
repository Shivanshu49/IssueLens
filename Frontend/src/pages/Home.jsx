import React from "react";
import { Link } from "react-router-dom";
import SectionHeading from "../components/SectionHeading";
import FeatureCard from "../components/FeatureCard";
import Button from "../components/Button";

export default function Home() {
  return (
    <div className="min-h-screen">
      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div>
            <h1 className="text-4xl md:text-5xl font-extrabold leading-tight text-[#0d3141]">
              See what changed.{" "}
              <span className="text-[#d5002c]">Know what broke.</span>
              <br /> Understand what got fixed.
            </h1>
            <p className="mt-6 text-gray-700 max-w-xl">
              IssueLens monitors your open-source GitHub repositories in real
              time and uses AI to explain code changes, track bug resolution,
              and surface risky regressions.
            </p>

            <div className="mt-8 flex items-center gap-4">
              <Button to="/dashboard">View Dashboard</Button>
              <a
                href="https://github.com"
                target="_blank"
                rel="noreferrer"
                className="text-sm text-[#0d3141] hover:underline"
              >
                View on GitHub
              </a>
            </div>
          </div>

          <div>
            <div className="grid grid-cols-1 gap-4">
              <div className="bg-[#0d3141] text-[#f7fbff] rounded-xl p-6">
                <p className="text-sm font-medium">Live</p>
                <p className="mt-2 text-xl font-bold">
                  Real-time GitHub event ingestion
                </p>
                <p className="mt-3 text-sm text-gray-100">
                  Webhooks → Pathway → Explanations
                </p>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="bg-[#f7fbff] border border-gray-200 rounded-lg p-4">
                  <p className="text-sm text-gray-600">Bugs fixed (30d)</p>
                  <p className="mt-2 text-2xl font-extrabold text-[#0d3141]">
                    128
                  </p>
                </div>
                <div className="bg-[#f7fbff] border border-gray-200 rounded-lg p-4">
                  <p className="text-sm text-gray-600">Potential regressions</p>
                  <p className="mt-2 text-2xl font-extrabold text-[#0d3141]">
                    3
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="mt-16">
          <SectionHeading
            title="Core Features"
            subtitle="Build clarity into your repo workflow with real-time AI explanations."
          />
          <div className="mt-8 grid md:grid-cols-3 gap-6">
            <FeatureCard title="Real-time monitoring">
              Ingest GitHub webhooks and process commits & PRs as they arrive.
            </FeatureCard>
            <FeatureCard title="AI explanations">
              LLM-powered explanations of diffs — human readable and concise.
            </FeatureCard>
            <FeatureCard title="Bug health metrics">
              Track bugs fixed vs unresolved with trend insights.
            </FeatureCard>
          </div>
          <div className="mt-6">
            <Link
              to="/features"
              className="text-sm text-[#0d3141] hover:underline"
            >
              See all features →
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
