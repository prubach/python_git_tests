from urllib.request import Request, urlopen

SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?set=True&bridgeType=probab&slipknotTypes=%2B31&raw=1'
DOWNLOAD_LINK = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}.png'


def get_proteins(search_string=SEARCH_STRING):
    req = Request(search_string, method='GET')
    proteins = []
    with urlopen(req) as resp:
        data = resp.read().decode('utf-8')
        for line in data.splitlines():
            if len(line)>4 and not line.startswith('#'):
                cells = line.strip().split(';')
                proteins.append((cells[0],cells[1]))
    return proteins

