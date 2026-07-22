import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { createIncident } from "../services/incidentCreate";

export default function CreateIncident() {
  const navigate = useNavigate();

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [severity, setSeverity] = useState("medium");

  const handleSubmit = async (
    e: React.FormEvent<HTMLFormElement>
  ) => {
    e.preventDefault();

    try {
      await createIncident({
        title,
        description,
        severity,
      });

      navigate("/incidents");
    } catch (error) {
      console.error(error);
      alert("Failed to create incident");
    }
  };

  return (
    <div className="min-h-screen bg-slate-100 flex justify-center items-center">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 rounded-xl shadow w-[500px]"
      >
        <h1 className="text-3xl font-bold mb-6">
          Create Incident
        </h1>

        <input
          className="border p-3 rounded-lg w-full mb-4"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <textarea
          className="border p-3 rounded-lg w-full mb-4"
          rows={5}
          placeholder="Description"
          value={description}
          onChange={(e) =>
            setDescription(e.target.value)
          }
        />

        <select
          className="border p-3 rounded-lg w-full mb-6"
          value={severity}
          onChange={(e) =>
            setSeverity(e.target.value)
          }
        >
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
          <option value="critical">Critical</option>
        </select>

        <button
          type="submit"
          className="bg-blue-600 text-white px-5 py-3 rounded-lg w-full"
        >
          Create Incident
        </button>
      </form>
    </div>
  );
}