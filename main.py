from Observer import Observerable, Person

if __name__== "__main__":
    observer=Observerable()
    person1= Person(['Ales', 'A'])
    observer.addObserver(person1)
    observer.addFrucht(["aplle" , "B"])

   