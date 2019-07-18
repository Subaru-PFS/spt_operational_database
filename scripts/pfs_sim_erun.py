from builtins import object
import numpy as np
import time

import sys
from pfs.datamodel.pfsConfig import PfsDesign, PfsConfig
import pfs.datamodel.utils as datamodel_utils


def make_pfsDesign(raCenter, decCenter, fiberIds, tracts, patches, ras, decs,
                   catIds, objIds, targetTypeIds, fiberMags_g,
                   pfiNominal_x, pfiNominal_y):
    '''
        Description
        -----------
            Make pfsDesign object

        Parameters
        ----------
            raCenter : `float`
            decCenter : `float`
            fiberIds : `numpy.ndarray` of `int`
            tracts : `numpy.ndarray` of `int`
            patches : `numpy.ndarray` of `str`
            ras : `numpy.ndarray` of `float`
            decs : `numpy.ndarray` of `float`
            catIds : `numpy.ndarray` of `int`
            objIds : `numpy.ndarray` of `int`
            targetTypeIds : `numpy.ndarray` of `int`
            fiberMags_g : `numpy.ndarray` of `float`
            pfiNominal_x : `numpy.ndarray` of `float`
            pfiNominal_y : `numpy.ndarray` of `float`

        Returns
        -------
            pfsDesign : `object` of `pfsDesign`
            pfsDesignId : `int`

        Note
        ----
            You need to have the latest PFS datamodel
    '''
    nFiber = len(fiberIds)
    raBoresight = raCenter
    decBoresight = decCenter
    fiberMags = [[mag] for mag in fiberMags_g]
    filterNames = [['g'] for i in range(nFiber)]
    pfiNominal = np.array((pfiNominal_x, pfiNominal_y)).transpose()
    pfsDesignId = datamodel_utils.calculate_pfsDesignId(fiberIds, ras, decs)
    pfsDesign = PfsDesign(pfsDesignId, raBoresight=raBoresight, decBoresight=decBoresight,
                          fiberId=fiberIds, tract=tracts, patch=patches,
                          ra=ras, dec=decs, catId=catIds, objId=objIds,
                          targetType=targetTypeIds, fiberMag=fiberMags,
                          filterNames=filterNames, pfiNominal=pfiNominal)
    pfsDesignId = pfsDesign.pfsDesignId
    pfsDesign.write('./out/fits/')
    return pfsDesign, pfsDesignId


def make_pfsConfig(pfsDesignId, visit0, fiberIds, tracts, patches, ras, decs,
                   catIds, objIds, targetTypeIds, fiberMags_g,
                   pfiNominal_x, pfiNominal_y, pfiCenter_x, pfiCenter_y):
    '''
        Description
        -----------
            Make pfsConfig object

        Parameters
        ----------
            pfsDesignId : `int`
            visit0 : `int`
            fiberIds : `numpy.ndarray` of `int`
            tracts : `numpy.ndarray` of `int`
            patches : `numpy.ndarray` of `str`
            ras : `numpy.ndarray` of `float`
            decs : `numpy.ndarray` of `float`
            catIds : `numpy.ndarray` of `int`
            objIds : `numpy.ndarray` of `int`
            targetTypeIds : `numpy.ndarray` of `int`
            fiberMags_g : `numpy.ndarray` of `float`
            pfiNominal_x : `numpy.ndarray` of `float`
            pfiNominal_y : `numpy.ndarray` of `float`
            pfiCenter_x : `numpy.ndarray` of `float`
            pfiCenter_y : `numpy.ndarray` of `float`

        Returns
        -------
            pfsConfig : `object` of `pfsConfig`

        Note
        ----
            You need to have the latest PFS datamodel
    '''
    nFiber = len(fiberIds)
    fiberMag = np.empty((nFiber, 5))
    for i in range(nFiber):
        fiberMag[i] = fiberMags_g[i]
    raBoresight = np.median(ras)
    decBoresight = np.median(decs)
    fiberMags = [[mag] for mag in fiberMag[:, 0]]
    filterNames = [['g'] for i in range(nFiber)]
    pfiNominal = np.array((pfiNominal_x, pfiNominal_y)).transpose()
    pfiCenter = np.array((pfiCenter_x, pfiCenter_y)).transpose()
    pfsConfig = PfsConfig(pfsDesignId=pfsDesignId, visit0=visit0, raBoresight=raBoresight, decBoresight=decBoresight,
                          fiberId=fiberIds, tract=tracts, patch=patches, ra=ras, dec=decs,
                          catId=catIds, objId=objIds, targetType=targetTypeIds,
                          fiberMag=fiberMags, filterNames=filterNames,
                          pfiCenter=pfiCenter, pfiNominal=pfiNominal)
    pfsConfig.write('./out/fits/')
    return pfsConfig
