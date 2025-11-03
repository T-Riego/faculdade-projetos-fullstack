def loginUsuario(perfil):
  if perfil.lower() == "admin":
    print("Bem vindo, administrador!")
  else:
    print("Bem vindo, usuário!")

loginUsuario("admin")
loginUsuario("Admin")
loginUsuario("user")
loginUsuario("usuario")
loginUsuario("Tiago")