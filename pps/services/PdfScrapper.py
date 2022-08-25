import re
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

class PdfScrapper:

    @staticmethod
    def readFile(fname, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        infile = open(f"./assets/pdf/{fname}.pdf", 'rb')

        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)

        infile.close()
        converter.close()

        text = output.getvalue()

        output.close

        return text

    def getData(txt, *keys):
        # "2118\w+"gm
        
        data = {}

        if 'stId' in keys:
            s = re.search("2118\w+", txt)
            data["id"] = s.group()

        if 'github' in keys:
            s = re.search("https://github\S+", txt)
            data["git"] = s.group()

        return data
        