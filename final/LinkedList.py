#!/usr/bin/env python

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    #print("Inserting %s & %s" % (atMe.myName() ,newFrob.myName() ) )
    #print("A")
    if atMe.getBefore() is None and atMe.getAfter() is None:
        #print("A")
        if newFrob.myName() < atMe.myName():
            #print("%s < %s" % ( newFrob.myName(), atMe.myName() ))
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        else:
            #print("%s > %s" % ( newFrob.myName(), atMe.myName() ))
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        return
    
#    #print("Z")
#    #print atMe.myName() ,newFrob.myName()
#    if atMe.myName() == newFrob.myName():
#        #print("Z.2")
#        atMeBefore = atMe.getBefore()
#        if atMe.getBefore():
#            atMeBefore.setAfter(newFrob)
#            newFrob.setBefore(atMeBefore)
#        atMe.setBefore(newFrob)
#        newFrob.setAfter(atMe)
#        return
        
    #print("B")
    #print atMe.getBefore() ,newFrob.myName() , atMe.myName()
    if atMe.getBefore() is None and newFrob.myName() < atMe.myName():
        #print("B")
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)
        return
            
    #print("C")
    if atMe.getAfter() is None and newFrob.myName() > atMe.myName():
        #print("C")
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
        return
    
    #print("D")
    if newFrob.myName() > atMe.myName() and newFrob.myName() > atMe.getAfter().myName():
        #print("D")
        insert(atMe.getAfter(), newFrob)
        return
    
    #print("E")
    if newFrob.myName() < atMe.myName() and newFrob.myName() < atMe.getBefore().myName():
        #print("E")
        insert(atMe.getBefore(), newFrob)
        return
        
    
    #print("F")
    #print "Before F: ", atMe.myName() , newFrob.myName() 
    if atMe.getAfter() and (atMe.myName() >= newFrob.myName() >= atMe.getAfter().myName()):
        #print("F")
        afterAtme = atMe.getAfter()
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
        newFrob.setAfter(afterAtme)
        afterAtme.setBefore(newFrob)
        return
        
    #print("G")
    if atMe.getBefore() and (atMe.getBefore().myName() <= newFrob.myName() <= atMe.myName()):
        #print("G")
        beforeAtme = atMe.getBefore()
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)
        newFrob.setBefore(beforeAtme)
        beforeAtme.setAfter(newFrob)
        return
    #print("Abandoning %s & %s" % (atMe.myName() ,newFrob.myName() ) )
    
def findFront(frob):
    print("Checking %s" % frob.myName())
    #print("Previous is %s" % frob.getBefore())
    if frob.getBefore() is None:
        #print("Returning %s" % frob.myName())
        return frob
    else:
        return findFront(frob.getBefore())

eric = Frob('eric')
andrew = Frob('andrew')
beto= Frob('beto')
abby= Frob('abby')
fred = Frob('fred')
gabby= Frob('gabby')
martha = Frob('martha')
ruth = Frob('ruth')
zara= Frob('zara')
xander= Frob('xander')
#insert(eric, andrew)
#insert(andrew, fred)
#insert(fred, martha)
#insert(martha, ruth)
beto = Frob('beto')
beto2 = Frob('beto')
abby = Frob('abby')
abby2 = Frob('abby')
insert(xander, beto)
insert(xander, abby)
insert(xander, abby2)
insert(xander, beto2)

p = Frob('percival')
r = Frob('rupert')
insert(p, r)

print findFront(p)
print findFront(r)

#next_elem = xander
#while next_elem:
# print next_elem.myName()
# next_elem = next_elem.getBefore()
