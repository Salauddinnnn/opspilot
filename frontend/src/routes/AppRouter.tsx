import { BrowserRouter, Routes, Route } from "react-router-dom";

import IncidentDetails from "../pages/IncidentDetails";
import CreateIncident from "../pages/CreateIncident";
import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Incidents from "../pages/Incidents";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
      <Route
  path="/incidents/create"
  element={<CreateIncident />}
/>
<Route
  path="/incidents/:id"
  element={<IncidentDetails />}
/>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/incidents" element={<Incidents />} />
      </Routes>
    </BrowserRouter>
  );
}