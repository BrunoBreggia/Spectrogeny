from BioSequence import DnaSeq
import numpy as np
from Matrix import Matrix

###################################################################
# 'Cumulative Fourier Power and Phase Spectra' method 
###################################################################

def CFPPS(dna:DnaSeq):
    """ Calculates the caracteristic 28-vector of the DNA sequence passed """

    # 1.Create indicator function
    indicators = {'A':None, 'C':None, 'G':None, 'T':None}
    for base in indicators.keys():
        indicators[base] = np.array([1 if char == base else 0 for char in str(dna)])

    # 2.DFT and cumulative power and phase spectra
    cumulativeSpectra = {'A':None, 'C':None, 'G':None, 'T':None}
    for base, baseIndex in indicators.items():
        # Discrete Fourier Transform:
        transform = np.fft.fft(baseIndex, len(baseIndex))
        # Power Spectrum:
        PS = np.absolute(transform)**2
        # Phase Spectrum:
        AS = np.angle(transform)
        # Cumulative Power Sepctrum:
        CumulativePS = np.array( [np.sum(PS[1:i]) for i in range(1,len(PS))] )
        # Cumulative Phase Sepctrum:
        CumulativeAS = np.array( [np.sum(AS[1:i]) for i in range(1,len(AS))] )
        # Assign to dict
        cumulativeSpectra[base] = (CumulativePS, CumulativeAS)

    # 3.Central Moment Vector
    CPS, CAS = 0, 1 # Descriptive indices
    momentVector = []
    means = {'A':None, 'C':None, 'G':None, 'T':None}
    baseCounts = {}
    bs, qty = np.unique( np.array( [nuc for nuc in str(dna)] ) , return_counts=True)
    for i in range(len(bs)):
        baseCounts[bs[i]] = qty[i]

    ########################################################################################
    def calculateCentralMoment(items, N_base, N_total, mean, cumulative_spectrum):
        n, N = N_base, N_total
        return_vector = [0]*items
        for i in range(1,items+1):
            scaleFactor = (N**i) * (n*(N-n))**(i-1)
            accumulation = np.sum( np.absolute(cumulative_spectrum-mean)**i )
            return_vector[i-1] = accumulation/scaleFactor
        return return_vector
    ########################################################################################

    for base in baseCounts.keys():
        meanCPS = np.sum(cumulativeSpectra[base][CPS]) / (len(cumulativeSpectra[base][CPS]))
        meanCAS = np.sum(cumulativeSpectra[base][CAS]) / (len(cumulativeSpectra[base][CAS]))
        cm1_base, cm2_base = calculateCentralMoment(2, baseCounts[base], len(dna), meanCPS, cumulativeSpectra[base][CPS])
        # Add elements to the moment vector
        momentVector += [meanCPS, meanCAS, cm1_base, cm2_base]
        means[base] = (meanCPS, meanCAS)
    # 4.Add Covariances
    COV_cps = {}
    COV_cas = {}
    N = len(dna)

    ########################################################################################
    def cov(cs1, mean_cs1, cs2, mean_cs2):
        length = len(cs1)
        add_up = np.sum( np.absolute(cs1 - mean_cs1) * np.absolute(cs2 - mean_cs2) )
        return add_up/length
    ########################################################################################
    
    for base1 in dna.alphabet():
        for base2 in dna.alphabet():
            if base1 != base2 and (base2,base1) not in COV_cps.keys():
                N_suma = (baseCounts[base1] + baseCounts[base2])/2
                COV_cps[base1, base2] = (N-1) / (N**2 * N_suma * (N-N_suma) ) * \
                    cov(cumulativeSpectra[base1][CPS], means[base1][CPS], cumulativeSpectra[base2][CPS], means[base2][CPS])
                COV_cas[base1, base2] = (N-1) / (N**2 * N_suma * (N-N_suma) ) * \
                    cov(cumulativeSpectra[base1][CAS], means[base1][CAS], cumulativeSpectra[base2][CAS], means[base2][CAS])
                # Add to the moment vector
                momentVector += [COV_cps[base1, base2], COV_cas[base1, base2]]

    return np.array(momentVector)
