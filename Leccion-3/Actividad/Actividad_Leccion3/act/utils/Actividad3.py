class Persona:
    """ 
    Persona. Es una clase que se describir a una persona

    Atributos:
    ==========
    altura: Se refiere a la altura de la persona
    edad: Se refiere a la edad de la persona 
    nombre: Se refiere al nombre de la persona

    Metodos:
    ========
    set_edad: metodo que permite darle un valor al atributo edad. Es decir, decir indicar la edad de la persona.
    get_edad: metodo que permite obtener la edad de una persona.
    set_nombre: metodo que permite indicar el nombre de una persona.
    get_nombre: metodo que permite obtener el nombre de una persona.
    set_altura: metodo que permite indicar la altura de una persona.
    get_altura: metodo que permite obtener la altura de una persona.
    
    
    Ejemplos:
    =========
    >>> import Persona
    >>> aux = Persona(26, Pedro)
    >>> resultado_mayor_edad = aux.mayor_edad()
    >>> resultado_nivel_estudios =  aux.nivel_estudios()
    """
    #Declarar un atributo que se pueda acceder desde cualquier clase. 
    altura = 1.7

    def __init__(self, edad, nombre):
        self.__edad = edad
        self.__nombre = nombre
    
    #GETTER y SETTER
    def set_edad(self, edad):
        self.__edad = edad
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre

    def set_altura(self, altura):
        self.__altura = altura
    def get_altura(self):
        return self.__altura

    #METHODS
    def mayor_edad(self):
        """
        Metodo Mayor de Edad. Comprueba si la persona es mayor de edad.
        Inputs:
            self.edad: operando
        Outputs:
            res: resultado de comprobar si la persona es mayor de edad.
        """
        if self.__edad >17:
            res = ( "La persona", self.get_nombre(), "es mayor de edad. Tiene ", self.get_edad())
            return res
        else:
            res = print(f"La persona {self.get_nombre()} es menor de edad. Tiene {self.get_edad()}")
            return res

    def nivel_estudios(self, nivel):
        """
        Metodo Nivel de Estudios. Indica el nivel de estudios de una persona.
        Inputs:
            nivel: descripcion
        Outputs:
            res: Devuelve el nivel de estudio de una persona dependiendo de las clases que heredan.
        """
        res = f"el nivel de estudio de {self.__nombre} es {nivel}"
        return res

    def altura_ajustada(self, altura):
        """
        Metodo altura ajustada. Indica el ajuste de la altura de la persona.
        Inputs:
            altura: descripcion en cm.
        Outputs:
            res: Devuelve la altura de una persona.
        """
        res = f"La altura de la persona es: {altura-0.2}"
        return res


#Crea una clase sin variables ni metodos
class alumnos:
    pass

#Crea una clase que herede todas las variables y metodos de la clase persona. Y se crea un objeto alumno.
class alumno(Persona):
    """ 
    alumo. Es una clase que hereda de persona y que por lo tanto realiza lo que cualquier otra persona, pero se diferencia con particularidades.

    Atributos:
    ==========
    nivel: Se refiere al nivel de estudios

    Metodos:
    ========
    nivel_estudios: metodo que indica el nivel de estudios del alumno.  
    """
    def __init__(self, edad, nombre):
        Persona.__init__(self,edad, nombre)
        self.nivel = 10

    #Crear metodo que sea niveles de estudios
    def nivel_estudios(self, nivel='basico'): 
        """
        Metodo Nivel de Estudios. Indica el nivel de estudios de un alumno.
        Inputs:
            nivel: descripcion
        Outputs:
            res: Devuelve el nivel de estudio de un alumno.
        """  
        res = super().nivel_estudios(nivel) 
        return res

class profesor(Persona):
    pass
    """ 
    Profesor. Es una clase que hereda de persona y que por lo tanto realiza lo que cualquier otra persona, pero se diferencia con particularidades.

    Atributos:
    ==========
    altura: Se refiere a la altura del profesor

    Metodos:
    ========
    altura_ajustada: Indica el ajuste de la altura del profesor. 
    
    """
    def altura_ajustada(self, altura):
        """
        Metodo altura ajustada. Indica el ajuste de la altura del profesor.
        Inputs:
            altura: descripcion en cm.
        Outputs:
            res: Devuelve la altura de una persona.
        """
        res =  f"La altura de la persona es: {altura-0.5}"
        return res

class personal(Persona):
    pass

    def altura_ajustada(self, altura):
        return f"La altura de la persona es: {altura-0.10}"



