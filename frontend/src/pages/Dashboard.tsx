import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getSummary,
  getSeverity,
} from "../services/dashboardService";

export default function Dashboard() {
  const navigate = useNavigate();

  const [summary, setSummary] = useState<any>(null);
  const [severity, setSeverity] = useState<any>(null);

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const summaryData = await getSummary();
      const severityData = await getSeverity();

      setSummary(summaryData);
      setSeverity(severityData);
    } catch (error) {
      console.error(error);
    }
  };

  if (!summary || !severity) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-100 p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold">
          OpsPilot Dashboard
        </h1>

        <div className="flex gap-3">
          <button
            onClick={() => navigate("/incidents")}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg"
          >
            Incidents
          </button>

          <button
            onClick={() => {
              localStorage.removeItem("token");
              navigate("/");
            }}
            className="bg-red-600 text-white px-4 py-2 rounded-lg"
          >
            Logout
          </button>
        </div>
      </div>

      <div className="grid grid-cols-4 gap-4 mb-8">
        <Card title="Total" value={summary.total} />
        <Card title="Open" value={summary.open} />
        <Card title="In Progress" value={summary.in_progress} />
        <Card title="Resolved" value={summary.resolved} />
      </div>

      <div className="grid grid-cols-4 gap-4">
        <Card title="Critical" value={severity.critical} />
        <Card title="High" value={severity.high} />
        <Card title="Medium" value={severity.medium} />
        <Card title="Low" value={severity.low} />
      </div>
    </div>
  );
}

function Card({
  title,
  value,
}: {
  title: string;
  value: number;
}) {
  return (
    <div className="bg-white rounded-xl shadow p-6">
      <h2 className="text-gray-500">{title}</h2>
      <p className="text-4xl font-bold mt-2">{value}</p>
    </div>
  );
}