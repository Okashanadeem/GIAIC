"""
Specialized agents for Health & Wellness Planner
"""

from .escalation_agent import escalation_agent
from .nutrition_expert_agent import nutrition_expert_agent
from .injury_support_agent import injury_support_agent

__all__ = [
    'escalation_agent',
    'nutrition_expert_agent', 
    'injury_support_agent'
]