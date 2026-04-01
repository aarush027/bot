export default function FileUpload({ onUpload, isProcessing }) {
  const handleDrop = (event) => {
    event.preventDefault();
    if (isProcessing) {
      return;
    }
    onUpload(event.dataTransfer.files[0]);
  };

  return (
    <div
      className="dropzone card"
      onDragOver={(event) => event.preventDefault()}
      onDrop={handleDrop}
      onClick={() => !isProcessing && document.getElementById("file-input").click()}
    >
      <input
        id="file-input"
        type="file"
        accept=".pdf,.txt"
        hidden
        disabled={isProcessing}
        onChange={(event) => onUpload(event.target.files[0])}
      />
      <h2>{isProcessing ? "Processing in progress" : "Upload SRS Document"}</h2>
      <p>
        {isProcessing
          ? "Please wait while the backend generates test cases."
          : "Drag and drop a PDF or TXT file, or click to browse."}
      </p>
    </div>
  );
}
