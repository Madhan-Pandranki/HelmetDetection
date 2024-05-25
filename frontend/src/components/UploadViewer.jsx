// src/FileUploadPreview.js
import React, { useState, useRef } from 'react';

const UploadViewer = ({ onUpload }) => {
  const [preview, setPreview] = useState(null);
  const [fileType, setFileType] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const fileType = file.type.split('/')[0];
      setFileType(fileType);

      const url = URL.createObjectURL(file);
      setPreview(url);
      setErrorMessage('');
      onUpload(url, fileType);
    }
  };

  const handleVideoError = () => {
    setErrorMessage('Failed to load video. The file format might not be supported.');
  };

  const handleReset = () => {
    setPreview(null);
    setFileType('');
    setErrorMessage('');
    fileInputRef.current.value = null; // Reset file input
    onUpload(null, null); // Reset display component
  };

  const triggerFileInput = () => {
    fileInputRef.current.click();
  };

  return (
    <div className="max-w-md mx-auto my-4 p-4 border rounded-lg shadow-lg">
      <input 
        type="file" 
        ref={fileInputRef} 
        onChange={handleFileChange} 
        accept="image/*,video/*" 
        className="hidden"
      />
      <button 
        onClick={triggerFileInput} 
        className="mt-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-700 focus:outline-none"
      >
        Choose File
      </button>
      <button 
        onClick={handleReset} 
        className="mt-2 ml-2 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700 focus:outline-none"
      >
        Reset
      </button>
      {errorMessage && <p className="mt-2 text-red-500">{errorMessage}</p>}
      {preview && (
        <div className="mt-4">
          {fileType === 'image' ? (
            <img src={preview} alt="Preview" className="w-full h-auto rounded-lg" />
          ) : (
            <video
              controls
              className="w-full h-auto rounded-lg"
              onError={handleVideoError}
            >
              <source src={preview} type="video/mp4" />
              <source src={preview} type="video/webm" />
              <source src={preview} type="video/ogg" />
              Your browser does not support the video tag.
            </video>
          )}
        </div>
      )}
    </div>
  );
};

export default UploadViewer;
