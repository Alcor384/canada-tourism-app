import { useState } from "react";
import api from "../api/axios";

export default function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {
    try {
      const res = await api.post("/auth/register", { username, password });
      alert("Successfully registered: " + res.data.username);
    } catch (err) {
      alert("Fail to register: " + err.response.data.detail);
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <input 
        placeholder="User Name"
        value={username}
        onChange={(e) => setUsername(e.target.value)} 
      />
      <input 
        type="password"
        placeholder="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)} 
      />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}
