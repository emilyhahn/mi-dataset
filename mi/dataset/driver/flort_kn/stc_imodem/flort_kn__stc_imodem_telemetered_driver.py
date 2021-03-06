from mi.dataset.parser.flort_kn__stc_imodem import Flort_kn_stc_imodemParser
from mi.dataset.dataset_driver import DataSetDriver
from mi.dataset.dataset_parser import DataSetDriverConfigKeys

def parse(basePythonCodePath, sourceFilePath, particleDataHdlrObj):
    with open(sourceFilePath,"r") as fil :
        parser = Flort_kn_stc_imodemParser(
            {DataSetDriverConfigKeys.PARTICLE_MODULE:"mi.dataset.parser.flort_kn__stc_imodem",DataSetDriverConfigKeys.PARTICLE_CLASS:"Flort_kn_stc_imodemParserDataParticleTelemetered"},
            None,
            fil,
            lambda state,file : None,
            lambda state : None)
        driver = DataSetDriver(parser, particleDataHdlrObj)
        driver.processFileStream()
    return particleDataHdlrObj
