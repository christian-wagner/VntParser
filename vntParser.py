import argparse
import os

def vntParser(inputfolder, outputfolder):
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    inputfilesnames = os.listdir(inputfolder)

    for inputfilename in inputfilesnames:
        inputfile = open(os.path.join(inputfolder, inputfilename), "r")
        lines = inputfile.readlines()

        for line in lines:
            if line.startswith("BODY"):
                text = line[line.index(":") + 1:]
                text = text.replace("=0A", "\n")
                text = text.replace("=C3=BC", "ü").replace("=C3=A4", "ä").replace("=C3=B6", "ö")
                text = text.replace("=C3=9C", "Ü").replace("=C3=84", "Ä").replace("=C3=96", "Ö")
                text = text.replace("=3D", "=")


                outputfile = open(os.path.join(outputfolder, os.path.splitext(inputfilename)[0]+".txt"), "w")
                outputfile.write(text)
                outputfile.close()

                inputfile.close()

                break


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Script to parse VNT files to TXT files.')
    parser.add_argument('--inputfolder', dest='inputfolder', action='store', help='Input folder that contains VNT files to parse', type=str)
    parser.add_argument('--outputfolder', dest='outputfolder', action='store',
                        help='Output folder to put resulting TXT files into',
                        required=True, type=str)

    args = parser.parse_args()

    vntParser(args.inputfolder, args.outputfolder)