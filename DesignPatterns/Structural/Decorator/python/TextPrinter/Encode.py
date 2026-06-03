from TextPrinter.TextPrinter import TextPrinter

class Encode(TextPrinter):

    def __init__(self, text_printer: TextPrinter):
        self.text_printer = text_printer

    def getText(self) -> str:
        return "Encoded " + self.text_printer.getText()