import { BrowserRouter, Routes, Route } from "react-router-dom";
import Register from "./pages/Register";

function App() {
  return (
   
      <Routes>
        <Route path="/" element={<h1>Welcome to Canada Tourism</h1>} />
        <Route path="/register" element={<Register />} />
      </Routes>
   
  );
}

export default App;
