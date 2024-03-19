
import os
import sys
import json
import zipfile
import sqlite3
import ArgMap

class HelloWorldTool:
    def run_op(self, argmap):

        print("hello, world")


def lookup_tool(probe):

    options = [thing for thing in dir(sys.modules[__name__]) if thing.endswith("Tool")]

    hits = [thing for thing in options if probe == thing or probe + "Tool" == thing]
    assert len(hits) > 0, "Failed to find the tool, options are {}".format(options)

    try: 
        return eval(f"{hits[0]}()")
    except:
        print("Error instantiating the tool")
        assert False, "Failed to find a good tool"


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(f"Usage: python3 entry_point.py TOOL_NAME arg1=val1 arg2=val2 ...")
        print("You must supply at least the tool name")
        quit()

    toolitem = lookup_tool(sys.argv[1])
    argmap = ArgMap.getFromArgv(sys.argv[2:])

    # U.set_fast_mode(argmap)

    toolitem.run_op(argmap)
