import numpy as np
import pandas as pd

def RunPrep(flagD,Vn,model, f_genereg, f_omics):
    # Read-in the omics data and assign concentrations of genes
    gExp_mpc = np.float64(f_omics.values[:,0])
    mExp_mpc = np.float64(f_omics.values[:,1]) # mRNA molecule copy number per cell (mpc)
    kGin = np.float64(f_omics.values[:,2])
    kGac = np.float64(f_omics.values[:,3])
    kTCleak = np.float64(f_omics.values[:,4])
    kTCmaxs = np.float64(f_omics.values[:,5])
    kTCd = np.float64(f_omics.values[:,6])

    # Read-in the activators matrix and assign concentrations of activators
    TARs0 = (f_genereg.astype(str).values) # Transcriptional Activator Regulator matrix
    numberofTARs = len(f_genereg.columns)
    spnames = [ele for ele in model.getStateIds()]
    spIDs = []
    for qq in range(numberofTARs):
        sps = spnames.index(f_genereg.columns[qq]) 
        spIDs.append(sps)
    f_genereg = None
    
    numberofgenes = int(len(gExp_mpc))

    mExp_mpc = correctCellCycleGenes(f_omics, mExp_mpc)

    ss = int(sum(gExp_mpc))
    GenePositionMatrix = np.zeros((numberofgenes,ss))
    ind = 0
    for i in range(numberofgenes):
        GenePositionMatrix[i, ind:ind+int(gExp_mpc[i])] = 1.0
        ind = ind + int(gExp_mpc[i])

    # xg Deterministic
    xgac_mpc_D = (kGac*gExp_mpc)/(kGin+kGac) #active genes initial condition
    xgin_mpc_D = gExp_mpc - xgac_mpc_D #inactive genes initial condition

    # xg Stochastic
    AllGenesVec = np.zeros(shape = (ss,1))
    IndsGenesOn = np.random.choice(ss, size=int(round(ss*kGac[0]/kGin[0])), replace=False)
    AllGenesVec[IndsGenesOn] = 1.0

    # Calculate Concentration of Active and Inactive Genes for each gene
    xgac_mpc = np.dot(GenePositionMatrix,AllGenesVec)
    xgac_mpc = xgac_mpc.ravel()
    xgin_mpc = gExp_mpc-xgac_mpc
    xgin_mpc = xgin_mpc.ravel()

    genedata = []
    if flagD==1:
        genedata = np.concatenate((xgac_mpc_D, xgin_mpc_D), axis=None)
    else:
        genedata = np.concatenate((xgac_mpc, xgin_mpc), axis=None)
    
    # Gene switching constants
    kGin_1 = kGin[0]
    kGac_1 = kGac[0]
    
    tcnas = np.ones((numberofgenes, numberofTARs))
    tck50as = np.zeros((numberofgenes, numberofTARs))
    tcnrs = np.ones((numberofgenes, numberofTARs))
    tck50rs = np.zeros((numberofgenes, numberofTARs))
    for qq in range(numberofgenes):
        for ww in range(numberofTARs):
            pars = TARs0[qq,ww].find(';')
            if pars>0:
                nH = np.float64(TARs0[qq,ww][0:pars])
                kH = np.float64(TARs0[qq,ww][pars+2::])
                if nH>0:
                    tcnas[qq,ww] = nH
                    tck50as[qq,ww] = kH
                else:
                    tcnrs[qq,ww] = abs(nH)
                    tck50rs[qq,ww] = kH

    mpc2nmcf_Vn = 1.0E9/(Vn*6.023E+23)
    # Convert to molecules per cell
    tck50as = tck50as*(1/mpc2nmcf_Vn)
    tck50rs = tck50rs*(1/mpc2nmcf_Vn)
    
    return genedata, GenePositionMatrix, AllGenesVec, kTCmaxs, kTCleak, kGin_1, kGac_1, kTCd, TARs0, tcnas, tcnrs, tck50as, tck50rs, spIDs 


def correctCellCycleGenes(f_omics: pd.DataFrame, mExp_mpc: np.array) -> np.array:
    '''
    Corrects specific cell cycle genes to display determinstic behavior. Eventual
    updates to the cell cycle components will render this function obsolete.

    Parameters
    - f_omics (pd.DataFrame): The omics data
    - mExp_mpc (np.array): The mRNA molecule copy number per cell
    
    Returns
    - mExp_mpc (np.array): The mRNA molecule copy number per cell
    '''
    indsDm = ['RB1', 'E2F1', 'E2F2', 'E2F3', 'CCND1', 'CCNE2', 'SKP2',
            'CDC25A', 'CDC25B', 'CDC25C', 'CCNA2', 'CDKN1B', 'CDH1',
            'CCNB1', 'CDC20', 'WEE1', 'CHEK1']
    for gene in indsDm:
        if gene in f_omics.index:
            gene_index = f_omics.index.get_loc(gene)
            mExp_mpc[gene_index] = 17.0

    return mExp_mpc
