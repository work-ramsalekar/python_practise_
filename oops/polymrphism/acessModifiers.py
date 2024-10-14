class Tp :
    def __init__(self,pub,prot,priv):
        self.pub = pub
        self._prot = prot
        self.__priv = priv


class main :
    h1 = Tp("public","protected","private")

    print(h1.pub)
    print(h1._prot)
    print(h1.__priv)