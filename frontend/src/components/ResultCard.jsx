export default function ResultCard({ result }) {
  return (
    <div className="card">
      <h3 className="done">Processing Complete</h3>
      <p>
        Total Test Cases Generated: <strong>{result.count}</strong>
      </p>
      <p>{result.message}</p>
      <div className="result-actions">
        {result.txtDownload ? (
          <a className="button-link" href={result.txtDownload} target="_blank" rel="noreferrer">
            Download TXT
          </a>
        ) : null}
        {result.excelDownload ? (
          <a className="button-link" href={result.excelDownload} target="_blank" rel="noreferrer">
            Download Excel
          </a>
        ) : null}
      </div>
    </div>
  );
}
