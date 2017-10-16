PREFIX = '[U:1:'
BASE = 76561197960265728


def convert_id3_to_id64(steamid: str) -> int:
    if not isinstance(steamid, str):
        raise TypeError('steamid must be a string')

    if PREFIX not in steamid or ']' not in steamid[-1]:
        raise ValueError("Expected steam id3 string such as [U:1:22202] instead got {}".format(steamid))

    u_index = steamid.find(PREFIX)
    steamid = steamid[u_index + len(PREFIX):-1]
    steamid = int(steamid)
    return steamid + BASE
