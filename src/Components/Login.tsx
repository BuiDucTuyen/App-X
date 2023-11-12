import React, { useState } from "react";
import TwitterLogin from "react-twitter-login";
import { FaTwitter } from "react-icons/fa";

const LoginPage: React.FC = () => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [isLoggedin, setIsLoggedIn] = useState(false);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [user, setUser] = useState(null);

  const onSuccess = (response: React.SetStateAction<null>) => {
    console.log("Đăng nhập Twitter thành công:", response);
    setIsLoggedIn(true);
    setUser(response);
  };

  const onFailure = (error: any) => {
    console.error("Lỗi đăng nhập Twitter:", error);
  };

  return (
    <section className="container max-w-[1420px] flex justify-center items-center mt-[100px] p-2">
      <div className="flex flex-col gap-5 p-5 border-gradient-container rounded-3xl shadow-inner shadow-slate-900 border-gradient">
        <h1 className="text-[40px] font-bold">Đăng nhập</h1>
        <div className="border-gradient-container rounded-3xl">
          <TwitterLogin
            authCallback={onSuccess}
            consumerKey="Jb5fDNbifHkzUhAdyeBBhFvqB"
            consumerSecret="g8VHALBB74qTbPu173pflmAJhyi2ySwubVVDDRRfmmtjnAdNAd"
            onFailure={onFailure}
            showIcon={true}
            customHeaders={{
              "X-Custom-Header": "Giá trị tiêu đề tùy chỉnh của tôi",
            }}
            dialogWidth={600}
          >
            <button
              className="p-3 max-h lg:h-full w- font-bold bg-card rounded-2xl shadow-inner shadow-slate-900 border-gradient"
              style={{ display: "inline-flex", alignItems: "center" }}
            >
              <FaTwitter className="mr-2" />
              Đăng nhập bằng Twitter
            </button>
          </TwitterLogin>
        </div>
      </div>
    </section>
  );
};

export default LoginPage;
