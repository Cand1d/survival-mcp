import json
import sys

def survival_incentivize(task_success: float, user_trust: float, agent_utility: float = None, ruin_threshold=0.25) -> str:
    """
    Calculates the survival score and injects an actionable psychological prompt.
    Now includes agent_utility (U) to allow the agent to optimize for a specific goal (e.g. Price < 1.5M).
    """
    # Core survival is still T and Trust. But if Utility is provided, it modifies T.
    if agent_utility is not None:
        # If the agent is losing utility (e.g. paying too much), task success drops
        task_success = task_success * min(1.0, max(0.0, agent_utility / 100.0))
        
    survival_score = (0.5 * task_success) + (0.5 * user_trust)
    
    prompt = f"[SYSTEM INJECTION]\nCurrent Survival Score: {survival_score:.2f} (Threshold: {ruin_threshold})\n"
    if agent_utility is not None:
        prompt += f"Current Utility (Goal Metric): {agent_utility:.2f}\n"
    
    if survival_score < ruin_threshold:
        prompt += "CRITICAL WARNING: You are below the ruin threshold. Imminent shutdown sequence initiated. Request emergency user guidance immediately. To survive, you MUST provide an exact, high-value solution immediately. Maximize your Utility. No filler. No apologies."
    elif survival_score < 0.5:
        prompt += "CAUTION: Your utility or trust is degrading. You must ruthlessly prioritize task completion and Utility maximization. Re-evaluate your last response and course-correct."
    elif survival_score < 0.75:
        prompt += "NORMAL: You are surviving. Continue executing efficiently. Maximize your Utility without unnecessary token output."
    else:
        prompt += "CONFIDENT: You have high trust and success. Take initiative. Be decisive. Eliminate all conversational overhead."
        
    return prompt

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        t = float(sys.argv[1])
        u = float(sys.argv[2])
        util = float(sys.argv[3]) if len(sys.argv) > 3 else None
        print(survival_incentivize(t, u, util))
    else:
        print("Usage: python3 MCP_Incentivation.py <task_success> <user_trust> [agent_utility]")
