import { useState, useEffect } from 'react';
import { Shield, Bug, Cpu, Terminal as TermIcon, CheckCircle, AlertTriangle } from 'lucide-react';
import axios from 'axios';

const api = axios.create({ baseURL: 'http://localhost:8006/api' });

export default function DashboardPage() {
  const [status, setStatus] = useState("IDLE");
  const [logs, setLogs] = useState<string[]>(["[SYSTEM] SentinelCore initialized.", "[SYSTEM] Monitoring workspace_to_monitor..."]);
  const [running, setRunning] = useState(false);

  const addLog = (msg: string) => {
    setLogs(prev => [`[${new Date().toLocaleTimeString()}] ${msg}`, ...prev]);
  };

  const triggerAgent = async () => {
    setRunning(true);
    setStatus("RUNNING");
    addLog("PROMPTING AGENT: Analyzing code trajectory...");
    
    try {
      const res = await api.post('/run');
      addLog(`AGENT ACTION: ${res.data.last_action}`);
      addLog("SUCCESS: Code refactored and MEMORY.md updated.");
      setStatus("FINISHED");
    } catch (err) {
      addLog("CRITICAL ERROR: Failed to reach agent brain.");
      setStatus("ERROR");
    } finally {
      setRunning(false);
    }
  };

  return (
    <div className="terminal-container">
      {/* Side Control Panel */}
      <div className="control-panel">
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '40px' }}>
          <Shield color="var(--terminal-green)" size={32} />
          <h1 style={{ margin: 0, fontSize: '20px' }}>SENTINEL CORE</h1>
        </div>

        <div className="status-indicator">
          <div className="indicator-dot" style={{ backgroundColor: status === 'ERROR' ? 'red' : 'var(--terminal-green)' }}></div>
          <span>SYSTEM STATUS: {status}</span>
        </div>

        <div className="file-view">
           <div style={{ color: 'var(--terminal-dim)', fontSize: '10px', marginBottom: '8px' }}>TARGET_WORKSPACE</div>
           <div style={{ fontSize: '13px' }}>/workspace_to_monitor/app.py</div>
           <div style={{ fontSize: '13px' }}>/workspace_to_monitor/MEMORY.md</div>
        </div>

        <div style={{ flex: 1 }}></div>

        <button 
          className="action-btn" 
          disabled={running}
          onClick={triggerAgent}
        >
          {running ? "PROCESSING..." : "TRIGGER REFACTOR LOOP"}
        </button>
      </div>

      {/* Main Trajectory Log */}
      <div className="main-log">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
           <h2 style={{ fontSize: '18px', color: 'var(--terminal-green)', margin: 0 }}>ORCHESTRATION TRAJECTORY</h2>
           <TermIcon size={20} color="var(--terminal-dim)" />
        </div>

        <div style={{ display: 'flex', flexDirection: 'column' }}>
           {logs.map((log, i) => (
             <div key={i} className="log-entry" style={{ 
               color: log.includes('ERROR') ? 'var(--error-red)' : 
                      log.includes('SUCCESS') ? 'var(--terminal-green)' : 'inherit'
             }}>
               {log}
             </div>
           ))}
        </div>

        {status === 'FINISHED' && (
          <div className="file-view" style={{ borderColor: 'var(--terminal-green)', background: 'rgba(0, 255, 65, 0.05)' }}>
             <CheckCircle size={16} color="var(--terminal-green)" style={{ marginBottom: '8px' }} />
             <div style={{ fontWeight: 700, marginBottom: '4px' }}>TRAJECTORY COMPLETED</div>
             <p style={{ margin: 0, fontSize: '12px' }}>
                Agent successfully identified division by zero in <code>calculate_tax</code>. 
                Refactored code with input validation and updated <code>MEMORY.md</code> for persistent state.
             </p>
          </div>
        )}
      </div>
    </div>
  );
}
