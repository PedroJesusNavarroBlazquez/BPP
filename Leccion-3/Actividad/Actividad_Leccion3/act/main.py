from utils import Actividad3

p = Actividad3.Persona(50,"Kass")
print(p.mayor_edad())

a = Actividad3.alumno(19,"Paco")
print(a.nivel_estudios())

p1 = Actividad3.personal(50,"Kass")
print(p1.get_edad())
print(p1.altura)

a1 = Actividad3.alumno(19,"Paco")
print(a1.nivel_estudios())


persona_pedro = Actividad3.Persona(17, "Pedro")
persona_pedro.mayor_edad()

print(persona_pedro.get_edad())
