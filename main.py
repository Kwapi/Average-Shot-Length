
import csv
import numpy
from timecode import Timecode

# file created with DaVinci Resolve and converted here: http://www.convertcsv.com/csv-viewer-editor.htm
file = open('cmbyn.csv')

csv_f = csv.reader(file)
framerate = 23.976

next(csv_f, None)  # skip the headers

frames = []
for row in csv_f:
	duration = row[2]
	timecode = Timecode(framerate,duration)
	frames.append(timecode.frames)


print 'mean' + str(numpy.mean(frames)/framerate)
print 'median' + str(numpy.median(frames)/framerate)