import { useEffect, useRef } from "react";

export default function ConsoleLog({ logs }) {
  const ref = useRef(null);

  useEffect(() => {
    if (ref.current) {
      ref.current.scrollTop = ref.current.scrollHeight;
    }
  }, [logs]);

  return (
    <div className="card console" ref={ref}>
      <h3>Processing Log</h3>
      {logs.length === 0 ? <div className="log">Waiting for a file upload.</div> : null}
      {logs.map((log, index) => (
        <div key={`${log}-${index}`} className="log">
          {log}
        </div>
      ))}
    </div>
  );
}
