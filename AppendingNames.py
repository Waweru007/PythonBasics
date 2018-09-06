names=["mike,","Tosh!", "Peter$$$", "Josh", "Jack"]

with open('test.txt', 'w+') as f:
    for item in names:
        f.write("%s\n" % item)


