# https://towardsdatascience.com/using-the-fitbit-web-api-with-python-f29f119621ea

# This is a python file you need to have in the same directory as your code so you can import it
import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd
import datetime

# You will need to put in your own CLIENT_ID and CLIENT_SECRET as the ones below are fake
CLIENT_ID = "12A1BC"
CLIENT_SECRET = "12345678901234567890123456789012"

