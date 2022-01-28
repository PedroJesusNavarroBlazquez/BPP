class operacionesMatematicas:
    """
    OperacionesMatematicas. Es una clase que se encarga de realizar operaciones matematicas sobre datos de tipo entero.
    
    Atributos:
    =========
    op1:
        primer operando
    op2:
        segundo operando

    Metodos:
    =======
    suma:
        Suma los operandos op1 y op2
    resta:
        Resta los operandos op1 y op2
    producto:
        Multiplica los operandos op1 y op2
    division:
        Divide el operando op1 entre op2

    Ejemplos:
    ========
    >>> import operacionesMatematicas
    >>> ot = operacionesMatematicas(op1, op2)
    >>> resultado_suma = ot.suma()
    >>> print(resultado_suma)
    >>> resultado_resta = ot.resta()
    >>> print(resultado_resta)
    """
    def __init__(self, op1, op2):
        # Comprobamos que es un entero.
        # assert(isinstance(op1, int) and isinstance(op2, int))
        self.op1 = op1
        self.op2 = op2

    def suma(self):
        """
        Suma los operandos op1 y op2
        """
        return self.op1+self.op2
    
    def resta(self):
        """
        Resta los operandos op1 y op2
        """
        return self.op1-self.op2

    def producto(self):
        """
        Multiplica los operandos op1 y op2
        """
        return self.op1*self.op2

    def division(self):
        """
        Divide los operandos op1 y op2
        """
        return self.op1/self.op2

    def es_primo(self):
        """
        Metodo para determinar si op1 es o no primo
        """
        primo = True
        for i in range(2,self.op1-1):
            if(self.op1%i == 0):
                primo = False
            return primo
