'''
Q. What is RegEx?
Ans. RegEx  stands for Regular expression. A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

'''

import re

txt = " I am Good and i am God. I eat Gud. G32dshsnxsnxnd. "
res = re.search("G.d", txt)

print(res)


print(type(res))
print(res.span())
print(res.group())


res = re.findall("a.", txt)
print(type(res))
print(res)


res = re.findall("G[1-9a-zA-Z]{0,}d", txt)
print(res)


res = re.split("\s", txt)
print(res)

res = re.sub("G[1-9a-zA-Z]{0,}d", "----", txt)
print(res)


txt = "OTP is 12345. Do not share OTP with unknown person."
otp = re.search("[0-9]{5}", txt)
if otp:
	print(otp.group())
else:
	print("No OTP")

