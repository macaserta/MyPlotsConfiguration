cuts = {}

_tmp = [
    #'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    #preselection paper WW 2022
    'Lepton_pt[0] > 25.',
    'Lepton_pt[1] > 20.',
   # '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.)',
    '(nLepton >= 2 && Alt(Lepton_pt,2, 0) < 10.)', #to suppress backgrounds from WZ and ZZ processes
    #'ptll>15',
    #To reduce top quark background contributions, events with one or more b-tagged jets are rejected.
    #'mll > 85', #to reject Z → 𝜏+𝜏− and Higgs boson background events
    #'(zeroJet || Sum(CleanJet_pt>30.0)<=3)',
    'noJetInHorn_pT30'
]

preselections = ' && '.join(_tmp)


cuts['SR'] = {
    'expr': 'mll > 85 && bVeto && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'categories' : {
        '0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0 && Lepton_pt[1]>=20',
        '1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0 && Lepton_pt[1]>=20',
        '2j' : 'Sum(CleanJet_pt>30.0)==2',
        'maj3j' : 'Sum(CleanJet_pt>30.0)>=3',
        'Inc': 'mll>12',
    }
}

cuts['TopCR']  = {
   'expr' : 'mll > 85 && ( ((zeroJet && !bVeto) || bReq1)  || bReq2 ) && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
   'categories' : {
       '0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0',
       '1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0',
       '2j' : 'Sum(CleanJet_pt>30.0)==2',
       'maj3j' : 'Sum(CleanJet_pt>30.0)>=3',
       'Inc': 'mll>12',
   }
}


cuts['TopCR_bReq2']  = {
   'expr' : 'mll > 85 && bReq2  && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
   'categories' : {
       '0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0',
       '1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0',
       '2j' : 'Sum(CleanJet_pt>30.0)==2',
       'maj3j' : 'Sum(CleanJet_pt>30.0)>=3',
       'Inc': 'mll>12',
   }
}


cuts['TopCR_bReq1']  = {
   'expr' : 'mll > 85 && ((zeroJet && !bVeto) || bReq1) && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
   'categories' : {
       '0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0',
       '1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0',
       '2j' : 'Sum(CleanJet_pt>30.0)==2',
       'maj3j' : 'Sum(CleanJet_pt>30.0)>=3',
       'Inc': 'mll>12',
   }
}


cuts['DYtautauCR']  = {
   'expr' : 'ptll<30 && mll < 85 && bVeto && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
   'categories' : {
       '0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0',
       '1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0',
       '2j' : 'Sum(CleanJet_pt>30.0)==2',
       'maj3j' : 'Sum(CleanJet_pt>30.0)>=3',
       'Inc': 'mll>12',
   }
}

cuts['nopromptCR'] = {
    'expr': 'bVeto && mll>85 && Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13',
    'categories' : {
        'Inc': 'mll>12',
        '0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0',
        '1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0',
        '2j' : 'Sum(CleanJet_pt>30.0)==2',
        'maj3j' : 'Sum(CleanJet_pt>30.0)>=3',

    }
}
