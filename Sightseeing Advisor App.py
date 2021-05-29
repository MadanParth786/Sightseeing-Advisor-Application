#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter
from tkinter import *
from tkinter import messagebox


# In[3]:


val =" "   #global variable
A = 0    #to store Value in A
operator = " " #global variable


# In[4]:


def Delhi():
    import random
    def randomSolution(tsp):
        cities = list(range(len(tsp)))
        solution = []
        for i in range (len(tsp)):
            randomCity = cities[random.randint(0,len(cities)-1)]
            solution.append(randomCity)
            cities.remove(randomCity)

        return solution

    def routeLen(tsp,solution):
        routelen =0
        for i in range(len(solution)):
            routelen += tsp[solution[i-1]] [solution[i]]
        
        return routelen  
    

    def getneibours(solution):
        neibours =[]
        length =[]
        for i in range (len(solution)):
            for j in range (i+1,len(solution)):
                neibour = solution.copy()
                neibour[i] = solution[j]
                neibour[j] =solution[i]
                neibours.append(neibour)
            
        return neibours      
        

    def getsoln(tsp,neibours):
        bestlen =routeLen(tsp,neibours[0])
        bestsoln = neibours[0]
        for neibour in neibours:
        
            currentroutelen =routeLen(tsp,neibour)
            if currentroutelen <bestlen:
                bestlen = currentroutelen
                bestsoln =neibour
                    
        return bestsoln,bestlen    
    
    
    
    

    def hillclimbing(tsp):
        print("****Welcome To Delhi****")
        print("Top 5 places for Sightseeging in a day are:[0->Red Fort,1->Qutub Minar,2->Humayun Tomb,3->India Gate,4->Jama Masjid ]")
        print("Current Optimal(Random) Solution: ")
        currentsoln = randomSolution(tsp)
        print(currentsoln)
        currentroutelen =routeLen(tsp,currentsoln)
        print("Total Distance:")
        print(currentroutelen)
        neibour =getneibours(currentsoln)
        print("All possible Ways for Sightseeing are: ")
        print(neibour)
        bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
    
        while bestsolutionlen <currentroutelen:
            currentsoln = bestsolution
            currentroutelen = bestsolutionlen
            bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
            print("Best Optimal Order for Sightseeing is:")
        return  currentsoln,currentroutelen                                
        
                                                     
        
                  
                  
    def main():
        Data = [ [0,18,8,7,1],
            [18,0,13,11,6],
            [8,13,0,3,9],
            [7,11,3,0,6],
            [1,6,9,6,0]
               ]
        print(hillclimbing(Data))
        print("***Hope you will Enjoy alot***")
    
    
    if __name__ == "__main__":
        main()
        
        
def Jaipur():
    import random
    def randomSolution(tsp):
        cities = list(range(len(tsp)))
        solution = []
        for i in range (len(tsp)):
            randomCity = cities[random.randint(0,len(cities)-1)]
            solution.append(randomCity)
            cities.remove(randomCity)

        return solution

    def routeLen(tsp,solution):
        routelen =0
        for i in range(len(solution)):
            routelen += tsp[solution[i-1]] [solution[i]]
        
        return routelen  
    

    def getneibours(solution):
        neibours =[]
        length =[]
        for i in range (len(solution)):
            for j in range (i+1,len(solution)):
                neibour = solution.copy()
                neibour[i] = solution[j]
                neibour[j] =solution[i]
                neibours.append(neibour)
            
        return neibours      
        

    def getsoln(tsp,neibours):
        bestlen =routeLen(tsp,neibours[0])
        bestsoln = neibours[0]
        for neibour in neibours:
        
            currentroutelen =routeLen(tsp,neibour)
            if currentroutelen <bestlen:
                bestlen = currentroutelen
                bestsoln =neibour
                    
        return bestsoln,bestlen    
    
    
    
    

    def hillclimbing(tsp):
        print("****Welcome To Jaipur****")
        print("Top 5 places for Sightseeging in a day are:[0->Amber Fort,1->Nahargarh Fort,2->Hawa Mahal,3->Jal Mahal,4->Jantar Mantar ]")
        print("Current Optimal(Random) Solution: ")
        currentsoln = randomSolution(tsp)
        print(currentsoln)
        currentroutelen =routeLen(tsp,currentsoln)
        print("Total Distance:")
        print(currentroutelen)
        neibour =getneibours(currentsoln)
        print("All possible Ways for Sightseeing are: ")
        print(neibour)
        bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
    
        while bestsolutionlen <currentroutelen:
            currentsoln = bestsolution
            currentroutelen = bestsolutionlen
            bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
            print("Best Optimal Order for Sightseeing is:")
        return  currentsoln,currentroutelen                                
        
                                                     
        
                  
                  
    def main():
        Data = [ [0,10,8,3,9],
            [10,0,14,10,14],
            [8,14,0,5,2],
            [3,10,5,0,4],
            [9,14,2,4,0]
           ]
        print(hillclimbing(Data))
        print("***Hope you will Enjoy alot***")
    
    
    if __name__ == "__main__":
        main() 
        
        
def Agra():
    import random
    def randomSolution(tsp):
        cities = list(range(len(tsp)))
        solution = []
        for i in range (len(tsp)):
            randomCity = cities[random.randint(0,len(cities)-1)]
            solution.append(randomCity)
            cities.remove(randomCity)

        return solution

    def routeLen(tsp,solution):
        routelen =0
        for i in range(len(solution)):
            routelen += tsp[solution[i-1]] [solution[i]]
        
        return routelen  
    

    def getneibours(solution):
        neibours =[]
        length =[]
        for i in range (len(solution)):
            for j in range (i+1,len(solution)):
                neibour = solution.copy()
                neibour[i] = solution[j]
                neibour[j] =solution[i]
                neibours.append(neibour)
            
        return neibours      
        

    def getsoln(tsp,neibours):
        bestlen =routeLen(tsp,neibours[0])
        bestsoln = neibours[0]
        for neibour in neibours:
        
            currentroutelen =routeLen(tsp,neibour)
            if currentroutelen <bestlen:
                bestlen = currentroutelen
                bestsoln =neibour
                    
        return bestsoln,bestlen    
    
    
    
    

    def hillclimbing(tsp):
        print("****Welcome To Agra****")
        print("Top 5 places for Sightseeging in a day are:[0->Agra Fort,1->Taj Mahal,2->Fatehpur Sikari,3->Akbar Tomb,4->Moti Masjid ]")
        print("Current Optimal(Random) Solution: ")
        currentsoln = randomSolution(tsp)
        print(currentsoln)
        currentroutelen =routeLen(tsp,currentsoln)
        print("Total Distance:")
        print(currentroutelen)
        neibour =getneibours(currentsoln)
        print("All possible Ways for Sightseeing are: ")
        print(neibour)
        bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
    
        while bestsolutionlen <currentroutelen:
            currentsoln = bestsolution
            currentroutelen = bestsolutionlen
            bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
            print("Best Optimal Order for Sightseeing is:")
        return  currentsoln,currentroutelen                                
        
                                                     
        
                  
                  
    def main():
        Data = [ [0,2,37,14,1],
            [2,0,41,16,4],
            [37,41,0,36,38],
            [14,16,36,0,11],
            [1,4,38,11,0]
           ]
        print(hillclimbing(Data))
        print("***Hope you will Enjoy alot***")
    
    
    if __name__ == "__main__":
        main() 
        
        
def Amritsar():
    import random
    def randomSolution(tsp):
        cities = list(range(len(tsp)))
        solution = []
        for i in range (len(tsp)):
            randomCity = cities[random.randint(0,len(cities)-1)]
            solution.append(randomCity)
            cities.remove(randomCity)

        return solution

    def routeLen(tsp,solution):
        routelen =0
        for i in range(len(solution)):
            routelen += tsp[solution[i-1]] [solution[i]]
        
        return routelen  
    

    def getneibours(solution):
        neibours =[]
        length =[]
        for i in range (len(solution)):
            for j in range (i+1,len(solution)):
                neibour = solution.copy()
                neibour[i] = solution[j]
                neibour[j] =solution[i]
                neibours.append(neibour)
            
        return neibours      
        

    def getsoln(tsp,neibours):
        bestlen =routeLen(tsp,neibours[0])
        bestsoln = neibours[0]
        for neibour in neibours:
        
            currentroutelen =routeLen(tsp,neibour)
            if currentroutelen <bestlen:
                bestlen = currentroutelen
                bestsoln =neibour
                    
        return bestsoln,bestlen    
    
    
    
    

    def hillclimbing(tsp):
        print("****Welcome To Amritsar****")
        print("Top 5 places for Sightseeging in a day are:[0->Golden Temple,1->Wagah Border,2->Partition Museum,3->Jallianwala Bagh,4->Baba Atal Tower ]")
        print("Current Optimal(Random) Solution: ")
        currentsoln = randomSolution(tsp)
        print(currentsoln)
        currentroutelen =routeLen(tsp,currentsoln)
        print("Total Distance:")
        print(currentroutelen)
        neibour =getneibours(currentsoln)
        print("All possible Ways for Sightseeing are: ")
        print(neibour)
        bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
    
        while bestsolutionlen <currentroutelen:
            currentsoln = bestsolution
            currentroutelen = bestsolutionlen
            bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
            print("Best Optimal Order for Sightseeing is:")
        return  currentsoln,currentroutelen                                
        
                                                     
        
                  
                  
    def main():
        Data = [ [0,35,1,1,1],
            [35,0,30,29,28],
            [1,30,0,2,1],
            [1,29,2,0,1],
            [1,28,1,1,0]
           ]
        print(hillclimbing(Data))
        print("***Hope you will Enjoy alot***")
    
    
    if __name__ == "__main__":
        main() 
        
        
        
        
def Chandigarh():
    import random
    def randomSolution(tsp):
        cities = list(range(len(tsp)))
        solution = []
        for i in range (len(tsp)):
            randomCity = cities[random.randint(0,len(cities)-1)]
            solution.append(randomCity)
            cities.remove(randomCity)

        return solution

    def routeLen(tsp,solution):
        routelen =0
        for i in range(len(solution)):
            routelen += tsp[solution[i-1]] [solution[i]]
        
        return routelen  
    

    def getneibours(solution):
        neibours =[]
        length =[]
        for i in range (len(solution)):
            for j in range (i+1,len(solution)):
                neibour = solution.copy()
                neibour[i] = solution[j]
                neibour[j] =solution[i]
                neibours.append(neibour)
            
        return neibours      
        

    def getsoln(tsp,neibours):
        bestlen =routeLen(tsp,neibours[0])
        bestsoln = neibours[0]
        for neibour in neibours:
        
            currentroutelen =routeLen(tsp,neibour)
            if currentroutelen <bestlen:
                bestlen = currentroutelen
                bestsoln =neibour
                    
        return bestsoln,bestlen    
    
    
    
    

    def hillclimbing(tsp):
        print("****Welcome To Chandigarh****")
        print("Top 5 places for Sightseeging in a day are:[0->Rose garden,1->Rock Garden,2->Sukhna Lake ,3->Fun City,4->Chandigarh Museum ]")
        
        print("Current Optimal(Random) Solution: ")
        currentsoln = randomSolution(tsp)
        print(currentsoln)
        currentroutelen =routeLen(tsp,currentsoln)
        print("Total Distance:")
        print(currentroutelen)
        neibour =getneibours(currentsoln)
        print("All possible Ways for Sightseeing are: ")
        print(neibour)
        bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
    
        while bestsolutionlen <currentroutelen:
            currentsoln = bestsolution
            currentroutelen = bestsolutionlen
            bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
            print("Best Optimal Order for Sightseeing is:")
        return  currentsoln,currentroutelen                                
        
                                                     
        
                  
                  
    def main():
        Data =[ [0,5,6,8,3],
            [5,0,6,8,2],
            [6,6,0,7,3],
            [8,8,7,0,7],
            [3,2,3,7,0]
           ]
        print(hillclimbing(Data))
        print("***Hope you will Enjoy alot***")
    
    
    if __name__ == "__main__":
        main()  
        
        
        
       
        
def Ahemadabad():
    import random
    def randomSolution(tsp):
        cities = list(range(len(tsp)))
        solution = []
        for i in range (len(tsp)):
            randomCity = cities[random.randint(0,len(cities)-1)]
            solution.append(randomCity)
            cities.remove(randomCity)

        return solution

    def routeLen(tsp,solution):
        routelen =0
        for i in range(len(solution)):
            routelen += tsp[solution[i-1]] [solution[i]]
        
        return routelen  
    

    def getneibours(solution):
        neibours =[]
        length =[]
        for i in range (len(solution)):
            for j in range (i+1,len(solution)):
                neibour = solution.copy()
                neibour[i] = solution[j]
                neibour[j] =solution[i]
                neibours.append(neibour)
            
        return neibours      
        

    def getsoln(tsp,neibours):
        bestlen =routeLen(tsp,neibours[0])
        bestsoln = neibours[0]
        for neibour in neibours:
        
            currentroutelen =routeLen(tsp,neibour)
            if currentroutelen <bestlen:
                bestlen = currentroutelen
                bestsoln =neibour
                    
        return bestsoln,bestlen    
    
    
    
    

    def hillclimbing(tsp):
        print("****Welcome To Ahembdabad****")
        print("Top 5 places for Sightseeging in a day are:[0->Sabarmati Ashram,1->Bhadra Fort,2->Sarkhej Roza,3->Vastrapur Lake,4->Kankaria Lake ]") 
        
        print("Current Optimal(Random) Solution: ")
        currentsoln = randomSolution(tsp)
        print(currentsoln)
        currentroutelen =routeLen(tsp,currentsoln)
        print("Total Distance:")
        print(currentroutelen)
        neibour =getneibours(currentsoln)
        print("All possible Ways for Sightseeing are: ")
        print(neibour)
        bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
    
        while bestsolutionlen <currentroutelen:
            currentsoln = bestsolution
            currentroutelen = bestsolutionlen
            bestsolution ,bestsolutionlen  = getsoln(tsp,neibour)
            print("Best Optimal Order for Sightseeing is:")
        return  currentsoln,currentroutelen                                
        
                                                     
        
                  
                  
    def main():
        Data =[ [0,9,13,8,9],
            [9,0,10,7,4],
            [13,10,0,8,12],
            [8,7,8,0,10],
            [9,4,12,10,0]
           ]
        print(hillclimbing(Data))
        print("***Hope you will Enjoy alot***")
    
    
    if __name__ == "__main__":
        main()        
        
        
        
        
        

        
        
        
        


# In[5]:


#root:Create Window: (***FIRST PART OF CODE***)
root =tkinter.Tk()
root.title("Sightseeing-Advisor")

#creating menu rows:
menurow0=Frame(root,bg="#000000")
menurow0.pack(expand=True,fill="both",)

menurow1=Frame(root,)
menurow1.pack(expand=True, fill="both",)

menurow2=Frame(root,)
menurow2.pack(expand=True,fill="both",)

menurow3=Frame(root,)
menurow3.pack(expand=True,fill="both",)

menurow4=Frame(root,)
menurow4.pack(expand=True,fill="both",)

menurow5=Frame(root,)
menurow5.pack(expand=True,fill="both",)


#creating menu titles:(***SECOND PART OF CODE***)
menutitle0=Button(
        menurow0,
        text = "Welcome to Sightseeing Advisor",
        font = ("Algerian", 24),
        relief = GROOVE,
        border = 1,  
        
)
menutitle0.pack(expand=True,fill="both",)


menutitle1=Button(
        menurow1,
        text = "City : Delhi",
        font = ("verdana", 22),
        relief = GROOVE,
        border = 2,
        bg = "#ffffff",
        command = Delhi,    #command is used to execute function           

)
menutitle1.pack(side=LEFT,expand=True,fill="both",)
menutitle1=Button(
        menurow1,
        text = "City : Jaipur",
        font = ("verdana", 22),
        relief = GROOVE,
        border = 2,
        command = Jaipur,    #command is used to execute function           

)
menutitle1.pack(side=LEFT,expand=True,fill="both",)

menutitle2=Button(
        menurow2,
        text =  "   City : Agra",
        font = ("verdana", 22),
        relief = GROOVE,
        border = 2,
        command = Agra,  #command is used to execute respective function.            

)
menutitle2.pack(side=LEFT,expand=True,fill="both",)

menutitle3=Button(
        menurow2,
        text = "City : Amritsar",
        font = ("verdana", 22),
        relief = GROOVE,
        border = 2,
        bg = "#ffffff",
        command = Amritsar,              

)
menutitle3.pack(side=LEFT,expand=True,fill="both",)


menutitle4=Button(
        menurow3,
        text = " City : Chandigarh",
        font = ("verdana", 22),
        relief = GROOVE,
        border = 2,
        bg = "#ffffff",
        command = Chandigarh,              

)
menutitle4.pack(side=LEFT,expand=True,fill="both",)

menutitle5=Button(
        menurow3,
        text = "City : Ahemedabad",
        font = ("verdana", 22),
        relief = GROOVE,
        border = 2,
        command = Ahemadabad,           

)
menutitle5.pack(side=LEFT,expand=True,fill="both",)

menutitle5=Button(
        menurow4,
        text = "   ******Explore Your Way With Full Convenience******",
        font = ("Castelar", 20),
        relief = GROOVE,
        bg = "#ffffff",
        border = 0,              

)
menutitle5.pack(side=RIGHT,expand=True,fill="both",)

menutitle6=Button(
        menurow5,
        text =  "(APP-DEVELOPER:PRIYA MITTAL,PARTH MADAN)",
        font = ("verdana", 10),
        relief = GROOVE,
        border = 1,

)
menutitle6.pack(side=RIGHT,expand=True,fill="both",)


root.mainloop()


# In[ ]:





# In[ ]:




