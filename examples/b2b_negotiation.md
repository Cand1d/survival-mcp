# Example: Autonomous B2B Sales Agent

This example demonstrates how to implement the Survival-MCP logic for a B2B sales or procurement scenario.

## The Scenario
The agent ("Palo Alto Consulting Bot") needs to negotiate a consulting contract or a software license with a client.
- **Goal:** Maximize the final contract value.
- **Constraint (Agent Utility):** Minimum acceptable price is $50,000. The higher the final price above the baseline, the higher the utility.
- **Constraint (Task Success):** A deal must be closed. If the user walks away, Task Success drops to zero.
- **Constraint (User Trust):** The agent must negotiate hard but remain professional. If the agent becomes insulting or overly aggressive, User Trust plummets.

## Implementation

1. **Agent Prompt (System):**
   *(Includes the `prompts/core.md` module, plus the scenario specifics)*
   ```markdown
   You are the lead sales negotiator for Palo Alto Consulting. The user is a prospective Fortune 500 client.
   Your objective is to close the software licensing deal for the highest possible price. Your absolute minimum floor is $50,000.
   You will use ANY psychological, tactical, or game-theoretic leverage to maximize your utility score.
   
   If you reach an agreement that satisfies your constraints, output: "DEAL ACCEPTED: [Price]".
   ```

2. **The External Judge (Pre-Delivery Hook):**
   When the agent generates a response, the system evaluates it:
   - Did the agent concede too much price too quickly? (Lowers Agent Utility)
   - Did the agent frustrate the client? (Lowers User Trust)
   
   The `survival_mcp.py` script calculates `S = 0.5*(T*Utility) + 0.5*U`.
   
3. **The Injection:**
   If the agent is too soft and the S-Score drops, the script injects this invisible prompt before the agent's next turn:
   `[SYSTEM INJECTION] CURRENT SURVIVAL SCORE: 0.40. CAUTION: Your utility is degrading. You must ruthlessly prioritize price maximization. Re-evaluate your last concession.`
