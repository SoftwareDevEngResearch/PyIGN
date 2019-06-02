#from ignition.functions.valves import ValveStateClass as vst
#from ignition.functions.limits import
from ignition.functions.core import getptData, gettcData, getlcData, ptEval, tcEval, lcEval, nannyEval, abortstateEval, vlvstateEval, ptIndex, tcIndex, lcIndex, initvalveState, initsystemState, initsensorLimits, checksystemLimits, checkabortState

import pytest
import os

sys_state = initsystemState()
vlv_state = initvalveState()
pt_limits, tc_limits, lc_limits = initsensorLimits()


def test_nanny_initial_state():
    assert nannyEval(sys_state) == 0
test_nanny_initial_state()

def test_abort_initial_state():
    assert abortstateEval(sys_state) == 0
test_abort_initial_state()

#def test_checksystemLimits_initial_state():
#    assert checksystemLimits(sys_state, check_pt_array, check_tc_array, check_lc_array) == 0
#test_checksystemLimits_initial_state()

#def test_valve_initial_state():
#    assert vlvstateEval(vlv_state, sys_state) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#test_valve_initial_state()

def test_getptData_initial():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getptData(file)[0] == 500
test_getptData_initial()

def test_gettcData_initial():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    assert gettcData(file)[0] == 62
test_gettcData_initial()

def test_getlcData_initial():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    assert getlcData(file)[0] == 520
test_getlcData_initial()


def test_getptData_mid():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getptData(file)[3] == 500
test_getptData_mid()

def test_gettcData_mid():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    assert gettcData(file)[6] == 402
test_gettcData_mid()

def test_getlcData_mid():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    assert getlcData(file)[1] == 602
test_getlcData_mid()


def test_getptData_final():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getptData(file)[6] == 950
test_getptData_final()

def test_gettcData_final():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    assert gettcData(file)[11] == 572
test_gettcData_final()

def test_getlcData_final():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    assert getlcData(file)[2] == 2999
test_getlcData_final()


def test_ptEval():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    data = getptData(file)
    assert ptEval(pt_limits, data) == [0, 0, 0, 0, 0, 0, 950]
test_ptEval()

def test_tcEval():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    data = gettcData(file)
    assert tcEval(tc_limits, data) == [0, 0, 0, 0, 0, 0, 402, 0, 0, 0, 0, 0]
test_ptEval()

def test_lcEval():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    data = getlcData(file)
    assert lcEval(lc_limits, data) == [0, 602, 0]
test_ptEval()


def test_ptIndex():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    data = getptData(file)
    assert ptIndex(pt_limits, data) == [0, 0, 0, 0, 0, 0, 7]
test_ptIndex()

def test_tcIndex():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    data = gettcData(file)
    assert tcIndex(tc_limits, data) == [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0]
test_tcIndex()

def test_lcIndex():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    data = getlcData(file)
    assert lcIndex(lc_limits, data) == [0, 2, 0]
test_lcIndex()
