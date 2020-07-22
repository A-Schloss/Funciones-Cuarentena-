 usuario de clase ():
	def  __init__ ( auto , nombre apellido , apellidos , pasword , correo electrónico ):
		auto . nombre_nombre = nombre_nombre
		auto . last_name = last_name
		auto . pasword = pasword
		auto . mail = mail
		auto . user_attempt  =  0
		auto . restablecer = 0
	def  describe_user ( self ):
		print ( ' \ n Nombre del usuario:' + self . first_name )
		print ( ' \ n apellido del usuario:' + self . last_name )
		print ( ' \ n pasword:' + self . pasword )
		print ( ' \ n mail:' + self . mail )
	def  greet_user ( self ):
		print ( 'Hola,' + self . first_name + ', bienvenido al programa.' )
	def  increment_login_attempts ( self , us ):
		si  nosotros  <=  10 :
			auto . user_attempt  =  us
		else : print ( "intentaste iniciar sesión demasiadas veces" )
	def  reset_loging_attempts ( self ):
	 	auto . reset = user_attempt
	def  número_libro ( sefl ):
		"" "Imprime los clientes qeu se han atendido" ""
		print ( "se han intentado iniciar sesion" + str ( sefl . user_attempt ) +  "veces." )
my_user = user ( 'Edwin' , 'Gonzalez' , 'Soporte321' , 'edwingonzales@gmail.es' )
print ( my_user . describe_user ())
my_user . increment_login_attempts ( 1 )
my_user . read_number ()
my_user . increment_login_attempts ( 2 )
my_user . read_number ()
my_user . increment_login_attempts ( 3 )
my_user . read_number ()
my_user . increment_login_attempts ( 4 )
my_user . read_number ()
my_user . increment_login_attempts ( 6 )
my_user . read_number ()
my_user . increment_login_attempts ( 7 )
my_user . read_number ()
my_user . increment_login_attempts ( 8 )
my_user . read_number ()
my_user . increment_login_attempts ( 9 )
my_user . read_number ()
my_user . increment_login_attempts ( 10 )
my_user . read_number ()
my_user . increment_login_attempts ( 11 )
my_user . read_number ()
my_user . increment_login_attempts ( 12 )
my_user . read_number ()
