class AccounException(Exception):
    def __init__(self,msg):
        self.msg = msg
        super().__init__(msg)

    def __str__(self):
        return f"This is Account Exception {self.msg}"