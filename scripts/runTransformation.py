import os
import argparse

from utils.logutils import log_message

def main( ):
    parser = argparse.ArgumentParser(description="utility for taking model as input and then process model as pre-defined methods")

    parser.add_argument('--modelname', dest='modelname', required=True,  help='Input Model Name for processing the feed file')
    parser.add_argument('--businessdate', dest='businessdate', required=True, help='businessdate for which you want to process the data. run date')
    parser.add_argument('--mode', dest='mode', default=",", required=True, help='mode as dev, qa, prod ')

    args = parser.parse_args()

    modelname    = args.modelname
    businessdate = args.businessdate
    mode         = args.mode

    log_message("+++++++++++++++++++++++++++++++ Main Program starts from here +++++++++++++++++++++++++++++++  ", "INFO")

if __name__ == '__main__':

    main()