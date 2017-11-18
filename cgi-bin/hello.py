#!/usr/bin/env python

import cgitb

cgitb.enable()  
print("Content-Type: text/html")
print("")

print("""<html>
	<head>
		<title>Formulario HTML</title>
	</head>
	<body>
	<p></p>
		<form>
			<label>Ingrese su correo</label>
				<input type="text" name="usuario" />
			<input type="submit" value="Ingresar" />
		</form>
	</body>
</html>""") 

print("""</p>
		<form>
			<label>Ingrese su correo</label>
				<input type="text" name="usuario" />
			<input type="submit" value="Ingresar" />
		</form>
	</body>
</html>
""")
