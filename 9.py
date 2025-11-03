import random
import time


OTP_LENGTH = 6
OTP_TTL = 120        
MAX_ATTEMPTS = 3     
LOCK_SECONDS = 30    


otp_store = {}      
attempts = {}       
lock_until = {}     

def gen_otp():
    start = 10**(OTP_LENGTH-1)
    end = 10**OTP_LENGTH - 1
    return str(random.randint(start, end))

def issue_otp(user):
    otp = gen_otp()
    expiry = time.time() + OTP_TTL
    otp_store[user] = (otp, expiry)
    attempts[user] = 0
    print(f"[DEMO] OTP for {user}: {otp}  (valid {OTP_TTL}s)")

def is_locked(user):
    t = lock_until.get(user, 0)
    return time.time() < t

def verify_otp(user, typed):
    
    if is_locked(user):
        rem = int(lock_until[user] - time.time())
        return False, f"Temporarily locked. Try after {rem} seconds."

    
    entry = otp_store.get(user)
    if not entry:
        return False, "No OTP issued. Please request an OTP."

    otp, expiry = entry
    if time.time() > expiry:
        otp_store.pop(user, None)
        return False, "OTP expired. Request again."

    if typed == otp:
        
        otp_store.pop(user, None)
        attempts[user] = 0
        return True, "OTP verified successfully!"
    else:
        
        attempts[user] = attempts.get(user, 0) + 1
        if attempts[user] >= MAX_ATTEMPTS:
            lock_until[user] = time.time() + LOCK_SECONDS
            attempts[user] = 0
            return False, f"Too many wrong tries. Locked for {LOCK_SECONDS} seconds."
        else:
            left = MAX_ATTEMPTS - attempts[user]
            return False, f"Incorrect OTP. Attempts left: {left}"


def easy_demo():
    print("=== Easy OTP Demo ===")
    user = input("Enter user-id (demo): ").strip()
    if not user:
        print("User-id required.")
        return

    while True:
        print("\n1) Issue OTP   2) Verify OTP   3) Lock status   4) Exit")
        choice = input("Choose (1-4): ").strip()
        if choice == "1":
            issue_otp(user)
        elif choice == "2":
            code = input("Enter OTP: ").strip()
            ok, msg = verify_otp(user, code)
            print(msg)
        elif choice == "3":
            if is_locked(user):
                rem = int(lock_until[user] - time.time())
                print(f"Locked for {rem} more seconds.")
            else:
                print("Not locked.")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    easy_demo()
