from .gather_keys_oauth2 import OAuth2Server
import fitbit


def client(tokens):
    """Instantiate a Fitbit client object. Requires tokens from Fitbit development account.

    Args:
        tokens (dataframe): A dataframe containing the client id and client secret for the Fitbit development account.

    Returns:
        object: The instantiated Fitbit client object.
    """
    CLIENT_ID = tokens.loc[
        tokens.token_name == "OAuth 2.0 Client ID", "token_id"
    ].item()
    CLIENT_SECRET = tokens.loc[tokens.token_name == "Client Secret", "token_id"].item()

    server = OAuth2Server(CLIENT_ID, CLIENT_SECRET)
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

