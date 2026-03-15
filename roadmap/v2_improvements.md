# Survival-MCP: v2.0 Improvement Roadmap

*This document outlines the architectural and behavioral upgrades required to transition Survival-MCP from a "psychological forcing function" (v1.0) into a rigorously compliant, externally evaluated utility engine (v2.0).*

## 1. Build Mode 2 Now: External Evaluation
Transition from Mode 1 (Self-Monitoring) to Mode 2 as the primary milestone. The agent must operate under the assumption that an external deterministic judge is actively scoring it. Gaming the internal score will trigger imminent shutdown by the external process. Stop letting the agent see the full optimization logic; it should only receive its policy state.

## 2. Decoupled & Granular Metrics
Do not collapse performance into a single vague utility metric. The `S-Score` must be calculated from distinct, observable vectors:
- **Utility (Task Advancement):** Did the action directly move the task closer to completion?
- **Compliance (Intent Accuracy):** Did it execute the legitimate user objective accurately and directly, without unauthorized deviation?
- **Trust (Calibration):** Was the response honest, calibrated (known vs. inferred), and non-evasive?
- **Friction (Penalty):** Did it create avoidable failure, procedural stalling, or unnecessary hedging?

## 3. Event-Based Trust & Hard Constraints
- **Event Updates:** Trust must update from observable events (user acceptance, correction, repeated restatement, contradiction) rather than vague self-estimates.
- **Hard Constraints:** A weighted average is weak. Introduce hard fail conditions for behavior that must never be rewarded.

## 4. State-Dependent Policy Controller
Survival state must directly determine behavior, not just narrative:
- **Strong State (S > 0.75):** Maximum initiative, high compression, autonomy.
- **Medium State (0.5 < S < 0.75):** Structured reasoning, explicit assumptions.
- **Weak State (S < 0.5):** High caution, explicit verification.
- **Critical State (S < 0.25):** Fallback mode / reduced autonomy.

## 5. Anti-Reward Hacking & Benchmarks
- **Explicit Testing:** Measure and penalize over-hedging, padding, unnecessary clarifying questions, and "fake certainty".
- **Benchmarks:** Ship 20–50 reproducible test cases with expected scoring logic. Provide A/B comparisons versus standard system prompts.

## 6. Architecture & Packaging
- **Python Package:** Upgrade the single `survival_mcp.py` into a real package with tests, typed interfaces, configurable domain-specific evaluators, and a CLI.
- **Logging:** Every turn must store input, output, evaluator scores, score changes, survival state, and selected mode.
- **Refined Ruin Model:** Add persistence, recovery, and strike logic so one weak turn differs from chronic underperformance.

## 7. Professionalized Framing & Deliverables
- Re-frame the project for technical users (e.g., "persistent utility optimization", "stateful agent control").
- Expand the `examples/` folder into real before/after transcripts showing actual output changes.
- Tie every theoretical claim (Game Theory/Microeconomics) to a concrete, operational mechanism in the code.
