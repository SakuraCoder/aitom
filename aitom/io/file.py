'''
Functions for reading and writing common files
'''

import aitom.io.mrcfile_proxy as TIM

def read_mrc_data(path, show_progress=False):
    #return read_mrc(path=path, show_progress=show_progress)['value']
    return TIM.read_data(path)

import aitom.tomominer.io.file as ATIF
def read_mrc_header(path):
    return ATIF.read_mrc(path=path, read_data=False)['header']

'''
Calculate voxel spacing 
from the mrc header obtained from read_mrc_header
in Angstrom unit
'''
def get_mrc_voxel_spacing(im):
    return (im['header']['MRC']['xlen'] / im['header']['MRC']['nx'])

def put_mrc(mrc, path, overwrite=False):
    put_mrc_data(mrc,path, overwrite=overwrite)

def put_mrc_data(mrc,path, overwrite=False):
    TIM.write_data(data=mrc,path=path, overwrite=overwrite)

