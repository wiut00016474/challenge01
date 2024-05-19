import os
import hashlib

def get_flag():
    flag = "flag{super_secret_flag}"
    return flag

def hash_flag(flag):
    return hashlib.sha256(flag.encode()).hexdigest()

def main():
    required_file = "Whiterabbit.py"
    required_content = "Wake up Neo"
    
    if os.path.exists(required_file):
        with open(required_file, "r") as f:
            content = f.read().strip()
        if content == required_content:
            flag = get_flag()
            hashed_flag = hash_flag(flag)
            print(f"Flag: {hashed_flag}")
        else:
            print(f"You have very little work left, go inside and wake up Neo")
    else:
        print(f"You are on the mattress wake up Neo first create a python or text file called Whiterabbit")

if __name__ == "__main__":
    main()
