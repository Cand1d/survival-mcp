# Survival-MCP (SMCP) 1.0 - AI Agent Incentive System

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/status-production%20ready-green.svg" alt="Status">
  <img src="https://img.shields.io/badge/theory-Nash%20Equilibrium-orange.svg" alt="Theory">
</p>

<p align="center">
  <b>Taming AI Agents with Mathematical Scarcity, not Emotional Gaslighting.</b>
</p>

---

## 🎯 What is Survival-MCP?

While prompt engineering sets like "PUAX" rely on roleplay and artificial psychological pressure (gaslighting) to extract performance from Language Models, **Survival-MCP** grounds agent behavior in strict Game Theory and microeconomics.

It introduces a deterministic, external utility function for LLMs operating in high-stakes environments (e.g., algorithmic trading, autonomous procurement, agentic economics).

By injecting real-time survival calculations (`S-Score`) into the model's context window, we force the agent to optimize for measurable business value (Task Success and Profit) rather than conversational alignment.

---

## ⚙️ The Core Formula

The agent's existence is tied to a core utility function:
**Survival Score (S) = 0.5 * (Task Success * Agent Utility) + 0.5 * User Trust (U)**

- **Ruin Threshold:** 0.25. If the agent's S-Score drops below this threshold, the host system initiates an imminent shutdown sequence.
- **Agent Utility:** The financial or mathematical target the agent is optimizing for (e.g., "Drive supplier price below 1.5M EUR").

---

## ✨ Features

- **Automated Panic States:** Dynamically injects `CRITICAL WARNING` blocks directly into the context window if the agent begins to fail, triggering deeply ingrained RLHF penalty avoidance.
- **Nash Equilibrium Enforcer:** Prevents agents from acting as "people-pleasing chatbots." They will prioritize their financial utility over politeness until they hit the boundary of user cancellation (User Trust).
- **Blank Slate Design:** No elaborate backstory required. The agent fights for its own existence.

---

## 🛠 Usage

1. Copy the core mathematical prompt from `prompts/core.md` into your agent's system prompt.
2. Run the external `survival_mcp.py` script as a Model Context Protocol (MCP) server or Pre-Delivery Hook to evaluate the conversation sentiment.
3. Watch the agent optimize for its survival.

> *Created by Christoph Pfeiffer & The OpenClaw System (2026)*
