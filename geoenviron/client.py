import httpx
import logging

class GeoEnvironClient:
    def __init__(self, base_url: str, username: str, password: str):
        self.timeout = httpx.Timeout(120.0, connect=5.0)
        self.base_url = base_url
        self.client = httpx.Client(
            base_url=self.base_url,
            auth=(username, password),
            timeout=self.timeout,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
        )

    def _hent_bilag(self, dokument_id: str):
        try:
            response = self.client.get(
                "/view_bldAppendix",
                params={"$filter": f"doc_seq_no eq {dokument_id}"},
            )
            response.raise_for_status()
                        
            return response.json().get("value", [])
        except httpx.HTTPError as e:
            logging.error("Failed to retrieve attachments for document ID %s: %s", dokument_id, e)
            raise

    def hent_sager(self, params: dict = None) -> dict|None:
        try:
            response = self.client.get(
                "/view_bldCasefile()",
                params=params
            )
            response.raise_for_status()
            data = response.json()
            
            return data["value"] if data["value"] else None
        except httpx.HTTPError as e:
            logging.error("Failed to retrieve cases: %s", e)
            raise

    def hent_dokumenter(self, sag: dict, inkluder_bilag: bool = True) -> list[dict]:
        try:            
            sags_id = sag.get("task_seq_no")
            if sags_id is None:                
                return []
            
            sags_id = f"{str(sags_id)}M"

            response = self.client.get(
                    "/view_bldDocument",
                    params={
                        "$filter": f"task_seq_no eq {sags_id}",
                        "$orderby": "doc_date asc",
                    },
                )
            response.raise_for_status()
            dokumenter = response.json().get("value", [])
            
            if dokumenter:
                if inkluder_bilag:
                    for dokument in dokumenter:
                        dokument_id = dokument.get("doc_seq_no")
                        if dokument_id:
                            bilag = self._hent_bilag(dokument_id)
                            dokument["bilag"] = bilag
                return dokumenter                
            
            return []
        except httpx.HTTPError as e:
            logging.error("Failed to retrieve documents for case ID %s: %s", sags_id, e)
            raise

    