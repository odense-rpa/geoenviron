import os

from geoenviron.client import GeoEnvironClient

def test_hent_sag():
    client = GeoEnvironClient(base_url=os.getenv("API_URL"), username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
    sag = client.hent_sag(params={"$top": 1, "$filter": f"case_no eq '2023-2749'"})
    assert sag is not None

def test_hent_dokumenter():
    client = GeoEnvironClient(base_url=os.getenv("API_URL"), username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
    sag = client.hent_sag(params={"$top": 1, "$filter": f"case_no eq '2023-2749'"})
    dokumenter = client.hent_dokumenter(sag=sag, inkluder_bilag=True)
    assert isinstance(dokumenter, list)
    assert len(dokumenter) > 0

