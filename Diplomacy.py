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

    def newMovement(self,dict,location,newAction,alt=None):
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
        if i=="":
            break
        inp.append(i)
    setup(inp)

def setup(lis):
    d={}
    loc={}
    for x in range(len(lis)):                           #commence movements
        lis[x]=lis[x].split()                           #lis[x] is the string input (ex. A Madrid Hold)
        temp=lis[x][0]                                  #lis[x][0] is the name of the army (ex. A), lis[x][1] is the location (ex. Madrid)
        d[temp]=Army(lis[x][0],lis[x][1],lis[x][2])     #d[temp] is the army object
        lis[x].pop(0)                                   #lis[x] now only has location, newAction, and alt
        #print(d[temp])
        d[temp].newMovement(d,*lis[x])                  #execute movement
        loc[temp]=d[temp].getLocation()                 #enter location into loc dict to reference; key=army name, value=location
        #print(d[temp])
    
    #print_dict(loc)
    
    ###insert fight function; compare all locations, if 2+ armies are in same city, make them fight###
    fight(d,loc,lis)
    
    print_dict(d)

def fight(armies,locations,lis):   #takes a dictionary of armies (key=army name, value=army object) and dictionary of locations (key=army name, value=army location)
    #loc=[]
    locs={}                             #locs is a dictionary (key=army location, value=list of army names at that location)
    for key in locations:
        if locations[key] not in locs:
            locs[locations[key]]=[key]
        else:
            locs[locations[key]].append(key)

    for key in locs:
        if len(locs[key])==1: del locs[key] #removes any location that only has one army since there won't be a fight there

    for key in locs:                #change all attacked armies Support to Hold
        for x in locs[key]:
            if armies[locs[x]].getMovement()=="Support":
                armies[locs[x]].setMovement("Hold")

    for x in range(len(lis)):
        temp=lis[x][0]
        if armies[temp].getMovement()=="Support":
            armies[temp].newMovement(armies,*lis[x])    #run all the supports for armies that aren't being attacked

    ### fight! go through all the remaining lists in locs (armies in one location) and see who (if anyone) wins ###

    print_dict(locs) #tests where the armies are

    print_dict(armies) #true output    
    

    ### DON'T USE, NOT USING!!!! ###
    #was in the for key in locations loop
    #loc.append(locations[key])
        ### if there are duplicates in loc, then there is more than 1 army at the location! ###
    #loc=list(set(loc))                 #loc now has one copy of each location where an army is
    
    '''for x in loc:                       #trying to find where the 
        pass'''
    

def main():
    inputs()

if __name__ == "__main__":
    main()