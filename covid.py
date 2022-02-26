import requests
import json
import discord
from datetime import date, timedelta, datetime

# for debugging
def get_api_url():
  date_two_days_before = date.today() - timedelta(2)
  api_url = "https://webhooks.mongodb-stitch.com/api/client/v2.0/app/covid-19-qppza/service/REST-API/incoming_webhook/global?country_iso3=NZL&hide_fields=_id,%20country,%20country_code,%20country_iso2,%20country_iso3,%20loc,%20state,%20uid&min_date=" + str(date_two_days_before) + "T00:00:00.000Z"
  return api_url

def fetch_data():
  # retreive data
  response = requests.get(get_api_url())
  json_data = json.loads(response.text)
  
  return json_data[-1]

def get_covid_info():
  covid_info = fetch_data()
  covid_dict = {}
  covid_dict["confirmed"] = covid_info["confirmed"]
  covid_dict["deaths"] = covid_info["deaths"]
  covid_dict["confirmed_daily"] = covid_info["confirmed_daily"]
  covid_dict["date"] = get_nz_date(covid_info["date"])
  return covid_dict

def get_nz_date(us_time):
  us_time_str = us_time.split("T")[0]
  nz_date = datetime.strptime(us_time_str, '%Y-%m-%d') + timedelta(1)
  return str(nz_date.date())
  