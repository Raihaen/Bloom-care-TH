from ortools.sat.python import cp_model
from collections import defaultdict
from .models import Assignment, Caregiver, Visit




def minimize_max_unique_caregivers_per_customer(model, caregiver_visit, caregivers, visits):
    customers = list(set(visit.customer for visit in visits))
    
    # Mapping: customer → list of caregiver assigned (BoolVar)
    caregiver_assigned_to_customer = {
        (customer, ci): model.NewBoolVar(f'caregiver_{ci}_assigned_to_customer_{customer}')
        for customer in customers
        for ci in range(len(caregivers))
    }


    # Link caregiver_assigned_to_customer with caregiver_visit decisions
    for vi, visit in enumerate(visits):
        customer = visit.customer
        for ci in range(len(caregivers)):
            # caregiver_visit[(ci, vi)] is a BoolVar → whether ci visits vi
            # If caregiver ci is assigned to any visit of customer, set caregiver_assigned_to_customer to 1
            model.AddImplication(caregiver_visit[(ci, vi)], caregiver_assigned_to_customer[(customer, ci)])

    # Sum unique caregivers per customer
    n_diff_caregivers = {}
    for customer in customers:
        assigned_vars = [caregiver_assigned_to_customer[(customer, ci)] for ci in range(len(caregivers))]
        n_diff = model.NewIntVar(0, len(caregivers), f'n_diff_caregivers_customer_{customer}')
        model.Add(n_diff == sum(assigned_vars))
        n_diff_caregivers[customer] = n_diff

    # Define max over all customers
    max_unique_caregivers = model.NewIntVar(0, len(caregivers), 'max_unique_caregivers')
    for n_diff in n_diff_caregivers.values():
        model.Add(n_diff <= max_unique_caregivers)

    # Objective: minimize max
    model.Minimize(max_unique_caregivers)

    return max_unique_caregivers

            


# def minimize_max_switches_per_caregiver(model, caregiver_visit, caregivers, switches_per_caregiver):
#     # For each caregiver, create BoolVars indicating if that switch happens (both visits assigned to caregiver)
#     switches_vars_per_caregiver = {}

#     for ci in range(len(caregivers)):
#         switches_vars = []
#         for (vi1, vi2) in switches_per_caregiver.get(ci, []):
#             switch_var = model.NewBoolVar(f'switch_c{ci}_v{vi1}_v{vi2}')
#             # switch_var == 1 iff caregiver assigned to both visits
#             model.AddBoolAnd([caregiver_visit[(ci, vi1)], caregiver_visit[(ci, vi2)]]).OnlyEnforceIf(switch_var)
#             model.AddBoolOr([caregiver_visit[(ci, vi1)].Not(), caregiver_visit[(ci, vi2)].Not()]).OnlyEnforceIf(switch_var.Not())
#             switches_vars.append(switch_var)
#         switches_vars_per_caregiver[ci] = switches_vars

#     # Sum switches per caregiver
#     total_switches_per_caregiver = {}
#     for ci, switches_vars in switches_vars_per_caregiver.items():
#         total_switches_per_caregiver[ci] = model.NewIntVar(0, len(switches_vars), f'total_switches_caregiver_{ci}')
#         model.Add(total_switches_per_caregiver[ci] == sum(switches_vars))

#     # Max switches over caregivers
#     max_switches = model.NewIntVar(0, max(len(v) for v in switches_vars_per_caregiver.values() or [[0]]), 'max_switches_per_caregiver')
#     model.AddMaxEquality(max_switches, list(total_switches_per_caregiver.values()))

#     # Objective: minimize max switches per caregiver
#     model.Minimize(max_switches)