# third-party libraries
import pytest
import  os

# local imports
from pyign.functions.core import getPTData, getTCData, getLCData, getLSData, getGOState, getAbortState, getNanny, getValveState, getIgnitorState, setValveState, setIgnitorState, setGOState, setAbortState, setNanny, _init_system, pt_index, tc_index, lc_index, check_limits, check_limit_switch, check_go, check_abort, check_pt_data, check_tc_data, check_lc_data



vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

def test_valve_initial_state():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    assert getValveState(vst, ist, abt) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
test_valve_initial_state()

def test_ignitor_initial_state():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    assert getIgnitorState(vst, ist, abt, gst) == 0
test_ignitor_initial_state()

def test_go_initial_state():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    assert getGOState(gst) == [0, 0, 0]
test_go_initial_state()

def test_abort_initial():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    assert getAbortState(abt) == 0
test_abort_initial()

def test_nanny_initial_state():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    assert getNanny(abt) == 0
test_nanny_initial_state()


def test_valve_set_state():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    setValveState(vst, 'f', 1)
    assert getValveState(vst, ist, abt) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
test_valve_set_state()

def test_ignitor_set_state():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    setGOState(gst, 'a', 1)
    setGOState(gst, 'b', 1)
    setGOState(gst, 'c', 1)
    setIgnitorState(ist, 1)
    assert getIgnitorState(vst, ist, abt, gst) == 1
test_ignitor_set_state()

def test_go_set_state():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    setGOState(gst, 'b', 1)
    assert getGOState(gst) == [0, 1, 0]
test_go_set_state()

def test_abort_set():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    setAbortState(abt, 1)
    assert getAbortState(abt) == 1
test_abort_set()

def test_nanny_set_state():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    setNanny(abt, 1)
    assert getNanny(abt) == 1
test_nanny_set_state()


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
    assert getLCData(file)[0] == 502
test_getLCData_initial()

def test_getLSData_initial():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/limit_data.txt')
    assert getLSData(file)[0] == 0
test_getLSData_initial()


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

def test_getLSData_mid():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/limit_data.txt')
    assert getLSData(file)[1] == 1
test_getLSData_mid()


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

def test_getLSData_final():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/limit_data.txt')
    assert getLSData(file)[10] == 0
test_getLSData_final()


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


def test_check_initial_pt_data():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data_2.txt')
    pt_data_2 = getPTData(file)

    assert check_pt_data(ptl, pt_data_2) == [0, 0, 0, 0, 0, 0, 0]
test_check_initial_pt_data()

def test_check_initial_tc_data():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data_2.txt')
    tc_data_2 = getTCData(file)

    assert check_tc_data(tcl, tc_data_2) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
test_check_initial_tc_data()

def test_check_initial_lc_data():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data_2.txt')
    lc_data_2 = getLCData(file)

    assert check_lc_data(lcl, lc_data_2) == [0, 0, 0]
test_check_initial_lc_data()

def test_check_initial_limits():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data_2.txt')
    pt_data_2 = getLCData(file)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data_2.txt')
    tc_data_2 = getLCData(file)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data_2.txt')
    lc_data_2 = getLCData(file)

    check_limits(abt, ptl, tcl, lcl, pt_data_2, tc_data_2, lc_data_2)
    assert getAbortState(abt) == 0
test_check_initial_limits()

def test_limit_switch_initial():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/limit_data_2.txt')
    ls_data_2 = getLSData(file)

    check_limit_switch(abt, vst, ls_data_2)
    assert getAbortState(abt) == 0
test_check_initial_limits()


def test_check_final_pt_data():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    pt_data = getPTData(file)

    assert check_pt_data(ptl, pt_data) == [0, 0, 0, 0, 0, 0, 950]
test_check_final_pt_data()

def test_check_final_tc_data():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data.txt')
    tc_data = getTCData(file)

    assert check_tc_data(tcl, tc_data) == [0, 0, 0, 0, 0, 0, 402, 0, 0, 0, 0, 0]
test_check_final_tc_data()

def test_check_final_lc_data():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data.txt')
    lc_data = getLCData(file)

    assert check_lc_data(lcl, lc_data) == [0, 602, 0]
test_check_final_lc_data()

def test_check_final_limits():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    pt_data_1 = getLCData(file)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/therm_data_2.txt')
    tc_data_2 = getLCData(file)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/load_data_2.txt')
    lc_data_2 = getLCData(file)

    check_limits(abt, ptl, tcl, lcl, pt_data_1, tc_data_2, lc_data_2)
    assert getAbortState(abt) == 1
test_check_final_limits()

def test_limit_switch_final():
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()

    setNanny(abt, 1)

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/limit_data.txt')
    ls_data = getLSData(file)

    check_limit_switch(abt, vst, ls_data)
    assert getAbortState(abt) == 1
test_check_final_limits()
