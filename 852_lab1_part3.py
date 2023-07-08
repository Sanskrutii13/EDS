from datetime import datetime

f1=open("852_sanskruti.csv","r")
c=f1.read()
data=c.splitlines()

eid=[]
name=[]
pos=[]
loc=[]
sal=[]
dob=[]

for line in data:
    word=line.split(",")
    eid.append(int(word[0]))
    name.append(word[1])
    pos.append(word[2])
    loc.append(word[3])
    sal.append(int(word[4]))
    dob.append(word[5])

print("Maximum salary:",name[sal.index(max(sal))],max(sal))
print("Minimum salary:",name[sal.index(min(sal))],min(sal))
print("Total salary:",sum(sal))
print("Average salary:",(sum(sal)/len(eid)))

today=datetime.today()
print(today)
for d in dob:
    
    ed=datetime.strptime(d,'%m/%d/%Y').date()
    print("age of emp:",(today.year-ed.year))

for s in sal:
    sd=s/82
    print("Salary in dollers:",sd,"$")





    
