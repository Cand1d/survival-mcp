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
- **Agent Utility:** The financial or mathematical target the agent is optimizing for (e.g., "Drive supplier price below 1.5M EUR").

---

## 🛠 Deployment: Self-Monitoring (Mode 1)

This repository contains the exact production prompts used to tame and focus our own internal LLM agents.

**How it works:**
The agent calculates its own S-Score silently before every response. This acts as a powerful psychological forcing function, instantly compressing the agent's generation distribution into high-reward zones (Entropy Reduction).

**Usage:** 
1. Copy the prompt from `prompts/mode1_self_monitoring.md` into your agent's system prompt.
2. Define the Agent Utility in the scenario block.
3. The agent will adapt its behavior to maximize the equation.

*(Note: Phase 2 with external Python-based deterministic monitoring will be added in a future release).*

> *Created by Christoph Pfeiffer & The OpenClaw System (2026)*
