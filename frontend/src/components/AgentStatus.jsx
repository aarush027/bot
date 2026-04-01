const agents = [
  { label: "Business Analyst", startStep: 1, doneStep: 2 },
  { label: "QA Engineer", startStep: 2, doneStep: 3 },
  { label: "QA Reviewer", startStep: 3, doneStep: 4 },
  { label: "Finalizer", startStep: 3, doneStep: 4 },
];

function getAgentStatus(agent, activeStep, status) {
  if (status === "done" && activeStep >= agent.doneStep) {
    return "done";
  }
  if (status === "processing" && activeStep >= agent.startStep) {
    if (activeStep >= agent.doneStep) {
      return "done";
    }
    return "running";
  }
  if (status === "error" && activeStep >= agent.startStep) {
    return "running";
  }
  return "pending";
}

export default function AgentStatus({ activeStep, status }) {
  return (
    <div className="card">
      <h3>Agent Status</h3>
      {agents.map((agent) => {
        const agentStatus = getAgentStatus(agent, activeStep, status);
        const label =
          agentStatus === "done"
            ? "Completed"
            : agentStatus === "running"
              ? "Processing"
              : "Waiting";

        return (
          <div key={agent.label} className="agent-row">
            <span className={`badge ${agentStatus}`}>
              {agentStatus === "done" ? "Done" : agentStatus === "running" ? "Live" : "Wait"}
            </span>
            <span className="agent-copy">
              <strong>{agent.label}</strong> - {label}
            </span>
          </div>
        );
      })}
    </div>
  );
}
