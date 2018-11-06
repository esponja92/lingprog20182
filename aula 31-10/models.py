class Person(object):
        def __init__(self, name):
            self.name = name

        def w(name):
                arq=open(name+".txt",'w')
                arq.write("nome :"+name+" \n")
                arq.close()

        def read(name):
                arq=open(name+".txt")
                data=["","",""]        
                l=0
                for line in arq:
                        line.replace("/n","").split(":")
                        data[l]= line[1]
                        l+=1
                return data



class Aluno(Person):
        def __init__(self, name, idade, dre):
                    super().__init__(name)
                    self.idade=idade
                    self.dre=dre

        def update(name, idade="", dre=None):
                arq=open(name+".txt", 'w')
                arq.write("nome:"+name+"\n" +\
                                  "idade:"+idade+" \n" + \
                                  "dre:"+ dre)
                arq.close()

class Professor(Person):
        def __init__(self):
                    super().__init__()


        def draw():
                return   "                 @@@  \
                  @@@        \
                   @@@                       H A P P Y \
                   @@@                                        \
           @@@@@@@@@@@@@@@@@@@@@@         H A L L O W E E N \
         @@@@@@@@@@@@@@@@@@@@@@@@@@ \
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \
     @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@ \
   @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@ \
@@@@@@@@@@     @@@@@@@@@@@@     @@@@@@@@@@ \
@@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@ \
@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@ \
@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@ \
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \
@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@ \
 @@@@@@@@  @@ @@ @@ @@ @@ @@ @@ @  @@@@@@@@ \
   @@@@@@@                        @@@@@@@ \
     @@@@@@  @@ @@ @@ @@ @@ @@ @ @@@@@@ \
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \
         @@@@@@@@@@@@@@@@@@@@@@@@@@ \
           @@@@@@@@@@@@@@@@@@@@@@" 
              

                

