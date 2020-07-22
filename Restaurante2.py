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
	def  set_number_served ( self , client ):
		si  cliente  > =  auto . cliente_servicio :
			auto . cliente_servicio  =  cliente
		de lo contrario : print ( "No puedes hacer eso" )  
my_new_restaurant = restaurant ( 'Chiringuito' , 'Mexicana' , 'open' )
print ( my_new_restaurant . get_descriptive_name ())
my_new_restaurant . read_number ()
my_new_restaurant . set_number_served ( 23 )
my_new_restaurant . read_number ()
my_new_restaurant . set_number_served ( 50 )
my_new_restaurant . read_number ()
my_new_restaurant . set_number_served ( 10 )
my_new_restaurant . read_number ()
