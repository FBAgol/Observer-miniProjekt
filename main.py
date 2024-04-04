from Observer import Observerable, Person

if __name__== "__main__":
    observer=Observerable()
    person1= Person(['Alex', 'A'])
    person2= Person(['Farzad', 'D'])
    person3= Person(['Michael', 'C'])

    observer.addObserver(person1)
    observer.addObserver(person2)
    observer.addObserver(person3)

    observer.addFrucht(["Apfel" , "B"])
    observer.addFrucht(["Banana" , "A"])
    observer.addFrucht(["Kivi" , "A"])

   