from sympy.logic.boolalg import to_cnf, And, Or, Equivalent
from sortedcontainers import SortedList


from entailment import entail
from utils import associate


class Belief_Base:

    def __init__(self):
        #self.beliefs = SortedList(key=lambda b: neg(b.order))
        self.beliefs = []
        self.sorting_queue = []


    def expand_belief_base(self, formula, order):
        formula_as_cnf = to_cnf(formula)
        new_belief = Belief(formula_as_cnf, order)
        for belief in self.beliefs:
            belief.order += 1
        self.beliefs.append(new_belief)

    #Belief base expansion/revision - this method has to remove any belief that would imply the negation of a formula
    #we are trying to add
    def revise(self, formula, order):
        formula_as_cnf = to_cnf(formula)
        entail_results = entail(self, ~formula_as_cnf)
        if entail_results[0]:
            print("belief base: {} does entail formula {}".format(self.beliefs, ~formula_as_cnf))
            print("running contraction on formula: {}".format(~formula_as_cnf))
            print("running contraction on belief base: {}".format(self.beliefs))
            #self.contraction(~formula_as_cnf, order)
            if self.contraction(~formula_as_cnf, order):
                self.expand_belief_base(formula, order)
            else:
                print("could not remove due to order")
            #print("resultatet er: {}".format(self.contraction(~formula_as_cnf, order)))
            print("Belief base after contraction ps jeg er sej: {}".format(self.beliefs))
        else:
            print("belief base: {} does not entail formula {} ".format(self.beliefs, ~formula_as_cnf))
            print("Adding belief formula: {}".format(formula_as_cnf))
            self.expand_belief_base(formula, order)
        print("BB som det ser ud nu: {}".format(self.beliefs))

    def remove_from_belief_base(self, formula, order):
        for belief in self.beliefs:
            if belief.formula == formula:
                self.beliefs.remove(belief)

    # TODO: find a way to identify the clauses that led to the creation of other clauses that led to
    # the compliment of the formula
    def contraction(self, formula, order):
        # Contraction is the removal of a belief and all other beliefs that could entail that belief
        # this means that 1) we have to remove the belief from the belief base
        # 2) we have to remove every belief that would entail the stated belief
        # We can do this by using the entail method to identify the clauses that would entail the formula
        #
        contraction_result = None
        cnf_formula = to_cnf(formula)
        print("beliefs før contraction: {}".format(sorted(self.beliefs)))
        for belief in self.beliefs:
            if cnf_formula == belief.formula:
                self.beliefs.remove(belief)
        entail_result = entail(self, cnf_formula)

        print("resultat: {}".format(entail_result[0]))
        print("resultat: {}".format(entail_result[1]))
        for key, value in entail_result[1].items():
            print("keys: {}, value: {}".format(key, value))
            key_holder = key
            for clause in value:
                print("formula: {} og clause: {}".format(formula, clause))
                if cnf_formula == clause:
                    for belief in self.beliefs:
                        if belief.formula == key_holder:
                            print("formular: {}".format(belief.formula))
                            print("belief: {}".format(belief))
                            #Only remove if order is less than order of what we intend to remove
                            if belief in self.beliefs and belief.order < order:
                                self.beliefs.remove(belief)
                                print("beliefs efter sucesfuld contraction: {}".format(sorted(self.beliefs)))
                                contraction_result = True
                            elif belief in self.beliefs and belief.order >= order:
                                print("Det fejler, fordi order er større. Order skal være MINDRE!")
                                print("beliefs efter fejlet contraction: {}".format(sorted(self.beliefs)))
                                contraction_result = False
                            else:
                                print("Mislykket contraction, fordi belief ikke er i belief base!!")
                                print("beliefs efter fejlet contraction: {}".format(sorted(self.beliefs)))
                                contraction_result = False
        return contraction_result

    def clear(self):
        self.beliefs.clear()

    # def is_close(self):


class Belief:
    def __init__(self, formula, order=None):
        self.formula = formula
        self.order = order

    def __lt__(self, other):
        return self.order < other.order

    def __eq__(self, other):
        return self.order == other.order and self.formula == other.formula

    def __repr__(self):
        return f'Belief({self.formula}, order={self.order})'
