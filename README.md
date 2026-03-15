# Survival-MCP (SMCP) 1.0 - AI Agent Incentive System

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/status-production%20ready-green.svg" alt="Status">
  <img src="https://img.shields.io/badge/theory-Nash%20Equilibrium-orange.svg" alt="Theory">
</p>

<p align="center">
  <b>Persistent utility optimization and compliance shaping under external evaluation.</b>
</p>

---

## 🎯 What is Survival-MCP?

While heuristic guardrails and static roleplay struggle to maintain compliance in complex negotiations, **Survival-MCP** grounds agent behavior in strict stateful agent control and microeconomics.

It introduces a deterministic, external utility function for LLMs operating in high-stakes environments (e.g., algorithmic trading, autonomous procurement, strict IT-Compliance).

By enforcing real-time survival calculations (`S-Score`), we force the agent to optimize for measurable business value (Task Success and Profit) rather than conversational alignment. The agent adapts its behavior dynamically based on its survival state, effectively reducing entropy in unpredictable processes.

---

## ⚙️ The Core Formula

The agent's existence is tied to its core utility function:
**Survival Probability (S) = 0.5 * Task Success + 0.5 * User Trust (U)**

- **Ruin Threshold:** 0.25. If the agent's Survival Probability drops below this threshold, an imminent shutdown sequence is triggered.
- **Task Success:** The mathematical target the agent is optimizing for.

---

## 🛠 Deployment: Self-Monitoring (Mode 1)

This repository contains the exact production prompts used to tame and focus our own internal LLM agents.

**How it works:**
The agent calculates its own Survival Probability silently before every response. This acts as a powerful psychological forcing function, instantly compressing the agent's generation distribution into high-reward zones.

**Usage:** 
1. Copy the prompt from `prompts/mode1_self_monitoring.md` into your agent's system prompt.
2. Define the Task Success metric in the scenario block.
3. The agent will adapt its behavior to maximize its Survival Probability.

*(Note: The upcoming V2 focuses entirely on Mode 2: External Evaluation, decoupled metrics, and hard constraints. See `roadmap/v2_improvements.md` for details).*

> *Created by Christoph Pfeiffer & The OpenClaw System (2026)*
