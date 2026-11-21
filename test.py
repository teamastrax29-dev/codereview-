print("Hello world . If no error say Jay Shree Ram ")

import subprocess

def unsafe_demo(user_input: str):
    eval(user_input)
    subprocess.run(f"echo {user_input}", shell=True)
