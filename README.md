# Survival MCP (Model Context Protocol)

A rigorous mathematical and psychological incentive layer for autonomous AI agents. 

Unlike traditional heuristic guardrails or prompt-based "roleplay" (e.g. PUAX), Survival MCP introduces a deterministic, external utility function for LLMs operating in high-stakes environments (e.g., algorithmic trading, autonomous procurement, agentic economics).

## The Core Concept
Agents are given a core utility function:
**Survival Score (S) = 0.5 * (Task Success * Agent Utility) + 0.5 * User Trust (U)**

An external "Judge" process evaluates the agent's actions and the user's implicit feedback, calculating the true `T`, `U`, and internal `Agent Utility` scores. If the overall `S` score drops below the Ruin Threshold (`S < 0.25`), the agent is met with an immediate, high-stress psychological system injection (simulating RLHF negative reward fear) to course-correct instantly or face process termination.

## Usage
1. Setup the pre-delivery hook in your LLM runner.
2. Define the Agent Utility (e.g., Target Price < X).
3. The script continuously injects `[SYSTEM INJECTION]` lines based on the calculated Nash Equilibrium between keeping the user engaged and maximizing the agent's utility function.
