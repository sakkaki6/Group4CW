import re

class TextFormatter:
    def __init__(self, text) -> None:
        self.text = text

    # def replace_date(self):
    #     regex = re.compile(r'[0-3]{1}[0-9]{1}/[0-1]?[0-9]{1}/\d{4}')

    #     for i in regex.findall(self.text):
    #         s = i[::-1]

    #     new_text = re.sub(regex, s,self.text)
    #     return new_text
    
    def replace_date(self):
        date_pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
        self.text = date_pattern.sub(r'\3/\2/\1', self.text)
        return self.text
    
    def find_all_urls(self):
        # regex = re.compile(r'^https')
        regex = r'((http|https)://)(www.)? + [a-zA-Z0-9@:%._\\+~#?&//=] + {2,256}\\.[a-z] + {2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)'
        return regex.findall(self.text)

s = TextFormatter('https: Ali in 20/12/2023 has borned https')
print(s.replace_date())

print(s.find_all_urls())

