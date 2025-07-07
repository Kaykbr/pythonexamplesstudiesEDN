def verificar_senha_forte(senha):
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres"
    
    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        return False, "A senha deve conter pelo menos um número"
    
    return True, "Senha forte!"

print("Verificador de Senha Forte")
print("Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número")
print("Digite 'sair' para encerrar o programa")

while True:
    senha = input("Digite uma senha: ")
    
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    eh_forte, mensagem = verificar_senha_forte(senha)
    
    if eh_forte:
        print(f"✓ {mensagem}")
        print("Senha aceita! Programa encerrado.")
        break
    else:
        print(f"✗ {mensagem}")
        print("Tente novamente.")
