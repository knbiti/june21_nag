class publisher:
    def __init__(self,pname='Nag',pplace='India'):
        self.name=pname
        self.place=pplace

    def show(self):
        print("Publisher Name = ",self.name)
        print("Publisher Place =",self.place)

ob=publisher('Nagendra','Andhara')
ob.show()
