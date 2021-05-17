import logging
import argparse
import entailment

from sympy import *
from belief_base import Belief_Base

u_input = ">>>"


# TODO:
# Write user input instructions for the user
# Ensure all methods convert to cnf
# Expand database but notify user that no logical check will verify validity
#
#
#

def initial_message():
    print("Welcome to belief base revision!")
    print(
        f"""Actions available:
        p = print base
        r = revise
        con = contract
        c = clear belief base
        h = help
        q = quit
        """)
    print("select an action: ")


def input_handler(belief_base):
    initial_message()
    action = input(u_input)
    action = action.lower()

    input_running = True
    while input_running:
        if action == "e":
            print("insert value(s) to add to your belief base")
            formula = input(u_input)
            print("Give an order, or default will be chosen")
            print("For default, press Enter")
            # Future work: Limit inputs to integers
            order = input(u_input)
            if order == "":
                order = 1
            try:
                belief_base.expand_belief_base(formula, int(order))
            except SympifyError:
                print("Invalid formula!")
            except ValueError:
                print("Order has to be a number or blank for default to be chosen!")
            print("added formula: {} with order: {} ".format(formula, order))
        elif action == "c":
            belief_base.clear()
        elif action == "con":
            try:
                formula = input("Write a formula to contract")
                print("Belief base after contraction with formula {} ".format(formula))
                order = input("write an order, or default will be chosen")
                if order == "":
                    order = 1
                belief_base.contraction(formula, int(order))
                print("Belief base after contraction with formula {} ".format(formula))
                print(belief_base)
            except SympifyError:
                print("Invalid formula!")
            except ValueError:
                print("Order has to be a number or blank for default to be chosen!")
        elif action == "q":
            input_running = false
            exit()
        elif action == "h":
            initial_message()
        elif action == "p":
            for belief in bb.beliefs:
                print(belief.formula, " order: {}".format(belief.order))
        elif action == "r":
                formula = input("Write a formula to revise belief base with")
                order = input("write an order, or default will be chosen")
                if order == "":
                    order = 1
                try:
                    belief_base.revise(formula, int(order))
                    print("Revised belief base: {}".format(belief_base, order))
                except SympifyError:
                    print("Invalid formula!")
                except ValueError:
                    print("Order has to be a number or blank for default to be chosen!")
        else:
            print("invalid user input. Press h for for help")
            print()

        input_handler(bb)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Belief base revision CLI tool.')
    parser.add_argument('--debug', action='store_true', help='enable debugging')
    args = parser.parse_args()

    bb = Belief_Base()
    input_handler(bb)
