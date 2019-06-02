import numpy as np



class ValveStateClass(object):
    """The State of a Valve determines if a valve is 'opened' or 'closed'.
        Attributes
        ----------
        safe : Valve 'Safe' Mode [12]
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
    def __init__(self, vlv_a=0, vlv_b=0, vlv_c=0, vlv_d=0, vlv_e=0, vlv_f=0, vlv_g=0, vlv_h=0, vlv_i=0, vlv_j=0, vlv_k=0):
        #self.__safe = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #Safe
        self._vlv_a = vlv_a
        self._vlv_b = vlv_b
        self._vlv_c = vlv_c
        self._vlv_d = vlv_d
        self._vlv_e = vlv_e
        self._vlv_f = vlv_f
        self._vlv_g = vlv_g
        self._vlv_h = vlv_h
        self._vlv_i = vlv_i
        self._vlv_j = vlv_j
        self._vlv_k = vlv_k
        self._vlv_state = [vlv_a, vlv_b, vlv_c, vlv_d, vlv_e, vlv_f, vlv_g, vlv_h, vlv_i, vlv_j, vlv_k]

    @property
    def vlv_state(self):
        #self._vlv_state = np.asarray(self._vlv_state)
        self._vlv_state = [self._vlv_a, self._vlv_b, self._vlv_c, self._vlv_d, self._vlv_e, self._vlv_f, self._vlv_g, self._vlv_h, self._vlv_i, self._vlv_j, self._vlv_k]
        return self._vlv_state
    #@property
    #def safe(self):
        #self.__safe = np.asarray(self.__safe)
    #    return self.__safe
    @property
    def vlv_a(self):
        #print("Getting a ABV-PR-110 State")
        return self._vlv_a
    @property
    def vlv_b(self):
        #print("Getting b ABV-PR-120 State")
        return self._vlv_b
    @property
    def vlv_c(self):
        #print("Getting c ABV-OX-210 State")
        return self._vlv_c
    @property
    def vlv_d(self):
        #print("Getting d ABV-FU-310 State")
        return self._vlv_d
    @property
    def vlv_e(self):
        #print("Getting e ABV-OX-220 State")
        return self._vlv_e
    @property
    def vlv_f(self):
        #print("Getting f ABV-FU-320 State")
        return self._vlv_f
    @property
    def vlv_g(self):
        #print("Getting g ABV-OX-230 State")
        return self._vlv_g
    @property
    def vlv_h(self):
        #print("Getting h ABV-FU-330 State")
        return self._vlv_h
    @property
    def vlv_i(self):
        #print("Getting i ABV-OX-240 State")
        return self._vlv_i
    @property
    def vlv_j(self):
        #print("Getting j ABV-FU-340 State")
        return self._vlv_j
    @property
    def vlv_k(self):
        #print("Getting k ABV-OX-250 State")
        return self._vlv_k

#    @vlv_state.setter
#    def vlv_state(self, vlv_a, vlv_b, vlv_c, vlv_d, vlv_e, vlv_f, vlv_g, vlv_h, vlv_i, vlv_j, vlv_k):
    ##def vlv_state(self, vlv_a, vlv_b, vlv_c, vlv_d, vlv_e, vlv_f, vlv_g, vlv_h, vlv_i, vlv_j, vlv_k):
        #print("Setting all valves to Safe State")
#        self._vlv_state = self.__safe
    @vlv_a.setter
    def vlv_a(self, vlv_a):
        #print("Setting a ABV-PR-110 State")
        self._vlv_a = vlv_a  #Manuel Mode a ABV-PR-110 Valve
    @vlv_b.setter
    def vlv_b(self, vlv_b):
        #print("Setting b ABV-PR-120 State")
        self._vlv_b = vlv_b  #Manuel Mode b ABV-PR-120 Valve
    @vlv_c.setter
    def vlv_c(self,vlv_c):
        #print("Setting c ABV-OX-210 State")
        self._vlv_c = vlv_c  #Manuel Mode c ABV-OX-210 Valve
    @vlv_d.setter
    def vlv_d(self, vlv_d):
        #print("Setting d ABV-FU-310 State")
        self._vlv_d = vlv_d  #Manuel Mode d ABV-FU-310 Valve
    @vlv_e.setter
    def vlv_e(self, vlv_e):
        #print("Setting e ABV-OX-220 State")
        self._vlv_e = vlv_e  #Manuel Mode e ABV-OX-220 Valve
    @vlv_f.setter
    def vlv_f(self, vlv_f):
        #print("Setting f ABV-FU-320 State")
        self._vlv_f = vlv_f  #Manuel Mode f ABV-FU-320 Valve
    @vlv_g.setter
    def vlv_g(self, vlv_g):
        #print("Setting g ABV-OX-230 State")
        self._vlv_g = vlv_g  #Manuel Mode g ABV-OX-230 Valve
    @vlv_h.setter
    def vlv_h(self, vlv_h):
        #print("Setting h ABV-FU-330 State")
        self._vlv_h = vlv_h  #Manuel Mode h ABV-FU-330 Valve
    @vlv_i.setter
    def vlv_i(self, vlv_i):
        #print("Setting i ABV-OX-240 State")
        self._vlv_i = vlv_i  #Manuel Mode i ABV-OX-240 Valve
    @vlv_j.setter
    def vlv_j(self, vlv_j):
        #print("Setting j ABV-FU-340 State")
        self._vlv_j = vlv_j  #Manuel Mode j ABV-FU-340 Valve
    @vlv_k.setter
    def vlv_k(self, vlv_k):
        #print("Setting k ABV-OX-250 State")
        self._vlv_k = vlv_k  #Manuel Mode k ABV-OX-250 Valve


class AbortStateClass(object):
    """The Abort State of a System determines if an 'Abort' has been tripped and the system is in maditory 'Safe' mode.
        Attributes
        ----------
        state : 'Abort' State [1]
        state[0] : 'Go' State
        state[1] : 'Abort Has Been Tripped' State
        nanny : Monitor System [1]
        """
    def __init__(self, sys_state=0, nanny=0):
        self._sys_state = sys_state  #Initiallize 'Abort' State
        self._nanny = nanny

    @property
    def sys_state(self):
        #self._state = np.asarray(self.state)
        #print("Getting State")
        return self._sys_state  #Return 'Abort' State
    @property
    def nanny(self):
        return self._nanny  #Return Nanny Mode

    @sys_state.setter
    def sys_state(self, sys_state):
        self._sys_state = sys_state  #Set 'Abort' State
    @nanny.setter
    def nanny(self, nanny):
        self._nanny = nanny  #Set Nanny Mode


if __name__ == '__main__':

    vlv = ValveStateClass()
    abt = AbortStateClass()
    '''
    #print(vlv.safe)
    print(vlv.vlv_e)
    vlv.vlv_a = 0
    print(vlv.vlv_a)
    vlv.vlv_a = 1
    print(vlv.vlv_a)
    vlv.vlv_a = 0
    print(vlv.vlv_a)

    abt = AbortStateClass()
    print(abt.state)
    abt.state = 0
    print(abt.state)
    abt.state = 1
    print(abt.state)
    abt.state = 0
    print(abt.state)

    print(vlv.vlv_state)
    print(vlv.vlv_c)
    vlv.vlv_c = 1
    print(vlv.vlv_c)
    print(vlv.vlv_state)
    #print(vlv.safe)
    #vlv.vlv_state = 1
    #print(vlv.vlv_state)

    print(vlv.vlv_e)
    vlv.vlv_a = 0
    print(vlv.vlv_a)
    vlv.vlv_a = 1
    print(vlv.vlv_a)
    vlv.vlv_a = 0
    print(vlv.vlv_a)
    '''
    print(abt.nanny)
    abt.nanny = 1
    print(abt.nanny)
