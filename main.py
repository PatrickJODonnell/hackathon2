import requests
from snowflake.snowpark.functions import udf
from snowflake.snowpark.types import StringType

def calculate_territorry(company: str):
    url=f'https://noticeably-touching-cow.ngrok-free.app/territory'
    result = requests.get(url, params={'company': company})
    return (result['territory'])                    


def calculate_company_revenue(company: str, territory: str):
    url=f'https://noticeably-touching-cow.ngrok-free.app/gather'
    result = requests.get(url, params={'company': company, 'territory': territory})
    return (result['company_revenue'])                    


def calculate_company_size(company: str, territory: str):
    url=f'https://noticeably-touching-cow.ngrok-free.app/gather'
    result = requests.get(url, params={'company': company, 'territory': territory})
    return (result['company_size'])                    


def calculate_industry(company: str, territory: str):
    url=f'https://noticeably-touching-cow.ngrok-free.app/gather'
    result = requests.get(url, params={'company': company, 'territory': territory})
    return (result['industry'])                    




