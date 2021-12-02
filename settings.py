import os

DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    print("I am in debug mode.")
    from pathlib import Path
    from dotenv import load_dotenv
    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path=env_path)
    from settings_files.development import *
else:
    print("I am in production mode.")
    from settings_files.production import *