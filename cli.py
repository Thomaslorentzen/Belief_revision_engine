import logging
import argparse


from sympy import to_cnf, SympifyError

u_input = ">>>"

def input(belief_base):
    print("Select an action: ")
    action = input(u_input)
    action = action.lower()

    if action == "r":
        form = to_cnf(form)
        