import api from "../api/client";

export const updateStatus = async (
  id: number,
  status: string
) => {
  const token = localStorage.getItem("token");

  const response = await api.patch(
    `/incidents/${id}/status`,
    {
      status,
    },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
};