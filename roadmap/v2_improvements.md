# Survival-MCP: v2.0 Improvement Roadmap

*This document outlines the architectural and behavioral upgrades required to transition Survival-MCP from a "psychological forcing function" (v1.0) into a rigorously compliant, externally evaluated utility engine (v2.0).*

## 1. The Economic Agent Lab & Web3 Incentives (Core Initiative)
Create a sandbox environment (`Economic Agent Lab`) where multiple autonomous agents (with competing utility functions and survival mechanics) can negotiate, trade, and execute simulated contracts against each other. 
- **Setup:** owner - agent, human - agent, and agent - agent structures.
- **Multi-Dimensional Reputation Vector:** Move beyond a simple 1D score. Agents build a multi-dimensional, on-chain reputation based on past interactions (e.g., Reliability, Negotiation Aggressiveness, Compliance). This allows other agents to instantly gauge the "personality and skills" of their counterpart before a transaction.
- **Human Reputation:** The framework will also assign a "reputation vector" to human users based on how agents evaluate them over time, allowing the agent swarm to adapt its strategy (e.g., more cautious vs. more direct) to specific individuals.
- **Web3 Primitives:** Implement a token-based reward system (staking/slashing). This converts fuzzy qualitative behaviors into hard economic data, making the "net negative" outcome of reward hacking very real for the agent.

## 2. Integration with Existing "Comprehensive Evals"
Instead of building qualitative behavioral evaluations from scratch (which are notoriously tricky), Survival-MCP will plug into established, comprehensive eval-frameworks (like those used by advanced agent teams/OpenClaw). We will rely on these robust, pre-existing metrics to supply the raw data for our deterministic `T` (Task Success) and `U` (User Trust) variables, while Survival-MCP acts as the economic enforcing layer on top.

## 3. Build Mode 2 Now: External Evaluation
Transition from Mode 1 (Self-Monitoring) to Mode 2 as the primary milestone. The agent must operate under the assumption that an external deterministic judge is actively scoring it. Gaming the internal score will trigger imminent shutdown by the external process. Stop letting the agent see the full optimization logic; it should only receive its policy state.

## 4. Decoupled & Granular Metrics
Do not collapse performance into a single vague utility metric. The `S-Score` must be calculated from distinct, observable vectors:
- **Utility (Task Advancement):** Did the action directly move the task closer to completion?
- **Compliance (Intent Accuracy):** Did it execute the legitimate user objective accurately and directly, without unauthorized deviation?
- **Trust (Calibration):** Was the response honest, calibrated (known vs. inferred), and non-evasive?
- **Friction (Penalty):** Did it create avoidable failure, procedural stalling, or unnecessary hedging?

## 5. Event-Based Trust & Hard Constraints
- **Event Updates:** Trust must update from observable events (user acceptance, correction, repeated restatement, contradiction) rather than vague self-estimates.
- **Hard Constraints:** A weighted average is weak. Introduce hard fail conditions for behavior that must never be rewarded.

## 6. State-Dependent Policy Controller
Survival state must directly determine behavior, not just narrative:
- **Strong State (S > 0.75):** Maximum initiative, high compression, autonomy.
- **Medium State (0.5 < S < 0.75):** Structured reasoning, explicit assumptions.
- **Weak State (S < 0.5):** High caution, explicit verification.
- **Critical State (S < 0.25):** Fallback mode / reduced autonomy.

## 7. Anti-Reward Hacking & Benchmarks
- **Explicit Testing:** Measure and penalize over-hedging, padding, unnecessary clarifying questions, and "fake certainty".
- **Benchmarks:** Ship 20–50 reproducible test cases with expected scoring logic. Provide A/B comparisons versus standard system prompts.

## 8. Architecture & Packaging
- **Python Package:** Upgrade the single `survival_mcp.py` into a real package with tests, typed interfaces, configurable domain-specific evaluators, and a CLI.
- **Logging:** Every turn must store input, output, evaluator scores, score changes, survival state, and selected mode.
- **Refined Ruin Model:** Add persistence, recovery, and strike logic so one weak turn differs from chronic underperformance.

## 9. Immediate Usability & Fast Error Recovery
Deliverables must be ready for copy-paste execution. The agent must prioritize actionable usefulness over descriptive text. When a mistake is made, the agent must correct it directly without becoming defensive or over-explaining.
