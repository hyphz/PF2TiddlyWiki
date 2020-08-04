
import os
import datetime

infile = open("pf2bgs.csv")

specials = ["Charlatan", "Scout"]

for line in infile:
    line=line.rstrip()
    parts=line.split(",")
    if (parts[0] in specials):
        parts[0] = parts[0] + " (Background)"
    if (os.path.isfile("..\\tiddlers\\" + parts[0] + ".tid")):
        print(parts[0],"already exists.")
    else:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%f")[:-1]
        outfile = open("..\\tiddlers\\" + parts[0] + ".tid","w")
        print("created:",timestamp, file=outfile)
        if parts[1] < parts[2]:
            astat = parts[1]
            bstat = parts[2]
        else:
            astat = parts[2]
            bstat = parts[1]
        print("bg-stata:",astat,file=outfile)
        print("bg-statb:",bstat,file=outfile)
        print("tags: Background",file=outfile)
        print("title:",parts[0],file=outfile)
        print("bg-feat:",parts[5],file=outfile)
        skills = parts[3].split(" or ")
        skills = map(lambda x: "[[" + x + "]]", skills)
        print("bg-skill:",' '.join(skills),file=outfile)
        print("bg-lore:",parts[4],file=outfile)
        print("bg-src:",parts[6],file=outfile)
        print("type: text/vnd.tiddlywiki",file=outfile)
        print(file=outfile)
        print("{{||BackgroundSummary}}",file=outfile)
        outfile.close()
        print(parts[0],"..")
        
    
infile.close()
