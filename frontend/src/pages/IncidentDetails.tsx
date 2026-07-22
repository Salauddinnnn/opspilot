import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { getIncident } from "../services/incidentDetails";
import { updateStatus } from "../services/updateStatus";
import {
  getComments,
  addComment,
} from "../services/commentService";
import { getAuditLogs } from "../services/auditService";

export default function IncidentDetails() {
  const navigate = useNavigate();
  const { id } = useParams();

  const [incident, setIncident] = useState<any>(null);
  const [status, setStatus] = useState("");

  const [comments, setComments] = useState<any[]>([]);
  const [comment, setComment] = useState("");

  const [auditLogs, setAuditLogs] = useState<any[]>([]);

  useEffect(() => {
    loadIncident();
    loadComments();
    loadAuditLogs();
  }, []);

  const loadIncident = async () => {
    try {
      const data = await getIncident(Number(id));
      setIncident(data);
      setStatus(data.status);
    } catch (error) {
      console.error(error);
    }
  };

  const loadComments = async () => {
    try {
      const data = await getComments(Number(id));
      setComments(data);
    } catch (error) {
      console.error(error);
    }
  };

  const loadAuditLogs = async () => {
    try {
      const data = await getAuditLogs(Number(id));
      setAuditLogs(data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleUpdateStatus = async () => {
    try {
      await updateStatus(Number(id), status);

      await loadIncident();
      await loadAuditLogs();

      alert("Status Updated Successfully");
    } catch (error) {
      console.error(error);
      alert("Failed to update status");
    }
  };

  const handleAddComment = async () => {
    if (!comment.trim()) return;

    try {
      await addComment(Number(id), comment);

      setComment("");

      await loadComments();
      await loadAuditLogs();

      alert("Comment Added Successfully");
    } catch (error) {
      console.error(error);
      alert("Failed to add comment");
    }
  };

  if (!incident) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Loading...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-100 p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold">
          Incident #{incident.id}
        </h1>

        <button
          onClick={() => navigate("/incidents")}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg"
        >
          Back
        </button>
      </div>

      {/* Incident Details */}
      <div className="bg-white rounded-xl shadow p-6 space-y-4">
        <div>
          <strong>Title:</strong> {incident.title}
        </div>

        <div>
          <strong>Description:</strong>
          <br />
          {incident.description}
        </div>

        <div>
          <strong>Severity:</strong> {incident.severity}
        </div>

        <div>
          <strong>Status:</strong> {incident.status}
        </div>

        <div>
          <strong>Created By:</strong> {incident.created_by}
        </div>

        <div>
          <strong>Assigned To:</strong>{" "}
          {incident.assigned_to ?? "Not Assigned"}
        </div>
      </div>

      {/* Status */}
      <div className="bg-white rounded-xl shadow p-6 mt-6">
        <h2 className="text-2xl font-bold mb-4">
          Update Status
        </h2>

        <div className="flex gap-4 items-center">
          <select
            value={status}
            onChange={(e) => setStatus(e.target.value)}
            className="border rounded-lg p-3"
          >
            <option value="open">Open</option>
            <option value="in_progress">In Progress</option>
            <option value="resolved">Resolved</option>
          </select>

          <button
            onClick={handleUpdateStatus}
            className="bg-green-600 text-white px-5 py-3 rounded-lg"
          >
            Save Status
          </button>
        </div>
      </div>

      {/* Comments */}
      <div className="bg-white rounded-xl shadow p-6 mt-6">
        <h2 className="text-2xl font-bold mb-4">
          Comments
        </h2>

        <div className="flex gap-3 mb-6">
          <input
            type="text"
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            placeholder="Write a comment..."
            className="border rounded-lg p-3 flex-1"
          />

          <button
            onClick={handleAddComment}
            className="bg-blue-600 text-white px-5 rounded-lg"
          >
            Add
          </button>
        </div>

        {comments.length === 0 ? (
          <p className="text-gray-500">
            No comments yet.
          </p>
        ) : (
          <div className="space-y-3">
            {comments.map((c) => (
              <div
                key={c.id}
                className="border rounded-lg p-4"
              >
                <p>{c.content}</p>

                <div className="text-sm text-gray-500 mt-2">
                  User #{c.user_id}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Audit Logs */}
      <div className="bg-white rounded-xl shadow p-6 mt-6">
        <h2 className="text-2xl font-bold mb-4">
          Audit Logs
        </h2>

        {auditLogs.length === 0 ? (
          <p className="text-gray-500">
            No audit logs available.
          </p>
        ) : (
          <div className="space-y-3">
            {auditLogs.map((log) => (
              <div
                key={log.id}
                className="border rounded-lg p-4"
              >
                <div className="font-semibold">
                  {log.action}
                </div>

                <div className="text-gray-600">
                  {log.description}
                </div>

                <div className="text-sm text-gray-500 mt-2">
                  User #{log.user_id}
                </div>

                <div className="text-xs text-gray-400">
                  {new Date(log.created_at).toLocaleString()}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}