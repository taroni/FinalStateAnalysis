# Embed IDs for jets
import FWCore.ParameterSet.Config as cms
import os

def preJets(process, jSrc, vSrc, mSrc, eSrc, **kwargs):
    postfix = kwargs.pop('postfix','')
    jType = kwargs.pop('jType','AK4PFchs')
    doBTag = kwargs.pop('doBTag',False)
    doFullJESUnc = kwargs.pop('doFullJESUnc',False)
    runningLocal = kwargs.pop('runningLocal',False)

    mod = cms.EDProducer(
        "MiniAODJetIdEmbedder",
        src=cms.InputTag(jSrc)
    )
    modName = 'miniPatJets{0}'.format(postfix)
    setattr(process,modName,mod)
    jSrc = modName

    pathName = 'runMiniAODJetEmbedding{0}'.format(postfix)
    setattr(process,pathName,cms.Path(getattr(process,modName)))
    process.schedule.append(getattr(process,pathName))

    # embed BTag SFs
    if doBTag :
        modName = 'miniJetsEmbedBTagSFLoose{0}'.format(postfix)
        mod = cms.EDProducer(
            "MiniAODJetBTagSFLooseEmbedder",
            src=cms.InputTag(jSrc)
        )
        jSrc = modName
        setattr(process,modName,mod)

        pathName = 'runMiniAODJetBTagSFLooseEmbedding{0}'.format(postfix)
        path = cms.Path(getattr(process,modName))
        setattr(process,pathName,path)
        process.schedule.append(getattr(process,pathName))

    # embed BTag SFs
    if doBTag :
        modName = 'miniJetsEmbedBTagSFMedium{0}'.format(postfix)
        mod = cms.EDProducer(
            "MiniAODJetBTagSFMediumEmbedder",
            src=cms.InputTag(jSrc)
        )
        jSrc = modName
        setattr(process,modName,mod)

        pathName = 'runMiniAODJetBTagSFMediumEmbedding{0}'.format(postfix)
        path = cms.Path(getattr(process,modName))
        setattr(process,pathName,path)
        process.schedule.append(getattr(process,pathName))

    # doFullJESUnc 
    if doFullJESUnc :
        # Provide proper path name for Jet Uncertainty file
        # V10 is most recent version for JES Uncertainties
        # https://hypernews.cern.ch/HyperNews/CMS/get/jes/642/1/1.html
        if runningLocal : fName = "../../NtupleTools/data/Spring16_25nsV10_DATA_UncertaintySources_AK4PFchs.txt" # recommended by JetMET
        else :
            cmsswversion=os.environ['CMSSW_VERSION']
            fName = "{0}/src/FinalStateAnalysis/NtupleTools/data/Spring16_25nsV10_DATA_UncertaintySources_AK4PFchs.txt".format(cmsswversion)

        modName = 'miniAODJetFullSystematicsEmbedding{0}'.format(postfix)
        mod = cms.EDProducer(
	    "MiniAODJetFullSystematicsEmbedder",
            src = cms.InputTag(jSrc),
            corrLabel = cms.string(jType),
            fName = cms.string(fName)
        )
        jSrc = modName
        setattr(process,modName,mod)

        pathName = 'jetFullSystematicsEmbedding{0}'.format(postfix)
        path = cms.Path(getattr(process,modName))
        setattr(process,pathName,path)
  
        process.schedule.append(getattr(process,pathName))

    # embed IP stuff
    modName = 'miniJetsEmbedIp{0}'.format(postfix)
    mod = cms.EDProducer(
        "MiniAODJetIpEmbedder",
        src = cms.InputTag(jSrc),
        vtxSrc = cms.InputTag(vSrc),
    )
    jSrc = modName
    setattr(process,modName,mod)

    pathName = 'runMiniAODJetIpEmbedding{0}'.format(postfix)
    path = cms.Path(getattr(process,modName))
    setattr(process,pathName,path)
    process.schedule.append(getattr(process,pathName))

    modName = 'miniAODJetSystematicsEmbedding{0}'.format(postfix)
    mod = cms.EDProducer(
	"MiniAODJetSystematicsEmbedder",
        src = cms.InputTag(jSrc),
        corrLabel = cms.string(jType)
    )
    jSrc = modName
    setattr(process,modName,mod)

    pathName = 'jetSystematicsEmbedding{0}'.format(postfix)
    path = cms.Path(getattr(process,modName))
    setattr(process,pathName,path)
  
    process.schedule.append(getattr(process,pathName))

    return jSrc

