#!/usr/bin/env python

"""Unit tests for tools.py
"""

# version
__id__ = '$Id: testtools.py 1332 2010-11-04 22:50:16Z farrowch $'

import os
import unittest
import numpy

# useful variables
thisfile = locals().get('__file__', 'file.py')
tests_dir = os.path.dirname(os.path.abspath(thisfile))
testdata_dir = os.path.join(tests_dir, 'testdata')

import diffpy.pdfmorph.tools as tools

##############################################################################
class TestTools(unittest.TestCase):

    def setUp(self):
        objfile = os.path.join(testdata_dir, "nickel_ss0.01.cgr")
        self.xobj, self.yobj = numpy.loadtxt(objfile, unpack = True)
        self.rho0 = 0.0917132
        return

    def test_estimateBaselineSlope(self):
        """check estimateBaselineSlope() using calculated data
        """
        slope = tools.estimateBaselineSlope(self.xobj, self.yobj)
        slopecalc = -4 * numpy.pi * self.rho0
        self.assertAlmostEqual(slopecalc, slope, 2)
        return

    def test_estimateScale(self):
        """check estimateScale() using calculated data
        """
        import random
        x = random.random()
        scale = tools.estimateScale(self.yobj, x * self.yobj)
        self.assertAlmostEquals(x, scale)
        return


# End of class TestRoutines

if __name__ == '__main__':
    unittest.main()

# End of file
