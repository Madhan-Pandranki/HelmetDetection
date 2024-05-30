// // // src/FileUploadPreview.js
// // import React, { useState, useRef } from 'react';

// // const UploadViewer = ({ onUpload }) => {
// //   const [preview, setPreview] = useState(null);
// //   const [fileType, setFileType] = useState('');
// //   const [errorMessage, setErrorMessage] = useState('');
// //   const fileInputRef = useRef(null);

// //   const handleFileChange = (e) => {
// //     const file = e.target.files[0];
// //     if (file) {
// //       const fileType = file.type.split('/')[0];
// //       setFileType(fileType);

// //       const url = URL.createObjectURL(file);
// //       setPreview(url);
// //       setErrorMessage('');
// //       onUpload(url, fileType);
// //     }
// //   };

// //   const handleVideoError = () => {
// //     setErrorMessage('Failed to load video. The file format might not be supported.');
// //   };

// //   const handleReset = () => {
// //     setPreview(null);
// //     setFileType('');
// //     setErrorMessage('');
// //     fileInputRef.current.value = null; // Reset file input
// //     onUpload(null, null); // Reset display component
// //   };

// //   const triggerFileInput = () => {
// //     fileInputRef.current.click();
// //   };

// //   return (
// //     <div className="max-w-md mx-auto my-4 p-4 border rounded-lg shadow-lg">
// //       <input 
// //         type="file" 
// //         ref={fileInputRef} 
// //         onChange={handleFileChange} 
// //         accept="image/*,video/*" 
// //         className="hidden"
// //       />
// //       <button 
// //         onClick={triggerFileInput} 
// //         className="mt-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-700 focus:outline-none"
// //       >
// //         Choose File
// //       </button>
// //       <button 
// //         onClick={handleReset} 
// //         className="mt-2 ml-2 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700 focus:outline-none"
// //       >
// //         Reset
// //       </button>
// //       {errorMessage && <p className="mt-2 text-red-500">{errorMessage}</p>}
// //       {preview && (
// //         <div className="mt-4">
// //           {fileType === 'image' ? (
// //             <img src={preview} alt="Preview" className="w-full h-auto rounded-lg" />
// //           ) : (
// //             <video
// //               controls
// //               className="w-full h-auto rounded-lg"
// //               onError={handleVideoError}
// //             >
// //               <source src={preview} type="video/mp4" />
// //               <source src={preview} type="video/webm" />
// //               <source src={preview} type="video/ogg" />
// //               Your browser does not support the video tag.
// //             </video>
// //           )}
// //         </div>
// //       )}
// //     </div>
// //   );
// // };

// // export default UploadViewer;




// import React, { useState } from 'react';
// import axios from 'axios';

// const FileUpload = () => {
//     const [file, setFile] = useState(null);
//     const [message, setMessage] = useState('');
//     const [output, setOutput] = useState('');

//     const handleFileChange = (event) => {
//         setFile(event.target.files[0]);
//     };

//     const handleSubmit = async (event) => {
//         event.preventDefault();
//         const formData = new FormData();
//         formData.append('file', file);

//         try {
//             const response = await axios.post('http://localhost:8000/upload_file/', formData, {
//                 headers: {
//                     'Content-Type': 'multipart/form-data',
//                 },
//             });
//             setMessage(response.data.message);
//             setOutput(response.data.output);
//         } catch (error) {
//             setMessage('Error uploading file');
//             console.error(error);
//         }
//     };

//     return (
//         <div>
//             <form onSubmit={handleSubmit}>
//                 <input type="file" onChange={handleFileChange} accept="image/*,video/*" />
//                 <button type="submit">Upload</button>
//             </form>
//             {message && <p>{message}</p>}
//             {output && <pre>{output}</pre>}
//         </div>
//     );
// };

// export default FileUpload;

import React, { useState } from 'react';
import axios from 'axios';
import cv2 from 'opencv.js';
// import { useNavigate } from 'react-router-dom';

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState('');
    // const navigate = useNavigate();

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:8000/upload_file/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log(response.data);
            // image_path=response.data
            // <img src={response.data}/>
            const src = cv2.imread(response.data);
            cv2.imshow(src);
            const keyPressHandler = (event) => {
              if (event.key === 'q') {
                  cv2.destroyAllWindows();
                  document.removeEventListener('keypress', keyPressHandler);
              }
            };
            document.addEventListener('keypress', keyPressHandler);
            // const { outputFilePath } = response.data;
            // navigate('/output', { state: { outputFilePath } });
        } catch (error) {
            setMessage('Error uploading file');
            console.error(error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} accept="image/*,video/*" />
                <button type="submit">Upload</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default FileUpload;
