import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { getIncidents } from "../services/incidentService";

export default function Incidents() {
  const navigate = useNavigate();

  const [incidents, setIncidents] = useState<any[]>([]);

  useEffect(() => {
    loadIncidents();
  }, []);

  const loadIncidents = async () => {
    try {
      const data = await getIncidents();
      setIncidents(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100 p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold">
          Incidents
        </h1>

        <div className="flex gap-3">
          <button
            onClick={() => navigate("/incidents/create")}
            className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
          >
            + Create Incident
          </button>

          <button
            onClick={() => navigate("/dashboard")}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Dashboard
          </button>

          <button
            onClick={() => {
              localStorage.removeItem("token");
              navigate("/");
            }}
            className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700"
          >
            Logout
          </button>
        </div>
      </div>

      <table className="w-full bg-white rounded-xl shadow overflow-hidden">
        <thead className="bg-gray-200">
          <tr>
            <th className="p-3 text-left">ID</th>
            <th className="p-3 text-left">Title</th>
            <th className="p-3 text-left">Severity</th>
            <th className="p-3 text-left">Status</th>
          </tr>
        </thead>

        <tbody>
          {incidents.map((incident) => (
            <tr
            key={incident.id}
            onClick={() => navigate(`/incidents/${incident.id}`)}
            className="border-t hover:bg-gray-50 cursor-pointer"
          >
              
              <td className="p-3">{incident.id}</td>
              <td className="p-3">{incident.title}</td>
              <td className="p-3">
                {incident.severity}
              </td>
              <td className="p-3">
                {incident.status}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}