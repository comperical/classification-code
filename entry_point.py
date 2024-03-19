
import os
import sys
import json
import zipfile
import sqlite3
import ArgMap

# This is an installation requirement
import PyPDF2
import utility as U


class ConvertBasicTool:
    def run_op(self, argmap):


        print(f"The folder base is {U.PROJECT_DATA_PATH}")
        print(f"The PDF base is {U.PDF_DOC_PATH}")

        codename = argmap.getStr("codename")
        longpath = U.get_pdf_doc_path(codename)
        print(f"Going to convert file {codename}, path {longpath}, to text")

        pagelist = U.get_pdf_text_pages(codename=codename)
        print(f"Got {len(pagelist)} pages from the PDF")

        textpath = U.get_text_form_path(codename)
        with open(textpath, 'w') as fh:
            for page in pagelist:
                fh.write(page)
                fh.write("\n")

        print(f"Wrote {len(pagelist)} pages for code name {codename} to {textpath}")


class HelloWorldTool:
    def run_op(self, _):
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
