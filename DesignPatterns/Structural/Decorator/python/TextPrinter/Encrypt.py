from TextPrinter.TextPrinter import TextPrinter

class Encrypt(TextPrinter):

    def __init__(self, text_printer: TextPrinter):
        self.text_printer = text_printer

    def getText(self) -> str:
        return "Encrypted " + self.text_printer.getText()