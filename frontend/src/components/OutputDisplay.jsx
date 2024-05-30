// // src/FileDisplay.js
// import React from 'react';

// const OutputDisplay = ({ preview, fileType }) => {
//   return (
//     <div className="max-w-md mx-auto my-4 p-4 border rounded-lg shadow-lg">
//       {preview ? (
//         fileType === 'image' ? (
//           <img src={preview} alt="Preview" className="w-full h-auto pt-16 rounded-lg" />
//         ) : (
//           <video controls className="w-full h-auto rounded-lg pt-16">
//             <source src={preview} type="video/mp4" />
//             <source src={preview} type="video/webm" />
//             <source src={preview} type="video/ogg" />
//             Your browser does not support the video tag.
//           </video>
//         )
//       ) : (
//         <p className="text-center text-gray-500 pt-6">No file uploaded</p>
//       )}
//     </div>
//   );
// };

// export default OutputDisplay;


import React from 'react';
import { useLocation } from 'react-router-dom';

const OutputPage = () => {
    const location = useLocation();
    const { outputFilePath } = location.state;

    return (
        <div>
            <h2>Output File</h2>
            <a href={`http://localhost:8000${outputFilePath}`} download>
                Download Output File
            </a>
        </div>
    );
};

export default OutputPage;
