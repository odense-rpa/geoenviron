# geoenviron

Python-klient til GeoEnviron API'et, som giver adgang til bygge- og miljøsagsakter, dokumenter og bilag fra et dansk kommunalt sagsstyringssystem.

> Denne klient er ikke officielt støttet eller godkendt af leverandøren bag GeoEnviron. Brug på eget ansvar.

## Om GeoEnviron

GeoEnviron er et kommunalt sagsstyringssystem til bygge- og miljøsager. API'et eksponerer sagsakter, dokumenter og bilag via OData-forespørgsler med HTTP Basic Auth.

## Installation

```bash
uv add git+https://github.com/odense-rpa/geoenviron
```

## Forudsætninger

- Python ≥ 3.13
- Adgang til en GeoEnviron-installation (URL, brugernavn og adgangskode)

## Nuværende funktionalitet

Klienten autentificerer med brugernavn og adgangskode (HTTP Basic Auth) og stiller følgende funktioner til rådighed:

| Funktion | Beskrivelse |
|---|---|
| `hent_sager` | Hent sagsakter med OData-filtrering (`$filter`, `$top` m.fl.) |
| `hent_dokumenter` | Hent dokumenter for en given sag, sorteret efter dato |
| `hent_bilag` | Hent bilag til et enkelt dokument |

```python
from geoenviron import GeoEnvironClient

client = GeoEnvironClient(
    base_url="https://geoenviron.kommune.dk",
    username="brugernavn",
    password="adgangskode",
)

sager = await client.hent_sager(filter="Status eq 'Åben'", top=100)
dokumenter = await client.hent_dokumenter(sags_id="12345", inkluder_bilag=True)
bilag = await client.hent_bilag(dokument_id="67890")
```

## Test

Integrationstests køres mod en live GeoEnviron-instans. Sæt følgende miljøvariabler før kørsel:

```bash
export API_URL="https://geoenviron.kommune.dk"
export USERNAME="brugernavn"
export PASSWORD="adgangskode"

uv run pytest
```

## Afhængigheder

| Pakke | Formål |
|---|---|
| `httpx` | HTTP-klient til asynkrone kald mod GeoEnviron REST API |
| `automation-server-client` | Klientbibliotek til Odense RPA Automation Server |
| `pytest` | Testframework til integrationstests |
| `ruff` | Linter og formatter |

## Licens

MIT
