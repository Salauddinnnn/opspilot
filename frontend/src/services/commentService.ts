import api from "../api/client";

const token = () => ({
  headers: {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  },
});

export const getComments = async (incidentId: number) => {
  const response = await api.get(
    `/incidents/${incidentId}/comments`,
    token()
  );

  return response.data;
};

export const addComment = async (
  incidentId: number,
  content: string
) => {
  const response = await api.post(
    `/incidents/${incidentId}/comments`,
    {
      content,
    },
    token()
  );

  return response.data;
};