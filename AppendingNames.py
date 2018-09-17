names=["mike,","Tosh!", "Peter$$$", "Josh", "Jack"]
# cd .. && ./opt/lampp/manager-linux-x64.run

with open('test.txt', 'w+') as f:
    for item in names:
        f.write("%s\n" % item)


