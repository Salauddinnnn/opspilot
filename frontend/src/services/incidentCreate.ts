import api from "../api/client";

export const createIncident = async (data: {
  title: string;
  description: string;
  severity: string;
}) => {
  const token = localStorage.getItem("token");

  const response = await api.post(
    "/incidents",
    data,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
};