"""Solver module for the Bloom Care scheduling problem."""

from .models import Assignment, Caregiver, Visit
from ortools.sat.python import cp_model
from datetime import datetime, timedelta 

def solve(visits: list[Visit], caregivers: list[Caregiver]) -> list[Assignment]:
    """
    Solve the scheduling problem.

    Args:
        visits: List of visits to be assigned
        caregivers: List of available caregivers

    Returns:
        List of Assignment objects representing which caregiver
          is assigned to which visit
    """
    # TODO: Implement the scheduling algorithm
    # This should return a list of Assignment objects
    # representing which caregiver is assigned to which visit

    #return []

    # we start by ininitializing the CP-SAT model
    model = cp_model.CpModel() 
    # variables : 
    caregiver_visit = {}
    objective_terms = [] 

        

    for ci in range(len(caregivers)): # basically a matrix of caregivers and visits. ci,vi iff caregiver ci is assigned to visit vi
        for vi in range(len(visits)):
            caregiver_visit[(ci, vi)] = model.NewBoolVar(f'caregiver_{ci}_visit_{vi}')
    
    
    ## constraints :

    for vi in range(len(visits)):# optimal is exactly one caregiver per visit : AddExactlyOne. If we want at least a fesible solution even it doesnt satisfy all visits. (replace by AddAtMostOne)
        model.AddExactlyOne(
            [caregiver_visit[(ci, vi)] for ci in range(len(caregivers))]
        )
    
    
    for ci, caregiver in enumerate(caregivers):
        for vi, visit in enumerate(visits):
            # Check if *any* availability slot for the caregiver fits this visit
            if not any(av.check_availability(visit) for av in caregiver.availability):
                model.Add(caregiver_visit[(ci, vi)] == 0)
    
    for vi, visit_i in enumerate(visits):
        for vj in range(vi +1, len(visits)):
            visit_j = visits[vj]
            if visit_i.overlaps(visit_j) :
                # if two visits overlap, they cannot be assigned to the same caregiver
                for ci in range(len(caregivers)):
                    model.Add(caregiver_visit[(ci, vi)] + caregiver_visit[(ci, vj)] <= 1)
    


    # skill-matching 
    for ci, caregiver in enumerate(caregivers):
        for vi, visit in enumerate(visits):
            if visit.required_skill not in caregiver.skills:
                model.Add(caregiver_visit[(ci, vi)] == 0)

 ## IN CASE WE USE (AddAtMostOne - WE WANT A FEASIBLE SOLUTION EVEN IF NOT ALL VISITS ARE ASSIGNED)
    # for vi in range(len(visits)):
    #     assigned = model.NewBoolVar(f'assigned_visit_{vi}')
    #     model.AddMaxEquality(assigned,
    #         [caregiver_visit[(ci, vi)] for ci in range(len(caregivers))])
    #     objective_terms.append(assigned)

    # if objective_terms:
    #     model.Maximize(sum (objective_terms))

  



    # code to start the solver

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 300.0 #5 mins for a start we can increase depending on the size of the data
    solver.parameters.num_search_workers = 4 
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        assignments = []
        for ci, caregiver in enumerate(caregivers):
            for vi, visit in enumerate(visits):
                if solver.Value(caregiver_visit[(ci, vi)]) == 1:
                    assignment = Assignment(caregiver_id=caregiver.id, visit_id=visit.id)
                    assignments.append(assignment)
        return assignments
    else:
        return []
