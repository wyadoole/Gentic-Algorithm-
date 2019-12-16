from random import randint# imports random libarary
from random import random# imports ramdint from random libary for random geuss

class DNA:
    def __init__(self, _targ, _genes=[]):# takes in peramater target and genes

        self.genes = []# genes that will be doing the geuss and pasing on to new generation
        self.target = _targ # target-> the phrase that the ai is trying to guess
        self.fitness = 0.0 # fitness stats at zero
        self.mutateRate = 0.1# sets the mutate rate


        if not _genes: # if their are no genes get them
            for i in range(len(_targ)):# get the rand of 1 to 100 from the population for geussing
                self.genes.append(chr(randint(32, 128)))# gets the genes that are to be used by the algorithm
        else:# if already have them
            self.genes = _genes# then just ge the genes

    def get_genes(self):# gets the genes for the algirthm
        return self.genes# returns the genes that were needed

    def set_genes(self, _genes): # set genes
        self.genes = _genes# sets the genes the are to be used in the algorithm

    def get_fitness(self):# gets fitness score
        return self.fitness  # returns fitniss score to be used to be figure out if that perent gene with have an offspring which is a new guess


    def calc_fitness(self):# calulates the finess score for the gene itself
        score = 0 # sets the defualt score to zero to be used
        for i in range(len(self.genes)): # gets the range of the genes to see it any of the letters were the same at the target
            if self.genes[i] == self.target[i]: # compares genes letter with the tarets letter
                score = score + 1 # gets the score
        self.fitness = float(score)/len(self.target)# calucaltes the actual fitness of the gene

    def crossover(self, partner):# the pairing of the genes if the score it high enough to go to the next generation for the
        child = DNA(_targ=self.target)# gets the childs data

        midpoint = randint(0, len(self.genes)-1)# # get sthe random genes the have passed from the last generation with this one
        childgenes = [] # sets the childs genes to empty an what until the alforithm has gathered them all

        for i in range(len(self.genes)):# get range of the 100 genes to be paired off
            if (i > midpoint):# gets the midpoint to be paired off with another gene
                childgenes.append(self.genes[i])# Gets the gene for the child in put in in an array
            else:# if partner already exist them pair them
                childgenes.append(partner.get_genes()[i])# does the actual pairing of the
        child.set_genes(childgenes)# sets the genes from new parents
        return child# returns new child

    def mutate(self):# does the mutation
        for i in range(len(self.genes)): # gets the gens
            if (random() < self.mutateRate):# gets the random muation rate
                self.genes[i] = chr(randint(32, 128)) # gets the genes that are to mutate


def main():
    print("""
        The code that runs uses a genetic algorithm to a phrase without given the phrase beforehand just using each generation to find the target or phrase. 
        But only the ones that score higher will be pared off and added to the pull for the next generation or next guess.   
        """) # prints out what the application does not part of oringinal code the I got from the web
    input("Press enter to continue")# # had to add to that you could read the print since it runs really fast and would be un readable
    target = ['h', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e'] # gets the target -> word or phrase
    population = []# get sthe empty array of the 100 poputation

    for i in range(100):# fill the population
        population.append(DNA(_targ=target))# check to see if the random created first generation does not have automaticaly the target
    gen = 1 # sets teh frist generation to 1
    finished = False # make the finshed bool to false so that it can run until found
    while not finished:# while not finished run this
        print("Each generation is a gues from a population of 100. The code runs until the target phrase is meet and the application quits ") # tell the use the peramtaters for quiting the applicaiton
        print("\nGeneration:", gen)# prints out the next gerneration to user dit not work in oringinal code


        for agent in population: # Gets the population
           print(agent.get_genes())# prints the gen

        matingPool = []# gets the array of mating pool

        for agent in population:# gets the agents
            agent.calc_fitness()# gets the calulated Fitniss pool

        for agent in population: # gets agent in pool for mating
            n = int(agent.get_fitness()*100) # gets the fitness score so that the indivual guess can product a new guess
            for i in range(n): # gets the agents for mating
                matingPool.append(agent)# actually get the number for the mating

        for i in range(len(population)): # get the polutation for amting
            a = randint(0, len(matingPool)-1) # get parent 1 for mating
            b = randint(0, len(matingPool)-1) # gets parent 2 for mating

            parentA = matingPool[a]# sets parent 1  to be paired
            parentB = matingPool[b]# sets the parent 2 to be paired

            child = parentA.crossover(parentB)# Gets the ofther parent to pair for mating
            child.mutate()# mating

            population[i] = child # adds the child to the polution for the next guess -> each generation has the offsprint of the first parent except from generation 1 which does not

        for agent in population:# gets population for next gernation
            if agent.get_genes() == target:# check targets has been found
                finished = True# if true  then stop
                print("\nTarget Reached:", agent.get_genes()) # tell the user that the target has been reached
                print("Once target is reached the guess cycle ends and quits the application")# and that it will stop running if that has been met
        gen = gen + 1 # adds the numebr of geeneration to current if no target has been reached


if __name__ == '__main__':
    main()# runs main loop


