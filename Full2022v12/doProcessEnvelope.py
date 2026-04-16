#!/usr/bin/env python                                                                                                                                                                                                                                                           

import sys
import optparse
import copy
import collections
import os.path
import math
import logging
import tempfile
import subprocess
import fileinput
import argparse
from sys import argv
import ROOT

######
######
######

filename = "/eos/user/m/mcaserta/mkShapesRDF_rootfiles/2026__WW_2022_def_4March/rootFile/mkShapes__2026__WW_2022_def_4March.root "

######
######
######

from mkShapesRDF.shapeAnalysis.ConfigLib import ConfigLib
configsFolder = "configs"
ConfigLib.loadLatestPickle(os.path.abspath(configsFolder), globals())
print(dir())
print(globals().keys())


cuts = cuts["cuts"]
inputFile = outputFolder + "/" + outputFile

ROOT.TH1.SetDefaultSumw2(True)

import mkShapesRDF.shapeAnalysis.latinos.LatinosUtils as utils

subsamplesmap = utils.flatten_samples(samples)
categoriesmap = utils.flatten_cuts(cuts)

from mkShapesRDF.shapeAnalysis.histo_utils import postProcessNuisances

nuisances_to_process = {}
for nuisance in nuisances.keys():
    if not (
            nuisances[nuisance].get("kind", "").endswith("envelope")
            or nuisances[nuisance].get("kind", "").endswith("rms")
            or nuisances[nuisance].get("kind", "").endswith("square")
    ):
        continue

    nuisances_to_process[nuisance] = nuisances[nuisance]

print("Nuisances to postprocess:")
print(nuisances_to_process.keys())
print("\n")

for nuisance in nuisances_to_process:
    print(nuisance)
    tmp_nuisance = {}
    tmp_nuisance[nuisance] = nuisances_to_process[nuisance]
    postProcessNuisances(filename, samples, aliases, variables, cuts, tmp_nuisance)


[mcaserta@lxplus947 Full2022v12]$ cuts = {}

_tmp = [
    #'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'Lepton_pt[0] > 25.',
    'Lepton_pt[1] > 10.',
    '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.)',
    '(nLepton >= 2 && Alt(Lepton_pt,2, 0) < 10.)',
    'ptll>15',
    'mll > 12',
    '(zeroJet || Sum(CleanJet_pt>30.0)<=3)',
    'noJetInHorn_pT30'
]

preselections = ' && '.join(_tmp)

cuts['Zee']  = {
   'expr' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11) && mll > 60 && mll < 120',
   'categories' : {
       '0j' : 'zeroJet',
       '1j' : 'oneJet && Alt(CleanJet_pt,1,0)<30',
       '2j' : 'multiJet',
       'Inc' : '1',
  }
}

cuts['Zmm']  = {
    'expr' : '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13) && mll > 60 && mll < 120',
    'categories' : {
        '0j' : 'zeroJet',
        '1j' : 'oneJet && Alt(CleanJet_pt,1,0)<30',
        '2j' : 'multiJet',
        'Inc' : '1',
    }
}

