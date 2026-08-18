groupPlot = {}

groupPlot['DY']  = {  
    'nameHR'   : 'DY',
    'isSignal' : 0,
    'color'    : 418, #kGreen+4
    'samples'  : ['DY']
}

groupPlot['top']  = {
    'nameHR'   : 'top',
    'isSignal' : 0,
    'color'    : 400,
    'samples'  : ['top']
}

groupPlot['WZ']  = {
    'nameHR'   : 'WZ',
    'isSignal' : 0,
    'color'    : 619,
    'samples'  : ['WZ']
}

groupPlot['ZZ']  = {
    'nameHR'   : 'ZZ',
    'isSignal' : 0,
    'color'    : 617,
    'samples'  : ['ZZ']
}

groupPlot['Fake']  = {
    'nameHR' : 'nonprompt',
    'isSignal' : 0,
    'color': 921,    # kGray + 1
    'colorPlt': "#778899",
    'samples'  : ['Fake']
}
##########SIGNAL#############
'''
groupPlot['WW']  = {
    'nameHR'   : 'WW',
    'isSignal' : 0,
    'color'    : 851,
    'samples'  : ['WW','ggWW']
}
'''
groupPlot['WW'] = {
    'nameHR': 'qqWW fiducial',
    'isSignal': 1,
    'color': 851,
    'samples': ['WW_B0', 'WW_B1', 'WW_B2', 'WW_B3']
}

groupPlot['ggWW'] = {
    'nameHR': 'ggWW fiducial',
    'isSignal': 1,
    'color': 632,
    'samples': ['ggWW_B0', 'ggWW_B1', 'ggWW_B2', 'ggWW_B3']
}


groupPlot['WW_nonfid'] = {
    'nameHR': 'qqWW nonfiducial',
    'isSignal': 0,
    'color': 418,
    'samples': ['WW_nonfid']
}
groupPlot['ggWW_nonfid'] = {
    'nameHR': 'ggWW nonfiducial',
    'isSignal': 0,
    'color': 419,
    'samples': ['ggWW_nonfid']
}

############################

#groupPlot['WW']  = {
#    'nameHR'   : 'WW',
#    'isSignal' : 1,
#    'color'    : 851,
#    'samples'  : ['WW']
#}

groupPlot['VVV']  = {  
    'nameHR' : 'VVV',
    'isSignal' : 0,
    'color': 857, # kAzure -3
    'colorPlt': "#4b0082",
    'samples'  : ['VVV']
}

groupPlot['Vg']  = {  
    'nameHR' : "$V\gamma$",
    'isSignal' : 0,
    'color'    : 810,   # kOrange + 10
    'colorPlt': "#e76300",
    'samples'  : ['Vg', 'VgS']
}

groupPlot['ggF']  = {
    'nameHR' : "ggF",
    'isSignal' : 0,
    'color'    : 623,
    'colorPlt': "",
    'samples'  : ['ggH_hww']
}

groupPlot['VBF']  = {
    'nameHR' : "VBF",
    'isSignal' : 0,
    'color'    : 600,
    'colorPlt': "",
    'samples'  : ['qqH_hww']
}

plot = {}


plot['DY']  = {  
    'color'    : 418,    # kGreen+2
    'isSignal' : 0,
    'isData'   : 0, 
    'scale'    : 1.0,
}

plot['Fake']  = {
    'color': 921,    # kGray + 1
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['top']  = {
    'color'    : 400,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}
###########SIGNAL############
'''
plot['WW']  = {
    'color'    : 851,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ggWW']  = {
    'color'    : 851,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}
'''
#################################
########FIDUCIAL#################


# plot.py

# --- WW ---

plot['WW_nonfid'] = {
    'color': 851,
    'isSignal': 0,   # stacked as background
    'isData': 0,
    'scale': 1.0
}

for i in range(4):

    plot[f'WW_B{i}'] = {
        'color': 851,
        'isSignal': 1,   # drawn as signal overlay
        'isData': 0,
        'scale': 1.0    # optional: enlarge for visibility
    }

# --- ggWW ---

plot['ggWW_nonfid'] = {
    'color': 632,
    'isSignal': 0,
    'isData': 0,
    'scale': 1.0
}

for i in range(4):

    plot[f'ggWW_B{i}'] = {
        'color': 632,
        'isSignal': 1,
        'isData': 0,
        'scale': 1.0
    }



##############################



plot['Vg']  = { 
    'color': 859,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['VgS']  = { 
    'color'    : 859, # kAzure -1  
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['WZ']  = {
    'color'    : 619,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['ZZ']  = {
    'color'    : 617,
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

plot['VVV']  = { 
    'color': 857, # kAzure -3  
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['qqH_hww'] = {
    'nameHR' : 'qqH',
    'color': 632+1, # kRed+1 
    'isSignal' : 0,
    'isData'   : 0,    
    'scale'    : 1    #
}

plot['ggH_hww'] = {
    'nameHR' : 'ggH',
    'color': 632, # kRed 
    'isSignal' : 0,
    'isData'   : 0,    
    'scale'    : 1    #
}

# data
'''
plot['DATA']  = { 
    'nameHR'   : 'Data',
    'color'    : 1 ,  
    'isSignal' : 0,
    'isData'   : 1 ,
    'isBlind'  : 0
}

'''
# Legend definition
legend = {}
legend['lumi'] = 'L = 109.0 fb^{-1}'
legend['sqrt'] = '#sqrt{s} = 13.6 TeV'
