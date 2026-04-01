const steps = [
  "Uploading SRS",
  "Extracting Requirements",
  "Generating Test Cases",
  "Reviewing",
  "Finalizing Output",
];

export default function Pipeline({ activeStep }) {
  return (
    <div className="card">
      <h3>Processing Pipeline</h3>
      {steps.map((step, index) => (
        <div key={step} className="pipeline-step">
          <span className={index <= activeStep ? "step-icon done" : "step-icon pending"}>
            {index <= activeStep ? "Done" : "Wait"}
          </span>
          <span>{step}</span>
        </div>
      ))}
    </div>
  );
}
