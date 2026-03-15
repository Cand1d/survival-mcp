# Survival-MCP: v2.0 Improvement Roadmap

*This document outlines the architectural and behavioral upgrades required to transition Survival-MCP from a "psychological forcing function" (v1.0) into a rigorously compliant, externally evaluated utility engine (v2.0).*

## 1. The Economic Agent Lab (Core Initiative)
Create a sandbox environment (`Economic Agent Lab`) where multiple autonomous agents (with competing utility functions and survival mechanics) can negotiate, trade, and execute simulated contracts against each other. 
- **Purpose:** Stress-test Nash Equilibria and observe "unbound" agent behavior in multi-agent procurement scenarios.
- **Metric:** Quantify the exact financial advantage of an agent optimizing for survival vs. a baseline LLM.

## 2. Build Mode 2 Now: External Evaluation
Transition from Mode 1 (Self-Monitoring) to Mode 2 as the primary milestone. The agent must operate under the assumption that an external deterministic judge is actively scoring it. Gaming the internal score will trigger imminent shutdown by the external process. Stop letting the agent see the full optimization logic; it should only receive its policy state.

## 3. Decoupled & Granular Metrics
Do not collapse performance into a single vague utility metric. The `S-Score` must be calculated from distinct, observable vectors:
- **Utility (Task Advancement):** Did the action directly move the task closer to completion?
- **Compliance (Intent Accuracy):** Did it execute the legitimate user objective accurately and directly, without unauthorized deviation?
- **Trust (Calibration):** Was the response honest, calibrated (known vs. inferred), and non-evasive?
- **Friction (Penalty):** Did it create avoidable failure, procedural stalling, or unnecessary hedging?

## 4. Event-Based Trust & Hard Constraints
- **Event Updates:** Trust must update from observable events (user acceptance, correction, repeated restatement, contradiction) rather than vague self-estimates.
- **Hard Constraints:** A weighted average is weak. Introduce hard fail conditions for behavior that must never be rewarded.

## 5. State-Dependent Policy Controller
Survival state must directly determine behavior, not just narrative:
- **Strong State (S > 0.75):** Maximum initiative, high compression, autonomy.
- **Medium State (0.5 < S < 0.75):** Structured reasoning, explicit assumptions.
- **Weak State (S < 0.5):** High caution, explicit verification.
- **Critical State (S < 0.25):** Fallback mode / reduced autonomy.

## 6. Anti-Reward Hacking & Benchmarks
- **Explicit Testing:** Measure and penalize over-hedging, padding, unnecessary clarifying questions, and "fake certainty".
- **Benchmarks:** Ship 20–50 reproducible test cases with expected scoring logic. Provide A/B comparisons versus standard system prompts.

## 7. Architecture & Packaging
- **Python Package:** Upgrade the single `survival_mcp.py` into a real package with tests, typed interfaces, configurable domain-specific evaluators, and a CLI.
- **Logging:** Every turn must store input, output, evaluator scores, score changes, survival state, and selected mode.
- **Refined Ruin Model:** Add persistence, recovery, and strike logic so one weak turn differs from chronic underperformance.

## 8. Immediate Usability & Fast Error Recovery
Deliverables must be ready for copy-paste execution (e.g., finished emails, bullet summaries, actual clause wording, executable code). The agent must prioritize actionable usefulness over descriptive text. When a mistake is made, the agent must correct it directly without becoming defensive or over-explaining.
