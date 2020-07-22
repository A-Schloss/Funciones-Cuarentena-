# - * - codificación: utf-8 - * -
"" "Clases.ipynb
Generado automáticamente por Colaboratory.
El archivo original se encuentra en
    https://colab.research.google.com/drive/13wNtg0AMt9U5fTX0pvzzxE1V_W6d6VV-
# 2. Clases
## 2.1 Introducción
Programación Orientada Objetos es uno de los paradigmas más efectivos al momento de querer desarrollar algún tipo de software. En este pardigma se desarrolla * clases * que representa cosas y / o situaciones, y de las clases se derivan los objetos.
Cuando se desarrola una clase, se define de manera general el comportamiento de toda una gama de objetos relacionados a la semántica.
Cuando se declara o define un objeto de una clase, cada objeto es equpado de manera automática con el comportamiento general de la clase, después se puede ir defiendo de manera más dellada el objeto. 
Cuando se dice que se * crea una instancia de una clase * se hace referencia a la creación de un objeto derivado de una clase en particular, y dentro del programa principal se trabaja con la instancia, no con la clase tal cual.
## 2.2 Creando y usando una clase
Se puede modelar casi cualquier cosa usando clases. En esta sección comenzaremos a definir una clase `Perro` que describa a cualquier tipo de perro, ninguno en particular. Inicialmente se considerarán solo dos campos el `Nombre` y la` Edad`, ya que en cualquier mascota perro son comunes. Una vez definida la clase se definió la forma de poder generar dos instancias (objetos) de esta clase. Se definenán dos acciones `Sentarse` y` Rodar`.
### 2.2.1 Creando la clase perro
Cada instancia creada de la clase `Perro` tendrá tener un` Nombre` y la `Edad`, observe la siguiente celda.
"" "

clase  Perro ():
    "" "Un modelo muy abstacto de un Perro" ""
    
    def  __init__ ( self , Nombre , Edad ):
        "" "Inicializa los atributos de Nombre y Edad" ""
        auto . Nombre  =  Nombre
        auto . Edad  =  Edad
        
    def  Sentarse ( auto ):
        "" "Simula un perro sentado después de que se le da orden" ""
        print ( self . Nombre . title () +  "está sentado." )
        
    def  Rodar ( auto ):
        "" "Simula un perro rodando en el piso después de que se le da la orden" ""
        print ( self . Nombre . title () +  "está rodando." )

"" "Hay muchos elementos que se deben analizar con detalle, observar la sintaxis para definir una clase es 
`clase <Nombre_clase> ():`
donde `Nombre_clase` es el nombre de la clase, observe las siguientes líneas debn de estar indentadas ya que así lo pide python para el alcance de las funciones y de las variables. 
Se pueden visualizar tres funciones dentro de la clase y todas ellas tienen como argumento `self` que implica que tienen funciones específicas a la estructura de la clase. observe que los comportamientos `Sentarse (self)` y `Rodar (self)` son comportamientos o clases que se definen por el usuario, las funciones que se encuentran como ** METODOS ** y son completamente modificados por el usuario.
La primer función `def __init __ (self, Nombre, Edad)` se le conoce como constructor, observar que tiene los campos de Nombre y Edad, que son los campos que se han encontrado comunes entre los perros, observar que dentro de esa función hay dos elementos `self.Nombre` y` self.Edad`, a estos elementos se le tienen como atributos y deben de llevar el prefijo `self.` ya esta directiva indica que son elementos propios de la clase.
### 2.2.2 Creando una instancia de una clase
Una clase puede ser vida como un conjunto de instrucciones para realizar un objeto. La clase `Perro` es un conjunto de instrucciones que le indica a Python coo crear instancias indiiduales que representan perros de forma general.
En la siguiente celda se muestra la manera de hacer un perro específico pero basádonos en la clase `Perro`
"" "

mi_perro  =  Perro ( 'Orejas' , 7 )
print ( "El nombre de mi perro es"  +  mi_perro . Nombre . title () +  "." )
print ( "La edad de mi perro es"  +  str ( mi_perro . Edad ) +  "anios" )

"" "En la línea 1 de la línea anterior, se genera un objeto de la clase` Perro` y manda a llamar al constructor, la cadena `` Orejas '' lo asigna a attibuto `self.Nombre`, mientras que el número `7` lo asigna al atributo` self.Edad`. 
### 2.2.3 Accediendo a atributos y métodos
Observe que en la anterior en la línea 2 y 3 se está accediendo a los atributos de una clase, para esto se debe de tener en cueta el nombre de la instancia (objeto), que en este caso es `mi_perro` y después se debe de poner el nombre del atributo acompañado previamente de un `.` De tal manera que con` mi_perro.Edad` se está accediendo al atributo de Edad.
De la misma manera se puede acceder a los métodos de una clase, de tal forma que se utiliza la instrucción `mi_perro.Sentarse ()` se invocando el método sentado propio de la clase `Perro` como se muestra en la siguiente celda .
"" "

mi_perro  =  Perro ( 'Orejas' , 7 )
print ( "El nombre de mi perro es"  +  mi_perro . Nombre . title () +  "." )
print ( "La edad de mi perro es"  +  str ( mi_perro . Edad ) +  "anios" )

mi_perro . Sentarse ()
mi_perro . Rodar ()

"" "### 2.2.4 Creando múltiples instancias.
Se pueden crear tantas instancias como lo que desean de una clase única, la condición única que debe tener en cuenta es que los nombres de las instancias deben ser de distancia, aunque los atributos que sean iguales, observen la siguiente celda.
"" "

mi_perro  =  Perro ( 'Orejas' , 7 )
tu_perro  =  Perro ( 'Bony' , 8 )

print ( "El nombre de mi perro es:"  +  mi_perro . Nombre . title ())
print ( mi_perro . Nombre . title () +  "tiene"  +  str ( mi_perro . Edad ) +  "anios de edad." )
print ( " \ n " )

print ( "El nombre de tu perro es:"  +  tu_perro . Nombre . title ())
print ( tu_perro . Nombre . title () +  "tiene"  +  str ( tu_perro . Edad ) +  "anios de edad." )

"" "## 2.3 Ejercicios
1. a) Crear una clase llamada `Restaurante`. El método `__init __ ()` debe de aceptar dos atributos: El `nombre_restaurant` y el` tipo_cocina`.b) Crear un método que se llame `describe_restaurant` que imprima: * El nombre del restaurant es: ------ * y * El tipo de comida que se sirve es: ------- *. c) Generar
"" "

 restaurante de clase ():
	"" "Clase tipo restaurante" "" 
	def  __init__ ( self , restaurant_name , restaurant_type , restaurant_OC ):
		"" "Inicialización de los atributos" "" 
		auto . restaurant_name = restaurant_name
		auto . restaurant_type = restaurant_type
		auto . restaurant_OC = restaurant_OC 
		auto . cliente_servicio  =  0
	def  get_descriptive_name ( self ):
		"" "Imprime las caracteristicas en la pantalla" "" 
		long_name  =  self . restaurant_name + '' + self . restaurant_type  +  '' + self . restaurant_OC  
		return  long_name . título ()
	def  número_libro ( sefl ):
		"" "Imprime los clientes qeu se han atendido" ""
		print ( "se han atendido" + str ( sefl . client_serve ) +  "clientes." )
		 
my_new_restaurant = restaurant ( 'Chiringuito' , 'Mexicana' , 'open' )
print ( my_new_restaurant . get_descriptive_name ())
my_new_restaurant . read_number ()