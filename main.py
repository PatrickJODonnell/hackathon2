import requests
import json


def calculate_territorry(company: str):
    url = f"https://noticeably-touching-cow.ngrok-free.app/territory"
    result = requests.get(url, params={"company": company})
    return result["territory"]


def calculate_company_revenue(company: str, territory: str):
    url = f"https://noticeably-touching-cow.ngrok-free.app/gather"
    result = requests.get(url, params={"company": company, "territory": territory})
    return result["company_revenue"]


def calculate_company_size(company: str, territory: str):
    url = f"https://noticeably-touching-cow.ngrok-free.app/gather"
    result = requests.get(url, params={"company": company, "territory": territory})
    return result["company_size"]


def calculate_industry(company: str, territory: str):
    url = f"https://noticeably-touching-cow.ngrok-free.app/gather"
    result = requests.get(url, params={"company": company, "territory": territory})
    return result["industry"]


def main_territory(event: dict, context: dict) -> dict:
    company = event['queryStringParameters']['company']
    response = calculate_territorry(company=company)
    return {
        "statusCode": 200,
        "body": json.dumps(response.json())
    }


def main_calculate_company_rev(event: dict, context: dict) -> dict:
    company = event['queryStringParameters']['company']
    territory = event['queryStringParameters']['territory']
    response = calculate_company_revenue(company=company, territory=territory)
    return {
        "statusCode": 200,
        "body": json.dumps(response.json())
    }


def main_calculate_company_size(event: dict, context: dict) -> dict:
    company = event['queryStringParameters']['company']
    territory = event['queryStringParameters']['territory']
    response = calculate_industry(company=company, territory=territory)
    return {
        "statusCode": 200,
        "body": json.dumps(response.json())
    }


def main_calculate_industry(event: dict, context: dict) -> dict:
    company = event['queryStringParameters']['company']
    territory = event['queryStringParameters']['territory']
    response = calculate_industry(company=company, territory=territory)
    return {
        "statusCode": 200,
        "body": json.dumps(response.json())
    }
