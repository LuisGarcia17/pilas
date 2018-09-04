class Pila:
    
    def __init__(self):
        """
        Constructor por omisión que inicializa una pila vacía.
        """
        self.top=None

    def emply(self):
        return self.top==None
    
    def push(self,item):
        """
        Agrega un nuevo elemento al tope de la pila.
        """
        node=nodopila(item,self.top)
        self.top=node
    
    def pop(self):
        """
        Regresa el elemento en el tope de la pila pero NO lo quita.
        """
        if not self.isEmply():
            node=self.top
            self.top=self.top.next
            
    def Top(self):
        return self.top.item
class nodopila:

   def __init__(self, item, link):
       self.item=item
       self.next=link
       
pila = Pila()
pila.push(1)
print(pila.emply())
print(pila.Top())
print(pila.emply())
pila.push(1)
pila.push(2)
pila.push(3)
print(pila.Top())









     
    
