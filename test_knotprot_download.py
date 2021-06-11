from knotprot_download import get_proteins


def test_get_proteins():
    proteins = get_proteins("https://knotprot.cent.uw.edu.pl/browse/?raw=1&set=False&bridgeType=probab%2Ccov_ion&knotTypes=%2B31")
    assert len(proteins)>=69

