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

    def setLocation(self, newLocation):
        self.location = newLocation

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
        return

    def support(self,dict,name,location,newAction,recipient):
        if recipient in dict:
            dict[recipient].troops+=1

    def move(self,newLocation):
        self.location=newLocation

    def die(self):
        self.location='[dead]'

class Diplomacy:
    def __init__(self, lis):
        self.lis = lis      # list of raw inputs; PREVIOUSLY lis in below functions
        self.armies = dict()    # dictionary of {armyName: armyObject}; PREVIOUSLY d in below functions
        self.setup()


    def print_dict(self):
        for key in self.armies:
            print(self.armies[key])


    def setup(self):
        loc={}
        for x in range(len(self.lis)):                           #commence movements
            self.lis[x]=self.lis[x].split()                           #lis[x] is the string input (ex. A Madrid Hold)
            temp=self.lis[x][0]                                  #lis[x][0] is the name of the army (ex. A), lis[x][1] is the location (ex. Madrid)
            self.armies[temp]=Army(self.lis[x][0],self.lis[x][1],self.lis[x][2])     #d[temp] is the army object
            #lis[x].pop(0)                                   #lis[x] now only has location, newAction, and alt
            #print(d[temp])
            #if self.armies[temp].getMovement!="Support":
            self.armies[temp].newMovement(self.armies,*self.lis[x])                  #execute movement
            loc[temp]=self.armies[temp].getLocation()                 #enter location into loc dict to reference; key=army name, value=location
            #print(d[temp])
        
        #print_dict(loc)
        #print_dict(d)

        # self.supportTest(d,loc,lis)
        #print(self.armies)
        self.supportTest(loc)

    # def supportTest(armies,locations,lis):   #takes a dictionary of armies (key=army name, value=army object) and dictionary of locations (key=army name, value=army location)
    def supportTest(self, locations):    
        locs={}                             #locs is a dictionary (key=army location, value=list of army names at that location)
        for key in locations:
            if locations[key] not in locs:
                locs[locations[key]]=[key]
            else:
                locs[locations[key]].append(key)

        rem={k:v for k,v in locs.items() if len(locs[k])!=1}    #rem is a dictionary (key=army location, value=list of armies at that location) with only fight areas

        for key in rem:                #change all attacked armies Support to Hold
            for x in rem[key]:         #x is the name of one army at the location rem[key]
                if self.armies[x].getMovement()=="Support":
                    self.armies[x].setMovement("Hold")
        
        for x in range(len(self.lis)):
            temp=self.lis[x][0]
            if self.armies[temp].getMovement()=="Support":
                self.armies[temp].support(self.armies,*self.lis[x])    #run all the supports for armies that aren't being attacked

        self.fight(rem)
        
        ### insert fight function; compare all locations, if 2+ armies are in same city, make them fight ###
        ### fight! go through all the remaining lists in locs (armies in one location) and see who (if anyone) wins ###

    def fight(self, rem):
        winner = False
        for key in rem:
            most = self.armies[rem[key][0]].troops
            for i in rem[key]:
                if self.armies[i].troops > most:
                    most = self.armies[i].troops
            # most = max(i.troops for i in rem[key])
            countMost = 0
            for i in rem[key]:
                if self.armies[i].troops == most: countMost += 1
            if countMost > 1:
                for army in rem[key]:
                    self.armies[army].die()
                # winner = False
            else:
                for army in rem[key]:
                    # print(army, self.armies[army].troops)
                    if self.armies[army].troops != most:
                        self.armies[army].die()
                # winner = True
                # winner_index = rem[key].index(most)

            # if winner: rem[key][winner_index].setLocation(key)



        #print("locs:")
        #print_dict(locs) #tests where the armies are

        #print("armies:")
        self.print_dict() #true output 
    
def inputs(): #makes a tuple of input strings
    inp=[]              #makes a list with each input line as a new index
    while 1:
        i=input()
        if i=="": break
        inp.append(i)
    # setup(inp)
    return inp

def main():
    game = Diplomacy(inputs())


if __name__ == "__main__":
    main()

# move all the armies first
# maybe have a list of all the existing locations
# go through list of locations and check if there is more than 1 army in location(s)
# for the locations w more than 1 army, check if any of the armies are supporting, and change to hold
# for each army in a location, add the supports and find army with max support
# check if max support is in the list more than once, if so every army dies
# if max support only occurs once, army with max support wins and occupies location