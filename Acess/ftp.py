from ftplib import FTP, error_perm
import os

def acess_ftp(host, user, passw):
    FTP_HOST = host
    FTP_USER = user
    FTP_PASS = passw

    REMOTE_FILE_PATH = ""
    LOCAL_FILE_PATH = ""

    ftp = None
    try:
        print(f"Try connect in server: {FTP_HOST}...")
        ftp = FTP(FTP_HOST, FTP_USER, FTP_PASS)
        ftp.encoding = "utf-8"
        
        print("Connection sucessful")
        ftp.dir()
        
        REMOTE_FILE_PATH = input("Specify the target directory: ")
        LOCAL_FILE_PATH = os.path.basename(REMOTE_FILE_PATH)
        print(f"Download {REMOTE_FILE_PATH} for {LOCAL_FILE_PATH}...")
        
        with open(LOCAL_FILE_PATH, "wb") as local_file:
            ftp.retrbinary(f"RETR {REMOTE_FILE_PATH}", local_file.write)

        print("Download sucessfuly")
        return LOCAL_FILE_PATH, REMOTE_FILE_PATH
    
    except FileNotFoundError as fNfE:
        print(f"Error: The file '{fNfE}' not found in server")
    except error_perm as eP:
        print(f"Permission error: {eP}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if ftp:
            print("Close conection with server")
            ftp.quit()

    # if os.path.exists(LOCAL_FILE_PATH):
    #     print(f"Verify: The file '{LOCAL_FILE_PATH}' is download")
    # else:
    #     print(f"Verify: The download of '{LOCAL_FILE_PATH}' fail")
def upload_and_delete(host, user, passw, local_encrypted_file, remote_original_file):
    FTP_HOST = host
    FTP_USER = user
    FTP_PASS = passw
    
    ftp = None

    try:
        ftp = FTP(FTP_HOST, FTP_USER, FTP_PASS)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.encoding = "utf-8"
        remote_encrypted_file = remote_original_file + ".encrypted"
        print(f"Uploading encrypted file {local_encrypted_file} to {remote_encrypted_file}...")
        with open(local_encrypted_file, "rb") as file:
            ftp.storbinary(f"STOR {remote_encrypted_file}", file)
        print(f"Encrypted file uploaded successfully")
        print(f"Deleting original file: {remote_original_file}...")

        ftp.delete(remote_original_file)
        print(f"Original file deleted successfuly on server")

        if os.path.exists(local_encrypted_file):
            os.remove(local_encrypted_file)
            print(f"Local encrypted file {local_encrypted_file} removed.")
        
        return True
    except error_perm as eP:
        print(f"Permission error during upload/delete: {eP}")
        return False
    except FileNotFoundError:
        print("Local encrypted file not found or remote file not found for deleting.")
        return False
    except Exception as e:
        print(f"Unexpected error during upload/delete: {e}")
        return False
    finally:
        if ftp:
            print("Close connection with server")
            ftp.quit()
