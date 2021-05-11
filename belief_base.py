import math
import logging
from operator import neg

from sympy.logic.boolalg import to_cnf, And, Or, Equivalent
from sortedcontainers import SortedList

from entailment import entail
from utils import associate


class Beliefbase:

    def __init__(self):
        self.beliefs = SortedList(key=lambda b: neg(b.order))
        self.sorting_queue = []

    def add_sorting_queue(self, belief, order):
        self.sorting_queue.append((belief, order))

    def run_sorting_queue(self):
        for belief, order in self.sorting_queue:
            self.beliefs.remove(belief)
            if order >= 0:
                belief.order = order
                self.beliefs.add(belief)
        self.sorting_queue = []

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

    def clear(self):
        self.beliefs.clear()


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
