from io import StringIO

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
        self.res = None
        self.setup()

    def __str__(self):
        return "\n".join(self.armies.values())

    def print_dict(self):
        res = []
        for key in self.armies:
            res.append(str(self.armies[key]))
        final = "\n".join(res)
        return final


    def setup(self):
        loc={}
        for x in range(len(self.lis)-1):                           #commence movements
            self.lis[x]=self.lis[x].split()                           #lis[x] is the string input (ex. A Madrid Hold)
            temp=self.lis[x][0]                                  #lis[x][0] is the name of the army (ex. A), lis[x][1] is the location (ex. Madrid)
            self.armies[temp]=Army(self.lis[x][0],self.lis[x][1],self.lis[x][2])     #d[temp] is the army object
            self.armies[temp].newMovement(self.armies,*self.lis[x])                  #execute movement
            loc[temp]=self.armies[temp].getLocation()                 #enter location into loc dict to reference; key=army name, value=location
        
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
        
        for x in range(len(self.lis)-1):
            temp=self.lis[x][0]
            if self.armies[temp].getMovement()=="Support":
                self.armies[temp].support(self.armies,*self.lis[x])    #run all the supports for armies that aren't being attacked

        self.fight(rem)
        
    def fight(self, rem):
        winner = False
        for key in rem:
            most = self.armies[rem[key][0]].troops
            for i in rem[key]:
                if self.armies[i].troops > most:
                    most = self.armies[i].troops
            countMost = 0
            for i in rem[key]:
                if self.armies[i].troops == most: countMost += 1
            if countMost > 1:
                for army in rem[key]:
                    self.armies[army].die()
            else:
                for army in rem[key]:
                    if self.armies[army].troops != most:
                        self.armies[army].die()

        self.res = self.print_dict() #true output

def diplomacy_solve(inputs):
    game = Diplomacy(inputs.split("\n"))
    print(game.res + "\n")
    return game.res + "\n"

def diplomacy_read(s):
    """
    read a string of armies and actions
    s a string
    return a list split by army and corresponding action
    """

    a = []
    for i in s:
        a.append(str(i))
    # a = s.split("\n")
    # a.pop(-1)
    return "".join(a)

def diplomacy_print(w, input, output):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(input) + str(output))

def diplomacy_eval(r, w):
    """
    r a reader
    w a writer
    """
    # print(r)
    inp = diplomacy_read(r)
    # print(inp)
    out = str(diplomacy_solve(inp))
    # print(out)
    diplomacy_print(w, inp, out)


if __name__ == "__main__":
    diplomacy_solve("A Madrid Move London\nB Barcelona Move London\nC Cairo Move London\nD Oslo Move London\nE Amsterdam Support A\nF Moscow Support B\nG Shanghai Support C\nH Tokyo Support D\nI Austin Move Amsterdam\nJ Taipei Move Moscow\nK Stockholm Move Shanghai\nL Lima Move Tokyo\n")
    r = StringIO(("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n"))
    # print(diplomacy_read(r))
    w = StringIO()
    # diplomacy_print(w, "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n", "A [dead]\nB Madrid\nC London\n")
    # diplomacy_eval(r, w)
    # w.getvalue()

# move all the armies first
# maybe have a list of all the existing locations
# go through list of locations and check if there is more than 1 army in location(s)
# for the locations w more than 1 army, check if any of the armies are supporting, and change to hold
# for each army in a location, add the supports and find army with max support
# check if max support is in the list more than once, if so every army dies
# if max support only occurs once, army with max support wins and occupies location