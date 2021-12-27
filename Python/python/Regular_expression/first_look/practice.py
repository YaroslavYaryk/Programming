import re



text = 'ahb acb aeb aeeb adcb axeb'
match = re.findall(r"a[\w]b",text) #['ahb', 'acb', 'aeb']

text = 'aba aca aea abba adca abea'
match = re.findall(r"a[\w]{2}a",text) #['abba', 'adca', 'abea']
print(match)


text = 'aba aca aea abba adca abea'
match = re.findall(r"ab[\w]a",text) #['abba', 'abea']

text = 'a1a a2a a3a a4a a5a aba aca'
match = re.findall(r"a[\d]a",text) #['a1a', 'a2a', 'a3a', 'a4a', 'a5a']

text = 'a1a, a22a, a333a, a4444a, a55555a, aba, aca'
match = re.findall(r"a[\d]+a",text) #['a1a', 'a22a', 'a333a', 'a4444a', 'a55555a']

text = 'aa a1a a22a a333a a4444a a55555a aba aca'
match = re.findall(r"a[\d]+a",text)

text = 'avb a1b a2b a3b a4b a5b abb acb'
match = re.findall(r"a[\D]b",text) #['avb', 'abb', 'acb']

text = 'ave a#b a2b a$b a4b a5b a-b acb'
match = re.findall(r"a[\W]b",text) #['a#b', 'a$b', 'a-b']

text =  'aba aea aca aza axa'
match = re.findall(r"a[bex]a", text) #['aba', 'aea', 'axa']

text = 'aba aea aca aza axa a-a a#a'
match = re.findall(r"a[^ex ]a", text) #['aba', 'aca', 'aza', 'a-a', 'a#a']

text = 'wйw wяw wёw w5w'
match = re.findall(r"w[а-я]w", text) #['wйw', 'wяw']

text = 'ааа ббб ёёё ззз ййй ААА Б18Б ЁЁЁ ЗЗ5З5 ЙЙЙ'
match = re.findall(r"[а-яА-Я]+", text) #['ааа', 'ббб', 'ззз', 'ййй', 'ААА', 'Б', 'Б', 'ЗЗ', 'З', 'ЙЙЙ']

# print(match)