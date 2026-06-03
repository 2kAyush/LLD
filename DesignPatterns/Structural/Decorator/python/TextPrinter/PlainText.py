from TextPrinter.TextPrinter import TextPrinter

class PlainText(TextPrinter):
    def __init__(self, text):
        self.text = text

    def getText(self) -> str:
        return "Plain " + self.text