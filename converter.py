# -*- coding: utf-8 -*-
"""
LING571 HW2

# This is a class used to convert CFG to CNF
# converter.py

Created on Thu Jan 23 22:16:23 2014

@author: haotianhe
"""

import sys

productions = {}

def convert(cfg, cnf):
    
    global productions
    reserves, singnter, mixrules, lonrules = sort(cfg)

    addrules(mixrules)


def addrules(mixrules):

    global productions

    for i in len(mixrules):


def sort(cfg):
    
    reserves = []
    singnter = []
    mixrules = []
    lonrules = []
    
    init_appr = True

    for line in cfg.readlines():

        if '->' in line:
            line = line.split('->')

            lhs = line[0].split()
            left = line[0].strip()
            
            rhs = line[1:][0].split()
            right = line[1:][0].strip()
            
            rule = lhs + rhs

            if not "'" in right:
                if len(rhs) == 2:
                    reserves.append(rule)
                elif len(rhs) == 1:
                    singnter.append(rule)
                else:
                    lonrules.append(rule)
            elif len(rhs) == 1:
                reserves.append(rule)
            else:
                mixrules.append(rule)

        else:
            continue

    return reserves, singnter, mixrules, lonrules




if __name__ == "__main__":

    if (len(sys.argv) == 2):
        cfg_path = sys.argv[0]
        cnf_path = sys.argv[1]
    else:
        cfg_path = "grammar.cfg"
        cnf_path = "grammar.cnf"

    cfg = open(cfg_path, 'r')
    cnf = open(cnf_path, 'a')

    convert(cfg, cnf)

    cfg.close()
    cnf.close()
