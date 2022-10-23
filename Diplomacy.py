class Army:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.troops=1

    def __str__(self):
        return self.name+' '+str(self.location)
        #return self.name+' '+str(self.location)+' '+str(self.troops)

    def newMovement(self,dict,location,newAction,alt=None):
        if newAction=='Hold':return
        elif newAction=='Support':
            self.support(dict,alt)
            return
        elif newAction=='Move':
            self.move(alt)
            return

    def support(self,dict,recipient):
        if recipient in dict:
            dict[recipient].troops+=1

    def move(self,newLocation):
        self.location=newLocation

    def die(self):
        if self.troops==0:self.location='[dead]'

def print_dict(d):
    for key in d:
        print(d[key])

def inputs(*i):
    #inp=inputs()
    ###make a loop function that reads everything in input and automatically appends them to lis###
    setup("hi")

def setup(s):
    lis=[]
    d={}
    s1="A Madrid Hold"
    lis.append(s1)
    s2="B Barcelona Move London"
    lis.append(s2)
    s3="C Paris Support B"
    lis.append(s3)

    for x in range(len(lis)):                   #commence movements
        lis[x]=lis[x].split()                   #lis[x] is the string input (ex. A Madrid Hold)
        temp=lis[x][0]                          #lis[x][0] is the name of the army (ex. A), lis[x][1] is the location (ex. Madrid)
        d[temp]=Army(lis[x][0],lis[x][1])       #d[temp] is the army object
        lis[x].pop(0)                           #lis[x] now only has location, newAction, and alt
        #print(d[temp])
        d[temp].newMovement(d,*lis[x])          #execute movement
        #print(d[temp])
    print_dict(d)

    ###insert fight function; compare all locations, if 2+ armies are in same city, make them fight###

if __name__ == "__main__":
    inputs(input())