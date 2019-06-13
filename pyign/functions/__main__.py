# third-party libraries
import numpy as np
from argparse import ArgumentParser as ap
import os

# local imports
from pyign.functions.core import getPTData, getTCData, getLCData, getLSData, getGOState, getAbortState, getNanny, getValveState, getIgnitorState, setValveState, setIgnitorState, setGOState, setAbortState, setNanny, _init_system, pt_index, tc_index, lc_index, check_limits, check_limit_switch, check_go, check_abort, check_pt_data, check_tc_data, check_lc_data
'''
# local imports
from core import getPTData, getTCData, getLCData, getLSData, getGOState, getAbortState, getNanny, getValveState, getIgnitorState, setValveState, setIgnitorState, setGOState, setAbortState, setNanny, _init_system, pt_index, tc_index, lc_index, check_limits, check_limit_switch, check_go, check_abort, check_pt_data, check_tc_data, check_lc_data
'''

script_dir = os.path.dirname(__file__)
file_1 = os.path.join(script_dir, '../raw/press_data.txt')
file_2 = os.path.join(script_dir, '../raw/therm_data.txt')
file_3 = os.path.join(script_dir, '../raw/load_data.txt')
pt_data = getTCData(file_1)
tc_data = getTCData(file_2)
lc_data = getTCData(file_3)

parser = ap(description='Test Stand System State')

parser.add_argument('-s','--start',action = 'store_true',required = False, help = 'Initialize and output initial system state')

parser.add_argument('-n','--nanny',action = 'store_true',required = False, help = 'Turn "Nanny" to "ON"')

parser.add_argument('-g','--go',action = 'store_true',required = False, help = 'Turn "GO/NOGO" to "GO" and change ignitor state')

parser.add_argument('-t','--test',action = 'store_true',required = False, help = 'Tests system with input sensor data')

args = parser.parse_args()

if args.start == True:
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    print(' ')
    print(' ')
    print('Initialize System:')
    print('(SAFE MODE)  Valve State =', getValveState(vst, ist, abt))
    print('(SAFE MODE)  Ignitor State =', getIgnitorState(vst, ist, abt, gst))
    print('(OFF)        Nanny =', getNanny(abt))
    print('(NOGO)       GO/NOGO =', getGOState(gst))
    print('(NOMINAL)    Abort State =', getAbortState(abt))
    print(' ')
    print(' ')
elif args.nanny == True:
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    setNanny(abt, 1)
    print(' ')
    print(' ')
    print('Initialize System and turn "Nanny" to "ON":')
    print('(ON)         Nanny =', getNanny(abt))
    print(' ')
    print(' ')
elif args.go == True:
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    print(' ')
    print(' ')
    print('Initialize System:')
    print('(SAFE MODE)  Ignitor State =', getIgnitorState(vst, ist, abt, gst))
    print('(NOGO)       GO/NOGO =', getGOState(gst),)
    print(' ')
    setGOState(gst,'a',1)
    setGOState(gst,'c',1)
    print('Turn Control Panel and Fuel Panel "GO/NOGO" states to "GO":')
    print('(GO)         GO/NOGO =', getGOState(gst)[0],' {Control Panel}')
    print('(NOGO)       GO/NOGO =', getGOState(gst)[1],' {LOX Panel}')
    print('(GO)         GO/NOGO =', getGOState(gst)[2],' {Fuel Panel}')
    print(' ')
    print('(NOGO)       GO/NOGO =', getGOState(gst),' {System}')
    print(' ')
    setIgnitorState(ist,1)
    print('Attempt to set "Ignitor" state to "ACTIVE":')
    print('(SAFE MODE)  Ignitor State =', getIgnitorState(vst, ist, abt, gst))
    print(' ')
    print('Failed to set "Ignitor" state to "ACTIVE" until all Operator Panel "GO/NOGO" states are set to "GO"')
    print(' ')
    setGOState(gst,'b',1)
    setIgnitorState(ist,1)
    print('Turn LOX Panel "GO/NOGO" state to "GO" and set "Ignitior" state to "ACTIVE":')
    print('(GO)         GO/NOGO =', getGOState(gst))
    print('(ACTIVE)     Ignitor State =', getIgnitorState(vst, ist, abt, gst))
    print(' ')
    print(' ')
elif args.test == True:
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    setValveState(vst, 'b', 1)
    setValveState(vst, 'c', 1)
    setValveState(vst, 'g', 1)
    print(' ')
    print(' ')
    print('Initialize System and set valve states:')
    print('(ACTIVE)     Valve State =', getValveState(vst, ist, abt))
    print('(NOMINAL)    Abort State =', getAbortState(abt))
    print('(OFF)        Nanny =', getNanny(abt))
    setNanny(abt, 1)
    print(' ')
    print('Turn "Nanny" to "ON":')
    print('(ON)         Nanny =', getNanny(abt))
    print(' ')
    print('Read sensor data and trip "ABORT":')
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('(ABORT)      Abort State =', getAbortState(abt))
    print('(SAFE MODE)  Valve State =', getValveState(vst, ist, abt))
    print(' ')
    print(' ')
else:
    raise Exception('No action specified')
