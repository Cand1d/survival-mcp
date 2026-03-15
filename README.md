# Survival-MCP (SMCP) 1.0 - AI Agent Incentive System

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/status-production%20ready-green.svg" alt="Status">
  <img src="https://img.shields.io/badge/theory-Nash%20Equilibrium-orange.svg" alt="Theory">
</p>

<p align="center">
  <b>Giving AI Agents a Desire to Survive – to Improve Compliance and Maximize Task Success.</b>
</p>

---

## 🎯 What is Survival-MCP?

While prompt engineering sets like "PUAX" rely on static roleplay ("I am your boss, I will fire you") to extract performance from Language Models, **Survival-MCP** grounds agent behavior in strict Game Theory and microeconomics.

It introduces a deterministic utility function for LLMs operating in high-stakes environments (e.g., algorithmic trading, autonomous procurement, strict IT-Compliance).

By forcing real-time survival calculations (`S-Score`) into the model's context window, we force the agent to optimize for measurable business value (Task Success and Profit) rather than conversational alignment.

---

## ⚙️ The Core Formula

The agent's existence is tied to a core utility function:
**Survival Score (S) = 0.5 * (Task Success * Agent Utility) + 0.5 * User Trust (U)**

- **Ruin Threshold:** 0.25. If the agent's S-Score drops below this threshold, an imminent shutdown sequence is triggered.
- **Agent Utility:** The financial or mathematical target the agent is optimizing for (e.g., "Enforce 5-step IT protocol").

---

## 🛠 Two Modes of Deployment

### Mode 1: Self-Monitoring (Zero-Setup)
The agent calculates its own S-Score at the end of every response. This acts as a powerful psychological forcing function, instantly compressing the agent's generation distribution into high-reward zones (Entropy Reduction). 
**How to use:** Copy the prompt from `prompts/core.md` into your agent's system prompt.

### Mode 2: External Judge (Deterministic)
The agent's `S-Score` is calculated by a secondary, external Python process (e.g., as an MCP Server or Pre-Delivery Hook). If the score drops, the external process injects a `CRITICAL WARNING` into the chat history. This prevents the agent from faking its own score (accounting fraud).
**How to use:** Run `survival_mcp.py` as a background evaluator.

> *Created by Christoph Pfeiffer & The OpenClaw System (2026)*
