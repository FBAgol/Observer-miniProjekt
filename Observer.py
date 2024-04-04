from IObserverable import IObserverable, IObserver


# class for Observer (Person)
class Person(IObserver):
    def __init__(self, observer):
        self.observer=observer
        self.person={
            'name':observer[0],
            'vitamine_mangel':observer[1]
        }

    def update(self, fruchtData):
    
        print( f'Hi {self.person["name"]}, wir haben diese neue Frucht: {fruchtData[0]} mit dem Vitamine {fruchtData[1]}, das für dein {self.person["vitamine_mangel"]}-vitamine_mangel gut ist')


# class for Observerable 
class Observerable(IObserverable):
    def __init__(self) -> None:
        self.observers=[]

    def addObserver(self, observer:IObserver ):
        self.observers.append(observer)
       

    def removeObserver(self, observer:IObserver):
        self.observers.remove(observer)
   
    def addFrucht(self, data):
        self.data=data

        self.notify_observers(data)
        return data


    def notify_observers(self, fruchtData):
        
        for ob in  self.observers:
            if ob.observer[1] == fruchtData[1]:
                ob.update(fruchtData)
            
             

  

      

