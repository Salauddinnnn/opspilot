import api from "../api/client";

export const getIncident = async (id: number) => {
  const token = localStorage.getItem("token");

  const response = await api.get(`/incidents/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};