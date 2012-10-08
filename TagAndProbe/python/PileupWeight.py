'''

Class which figures out the correct PU weight.
Takes as input a MC PU tag (i.e. 'S7') and a set of .root files with the
pileup distributions (generated by pileupCalc.py [1])

[1] https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData

Author: Evan K. Friis, UW

'''

import array
from FinalStateAnalysis.Utilities.FileInPath import FileInPath
import ROOT

# MC distributions (built at bottom of file)
_MC_PU_DISTRIBUTIONS = {}

class PileupWeight(object):
    def __init__(self, mctag, *datafiles):
        '''
        Build a PU weight object.

        [mctag] must reflect the PU distribution used in simulation and
        currently be either 'S6' or 'S10'.

        [datafiles] is a list of .root files generated a la

        https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData

        Note that for 7TeV data there must be 500 bins (0-50) and for 8TeV there
        should 600 bins (0-60)

        '''
        self.data = None
        for filename in datafiles:
            file = ROOT.TFile.Open(filename)
            pu = file.Get('pileup')
            if self.data is None:
                self.data = pu.Clone()
                self.data.SetDirectory(0)
            else:
                self.data.Add(pu)
            file.Close()

        # Normalize
        self.data.Scale(1./self.data.Integral())

        if not mctag in _MC_PU_DISTRIBUTIONS:
            raise KeyError("Unknown PU distribution %s, allowed: %s" %
                           (mctag, " ".join(_MC_PU_DISTRIBUTIONS.keys())))

        mc_base = ROOT.TFile.Open(_MC_PU_DISTRIBUTIONS[mctag]).Get('pileup')
        self.mc = mc_base.Clone()

        # Make sure bins are consistent
        if not ROOT.TEfficiency.CheckBinning(self.mc, self.data):
            raise ValueError("Data and MC PU histograms "
                             "do not have the same binning!")

        # Normalize MC
        self.mc.Scale(1./self.mc.Integral())

    def __call__(self, ntruepu):
        '''
        Get the PU weight given the true number of interactions
        '''
        bin = self.data.FindBin(ntruepu)
        data = self.data.GetBinContent(bin)
        mc = self.mc.GetBinContent(bin)
        if mc:
            return data/mc
        else:
            return 1.0

_MC_PU_DISTRIBUTIONS['S10'] = FileInPath("FinalStateAnalysis/TagAndProbe/data/MC_Summer12_PU_S10-600bins.root")
_MC_PU_DISTRIBUTIONS['S7'] = None
_MC_PU_DISTRIBUTIONS['S6'] = FileInPath("FinalStateAnalysis/TagAndProbe/data/MC_Fall11_PU_S6-500bins.root")
