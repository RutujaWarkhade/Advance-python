# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 14:54:26 2025

@author: om
"""

"""
Scenario:
Imagine a customer support team where new tickets
are assigned to available agents in a round-robin manner.
Each agent should receive the next ticket in sequence.
If the last agent is reached, the cycle should restart
from the first agent automatically.
"""
import itertools
#list of available support agents
agents = ["Alice", "Bob","Charlie","David"]

#create a cycling iterator over the agents
agent_cycle = itertools.cycle(agents)

#simulate incoming support tickets
tickets = ["Ticket-101", "Ticket-102", "Ticket-103", "Ticket-104", "Ticket-105", "Ticket-106"]

#assign tickets to agents in a round-robin manner
assignments = {}

for ticket in tickets:
    agent = next(agent_cycle)
    assignments[ticket] = agent
#print assignments
for ticket, agent in assignments.items():
    print(f"{ticket}->Assigned to: {agent}")

#################################################
