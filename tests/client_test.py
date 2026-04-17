import os

from geoenviron.client import GeoEnvironClient

def test_hent_sager():
    client = GeoEnvironClient(base_url=os.getenv("API_URL"), username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
    sager = client.hent_sager(params={"$top": 1, "$filter": f"case_no eq '2023-2749'"})
    assert isinstance(sager, list)

def test_hent_dokumenter():
    client = GeoEnvironClient(base_url=os.getenv("API_URL"), username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
    sager = client.hent_sager(params={"$top": 1, "$filter": f"case_no eq '2023-2749'"})
    if sager:
        sag = sager[0]
        dokumenter = client.hent_dokumenter(sag=sag, inkluder_bilag=True)
    assert isinstance(dokumenter, list)
    assert len(dokumenter) > 0

