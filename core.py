"""Data file from sensors is read and formatted"""
import numpy as np
#import sys

from ignition.functions.limits import PTLimitClass as ptl
from ignition.functions.limits import TCLimitClass as tcl
from ignition.functions.limits import LCLimitClass as lcl

from ignition.functions.valves import ValveStateClass as vst
from ignition.functions.valves import AbortStateClass as abt
'''
from limits import PTLimitClass as ptl
from limits import TCLimitClass as tcl
from limits import LCLimitClass as lcl

from valves import ValveStateClass as vst
from valves import AbortStateClass as abt
'''

def getptData(filename):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    try:
        in_data = np.loadtxt(filename)
    except IOError:
        print ('Pressure Transducer Input Data File Read Error', filename)
    return in_data

def gettcData(filename):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    try:
        in_data = np.loadtxt(filename)
    except IOError:
        print ('Thermocouple Input Data File Read Error', filename)
    return in_data

def getlcData(filename):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    try:
        in_data = np.loadtxt(filename)
    except IOError:
        print ('Load Cell Input Data File Read Error', filename)
    return in_data


def ptEval(pt_limits, pt_values):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    ptlimitarray = pt_limits.pt_limits
    pt = []
    for i in range(len(ptlimitarray)):
        x=(pt_values[i]-ptlimitarray[i])
        if x >= 0:
            pt.append(pt_values[i])
        else:
            pt.append(0)
    return pt

def tcEval(tc_limits, tc_values):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    tclimitarray = tc_limits.tc_limits
    tc = []
    for i in range(len(tclimitarray)):
        x=(tc_values[i]-tclimitarray[i])
        if x >= 0:
            tc.append(tc_values[i])
        else:
            tc.append(0)
    return tc

def lcEval(lc_limits, lc_values):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    lclimitarray = lc_limits.lc_limits
    lc = []
    for i in range(len(lclimitarray)):
        x=(lc_values[i]-lclimitarray[i])
        if x >= 0:
            lc.append(lc_values[i])
        else:
            lc.append(0)
    return lc


def ptIndex(pt_limits, pt_array):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    pt_index = []
    x = ptEval(pt_limits, pt_array)
    i = 0
    for line in pt_array:
        i += 1
        if line != x[i-1]:
            pt_index.append(0)
        elif line == x[i-1]:
            pt_index.append(i)
    return pt_index

def tcIndex(tc_limits, tc_array):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    tc_index = []
    x = tcEval(tc_limits, tc_array)
    i = 0
    for line in tc_array:
        i += 1
        if line != x[i-1]:
            tc_index.append(0)
        elif line == x[i-1]:
            tc_index.append(i)
    return tc_index

def lcIndex(lc_limits, lc_array):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    lc_index = []
    x = lcEval(lc_limits, lc_array)
    i = 0
    for line in lc_array:
        i += 1
        if line != x[i-1]:
            lc_index.append(0)
        elif line == x[i-1]:
            lc_index.append(i)
    return lc_index


def abortstateEval(sys_state):
    return (sys_state.sys_state)

def abortstateSet(sys_state, args):
    sys_state.sys_state = args
    return sys_state

def nannyEval(sys_state):
    return (sys_state.nanny)

def nannySet(sys_state, args):
    sys_state.nanny = args
    return sys_state

def vlvstateEval(vlv_state, sys_state):
    checkabortState(sys_state)
    return (vlv_state.vlv_state)

def vlvstateSet(vlv_state, valve, args):
    if valve == 'a':
        vlv_state.vlv_a = args
    elif valve == 'b':
        vlv_state.vlv_b = args
    elif valve == 'c':
        vlv_state.vlv_c = args
    elif valve == 'd':
        vlv_state.vlv_c = args
    elif valve == 'e':
        vlv_state.vlv_e = args
    elif valve == 'f':
        vlv_state.vlv_f = args
    elif valve == 'g':
        vlv_state.vlv_g = args
    elif valve == 'h':
        vlv_state.vlv_h = args
    elif valve == 'i':
        vlv_state.vlv_i = args
    elif valve == 'j':
        vlv_state.vlv_j = args
    elif valve == 'k':
        vlv_state.vlv_k = args
    return abortstateEval(sys_state)

def checksystemLimits(sys_state, check_pt_array, check_tc_array, check_lc_array):
    if sys_state.nanny == 1:
        pt = ptIndex(pt_limits, check_pt_array)
        tc = tcIndex(tc_limits, check_tc_array)
        lc = lcIndex(lc_limits, check_lc_array)
        if np.sum(pt)!= 0:
            abortstateSet(sys_state, 1)
        elif np.sum(tc)!= 0:
            abortstateSet(sys_state, 1)
        elif np.sum(lc)!= 0:
            abortstateSet(sys_state, 1)
    return sys_state

def checkabortState(sys_state):
    if sys_state.sys_state == 1:
        vlvstateSet(vlv_state, 'a', 0)
        vlvstateSet(vlv_state, 'b', 0)
        vlvstateSet(vlv_state, 'c', 0)
        vlvstateSet(vlv_state, 'd', 0)
        vlvstateSet(vlv_state, 'e', 0)
        vlvstateSet(vlv_state, 'f', 0)
        vlvstateSet(vlv_state, 'g', 0)
        vlvstateSet(vlv_state, 'h', 0)
        vlvstateSet(vlv_state, 'i', 0)
        vlvstateSet(vlv_state, 'j', 0)
        vlvstateSet(vlv_state, 'k', 0)
    return vlv_state

def initsystemState():
    sys_state = abt()
    return sys_state

def initvalveState():
    vlv_state = vst()
    return vlv_state

def initsensorLimits():
    pt_limits = ptl()
    tc_limits = tcl()
    lc_limits = lcl()
    return pt_limits, tc_limits, lc_limits

if __name__ == '__main__':

    sys_state = initsystemState()
    vlv_state = initvalveState()
    pt_limits, tc_limits, lc_limits = initsensorLimits()
    print(vlvstateEval(vlv_state, sys_state))
    '''
    print(abortstateEval(sys_state))
    abortstateSet(sys_state,1)
    print(abortstateEval(sys_state))
    abortstateSet(sys_state,0)
    print(sys_state.sys_state)

    print(abortstateEval(sys_state))
#    abortstateSet(sys_state,1)
#    print(abortstateEval(sys_state))
#    abortstateSet(sys_state,0)
#    print(sys_state.state)

    #nanny = 1
    print(nannyEval(sys_state))
    nannySet(sys_state, 1)
    print(nannyEval(sys_state))
    '''
    ####

    nannySet(sys_state, 1)
    print(nannyEval(sys_state))
    pt_array = [500, 500, 530, 500, 530, 500, 750]
    tc_array = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_array = [599, 599, 2999]
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    vlvstateSet(vlv_state, 'b', 1)
    vlvstateSet(vlv_state, 'c', 1)
    vlvstateSet(vlv_state, 'g', 1)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))
    print(vlvstateEval(vlv_state, sys_state))

    pt_array = [500, 500, 530, 500, 530, 500, 750]
    tc_array = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_array = [599, 599, 3999]
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))

    vlvstateSet(vlv_state, 'b', 1)
    vlvstateSet(vlv_state, 'c', 1)
    vlvstateSet(vlv_state, 'g', 1)
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))

    abortstateSet(sys_state, 0)
    vlvstateSet(vlv_state, 'b', 1)
    vlvstateSet(vlv_state, 'c', 1)
    vlvstateSet(vlv_state, 'g', 1)

    nannySet(sys_state, 0)
    print(nannyEval(sys_state))
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))

    nannySet(sys_state, 1)
    pt_array = [500, 500, 530, 500, 530, 500, 750]
    tc_array = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_array = [599, 599, 2999]
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))

    vlvstateSet(vlv_state, 'b', 1)
    vlvstateSet(vlv_state, 'c', 1)
    vlvstateSet(vlv_state, 'g', 1)
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))

    pt_array = [500, 500, 530, 500, 530, 500, 750]
    tc_array = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_array = [599, 599, 3999]
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))

    vlvstateSet(vlv_state, 'b', 1)
    vlvstateSet(vlv_state, 'c', 1)
    vlvstateSet(vlv_state, 'g', 1)
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))
    print('next')

    pt_array = [500, 500, 530, 500, 530, 500, 750]
    tc_array = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_array = [599, 599, 2999]
    checksystemLimits(sys_state, pt_array, tc_array, lc_array)
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))

    ####
    '''
    print(abortstateEval(sys_state))
    print(vlvstateEval(vlv_state, sys_state))
    vlvstateSet(vlv_state, 'c', 1)
    print(vlvstateEval(vlv_state, sys_state))
    vlvstateSet(vlv_state, 'c', 0)
    '''
#    print(b)
#    b = abortstateEval()
#    print(b)
#    print(abortstateSet(0))

    '''
    print(abtEval())
    print(abtSet(1))
    print(abtSet(0))
    '''
