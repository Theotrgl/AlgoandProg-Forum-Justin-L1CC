#Number 2

f=open("Text.txt", mode="r",encoding="utf-8")
new=open("New_Text.txt",mode="x",encoding="utf-8")

Lines=f.read().split('\n')
Counter=1
for Lines in Lines:
    new.write(str(Counter)+" "+Lines+'\n')
    Counter += 1
new.close()
#%%
#Number 3
file=open("Text.txt",mode="r",encoding="utf-8")
text = file.readlines()

words = 0
for n in text:
    word = n.split()
    for m in word:
        words += 1


letters = 0
for x in text:
    letter = x.split()
    for y in letter:
        for z in y:
            letters += 1

print(f"The average word length is: {letters/words}")

file.close()

# %%

#Number 4

file=open("Miyagi.txt",mode="r",encoding="utf-8")
text=file.read().split()
exceptions=["Mr.","Ms.","Jr.","Mrs.","Dr."]
new_text=""

for words in text:
    if "?" not in words and "!" not in words:
        new_text+=(words + " ")
        if words not in exceptions and "." in words.split(" "):
            pass
        if words not in exceptions and "." in words[-1]:
            new_text+="\n"
    else:
        new_text+=(words+"\n")

print(new_text)
# %%
