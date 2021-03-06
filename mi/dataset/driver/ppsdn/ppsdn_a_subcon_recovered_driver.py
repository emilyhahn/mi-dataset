#!/usr/bin/env python

"""
@package mi.dataset.driver.ppsdn_a_subcon
@file marine-integrations/mi/dataset/driver/ppsdn/ppsdn_a_subcon_recovered_driver.py
@author Rachel Manoni
@brief Driver for the ppsdn_a_subcon instrument

Release notes:

Initial Release
"""

from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.ppsdn_a_subcon import PpsdnASubconParser


def parse(basePythonCodePath, sourceFilePath, particleDataHdlrObj):
    """
    This is the method called by Uframe
    :param basePythonCodePath This is the file system location of mi-dataset
    :param sourceFilePath This is the full path and filename of the file to be parsed
    :param particleDataHdlrObj Java Object to consume the output of the parser
    :return particleDataHdlrObj
    """
    with open(sourceFilePath, 'r') as stream_handle:
        driver = PpsdnASubconRecoveredDriver(basePythonCodePath, stream_handle, particleDataHdlrObj)
        driver.processFileStream()
    return particleDataHdlrObj


class PpsdnASubconRecoveredDriver(SimpleDatasetDriver):
    """
    Derived driver class
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        parser_config = {
            DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.ppsdn_a_subcon',
            DataSetDriverConfigKeys.PARTICLE_CLASS: 'PpsdnASubconInstrumentDataParticle'
        }

        # The parser inherits from simple parser - other callbacks not needed here
        parser = PpsdnASubconParser(parser_config,
                                    stream_handle,
                                    self._exception_callback)

        return parser
