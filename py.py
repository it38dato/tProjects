tags=["<p>","</p>","<strong>","</strong>","<br>","&nbsp;&nbsp;&nbsp;"]
#print(tags[2])
with open("text.txt") as fe:
    fr = fe.read()
    #print(fr)
rtn = fr.replace("    ", tags[5]).replace("\n", tags[4])
#print(rtn)
#print(tags[0], rtn, tags[1])
rtn1 = tags[0]+rtn+tags[1]
#print(rtn1)
with open("output.txt", "w") as fe:
    fe.write(rtn1+"\n")
