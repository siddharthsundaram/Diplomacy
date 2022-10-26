class Army:
    def __init__(self,name,location,movement):
        self.name=name
        self.location=location
        self.movement=movement
        self.troops=1

    def __str__(self):
        return self.name+' '+str(self.location)
        #return self.name+' '+str(self.location)+' '+str(self.troops)

    def getLocation(self):
        return self.location

    def getMovement(self):
        return self.movement

    def setMovement(self,newMovement):
        self.movement=newMovement

    def newMovement(self,dict,name,location,newAction,alt=None):
        #(self,dict,alt=None):
        if self.movement=='Hold':return
        elif self.movement=='Move':
            self.move(alt)
            return
        '''elif self.movement=='Support':
            self.support(dict,alt)
            return'''

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

def inputs(): #makes a tuple of input strings
    inp=[]              #makes a list with each input line as a new index
    while 1:
        i=input()
        if i=="": break
        inp.append(i)
    setup(inp)

def setup(lis):
    d={}
    loc={}
    for x in range(len(lis)):                           #commence movements
        lis[x]=lis[x].split()                           #lis[x] is the string input (ex. A Madrid Hold)
        temp=lis[x][0]                                  #lis[x][0] is the name of the army (ex. A), lis[x][1] is the location (ex. Madrid)
        d[temp]=Army(lis[x][0],lis[x][1],lis[x][2])     #d[temp] is the army object
        #lis[x].pop(0)                                   #lis[x] now only has location, newAction, and alt
        #print(d[temp])
        d[temp].newMovement(d,*lis[x])                  #execute movement
        loc[temp]=d[temp].getLocation()                 #enter location into loc dict to reference; key=army name, value=location
        #print(d[temp])
    
    #print_dict(loc)
    #print_dict(d)

    supportTest(d,loc,lis)

def supportTest(armies,locations,lis):   #takes a dictionary of armies (key=army name, value=army object) and dictionary of locations (key=army name, value=army location)
    locs={}                             #locs is a dictionary (key=army location, value=list of army names at that location)
    for key in locations:
        if locations[key] not in locs:
            locs[locations[key]]=[key]
        else:
            locs[locations[key]].append(key)

    rem={k:v for k,v in locs.items() if len(locs[k])!=1}    #rem is a dictionary (key=army location, value=list of armies at that location) with only fight areas

    for key in rem:                #change all attacked armies Support to Hold
        for x in rem[key]:         #x is the name of one army at the location rem[key]
            if armies[x].getMovement()=="Support":
                armies[x].setMovement("Hold")
    
    for x in range(len(lis)):
        temp=lis[x][0]
        if armies[temp].getMovement()=="Support":
            armies[temp].newMovement(armies,*lis[x])    #run all the supports for armies that aren't being attacked

    ### insert fight function; compare all locations, if 2+ armies are in same city, make them fight ###
    ### fight! go through all the remaining lists in locs (armies in one location) and see who (if anyone) wins ###

    #print("locs:")
    #print_dict(locs) #tests where the armies are

    #print("armies:")
    print_dict(armies) #true output    
    

def main():
    inputs()

if __name__ == "__main__":
    main()

# move all the armies first
# maybe have a list of all the existing locations
# go through list of locations and check if there is more than 1 army in location(s)
# for the locations w more than 1 army, check if any of the armies are supporting, and change to hold
# for each army in a location, add the supports and find army with max support
# check if max support is in the list more than once, if so every army dies
# if max support only occurs once, army with max support wins and occupies location