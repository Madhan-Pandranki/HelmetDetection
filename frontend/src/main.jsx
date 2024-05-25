import React, { useState } from "react";
import { Outlet, RouterProvider, createBrowserRouter } from "react-router-dom";
import ReactDOM from "react-dom/client";
import App from "./components/App";
import About from "./components/About";
import Contact from "./components/Contact";
import "./index.css";
import Header from "./components/Header";
// import OutputDisplay from "./components/OutputDisplay";
// import UploadViewer from "./components/UploadViewer";

const Applayout = () => {
  // const [filePreview, setFilePreview] = useState(null);
  // const [fileType, setFileType] = useState("");

  // const handleUpload = (preview, type) => {
  //   setFilePreview(preview);
  //   setFileType(type);
  // };

  return (
    <div>
      <Header></Header>
      {/* <h1 className="text-2xl font-bold text-center my-8">
        Upload and Preview Image/Video
      </h1>
      <UploadViewer onUpload={handleUpload} />
      <h1 className="text-2xl font-bold text-center my-8">
        Display Output Image/Video
      </h1>
      <OutputDisplay preview={filePreview} fileType={fileType} /> */}
      <Outlet />
    </div>
  );
};
const appRouter = createBrowserRouter([
  {
    path: "/",
    element: <Applayout />,
    children: [
      {
        path: "/",
        element: <App />,
      },
      {
        path: "/about",
        element: <About />,
      },
      {
        path: "/contact",
        element: <Contact />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={appRouter} />
  </React.StrictMode>
);
