import fw2kmllib
from sys import argv

if len(argv) > 1:
    tool = fw2kmllib.fw2kml()
    tool.convertFile('TestCases/timejitter.csv')
