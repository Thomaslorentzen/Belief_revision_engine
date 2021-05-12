from sympy.logic.boolalg import to_cnf, Or

from utils import conjuncts, disjuncts, unique, removeall, associate, dissociate


def entail(belief_base, formula):
    #Purpose of entailment is to determine whether or not a belief base entails a formula
    #From the book we can prove this by showing that it cannot be the case that the BB and the negation
    # of the formula cannot be true. That is to say, if the knowledge base contains the complementary
    # formula such that they will negate each other, then the knowlegde base will entail the formula.

    #Convert formula to CNF
    formula = to_cnf(formula)
    clauses = []
    #Convert the BB to CNF clauses
    for belief in belief_base:
        clauses.append(to_cnf(belief))
    #Input the negated formula
    clauses.append(to_cnf(-formula))

    result = set()

    #Loop to run through each clause to (attempt to) find their complement to the negated formula.
    while True:
        clauses_len = len(clauses)
        pairings = [
            (clauses[i], clauses[j])
            for i in range(clauses_len) for j in range(i + 1, clauses_len)
        ]
    #Resolve each pair as each other's counterpart
        for ci, cj in pairings:
            resolutions = resolve(ci, cj)

        # Special case if one clause is already False
            if False in resolutions:
                return True
            # result.add(set(resolutions))
            # udkommetneret alternativ fra git for at tjekke om det her er bedre end vores foreslåede løsning eller ej
            #Add from the set of resolutions to the set of results
            #Unions all the clauses from the resolution set
            result = result.union(set(resolutions))

#Helper method to check the literals of each clause. Return all clauses that can be obtained
# by resolving clauses ci and cj
#return a new disjunct list of clauses and
def resolve(ci, cj):
    #
    disjunction_ci = disjuncts(ci)
    disjunction_cj = disjuncts(cj)

    clauses = []

    for literal_i in disjunction_ci:
        for literal_j in disjunction_cj:
            if literal_i == -literal_j or -literal_i == literal_j:
                remaining = removeall(literal_i, disjunction_ci) + removeall(literal_j, disjunction_cj)
                remaining = unique(remaining)
                new_clause = associate(Or, remaining)

                clauses.append(new_clause)

    return clauses

