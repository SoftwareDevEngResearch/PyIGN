# states.py
import numpy as np

class ValveState(object):
    """The State of a Valve determines if a valve set to 'opened' or 'closed'.

        Attributes
        ----------
        manuel : manuel mode [12]
        a : valve ABV-PR-110
        b : valve ABV-PR-120
        c : valve ABV-OX-210
        d : valve ABV-FU-310
        e : valve ABV-OX-220
        f : valve ABV-FU-320
        g : valve ABV-OX-230
        h : valve ABV-FU-330
        i : valve ABV-OX-240
        j : valve ABV-FU-340
        k : valve ABV-OX-250
        """
    def __init__(self, valve_a=0, valve_b=0, valve_c=0, valve_d=0, valve_e=0, valve_f=0, valve_g=0, valve_h=0, valve_i=0, valve_j=0, valve_k=0):
        self._valve_a = valve_a
        self._valve_b = valve_b
        self._valve_c = valve_c
        self._valve_d = valve_d
        self._valve_e = valve_e
        self._valve_f = valve_f
        self._valve_g = valve_g
        self._valve_h = valve_h
        self._valve_i = valve_i
        self._valve_j = valve_j
        self._valve_k = valve_k
        self._valve_state = [valve_a, valve_b, valve_c, valve_d, valve_e, valve_f, valve_g, valve_h, valve_i, valve_j, valve_k]

    @property
    def valve_state(self):
        self._valve_state = [self._valve_a, self._valve_b, self._valve_c, self._valve_d, self._valve_e, self._valve_f, self._valve_g, self._valve_h, self._valve_i, self._valve_j, self._valve_k]
        return self._valve_state
    @property
    def valve_a(self):
        return self._valve_a #Return a ABV-PR-110 Valve
    @property
    def valve_b(self):
        return self._valve_b #Return b ABV-PR-120 Valve
    @property
    def valve_c(self):
        return self._valve_c #Return c ABV-OX-210 Valve
    @property
    def valve_d(self):
        return self._valve_d #Return d ABV-FU-310 Valve
    @property
    def valve_e(self):
        return self._valve_e #Return e ABV-OX-220 Valve
    @property
    def valve_f(self):
        return self._valve_f #Return f ABV-FU-320 Valve
    @property
    def valve_g(self):
        return self._valve_g #Return g ABV-OX-230 Valve
    @property
    def valve_h(self):
        return self._valve_h #Return h ABV-FU-330 Valve
    @property
    def valve_i(self):
        return self._valve_i #Return i ABV-OX-240 Valve
    @property
    def valve_j(self):
        return self._valve_j #Return j ABV-FU-340 Valve
    @property
    def valve_k(self):
        return self._valve_k #Return k ABV-OX-250 Valve

    @valve_a.setter
    def valve_a(self, valve_a):
        self._valve_a = valve_a  #Set a ABV-PR-110 Valve
    @valve_b.setter
    def valve_b(self, valve_b):
        self._valve_b = valve_b  #Set b ABV-PR-120 Valve
    @valve_c.setter
    def valve_c(self,valve_c):
        self._valve_c = valve_c  #Set c ABV-OX-210 Valve
    @valve_d.setter
    def valve_d(self, valve_d):
        self._valve_d = valve_d  #Set d ABV-FU-310 Valve
    @valve_e.setter
    def valve_e(self, valve_e):
        self._valve_e = valve_e  #Set e ABV-OX-220 Valve
    @valve_f.setter
    def valve_f(self, valve_f):
        self._valve_f = valve_f  #Set f ABV-FU-320 Valve
    @valve_g.setter
    def valve_g(self, valve_g):
        self._valve_g = valve_g  #Set g ABV-OX-230 Valve
    @valve_h.setter
    def valve_h(self, valve_h):
        self._valve_h = valve_h  #Set h ABV-FU-330 Valve
    @valve_i.setter
    def valve_i(self, valve_i):
        self._valve_i = valve_i  #Set i ABV-OX-240 Valve
    @valve_j.setter
    def valve_j(self, valve_j):
        self._valve_j = valve_j  #Set j ABV-FU-340 Valve
    @valve_k.setter
    def valve_k(self, valve_k):
        self._valve_k = valve_k  #Set k ABV-OX-250 Valve

'''
class LimitSwitchState(object):
    """The State of a Limit Switch determines if a valve is 'opened' or 'closed'.

        Attributes
        ----------
        manuel : manuel mode [12]
        a : limit switch ABV-PR-110
        b : limit switch ABV-PR-120
        c : limit switch ABV-OX-210
        d : limit switch ABV-FU-310
        e : limit switch ABV-OX-220
        f : limit switch ABV-FU-320
        g : limit switch ABV-OX-230
        h : limit switch ABV-FU-330
        i : limit switch ABV-OX-240
        j : limit switch ABV-FU-340
        k : limit switch ABV-OX-250
        l : limit switch MNL-FU-350
        """
    def __init__(self, limit_switch_a=0, limit_switch_b=0, limit_switch_c=0, limit_switch_d=0, limit_switch_e=0, limit_switch_f=0, limit_switch_g=0, limit_switch_h=0, limit_switch_i=0, limit_switch_j=0, limit_switch_k=0, limit_switch_l=0):
        self._limit_switch_a = limit_switch_a
        self._limit_switch_b = limit_switch_b
        self._limit_switch_c = limit_switch_c
        self._limit_switch_d = limit_switch_d
        self._limit_switch_e = limit_switch_e
        self._limit_switch_f = limit_switch_f
        self._limit_switch_g = limit_switch_g
        self._limit_switch_h = limit_switch_h
        self._limit_switch_i = limit_switch_i
        self._limit_switch_j = limit_switch_j
        self._limit_switch_k = limit_switch_k
        self._limit_switch_l = limit_switch_l
        self._limit_switch_state = [limit_switch_a, limit_switch_b, limit_switch_c, limit_switch_d, limit_switch_e, limit_switch_f, limit_switch_g, limit_switch_h, limit_switch_i, limit_switch_j, limit_switch_k, limit_switch_l]
    @property
    def limit_switch_state(self):
        self._limit_switch_state = [self._limit_switch_a, self._limit_switch_b, self._limit_switch_c, self._limit_switch_d, self._limit_switch_e, self._limit_switch_f, self._limit_switch_g, self._limit_switch_h, self._limit_switch_i, self._limit_switch_j, self._limit_switch_k, self._limit_switch_l]
        return self._limit_switch_state
    @property
    def limit_switch_a(self):
        return self._limit_switch_a #Return a ABV-PR-110 Limit Switch
    @property
    def limit_switch_b(self):
        return self._limit_switch_b #Return b ABV-PR-120 Limit Switch
    @property
    def limit_switch_c(self):
        return self._limit_switch_c #Return c ABV-OX-210 Limit Switch
    @property
    def limit_switch_d(self):
        return self._limit_switch_d #Return d ABV-FU-310 Limit Switch
    @property
    def limit_switch_e(self):
        return self._limit_switch_e #Return e ABV-OX-220 Limit Switch
    @property
    def limit_switch_f(self):
        return self._limit_switch_f #Return f ABV-FU-320 Limit Switch
    @property
    def limit_switch_g(self):
        return self._limit_switch_g #Return g ABV-OX-230 Limit Switch
    @property
    def limit_switch_h(self):
        return self._limit_switch_h #Return h ABV-FU-330 Limit Switch
    @property
    def limit_switch_i(self):
        return self._limit_switch_i #Return i ABV-OX-240 Limit Switch
    @property
    def limit_switch_j(self):
        return self._limit_switch_j #Return j ABV-FU-340 Limit Switch
    @property
    def limit_switch_k(self):
        return self._limit_switch_k #Return k ABV-OX-250 Limit Switch
    @property
    def limit_switch_l(self):
        return self._limit_switch_l #Return l MNL-FU-350 Limit Switch
    @limit_switch_a.setter
    def limit_switch_a(self, limit_switch_a):
        self._limit_switch_a = limit_switch_a  #Set a ABV-PR-110 Limit Switch
    @limit_switch_b.setter
    def limit_switch_b(self, limit_switch_b):
        self._limit_switch_b = limit_switch_b  #Set b ABV-PR-120 Limit Switch
    @limit_switch_c.setter
    def limit_switch_c(self,limit_switch_c):
        self._limit_switch_c = limit_switch_c  #Set c ABV-OX-210 Limit Switch
    @limit_switch_d.setter
    def limit_switch_d(self, limit_switch_d):
        self._limit_switch_d = limit_switch_d  #Set d ABV-FU-310 Limit Switch
    @limit_switch_e.setter
    def limit_switch_e(self, limit_switch_e):
        self._limit_switch_e = limit_switch_e  #Set e ABV-OX-220 Limit Switch
    @limit_switch_f.setter
    def limit_switch_f(self, limit_switch_f):
        self._limit_switch_f = limit_switch_f  #Set f ABV-FU-320 Limit Switch
    @limit_switch_g.setter
    def limit_switch_g(self, limit_switch_g):
        self._limit_switch_g = limit_switch_g  #Set g ABV-OX-230 Limit Switch
    @limit_switch_h.setter
    def limit_switch_h(self, limit_switch_h):
        self._limit_switch_h = limit_switch_h  #Set h ABV-FU-330 Limit Switch
    @limit_switch_i.setter
    def limit_switch_i(self, limit_switch_i):
        self._limit_switch_i = limit_switch_i  #Set i ABV-OX-240 Limit Switch
    @limit_switch_j.setter
    def limit_switch_j(self, limit_switch_j):
        self._limit_switch_j = limit_switch_j  #Set j ABV-FU-340 Limit Switch
    @limit_switch_k.setter
    def limit_switch_k(self, limit_switch_k):
        self._limit_switch_k = limit_switch_k  #Set k ABV-OX-250 Limit Switch
    @limit_switch_l.setter
    def limit_switch_l(self, limit_switch_l):
        self._limit_switch_l = limit_switch_l  #Set l MNL-FU-350 Limit Switch
'''

class IgnitorState(object):
    """The Ignitor State determines if the engine ignitor has lit.

        Attributes
        ----------
        ignitor_state : Ignitor State [1]
        """
    def __init__(self, ignitor_state=0):
        self._ignitor_state = ignitor_state  #Ignitor State

    @property
    def ignitor_state(self):
        return self._ignitor_state  #Return Ignitor State

    @ignitor_state.setter
    def ignitor_state(self, ignitor_state):
        self._ignitor_state = ignitor_state  #Set Ignitor State


class AbortState(object):
    """The Abort State of a System determines if an 'Abort' has been tripped and the system is in maditory 'Safe' mode.

        Attributes
        ----------
        state : 'Abort' State [1]
        state[0] : 'Go' State
        state[1] : 'Abort Has Been Tripped' State
        nanny : Monitor System [1]
        """
    def __init__(self, abort_state=0, nanny=0):
        self._abort_state = abort_state  #Initialize 'Abort' State
        self._nanny = nanny

    @property
    def abort_state(self):
        return self._abort_state  #Return 'Abort' State
    @property
    def nanny(self):
        return self._nanny  #Return Nanny Mode

    @abort_state.setter
    def abort_state(self, abort_state):
        self._abort_state = abort_state  #Set 'Abort' State
    @nanny.setter
    def nanny(self, nanny):
        self._nanny = nanny  #Set Nanny Mode

class GoState(object):
    """A 'GO' signal is required from all control ends before beginning the ignition phase.

        Attributes
        ----------
        GO : States [3]
        go_control : Control Panel State
        go_lox : LOX Panel State
        go_fuel : Fuel Panel State
        """
    def __init__(self, go_control=0, go_lox=0, go_fuel=0):
        self._go_control = go_control
        self._go_lox = go_lox
        self._go_fuel = go_fuel
        self._go_states = [go_control, go_lox, go_fuel]  #Panel 'GO' States

    @property
    def go_states(self):
        self._go_states = [self._go_control, self._go_lox, self._go_fuel]
        return self._go_states
    @property
    def go_control(self):
        return self._go_control #Control Panel 'GO' State
    @property
    def go_lox(self):
        return self._go_lox #LOX Panel 'GO' State
    @property
    def go_fuel(self):
        return self._go_fuel #Fuel Panel 'GO' State

    @go_control.setter
    def go_control(self, go_control):
        self._go_control = go_control  #Set Control Panel 'GO' State
    @go_lox.setter
    def go_lox(self, go_lox):
        self._go_lox = go_lox  #Set LOX Panel 'GO' State
    @go_fuel.setter
    def go_fuel(self,go_fuel):
        self._go_fuel = go_fuel  #Set Fuel Panel 'GO' State




if __name__ == '__main__':

    '''
    vlv = ValveState()
    lss = LimitSwitchState()
    ign = IgnitorState()
    abt = AbortState()
    '''
    ####
    '''
    print(vlv.valve_e)
    vlv.valve_a = 0
    print(vlv.valve_a)
    vlv.valve_a = 1
    print(vlv.valve_a)
    vlv.valve_a = 0
    print(vlv.valve_a)
    abt = AbortState()
    print(abt.abort_state)
    abt.abort_state = 0
    print(abt.abort_state)
    abt.abort_state = 1
    print(abt.abort_state)
    abt.abort_state = 0
    print(abt.abort_state)
    print(vlv.valve_state)
    print(vlv.valve_c)
    vlv.valve_c = 1
    print(vlv.valve_c)
    print(vlv.valve_state)
    print(vlv.valve_e)
    vlv.valve_a = 0
    print(vlv.valve_a)
    vlv.valve_a = 1
    print(vlv.valve_a)
    vlv.valve_a = 0
    print(vlv.valve_a)
    print(abt.nanny)
    abt.nanny = 1
    print(abt.nanny)
    print(ign.ignitor_state)
    ign.ignitor_state = 1
    print(ign.ignitor_state)
    '''
    ####
    '''
    gst = GoState()
    print(gst.go_states)
    print(gst.go_lox)
    gst.go_lox = 1
    print(gst.go_lox)
    print(gst.go_states)
    '''
