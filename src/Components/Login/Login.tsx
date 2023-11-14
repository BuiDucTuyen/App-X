import React from "react";
import { FaTwitter } from "react-icons/fa";
import axios from "axios";

const LoginPage: React.FC = () => {
  const handleTwitterLogin = async () => {
    try {
      const response = await axios.get("http://localhost:5000/twitter_login");

      window.location.href = response.data.twitterAuthUrl;
    } catch (error) {
      console.error("Lỗi đăng nhập Twitter:", error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="bg-white p-8 rounded shadow-md">
        <h1 className="text-2xl font-bold mb-4">Đăng nhập</h1>
        <button
          onClick={handleTwitterLogin}
          className="bg-blue-500 text-white py-2 px-4 rounded flex items-center"
        >
          <FaTwitter className="mr-2" />
          Đăng nhập bằng Twitter
        </button>
        
      </div>
    </div>
  );
};

export default LoginPage;
