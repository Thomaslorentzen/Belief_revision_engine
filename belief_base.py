import math
import logging
from operator import neg

from sympy.logic.boolalg import to_cnf, And, Or, Equivalent
from sortedcontainers import SortedList


class Beliefbase:

    def __init__(self):
        self.beliefs = SortedList(key=lambda b: neg(b.order))

    def expand_belief_base(self, formula):
        order = 1
        formula_as_cnf = to_cnf(formula)
        new_belief = Belief(formula_as_cnf, order)
        for belief in self.beliefs:
            belief.order += 1
        self.beliefs.append(new_belief)

    def remove_from_belief_base(self, formula):
        for belief in self.beliefs:
            if belief.formula == formula:
                self.beliefs.remove(belief)


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
