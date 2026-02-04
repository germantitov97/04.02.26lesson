# both counts how many digits are in the text
text: str = "Hello, World!!"
print(len("Hello, World!!"))
print(len(text))

# remove spaces from the start and the end of the text
text1: str = "   Hello, World!!   "
print(text.strip())

# making the text to be in lower cases
text2: str = "Hello, World!!"
print(text2.lower())

# making the text to be in upper cases
text3: str = "Hello, World!!"
print(text3.upper())


text4: str = "Hello, World!!"
# replaces the "world" with "python"
print(text4.replace("World", "Python"))
# replace the "l" to "t"
print(text4.replace("l", "t"))
# replace "t" to empty (erase it)
print(text4.replace("t", ""))

# split the text in each space and add []
text5: str = "Hello, World!! good morning"
print(text5.split())
# split the text on each '*' and add []
text5 = "Hello,*World!!*good*morning"
print(text5.split('*'))

# swap the cases on the second "AasdasBcccC" to "aASDASbCCCc"
print('"AasdasBcccC".swapcase()', "AasdasBcccC".swapcase())

