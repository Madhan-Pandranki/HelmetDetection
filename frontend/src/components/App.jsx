// import { useState } from 'react'
import { useState } from "react";
import "../App.css";
import FileUpload from "./UploadViewer";
import OutputPage from "./OutputDisplay";
// import VideoUploader from '../../VideoUploader'
// import Header from './Header'

function App() {
  // const [filePreview, setFilePreview] = useState(null);
  // const [fileType, setFileType] = useState("");

  // const handleUpload = (preview, type) => {
  //   setFilePreview(preview);
  //   setFileType(type);
  // };
  return (
    <>
      {/* <Header></Header> */}
      {/* <VideoUploader></VideoUploader> */}
      <h1 className="text-2xl font-bold text-center my-8">
        Upload and Preview Image/Video
      </h1>
      <FileUpload  />
      {/* <UploadViewer onUpload={handleUpload} /> */}
      <h1 className="text-2xl font-bold text-center my-8">
        Display Output Image/Video
      </h1>
      {/* <OutputDisplay preview={filePreview} fileType={fileType} /> */}
      {/* <OutputPage/> */}
    </>
  );
}

export default App;

// import React, { useState } from "react";
// import UploadViewer from "./UploadViewer"; // Assuming you have an UploadViewer component
// import OutputDisplay from "./OutputDisplay"; // Assuming you have an OutputDisplay component

// const About = () => {
//   const [filePreview, setFilePreview] = useState(null);
//   const [fileType, setFileType] = useState(null);

//   // Function to handle upload and set preview
//   const handleUpload = (file, type) => {
//     setFilePreview(file);
//     setFileType(type);
//   };

//   return (
//     <div className="max-w-4xl mx-auto py-8 px-4">
//       <div className="flex flex-wrap justify-center">
//         <div className="w-full md:w-1/2">
//           <h1 className="text-2xl font-bold text-center my-8">
//             Upload and Preview Image/Video
//           </h1>
//           <UploadViewer onUpload={handleUpload} />
//         </div>
//         {/* <div className="w-full md:w-1/2">
//           <h1 className="text-2xl font-bold text-center my-8">
//             Display Output Image/Video
//           </h1>
//           <OutputDisplay preview={filePreview} fileType={fileType} />
//         </div> */}
//       </div>
//       {/* Your existing About content goes here */}
//     </div>
//   );
// };

// export default About;


// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import FileUpload from './UploadViewer';
// import OutputPage from './OutputDisplay';

// function App() {
//     return (
//         <>
//             {/* <Routes> */}
//                 <Route path="/" element={<FileUpload />} />
//                 <Route path="/output" element={<OutputPage />} />
//             {/* </Routes> */}
//         </>
//     );
// }

// export default App;
