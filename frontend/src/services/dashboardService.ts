import api from "../api/client";

export const getSummary = async () => {
  const token = localStorage.getItem("token");

  const response = await api.get("/dashboard/summary", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};

export const getSeverity = async () => {
  const token = localStorage.getItem("token");

  const response = await api.get("/dashboard/severity", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};