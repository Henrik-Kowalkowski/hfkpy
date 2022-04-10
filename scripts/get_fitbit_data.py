# https://towardsdatascience.com/using-the-fitbit-web-api-with-python-f29f119621ea

import pathlib
import pandas as pd

# secrets
token_path = pathlib.Path(__file__).parents[1] / "tokens.csv"
tokens = pd.read_csv(token_path)

# this is a python file you need to have in the same directory as your code so you can import it
import gather_keys_oauth2 as Oauth2
import fitbit


CLIENT_ID = tokens.loc[tokens.token_name == "OAuth 2.0 Client ID", "token_id"].values[0]
CLIENT_SECRET = tokens.loc[tokens.token_name == "Client Secret", "token_id"].values[0]

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token["access_token"])
REFRESH_TOKEN = str(server.fitbit.client.session.token["refresh_token"])
auth2_client = fitbit.Fitbit(
    CLIENT_ID,
    CLIENT_SECRET,
    oauth2=True,
    access_token=ACCESS_TOKEN,
    refresh_token=REFRESH_TOKEN,
)

# most granular data is intraday
# https://dev.fitbit.com/build/reference/web-api/intraday/get-activity-intraday-by-date/
oneDate = pd.datetime(year=2022, month=4, day=7)
oneDayData = auth2_client.intraday_time_series(
    "activities/heart", oneDate, detail_level="1min"
)

pd.DataFrame(oneDayData["activities-heart-intraday"]["dataset"])

oneDayData = auth2_client.intraday_time_series(
    "activities/calories", oneDate, detail_level="1min"
)

auth2_client.sl
