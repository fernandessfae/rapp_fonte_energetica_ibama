import json
import requests
import urllib3
import pandas as pd
from requests.exceptions import RequestException

def is_json_link(link: str) -> bool:

    # Disable SSL warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        # Define a timeout for the request and raise a status code
        response = requests.get(link, timeout=10, verify=False)  
        response.raise_for_status()

        # Tenta decodificar o conteúdo da resposta como JSON
        # Se o conteúdo não for JSON válido, json.loads() ou response.json() levantará um ValueError
        json.loads(response.text)
        return True
    
    except ValueError:
        return False
    
    except RequestException as e:
        # Capture requisition errors such as connection errors, timeouts, etc.
        print(f"Error to access {link}: {e}")
        return False
    
    except Exception as e:
        print(f"Unexpected error occurred while checking {link}: {e}")
        return False

def convert_json_to_dataframe(link: str) -> pd.DataFrame:

    if not is_json_link(link):
        raise ValueError(f"The provided link {link} is not a valid JSON link.")

    response = requests.get(link, verify=False)

    if response.status_code != 200:
        raise ConnectionError(f"Failed to retrieve data from {link}. "
                              f"Status code: {response.status_code}")
    
    data = json.loads(response.content)
    df: pd.DataFrame = pd.DataFrame.from_dict(data['data'])
    return df


if __name__ == "__main__":
    energetic_source_cnpj_ibama_etl: pd.DataFrame = convert_json_to_dataframe(
    'https://dadosabertos.ibama.gov.br/dados/RAPP/fonteEnergetica/relatorio.json'
    )
    print(energetic_source_cnpj_ibama_etl.head())