'''

Ntuple branch template sets for tau objects.

Each string is transformed into an expression on a FinalStateEvent object.

{object} should be replaced by an expression which evaluates to a pat::Muon
i.e. daughter(1) or somesuch.

Author: Evan K. Friis

'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

info = PSet(
    objectGenDecayMode = '{object}.userInt("genDecayMode")',
    objectLeadTrackPt = '{object}.userFloat("ps_ldTrkPt")',
    objectDecayMode = '{object}.decayMode',
    objectTNPId = '{object}.userInt("ps_sel_nom")',
)

# ID and isolation
id = PSet(

    #Against Electron
    #STD
    objectAntiElectronLoose  = '{object}.tauID("againstElectronLoose")',
    objectAntiElectronMedium = '{object}.tauID("againstElectronMedium")',
    objectAntiElectronTight  = '{object}.tauID("againstElectronTight")',
    #MVA
##    objectAntiElectronMVA = '{object}.tauID("againstElectronMVA")',
    #MVA2
##    objectAntiElectronMVA2Vloose = '{object}.tauID("againstElectronVLooseMVA2")',
##    objectAntiElectronMVA2Loose  = '{object}.tauID("againstElectronLooseMVA2")',
##    objectAntiElectronMVA2Medium = '{object}.tauID("againstElectronMediumMVA2")',
##    objectAntiElectronMVA2Tight  = '{object}.tauID("againstElectronTightMVA2")',
    #MVA3
    objectAntiElectronMVA3Loose  = '{object}.tauID("againstElectronLooseMVA3")',
    objectAntiElectronMVA3Medium = '{object}.tauID("againstElectronMediumMVA3")',
    objectAntiElectronMVA3Tight  = '{object}.tauID("againstElectronTightMVA3")',
    objectAntiElectronMVA3VTight = '{object}.tauID("againstElectronVTightMVA3")',

    #Against Muon
    objectAntiMuonLoose  = '{object}.tauID("againstMuonLoose")',
    objectAntiMuonMedium = '{object}.tauID("againstMuonMedium")',
    objectAntiMuonTight  = '{object}.tauID("againstMuonTight")',
    #v2
    objectAntiMuonLoose2  = '{object}.tauID("againstMuonLoose2")',
    objectAntiMuonMedium2 = '{object}.tauID("againstMuonMedium2")',
    objectAntiMuonTight2  = '{object}.tauID("againstMuonTight2")',

    #ISO
    objectDecayFinding = '{object}.tauID("decayModeFinding")',
    #STD
    objectVLooseIso = '{object}.tauID("byVLooseCombinedIsolationDeltaBetaCorr")',
    objectLooseIso  = '{object}.tauID("byLooseCombinedIsolationDeltaBetaCorr")',
    objectMediumIso = '{object}.tauID("byMediumCombinedIsolationDeltaBetaCorr")',
    objectTightIso  = '{object}.tauID("byTightCombinedIsolationDeltaBetaCorr")',
    #3hits
    objectLooseIso3Hits  = '{object}.tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits")',
    objectMediumIso3Hits = '{object}.tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits")',
    objectTightIso3Hits  = '{object}.tauID("byTightCombinedIsolationDeltaBetaCorr3Hits")',
    #MVA
    objectLooseMVAIso  = '{object}.tauID("byLooseIsolationMVA")',
    objectMediumMVAIso = '{object}.tauID("byMediumIsolationMVA")',
    objectTightMVAIso  = '{object}.tauID("byTightIsolationMVA")',
    #MVA2
    objectLooseMVA2Iso  = '{object}.tauID("byLooseIsolationMVA2")',
    objectMediumMVA2Iso = '{object}.tauID("byMediumIsolationMVA2")',
    objectTightMVA2Iso  = '{object}.tauID("byTightIsolationMVA2")',

    objectGenEnergy      = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).energy() : -999',
    objectGenPt          = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).pt() : -999',
    objectGenPx          = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).px() : -999',
    objectGenPy          = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).py() : -999',
    objectGenPz          = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).pz() : -999',
    objectGenEta         = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).eta() : -999',
    objectGenPhi         = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).phi() : -999',
    objectGenMotherPdgId = '? (getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isAvailable && getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticleMotherSmart({object_idx}, 15, 0).pdgId() : -999',
    objectGenMotherPt =  '? (getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isAvailable && getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticleMotherSmart({object_idx}, 15, 0).pt() : -999', 
    objectGenMotherEnergy =  '? (getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isAvailable && getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticleMotherSmart({object_idx}, 15, 0).energy() : -999', 
    objectGenMotherEta =  '? (getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isAvailable && getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticleMotherSmart({object_idx}, 15, 0).eta() : -999', 
    objectGenMotherPhi =  '? (getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isAvailable && getDaughterGenParticleMotherSmart({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticleMotherSmart({object_idx}, 15, 0).phi() : -999', 

    objectComesFromHiggs = 'comesFromHiggs({object_idx}, 15, 1)',
    objectGenPdgId       = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).pdgId() : -999',
    objectGenCharge      = '? (getDaughterGenParticle({object_idx}, 15, 0).isAvailable && getDaughterGenParticle({object_idx}, 15, 0).isNonnull) ? getDaughterGenParticle({object_idx}, 15, 0).charge() : -999',


)
trigger = PSet(
    objectMatcheEle22WP90RhoTau20    = r'matchToHLTPath({object_idx}, "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v\\d+")',
    objectMatcheEle22WP90NoIsoTau20  = r'matchToHLTPath({object_idx},"HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v\\d+")',
    objectMatcheEle20CaloIdIsoRhoLooseIsotau20 = r'matchToHLTPath({object_idx},"Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v\\d+")',
    objectMatcheEle20CaloIdIsoMediumIsotau20 = r'matchToHLTPath({object_idx},"Ele20_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20\\d+")',
    objectMatcheEle18CaloIdIsoMediumIsotau20 = r'matchToHLTPath({object_idx},"Ele18_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20\\d+")',
    objectMatcheEle15CaloIdIsoTightIsotau20 = r'matchToHLTPath({object_idx},"Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TightIsoPFTau20\\d+")',
    objectMatcheEle15CaloIdIsoMediumIsotau20 = r'matchToHLTPath({object_idx},"Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20\\d+")',
    

)


