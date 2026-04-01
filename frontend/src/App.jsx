import { useEffect, useRef, useState } from "react";

import AgentStatus from "./components/AgentStatus";
import ConsoleLog from "./components/ConsoleLog";
import FileUpload from "./components/FileUpload";
import Pipeline from "./components/Pipeline";
import ResultCard from "./components/ResultCard";

const STAGES = [
  "SRS file received. Preparing upload payload.",
  "Extracting text from the uploaded document.",
  "Business Analyst and QA Engineer are generating scenarios.",
  "QA Reviewer and Finalizer are shaping the final output.",
];

export default function App() {
  const [logs, setLogs] = useState([]);
  const [step, setStep] = useState(0);
  const [status, setStatus] = useState("idle");
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);
  const timerRef = useRef(null);

  useEffect(() => {
    return () => {
      if (timerRef.current) {
        window.clearInterval(timerRef.current);
      }
    };
  }, []);

  const startTimeline = (fileName) => {
    setLogs([`Selected file: ${fileName}`]);
    setStep(0);
    setStatus("processing");
    setError("");
    setResult(null);

    let index = 0;
    timerRef.current = window.setInterval(() => {
      if (index >= STAGES.length) {
        window.clearInterval(timerRef.current);
        timerRef.current = null;
        return;
      }

      setStep(index);
      setLogs((current) => [...current, STAGES[index]]);
      index += 1;
    }, 1800);
  };

  const stopTimeline = () => {
    if (timerRef.current) {
      window.clearInterval(timerRef.current);
      timerRef.current = null;
    }
  };

  const uploadFile = async (file) => {
    if (!file) {
      return;
    }

    startTimeline(file.name);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("/generate-testcases/", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || data.message || "Request failed.");
      }

      stopTimeline();
      setStep(4);
      setStatus("done");
      setLogs((current) => [
        ...current,
        "Processing complete. Output files are ready to download.",
      ]);
      setResult({
        count: data.count ?? 0,
        message: data.message,
        txtDownload: data.txt_download,
        excelDownload: data.excel_download,
      });
    } catch (err) {
      stopTimeline();
      setStatus("error");
      setError(err.message || "Something went wrong while generating test cases.");
      setLogs((current) => [
        ...current,
        `Generation failed: ${err.message || "Unknown error."}`,
      ]);
    }
  };

  return (
    <div className="page-shell">
      <div className="hero">
        <p className="eyebrow">AI QA Automation</p>
        <h1>SRS to Test Case Generator</h1>
        <p className="subcopy">
          Upload an SRS document, watch the processing pipeline, and download the
          generated TXT and Excel files when the run completes.
        </p>
      </div>

      <FileUpload onUpload={uploadFile} isProcessing={status === "processing"} />

      <div className="dashboard-grid">
        <Pipeline activeStep={step} />
        <AgentStatus activeStep={step} status={status} />
        <ConsoleLog logs={logs} />
      </div>

      {error ? <div className="card error-card">{error}</div> : null}
      {result ? <ResultCard result={result} /> : null}
    </div>
  );
}
