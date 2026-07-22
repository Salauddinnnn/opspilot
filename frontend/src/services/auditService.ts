import api from "../api/client";

const token = () => ({
  headers: {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  },
});

export const getAuditLogs = async (
  incidentId: number
) => {
  const response = await api.get(
    `/incidents/${incidentId}/audit-logs`,
    token()
  );

  return response.data;
};