# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 07:04:41 2025

@author: om
"""
"""
#Hospital managment System:
1)time read start time
2)token no. *10
3)tell time at which it should come
"""

from datetime import datetime, timedelta
import itertools

patients = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']

patient_cycle = itertools.cycle(patients)

current_time = datetime.now()

time = []
i = 1
for i in range(len(patients)):
    a = current_time + timedelta(minutes=10*i)

    after_time = a.strftime('%H:%M:%S')
    time.append(after_time)

    
time_allocate = {}
for t in time:
    patient = next(patient_cycle)
    time_allocate[t] = patient
    
for t, patient in time_allocate.items():
    print(f"{patient} allocate time : {t}")





















import time
import itertools

# Constants
LOG_FILE = "C:/1-Python/hospital_schedule.log"
patients = [f"Patient-{i+1}" for i in range(10)]
consultation_time = 10  # First patient's time (in minutes)
tickets = ["Ticket-101", "Ticket-102", "Ticket-103", "Ticket-104", "Ticket-105"]

# Create cycling iterator for tickets
ticket_cycle = itertools.cycle(tickets)

# Schedule patients based on consultation time
def schedule_patients():
    start_time = time.time()
    current_time = start_time
    schedule = {}

    for patient in patients:
        start_time_formatted = time.strftime('%H:%M:%S', time.localtime(current_time))
        end_time = current_time + (consultation_time * 60)
        end_time_formatted = time.strftime('%H:%M:%S', time.localtime(end_time))
        ticket = next(ticket_cycle)  # Get a ticket using cycle
        schedule[patient] = (start_time_formatted, end_time_formatted, ticket)
        current_time = end_time  # update time for next patient

    return schedule

# Write schedule to log file
def log_schedule(schedule):
    with open(LOG_FILE, "a") as file:
        for patient, (start, end, ticket) in schedule.items():
            log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} INFO {patient} with {ticket} appointment from {start} to {end}\n"
            file.write(log_entry)
            print(log_entry.strip())

# Run the schedule
schedule = schedule_patients()
log_schedule(schedule)
