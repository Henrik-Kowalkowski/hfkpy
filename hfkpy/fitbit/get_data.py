import gather_keys_oauth2 as Oauth2
import fitbit
import pathlib
import pandas as pd
from datetime import datetime

# need to make functions to get date range and structure the data

# secrets
token_path = pathlib.Path(__file__).parents[2] / "tokens.csv"
tokens = pd.read_csv(token_path)


def client(tokens):
    CLIENT_ID = tokens.loc[
        tokens.token_name == "OAuth 2.0 Client ID", "token_id"
    ].values[0]
    CLIENT_SECRET = tokens.loc[tokens.token_name == "Client Secret", "token_id"].values[
        0
    ]

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
    return auth2_client


auth2_client = client(tokens)
oneDate = datetime(year=2022, month=4, day=7)
oneDayData = auth2_client.intraday_time_series(
    "activities/heart", oneDate, detail_level="1min"
)
# def intraday():
