'''

Define styles for the different data samples.

The keys correspond to "logical" samples, defined in data_name_map of
datadefs.py

The values are dictionaries, which can be passed as kwargs to objects which
inherit from rootpy Plottable


http://ndawe.github.com/rootpy/reference/rootpy.plotting.html#rootpy.plotting.core.Plottable

'''

from FinalStateAnalysis.Utilities.solarized import colors

data_styles = {
    'GluGlu_LFV_HToETau_M200*' : {
        'legendstyle' : 'l',
        'drawstyle' : 'hist',
        #'fillcolor' : '#ffc000',
        'linecolor' : '#ffc00',
        'linewidth' : 2,
        'name' : "M_{H} = 200 GeV (B=10%)"
        },
    'ggM300*' : {
        'legendstyle' : 'l',
        'drawstyle' : 'hist',
        #'fillcolor' : '#ff0000',
        'linecolor' : '#ff0000',
        'linewidth' : 2,
        'name' : "M_{H} = 300 GeV (B=10%)"
        },
    'ggM450*' : {
        'legendstyle' : 'l',
        'drawstyle' : 'hist',
        #'fillcolor' : '#3167a0',
        'linecolor' : '#3167a0',
        'linewidth' : 2,
        'name' : "M_{H} = 450 GeV (B=10%)"
        },
    'ggM600*' : {
        'legendstyle' : 'l',
        'drawstyle' : 'hist',
        #'fillcolor' : '#31a06b',
        'linecolor' : '#31a06b',
        'linewidth' : 2,
        'name' : "M_{H} = 600 GeV (B=10%)"
        },
    'ggM750*' : {
        'legendstyle' : 'l',
        'drawstyle' : 'hist',
        #'fillcolor' : '#a0319e',
        'linecolor' : '#a0319e',
        'linewidth' : 2,
        'name' : "M_{H} = 750 GeV (B=10%)"
        },
    'ggM900*' : {
        'legendstyle' : 'l',
        'drawstyle' : 'hist',
        #'fillcolor' : '#fe5e06',
        'linecolor' : '#fe5e06',
        'linewidth' : 2,
        'name' : "M_{H} = 900 GeV (B=10%)"
        },
    'DY*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#FFCC66',
        'linecolor' : '#FFCC66',
        'name' : "DY + jets",
        'fillstyle': 'solid',
        },
    'W*JetsToLNu*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#ff99ff',
        'linecolor' : '#ff99ff',
        'name' : "W + jets",
        'fillstyle': 'solid',
    },
    'fakes' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#ff99ff',
        'linecolor' : '#ff99ff',
        'name' : "mis-id #tau",
        'fillstyle': 'solid',
    },
    'QCD*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['cyan'],
        'linecolor' :colors['cyan'],
        'name' : "QCD",
        'fillstyle': 'solid',
    },
    'TT_*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#9999CC',
        'linecolor' : '#9999CC',
        'name' : "TT, singleT",
        'fillstyle': 'solid',
    },
    'VH*HWW' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['orange'],
        'linecolor' : colors['orange'],
        'name' : "VH H#rightarrowWW",
        'fillstyle': 'solid',
    },
    'VH*' : {
        'legendstyle' : 'l',
        'drawstyle' : 'hist',
        'fillcolor' : '#1C1C76',
        'fillstyle' : 0,
        'linestyle' : 2,
        'linewidth' : 4,
        'linecolor' : '#1C1C76',
        'name' : "VH",
    },
    'WZ*ZToTauTau*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#66cccc',
        'linecolor' : '#66cccc',
        'name' : "WZ#rightarrowl#tau#tau",
        'fillstyle': 'solid',
    },
    'GluGluHToTauTau_M125*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['blue'],
        'linecolor' : colors['blue'],
        'name' : "SM Higgs",
        'fillstyle': 'solid',
    },
    'WZ*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#66cccc',
        'linecolor' : '#66cccc',
        'name' : "WZ#rightarrow3l",
        'fillstyle': 'solid',
    },
    'WW*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#66cccc',
        'linecolor' : '#66cccc',
        'name' : "Dibosons",
        'fillstyle': 'solid',
    },
    'ZZ*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'linecolor' : '#66cccc',
        'fillcolor' : '#66cccc',
        'name' : "ZZ",
        'fillstyle': 'solid',
    },
    'EWK*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'linecolor' : '#50A634',
        'fillcolor' : '#50A634',
        'name' : "EWK Z and W",
        'fillstyle': 'solid',
    },
    'data*' : {
        'legendstyle' : 'pe',
        'drawstyle' : 'pe',
        'markerstyle' : 20,
#        'markersize'  : 2,
        'name' : "Observed",
    },
}

#makes life easier when converting shape files
#data_styles['fakes'] = data_styles['W*JetsToLNu*']
data_styles['zz'] = data_styles['ZZ*']
data_styles['wz'] = data_styles['WZ*']
data_styles['charge_fakes'] = data_styles['TT_*']
data_styles['ST*'] = data_styles['TT_*']
