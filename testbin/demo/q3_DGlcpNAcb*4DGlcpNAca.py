import sys
sys.path.insert(0, '../../')
import gmml
temp = gmml.Assembly()

temp.ExtractOntologyInfoByOligosaccharideNameSequenceByRegex(sys.argv[1], "DGlcpNAcb*4DGlcpNAca")

