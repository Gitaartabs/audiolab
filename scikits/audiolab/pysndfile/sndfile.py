from _sndfile import sndfile_version, Format
from _sndfile import *
import _sndfile

print sndfile_version()

f = Format(type='wav')
print f

majors = available_file_formats()
print available_encoding('wav')

try:
    a = Sndfile('test1.wav')
except IOError, e:
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print e
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

a = Sndfile('test.wav')
print a
