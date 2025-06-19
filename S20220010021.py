# PYTHON CODE IMPLEMENTATION OF AC3 ALGORITHM

# Question : Implement AC-3 algorithm to solve the CSP given below.
# Variables:
# {X, Y, Z}

# Constraints:
# X=Y; X>=Z; Y!=Z; 

# Arcs:
# X=Y; X>=Z; Y=X; Y!=Z; Z<=X; Z!=Y

# Queue (in Ascending order):
# X=Y
# X>=Z
# Y=X 
# Y!=Z 
# Z<=X
# Z!=Y

# Variables and their Domain Values:
# X={1,2,3,4}
# Y={2,4}
# Z={2,5,8}


# Solution : 


from collections import deque

print("<<<<<<<<<<<<<< This code is prepared by Aryan sharma >>>>>>>>>>>>>>")
print("")

#function to check if domain is revised

def revise_domains(domains, constraints, a, b):
    # Flag which checks
    revised = False
    new_domain = set()
    
    #checks in domain a 
    for value_a in domains[a]:
       
       #checks if there is any other value in b which satisfies it 
        if any(constraints[(a, b)](value_a, value_b) for value_b in domains[b]):
            new_domain.add(value_a)
        else:
            #if not satisfying value is found it is turned to true/false
            revised = True
    domains[a] = new_domain
    return revised
    
#optimizes the csp 

def optimize_csp_problem():
    """
    This function optimizes the CSP problem.
    """

#this function checks for ac3 constraints


    
def algorithm(variables, domains, constraints):
    #we give variable from queue
    queue = deque([(a, b) for a in variables for b in variables if a != b])
    
    while queue:
        (a, b) = queue.popleft()
        # this checks for revised domain
        if revise_domains(domains, constraints, a, b):
            # checks if the domain is empty or not
            if not domains[a]:
                return {}
            # new constraint added 
            for c in variables:
                if c != a and c != b:
                    queue.append((c, a))
    
    return domains

#function which validate csp sol

def validate_csp_solution(solution):
    """
    This function validates the solution to the CSP problem.
    """
# varibale domain given in ques

vars_set = {'Var1', 'Var2', 'Var3'}
domains_set = {'Var1': {1, 2, 3, 4}, 'Var2': {2, 4}, 'Var3': {2, 5, 8}}
constraints_dict = {
    ('Var1', 'Var2'): lambda x, y: x == y,
    ('Var1', 'Var3'): lambda x, z: x >= z,
    ('Var2', 'Var1'): lambda y, x: y == x,
    ('Var2', 'Var3'): lambda y, z: y != z,
    ('Var3', 'Var1'): lambda z, x: z <= x,
    ('Var3', 'Var2'): lambda z, y: z != y
}

#function analysis the solution

def csp_analysis(variables, domains, constraints):
    """
    This function performs analysis on the given CSP problem.
    """ 
  #now we print the sol

new_domains_set = algorithm(vars_set, domains_set, constraints_dict)
print("Final domains after AC-3 algorithm:")
print(new_domains_set)