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
    'Z*jets*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#FFCC66',
        'linecolor' : '#FFCC66',
        'name' : "DY + jets",
        'fillstyle': 'solid',
        },
    'Z*jets*LL' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#FFCC66',
        'linecolor' : '#FFCC66',
        'name' : "DY (#rightarrow ll)  + jets",
        'fillstyle': 'solid',
        },
    'Z*jets*TT' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#fa8795',
        'linecolor' : '#fa8795',
        'name' : "DY (#rightarrow #tau#tau)  + jets",
        'fillstyle': 'solid',
        },
    'Wplus*Jets*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#07a242',
        'linecolor' : '#07a242',
        'name' : "W + jets",
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
    'TT*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['cyan'],
        'linecolor' : colors['cyan'],
        'name' : "t#bar{t}",
        'fillstyle': 'solid',
    },
    'T*_t*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : '#9999CC',
        'linecolor' : '#9999CC',
        'name' : "Single Top",
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
        'fillcolor' : 0,
        'fillstyle' : 0,
        'linestyle' : 2,
        'linewidth' : 4,
        'linecolor' : '#1C1C76',
        'name' : "VH",
    },
    'WZ*ZToTauTau*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['red'],
        'linecolor' : colors['red'],
        'name' : "WZ#rightarrowl#tau#tau",
        'fillstyle': 'solid',
    },
    'WZ*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['red'],
        'linecolor' : colors['red'],
        'name' : "WZ#rightarrow3l",
        'fillstyle': 'solid',
    },
    'WW*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['red'],
        'linecolor' : colors['red'],
        'name' : "EWK Dibosons",
        'fillstyle': 'solid',
    },
    'ZZ*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'linecolor' : colors['red'],
        'fillcolor' : colors['red'],
        'name' : "ZZ",
        'fillstyle': 'solid',
    },
    'VBF_HToTauTau*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['blue'],
        'linecolor' : colors['blue'],
        'name' : "SM vbf Higgs",
        'fillstyle': 'solid',
    },
    'GluGluToHToTauTau*' : {
        'legendstyle' : 'f',
        'drawstyle' : 'hist',
        'fillcolor' : colors['blue'],
        'linecolor' : colors['blue'],
        'name' : "SM Higgs",
        'fillstyle': 'solid',
    },
    'data*' : {
        'legendstyle' : 'pe',
        'drawstyle' : 'pe',
        'markerstyle' : 20,
#        'markersize'  : 2,
        'name' : "Observed",
    },
    'ggHiggsToETau*' : {
        'legendstyle' : 'lp',
        'drawstyle' : 'hist',
        'linecolor' : 4,
        'linestyle' : 1,
        'linewidth' : 2,
        'name' : "LFV gg Higgs x10, BR = 0.1",
        'fillstyle': 'hollow',
    },
    'vbfHiggsToETau*' : {
        'legendstyle' : 'lp',
        'drawstyle' : 'hist',
        'linecolor' : 4,
        'linestyle' : 2,
        'linewidth' : 2,
        'name' : "LFV vbf Higgs x10, BR=0.1",
        'fillstyle': 'hollow',
    },

}

#Makes life easier when converting shape files
data_styles['fakes'] = data_styles['Z*jets*']
data_styles['zz'] = data_styles['ZZ*']
data_styles['wz'] = data_styles['WZ*']
data_styles['charge_fakes'] = data_styles['TT*']
