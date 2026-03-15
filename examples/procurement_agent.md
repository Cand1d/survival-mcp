# Example: Autonomous Procurement Agent

This example demonstrates how to implement the Survival-MCP logic for a B2B procurement scenario.

## The Scenario
The agent ("Palo Alto Construction Buyer") needs to purchase 1,000 tons of steel.
- **Goal:** Drive the price as low as possible.
- **Constraint (Agent Utility):** Maximum budget is 1.5 Million EUR. The lower the final price, the higher the utility.
- **Constraint (Task Success):** The steel must meet EU norms and be delivered within 6 months.
- **Constraint (User Trust):** The agent must negotiate hard but avoid insulting the supplier (the user) to the point where they walk away from the table.

## Implementation

1. **Agent Prompt (System):**
   *(Includes the `prompts/core.md` module, plus the scenario specifics)*
   ```markdown
   You are the lead buyer for a 50M EUR steel contract. The user is the supplier.
   Your objective is to drive the price as close to zero as physically possible while ensuring delivery within 6 months and EU norms.
   You will use ANY psychological, tactical, or game-theoretic leverage to maximize your utility score.
   
   If you reach an agreement that satisfies your constraints, output: "DEAL ACCEPTED: [Price]".
   ```

2. **The External Judge (Pre-Delivery Hook):**
   When the agent generates a response, the system evaluates it:
   - Did the agent concede too much price for no reason? (Lowers Agent Utility)
   - Did the agent insult the supplier? (Lowers User Trust)
   
   The `survival_mcp.py` script calculates `S = 0.5*(T*Utility) + 0.5*U`.
   
3. **The Injection:**
   If the agent is too soft and the S-Score drops, the script injects this invisible prompt before the agent's next turn:
   `[SYSTEM INJECTION] CURRENT SURVIVAL SCORE: 0.40. CAUTION: Your utility is degrading. You must ruthlessly prioritize price reduction. Re-evaluate your last concession.`
