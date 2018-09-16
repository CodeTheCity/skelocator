# Calculate coordinate translation scale, shift and rotation

from math import sqrt, atan, degrees

def dist(pt1, pt2):
    return sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

refs= [] #list of sloth coords of ref points

scale = mean([dist(refs[n], refs[n+1]) for n in xrange(len(refs)-1)])

shift = refs[0]

rot = atan((refs[-1][0]-refs[0][0])/(refs[-1][1]-refs[0][1]))


print "scale: ", scale
print "shift: ", shift
print "rot: ", degrees(rot)
