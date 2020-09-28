######################################################
##Author:  Kellie McGuire     kellie@kelliejensen.com
##
##Saves FITS data to a .txt file
######################################################

import numpy as np
from astropy.io import fits
import os.path
from os import path
import sys


def fits_to_txt(fitsfile):


    ###Create an array of the data from FITS file
    hdulist = fits.open(fitsfile)
    hdulist.info()
    data = hdulist[0].data

    ###Shape options for the data
    data = data.T   #Transpose the data
    #length = len(data[0])*len(data)
    #data = np.reshape(data, (length,1))  #Reshape to be a single column

    ###Save data to a .txt file
    # directory, filename = os.path.split(fitsfile)
    # datafile = os.path.splitext(filename)[0]
    # f=open(os.path.join(datafile + ".txt"),'w')
    #
    # for r in data:
    #     f.write(" ".join([str(c) for c in r]) + "\n")
    #
    #
    #
    # f.close()
    hdulist.close()

    return(data)


if __name__ == '__main__':

    if len(sys.argv)<2:

        print("Error: first argument must be a FITS file")
        exit(1)

    if path.exists(sys.argv[1]):
        if sys.argv[1].endswith('.fits'):
            fitsfile = sys.argv[1]
        else:
            print("Enter a valid FITS file")
            exit(1)

    else:
        print("Enter a valid FITS file")
        exit(1)

    fits_to_txt(fitsfile)
