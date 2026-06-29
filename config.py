import os

environment = os.getenv("ENVIRONMENT", "development")

if environment == "development":
    from config_dev import *
else:
    from config_stage import *