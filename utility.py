

import os
import PyPDF2


PROJECT_DATA_PATH = os.path.expanduser("~/Desktop/TSIClassification")

PDF_DOC_PATH = os.sep.join([PROJECT_DATA_PATH, "pdfdocs"])

TEXT_FORM_PATH = os.sep.join([PROJECT_DATA_PATH, "textform"])




DOC_CODE_NAMES = {
    "PartA" : "A - Rules for Offshore Units at fixed locations _ MODU 2021 - Part A.pdf"
}


def get_pdf_doc_path(codename):
    assert codename in DOC_CODE_NAMES, f"Invalid codename {codename}, options are ${DOC_CODE_NAMES.keys()}"
    longname = DOC_CODE_NAMES[codename]
    return os.sep.join([PDF_DOC_PATH, longname])


def get_text_form_path(codename):
    assert codename in DOC_CODE_NAMES, f"Invalid codename {codename}, options are ${DOC_CODE_NAMES.keys()}"
    return os.sep.join([TEXT_FORM_PATH, codename + ".txt"])


def get_pdf_text_pages(codename=None, filepath=None):

    assert codename is not None or filepath is not None, "You must supply either a codename= or a filepath= argument"
    docpath = get_pdf_doc_path(codename) if codename is not None else filepath

    def genpages():
        with open(docpath, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            for pob in pdf.pages:
                yield pob.extract_text()

    return list(genpages())

