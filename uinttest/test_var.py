
'''
# new Test_Var for every test method
'''

import unittest
import HtmlTestRunner
import time
import os
import sys
import logging

g_var = -1

class Test_Var(unittest.TestCase):
    def setUp(self):
        self.var = -1
        pass

    def tearDown(self):
        pass


    def test_1(self):
        global g_var
        logging.warning('\n\n*************************** test_1 *****************************')

        self.assertEqual(g_var, -1, 'g_var=%d'%g_var)
        self.assertEqual(self.var, -1, 'self.var=%d'%self.var)

        g_var = 2
        self.var = 2

    def test_2(self):
        global g_var
        logging.warning('\n\n*************************** test_1 *****************************')

        self.assertEqual(g_var, 2, 'g_var=%d' % g_var)
        self.assertEqual(self.var, 2, 'self.var=%d' % self.var)

if __name__ == '__main__':
    print('enter')
    test_report = './report'
    argTmp = sys.argv[0]
    if len(sys.argv) > 1:
        test_report = sys.argv[1]
        sys.argv = []
        sys.argv.append(argTmp)

    log_path = test_report + '/log/'
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logging.basicConfig(filename=log_path + argTmp + ".log",
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        level=logging.DEBUG)
    logging.info('begin')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=test_report))
    logging.info('end')
    print('exit')