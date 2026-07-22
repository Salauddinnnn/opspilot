import api from "../api/client";

export interface LoginRequest {
  email: string;
  password: string;
}

export const login = async (data: LoginRequest) => {
  const response = await api.post("/auth/login", data);
  return response.data;
};