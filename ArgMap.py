
import re, os, sys, fileinput, random

MAGIC_BAD_CODE = -912837465

class ArgMap:

    # Huge bug, I was previously using this statement to declare _dataMap, 
    # this way of definition made it Global for all ArgMap objects!!!
    # _dataMap = {}

    def __init__(self):
        self._dataMap = {}

    # Play nice with Java programmers
    def containsKey(self, onekey):
        return onekey in self._dataMap

    def put(self, mykey, myval):
        self._dataMap[mykey] = myval

    def getStr(self, onekey, defval=MAGIC_BAD_CODE):

        if defval == MAGIC_BAD_CODE:
          assert onekey in self._dataMap, "Required key {} not found in ArgMap".format(onekey)
        else:
          assert type(defval) == str, f"Attempt to pass a non-string default value {defval} to getStr(...) method"


        if onekey in self._dataMap:
            return self._dataMap[onekey]
        return defval


    def getDbl(self, onekey, defval=MAGIC_BAD_CODE):

        if defval == MAGIC_BAD_CODE:
          assert onekey in self._dataMap, "Required key {} not found in ArgMap".format(onekey)
        else:
          assert type(defval) == float, "Attempt to pass a non-float default value to getDbl(...) method"

        mystr = self.getStr(onekey, defval=str(defval))
        return None if mystr == None else float(mystr)


    def getInt(self, onekey, defval=MAGIC_BAD_CODE):
        if defval == MAGIC_BAD_CODE:
          assert onekey in self._dataMap, "Required key {} not found in ArgMap".format(onekey)
        else:
          assert type(defval) == int, "Attempt to pass a non-int default value to getInt(...) method"

        mystr = self.getStr(onekey, defval=str(defval))
        return None if mystr == None else int(mystr)

    def getBit(self, onekey, defval=MAGIC_BAD_CODE):
        if defval == MAGIC_BAD_CODE:
          assert onekey in self._dataMap, "Required key {} not found".format(onekey)
        else:
          assert type(defval) == bool, "Attempt to pass a non-bool default value to getBit(...) method"

        if onekey in self._dataMap:
            oneval = self._dataMap[onekey].lower()
            assert oneval == 'true' or oneval == 'false', "Expected true or false value, got {}".format(oneval)
            return oneval == 'true'

        return defval


    def size(self):
        return len(self._dataMap)

    def hasKey(self, onekey):
        return onekey in self._dataMap

    def hasKeyAssert(self, onekey):
        assert self.hasKey(onekey), "Key {} not found in datamap".format(onekey)

    def __str__(self):
        return "%s" % self._dataMap

def getFromArgv(argv):

    amap = ArgMap()

    for onearg in argv:
        if "=" in onearg:
            toks = onearg.split("=")
            amap.put(toks[0], toks[1])
            
    return amap
            
if __name__ == "__main__":

    amap = getFromArgv(sys.argv)
    
    print("Key xint = {}".format(amap.getInt('xint')))

