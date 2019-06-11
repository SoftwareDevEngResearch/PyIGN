#from .Users.devonburson.Documents.ME_599_SD.P_Code.PyIgn.functions.core import getPTData

#from core import getPTData

#PATHONPAT=.
from pyign.functions.core import getPTData, getTCData, getLCData, getGOState, getAbortState, getNanny, getValveState, getIgnitorState, setValveState, setIgnitorState, setGOState, setAbortState, setNanny, _init_system, pt_index, tc_index, lc_index, check_limits, check_limit_switch, check_go, check_abort, check_pt_data, check_tc_data, check_lc_data

import pytest
import os
'''
need tests:
    INITIALIZE:
        - InitializeSystem()
        - InitializeLimits()
    GET:
        - getValveState()
        - getIgnitorState()
        -
        - ### getGOState()
        - ### getAbortState()
        - ### getNanny()
        -
        - ### getPTData()
        - ### getTCData()
        - ### getLCData()
    SET:
        - setValveState()
        - setIgnitorState()
        -
        - setGOState()
        - setAbortState()
        - setNanny()
    INDEX:
        - ### pt_index()
        - ### tc_index()
        - ### lc_index()
    CHECK:
        - ### check_pt_data()
        - ### check_tc_data()
        - ### check_lc_data()
        -
        - check_limits()
        - check_limit_switch()
        - check_go()
        - check_abort()
'''




vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

def test_valve_initial_state():
    assert getValveState(vst, ist, abt) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
test_valve_initial_state()

def test_go_initial_state():
    assert getGOState(gst) == [0, 0, 0]
test_go_initial_state()


def test_abort_initial():
    assert getAbortState(abt) == 0
test_abort_initial()

def test_nanny_initial_state():
    assert getNanny(abt) == 0
test_nanny_initial_state()

#def test_check_limits_initial_state():
#    assert check_limits(abt, check_pt_array, check_tc_array, check_lc_array) == 0
#test_check_limits_initial_state()

#def test_valve_initial_state():
#    assert getValveState(vst, abt) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#test_valve_initial_state()

def test_getPTData_initial():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getPTData(file)[0] == 500
test_getPTData_initial()

def test_getTCData_initial():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    assert getTCData(file)[0] == 62
test_getTCData_initial()

def test_getLCData_initial():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    assert getLCData(file)[0] == 520
test_getLCData_initial()


def test_getPTData_mid():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getPTData(file)[3] == 500
test_getPTData_mid()

def test_getTCData_mid():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    assert getTCData(file)[6] == 402
test_getTCData_mid()

def test_getLCData_mid():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    assert getLCData(file)[1] == 602
test_getLCData_mid()


def test_getPTData_final():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getPTData(file)[6] == 950
test_getPTData_final()

def test_getTCData_final():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    assert getTCData(file)[11] == 572
test_getTCData_final()

def test_getLCData_final():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    assert getLCData(file)[2] == 2999
test_getLCData_final()


def test_check_pt_data():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    data = getPTData(file)
    assert check_pt_data(ptl, data) == [0, 0, 0, 0, 0, 0, 950]
test_check_pt_data()

def test_check_tc_data():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    data = getTCData(file)
    assert check_tc_data(tcl, data) == [0, 0, 0, 0, 0, 0, 402, 0, 0, 0, 0, 0]
test_check_tc_data()

def test_check_lc_data():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    data = getLCData(file)
    assert check_lc_data(lcl, data) == [0, 602, 0]
test_check_lc_data()


def test_pt_index():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    data = getPTData(file)
    assert pt_index(ptl, data) == [0, 0, 0, 0, 0, 0, 7]
test_pt_index()

def test_tc_index():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    data = getTCData(file)
    assert tc_index(tcl, data) == [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0]
test_tc_index()

def test_lc_index():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    data = getLCData(file)
    assert lc_index(lcl, data) == [0, 2, 0]
test_lc_index()
