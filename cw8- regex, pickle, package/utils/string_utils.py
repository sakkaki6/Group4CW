class StringUtils:
    def __init__(self,text) -> None:
        self.text = text

    def upper(self):
        return self.text.upper()

    def lower(self):
        return self.text.lower()

    def title(self):
        return self.text.title()

    def swapcase(self):
        return self.text.swapcase()

    def capittalize(self):
        return self.text.capitalize()