#!/bin/bash
set -o errexit
set -o nounset

HZZ=${HZZ:-0}

# Check CMSSW version
MAJOR_VERSION=`echo $CMSSW_VERSION | sed "s|CMSSW_\([0-9]\)_.*|\1|"`
MINOR_VERSION=`echo $CMSSW_VERSION | sed "s|CMSSW_\([0-9]\)_\([0-9]\)_.*|\2|"`


# Tags for 7XX

pushd $CMSSW_BASE/src

# HZZ MELA, MEKD etc.
if [ "$HZZ" = "1" ]; then
    echo "Checking out ZZ MELA and Higgs combine"
    git clone https://github.com/cms-analysis/HiggsAnalysis-ZZMatrixElement.git ZZMatrixElement
    pushd ZZMatrixElement
    git checkout -b from-V00-02-01-patch1 V00-02-01-patch1
    popd
    git clone -b 74x-root6 https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
fi

echo "Checking out material to run new tau MVA ID"
pushd $CMSSW_BASE/src
git cms-addpkg DataFormats/PatCandidates
git cms-addpkg PhysicsTools/PatAlgos
git cms-addpkg RecoTauTag/Configuration
git cms-addpkg RecoTauTag/RecoTau

git cms-addpkg RecoMET/METFilters
git cms-addpkg EgammaAnalysis/ElectronTools
git cms-addpkg RecoEgamma/EgammaTools
git cms-addpkg RecoEgamma/ElectronIdentification
git cms-addpkg RecoJets/JetProducers
git cms-addpkg SimDataFormats/HTXS

if [ "$MAJOR_VERSION" = "9" ] && [ "$MINOR_VERSION" < "4" ] ; then
    echo "until  the fix is merged a custum fix is needed (taken from ahinzmann)"
    git remote add taroniCMSSW https://github.com/taroni/cmssw.git
    git fetch taroniCMSSW
    git checkout taroniCMSSW/porting92X --  RecoJets/JetProducers/src/PileupJetIdAlgo.cc
fi

echo "Checking out mva met and svFit material:"
# svFit packaged checked out for everyone so that svFit code in FSA compiles
git clone git@github.com:veelken/SVFit_standalone.git TauAnalysis/SVfitStandalone
pushd TauAnalysis/SVfitStandalone
git checkout svFit_2015Apr03
popd


##Doesn't work. Need to clone and modify my version
pushd $CMSSW_BASE/src
git remote add cms-egamma git@github.com:cms-egamma/cmssw.git
git fetch cms-egamma
git checkout cms-egamma/EGM_94X_v1 -- EgammaAnalysis/ElectronTools
popd

cd EgammaAnalysis/ElectronTools/data
git clone https://github.com/ECALELFS/ScalesSmearings.git
cd - 

cd $CMSSW_BASE/src



popd

