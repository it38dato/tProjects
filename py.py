# fr - read file
# fo - output file
# fw - write file
# l - line
# rt - replace tab
tags=["<p>","</p>","<strong>","</strong>","</br>","&nbsp"]
#print(tags[2])
fr = open("text.txt", "r") 
#fo=fr.read()
#print(fo)
fe = open("editor.txt", "w")
#fe.write(fo)
for l in fr:
    #print(l, end="")   
    rt=l.replace("    ", tags[5])
    fe.write(rt)
for l in fr:
    #print(l, end="")   
    rt=l.replace("    ", tags[5])    
    fe.write(rt)
    rn=l.join([l.strip() + tags[4]])
    fe.write(rn)
fe.close()
fr.close()
