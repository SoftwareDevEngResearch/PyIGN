# limits.py
import numpy as np

class PTLimits(object):
    """The Pressure Transducer Limits determine when 'Safe' mode breaks.

        Attributes
        ----------
        pt : pressure transducers [7]
        a : pressure transducer PT-OX-110
        b : pressure transducer PT-FU-120
        c : pressure transducer PT-OX-210
        d : pressure transducer PT-FU-310
        e : pressure transducer PT-OX-220
        f : pressure transducer PT-FU-320
        g : pressure transducer PT-CC-410
        """
    def __init__(self, pt_a=800, pt_b=800, pt_c=800, pt_d=800, pt_e=750, pt_f=750, pt_g=900):
        self._pt_a = pt_a
        self._pt_b = pt_b
        self._pt_c = pt_c
        self._pt_d = pt_d
        self._pt_e = pt_e
        self._pt_f = pt_f
        self._pt_g = pt_g
        self._pt_limits = [pt_a, pt_b, pt_c, pt_d, pt_e, pt_f, pt_g]  #Pressure Transducers

    @property
    def pt_limits(self):
        self._pt_limits = [self._pt_a, self._pt_b, self._pt_c, self._pt_d, self._pt_e, self._pt_f, self._pt_g]
        return self._pt_limits
    @property
    def pt_a(self):
        return self._pt_a #Pressure Transducer a PT-OX-110
    @property
    def pt_b(self):
        return self._pt_b #Pressure Transducer b PT-FU-120
    @property
    def pt_c(self):
        return self._pt_c #Pressure Transducer c PT-OX-210
    @property
    def pt_d(self):
        return self._pt_d #Pressure Transducer d PT-FU-310
    @property
    def pt_e(self):
        return self._pt_e #Pressure Transducer e PT-OX-220
    @property
    def pt_f(self):
        return self._pt_f #Pressure Transducer f PT-FU-320
    @property
    def pt_g(self):
        return self._pt_g #Pressure Transducer g PT-CC-410

    @pt_a.setter
    def pt_a(self, pt_a):
        self._pt_a = pt_a  #Set Pressure Transducer a PT-OX-110 Limit
    @pt_b.setter
    def pt_b(self, pt_b):
        self._pt_b = pt_b  #Set Pressure Transducer b PT-FU-120 Limit
    @pt_c.setter
    def pt_c(self, pt_c):
        self._pt_c = pt_c  #Set Pressure Transducer c PT-OX-210 Limit
    @pt_d.setter
    def pt_d(self, pt_d):
        self._pt_d = pt_d  #Set Pressure Transducer d PT-FU-310 Limit
    @pt_e.setter
    def pt_e(self, pt_e):
        self._pt_e = pt_e  #Set Pressure Transducer e PT-OX-220 Limit
    @pt_f.setter
    def pt_f(self, pt_f):
        self._pt_f = pt_f  #Set Pressure Transducer f PT-FU-320 Limit
    @pt_g.setter
    def pt_g(self, pt_g):
        self._pt_g = pt_g  #Set Pressure Transducer g PT-CC-410 Limit


class TCLimits(object):
    """The Thermocouple Limits determine when 'Safe' mode breaks.

        Attributes
        ----------
        t : thermocouple [12]
        a : thermocouple T-OX-210
        b : thermocouple T-FU-310
        c : thermocouple T-OX-220
        d : thermocouple T-OX-230
        e : thermocouple T-OX-240
        f : thermocouple T-OX-250
        g : thermocouple T-FU-320
        h : thermocouple T-OX-260
        i : thermocouple T-OX-270
        j : thermocouple T-CC-410
        k : thermocouple T-CC-420
        l : thermocouple T-CC-430
        """
    def __init__(self, tc_a=83, tc_b=303, tc_c=73, tc_d=73, tc_e=73, tc_f=73, tc_g=303, tc_h=73, tc_i=73, tc_j=573, tc_k=573, tc_l=573):
        self._tc_a = tc_a
        self._tc_b = tc_b
        self._tc_c = tc_c
        self._tc_d = tc_d
        self._tc_e = tc_e
        self._tc_f = tc_f
        self._tc_g = tc_g
        self._tc_h = tc_h
        self._tc_i = tc_i
        self._tc_j = tc_j
        self._tc_k = tc_k
        self._tc_l = tc_l
        self._tc_limits = [tc_a, tc_b, tc_c, tc_d, tc_e, tc_f, tc_g, tc_h, tc_i, tc_j, tc_k, tc_l]  #Thermocouple

    @property
    def tc_limits(self):
        self._tc_limits = [self._tc_a, self._tc_b, self._tc_c, self._tc_d, self._tc_e, self._tc_f, self._tc_g, self._tc_h, self._tc_i, self._tc_j, self._tc_k, self._tc_l]
        return self._tc_limits
    @property
    def tc_a(self):
        return self._tc_a #Thermocouple a T-OX-210
    @property
    def tc_b(self):
        return self._tc_b #Thermocouple b T-FU-310
    @property
    def tc_c(self):
        return self._tc_c #Thermocouple c T-OX-220
    @property
    def tc_d(self):
        return self._tc_d #Thermocouple d T-OX-230
    @property
    def tc_e(self):
        return self._tc_e #Thermocouple e T-OX-240
    @property
    def tc_f(self):
        return self._tc_f #Thermocouple f T-OX-250
    @property
    def tc_g(self):
        return self._tc_g #Thermocouple g T-FU-320
    @property
    def tc_h(self):
        return self._tc_h #Thermocouple h T-OX-260
    @property
    def tc_i(self):
        return self._tc_i #Thermocouple i T-OX-270
    @property
    def tc_j(self):
        return self._tc_j #Thermocouple j T-CC-410
    @property
    def tc_k(self):
        return self._tc_k #Thermocouple k T-CC-420
    @property
    def tc_l(self):
        return self._tc_l #Thermocouple l T-CC-430

    @tc_a.setter
    def tc_a(self, tc_a):
        self._tc_a = tc_a  #Set Thermocouple a T-OX-210 Limit
    @tc_b.setter
    def tc_b(self, tc_b):
        self._tc_b = tc_b  #Set Thermocouple b T-FU-310 Limit
    @tc_c.setter
    def tc_c(self,tc_c):
        self._tc_c = tc_c  #Set Thermocouple c T-OX-220 Limit
    @tc_d.setter
    def tc_d(self, tc_d):
        self._tc_d = tc_d  #Set Thermocouple d T-OX-230 Limit
    @tc_e.setter
    def tc_e(self, tc_e):
        self._tc_e = tc_e  #Set Thermocouple e T-OX-240 Limit
    @tc_f.setter
    def tc_f(self, tc_f):
        self._tc_f = tc_f  #Set Thermocouple f T-OX-250 Limit
    @tc_g.setter
    def tc_g(self, tc_g):
        self._tc_g = tc_g  #Set Thermocouple g T-FU-320 Limit
    @tc_h.setter
    def tc_h(self,tc_h):
        self._tc_h = tc_h  #Set Thermocouple h T-OX-260 Limit
    @tc_i.setter
    def tc_i(self, tc_i):
        self._tc_i = tc_i  #Set Thermocouple i T-OX-270 Limit
    @tc_j.setter
    def tc_j(self, tc_j):
        self._tc_j = tc_j  #Set Thermocouple j T-CC-410 Limit
    @tc_k.setter
    def tc_k(self, tc_k):
        self._tc_k = tc_k  #Set Thermocouple k T-CC-420 Limit
    @tc_l.setter
    def tc_l(self, tc_l):
        self._tc_l = tc_l  #Set Thermocouple l T-CC-430 Limit


class LCLimits(object):
    """The Load Cell Limits determine when 'Safe' mode breaks and propellant tank levels.

        Attributes
        ----------
        lc : load cell [3]
        a : load cell LC-OX-210
        b : load cell LC-FU-310
        c : load cell LC-CC-410
        """
    def __init__(self, lc_a=600, lc_b=600, lc_c=3000):
        self._lc_a = lc_a
        self._lc_b = lc_b
        self._lc_c = lc_c
        self._lc_limits = [lc_a, lc_b, lc_c]  #Load Cells

    @property
    def lc_limits(self):
        self._lc_limits = [self._lc_a, self._lc_b, self._lc_c]
        return self._lc_limits
    @property
    def lc_a(self):
        return self._lc_a #Load Cell a LC-OX-210
    @property
    def lc_b(self):
        return self._lc_b #Load Cell b LC-FU-310
    @property
    def lc_c(self):
        return self._lc_c #Load Cell c LC-CC-410

    @lc_a.setter
    def lc_a(self, lc_a):
        self._lc_a = lc_a  #Set Load Cell a LC-OX-210 Limit
    @lc_b.setter
    def lc_b(self, lc_b):
        self._lc_b = lc_b  #Set Load Cell a LC-FU-310 Limit
    @lc_c.setter
    def lc_c(self,lc_c):
        self._lc_c = lc_c  #Set Load Cell a LC-CC-410 Limit





if __name__ == '__main__':
    '''
    lcl = LCLimits()
    print(lcl.lc_limits)
    print(lcl.lc_a)
    lcl.lc_a = 1
    print(lcl.lc_a)
    print(lcl.lc_limits)
    tcl = TCLimits()
    print(tcl.tc_limits)
    print(tcl.tc_a)
    tcl.tc_a = 1
    print(tcl.tc_a)
    print(tcl.tc_limits)
    ptl = PTLimits()
    print(ptl.pt_limits)
    print(ptl.pt_c)
    ptl.pt_c = 1
    print(ptl.pt_c)
    print(ptl.pt_limits)
    '''
