import api from "../api/client";

export const getIncidents = async () => {
  const token = localStorage.getItem("token");

  const response = await api.get("/incidents", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};