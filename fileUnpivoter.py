from fileLib import *
csv = CSV("migr_asyappctza.tsv","r+")
liste = csv.explode("\t")[0][1:]
print len(csv.explode("\t"))
print csv.fileArrayExploded[1]
csv.close()
f = open("migr_asyappctza_unpivot.csv","w+")
f.write("citizen;sex;unit;age;asyl_app;geo;time;amount")
for i in csv.fileArrayExploded[1:]:
    string = replace(i[0],",",";")
    string1 = "\n" + string
    for j in range(1, len(i)):
        string += ";" + liste[j - 1] + ";" + replace(strip(i[j],"p"),":","N/A")
        if j + 1 < len(i): string += string1
    f.write(string+"\n")
f.close()
        
