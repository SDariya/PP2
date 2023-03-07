

import re
a1 = "abbbbbb"
b1 = re.match("a*b", a1)
print(b1)

#2
a2 = "abb"
b2 = re.match("ab{2}|b{3}", a2)
print(b2)

#3
a3 = "d_sharipkazy"
b3 = re.findall(".+_.+", a3)
print(b3)

#4
a4 = "Sharipkazy"
b4 = re.findall("[A-Z]{1}[a-z]+", a4)
print(b4)

#5
a5 = "aqwertyb"
b5 = re.match("^a.*b$", a5)
print(b5)

#6
a6 = " d tg ,. "
b6 = a6.replace(".", ":").replace(",", ":").replace(" ", ":")
print(b6)

#7
a7 = "dariya_sharipkazy"
b7 = a7.title().replace("_", "")
print(b7)

#8
a8 = "mayBeEeee"
b8 = re.split("[A-Z]", a8)
print(b8)

#9
a9 = "mayBeEeee"
b9 = re.sub(r"(\w)([A-Z])", r"\1 \2", a9)
print(b9)

#10
a10 = "sharipkazyDariya"
b10 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', a10).lower()
print(b10)