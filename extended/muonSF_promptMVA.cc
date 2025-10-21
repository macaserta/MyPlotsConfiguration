
#include <vector>
#include "TLorentzVector.h"
#include "correction.h"
#include "ROOT/RVec.hxx"
#include "TH2D.h"
#include "TFile.h"
#include <map>
#include <sstream>
#include <fstream>

using namespace ROOT;
using namespace ROOT::VecOps;

typedef std::map<std::string, std::map<std::string, std::string>> map_dict;

class muonSF_promptMVA{
public:
  
  correction::Correction::Ref cset_muon;  

  muonSF_promptMVA() {
    auto csetMu = correction::CorrectionSet::from_file("/afs/cern.ch/user/m/mcaserta/private/Production/mkShapesRDF/PlotsConfigurationsRun3_mayra/ControlRegions/MyPlotsConfiguration/extended/muonSF_latinos_promptMVA_2022.json");
    cset_muon = (correction::Correction::Ref)csetMu->at("NUM_TightID_HWW_LooseIso_tthMVA_DEN_LoosePFIso");    
  }

  std::vector<RVecF> operator()(RVecF Lepton_eta, RVecF Lepton_pt, RVecF Muon_pt, RVecF Muon_eta, RVecI Lepton_muonIdx, RVecI Lepton_pdgId){

    RVecF muonSF(Lepton_eta.size(), 1.0);
    RVecF muonSF_up(Lepton_eta.size(), 1.0);
    RVecF muonSF_do(Lepton_eta.size(), 1.0);

    double eta = 0.0;
    double pt = 0.0;		    

    for (unsigned int i=0; i<Lepton_pt.size(); i++){

      if (abs(Lepton_pdgId[i])==11){
	      continue;}
      else{
	eta = ROOT::VecOps::Max(ROOT::RVecF{ROOT::VecOps::Min(ROOT::RVecF{Muon_eta[Lepton_muonIdx[i]], 2.39}), -2.39});
	pt = ROOT::VecOps::Max(ROOT::RVecF{Muon_pt[Lepton_muonIdx[i]], 10.01});		
//	if (Lepton_pt[i] > 1e6) {
//		pt = Muon_pt[Lepton_muonIdx[i]];
//         }

//	pt = ROOT::VecOps::Max(ROOT::RVecD{pt, 10.01});
//	if (Muon_eta[Lepton_muonIdx[i]] == Lepton_eta[i]){
//
//		continue;}
//	else {
//	std::cout << "[ Lepton_pdgId " <<  Lepton_pdgId[i] << "] "
//			<< "Index" <<  Lepton_muonIdx[i]
 //                         << "eta after smearing=" << Lepton_eta[i]
  //                 //	  << " pt=" << Lepton_pt[i]
   //                       << " Muon_eta original=" << Muon_eta[Lepton_muonIdx[i]]
  //                 //       << " Muon_pt original" << Muon_pt[Lepton_muonIdx[i]]
   //                       << std::endl;
    //            }
	
        muonSF[i] = cset_muon->evaluate({eta, pt, "nominal"});
        float tmp_stat = cset_muon->evaluate({eta, pt, "stat"});
	float tmp_syst = cset_muon->evaluate({eta, pt, "syst"});
        float tmp_var = muonSF[i] * TMath::Sqrt( (tmp_stat/muonSF[i])*(tmp_stat/muonSF[i]) + (tmp_syst/muonSF[i])*(tmp_syst/muonSF[i]) );
        muonSF_up[i] = muonSF[i] + tmp_var;
        muonSF_do[i] = muonSF[i] - tmp_var;
      }
    }
  // else if(abs(Lepton_pdgId[i])==11){
//	std::cout << "[ELECTRON INDEX " << i << "] "
//		 << std::endl;

//   }

    std::vector<RVecF> result =	{muonSF,muonSF_up,muonSF_do};
    return result;
  }
};

