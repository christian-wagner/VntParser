#!python3
import argparse
import os
import quopri
import codecs

def vntParser(inputfolder, outputfolder):
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)
    inputfilesnames = os.listdir(inputfolder)

    for inputfilename in inputfilesnames:
        if inputfilename.lower().endswith('.vnt'):
            inputfile = open(os.path.join(inputfolder, inputfilename), "r")
            lines = inputfile.readlines()
            # note that in vnt files only body line contains your actual text
            for line in lines:
                if line.startswith("BODY"):
                    text = line[line.index(":") + 1 :]
                    text = str(quopri.decodestring(text, header=False),'utf-8') # convert from quoted-printable to unencoded stream then to utf-8
                    outputfile = codecs.open(os.path.join(outputfolder, os.path.splitext(inputfilename)[0]+".txt"), "w", "utf-8") # save as utf-8 file
                    outputfile.write(text)
                    outputfile.close()
                    inputfile.close()
                    break

# call from command prompt
if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description='Script to parse VNT files to TXT files.')
    parser.add_argument('--inputfolder', dest='inputfolder', action='store', help='Input folder that contains VNT files to parse', type=str)
    parser.add_argument('--outputfolder', dest='outputfolder', action='store', help='Output folder to put resulting TXT files into', required=True, type=str)
    args = parser.parse_args()
    vntParser(args.inputfolder, args.outputfolder)
