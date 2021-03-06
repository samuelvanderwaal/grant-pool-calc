import sys
import requests
import json
import pytz
from dateutil import parser, utils
from datetime import datetime

# Create default UTC tzone object
default_tz = pytz.utc

# GraphQL Queries
grant_pool = """
{
    factoids
    {
    grantPool
    }
}
"""

history = """
{
    history
    {
        factoids
            {
            grantPool
        }
    }
}
 """

r1 = requests.post("http://159.89.231.170/", json={'query': grant_pool})
r2 = requests.post("http://159.89.231.170/", json={'query': history})

resp1 = json.loads(r1.text)
resp2 = json.loads(r2.text)

current_grant_fcts = resp1["data"]["factoids"]["grantPool"]

# All historical grant pool data sorted with most recent last.
# Data is formatted as lists: [unix_ts_ms, grant_pool_fcts]
data = resp2["data"]["history"]["factoids"]["grantPool"]

# The first item will almost always be an incomplete day so use the next two
# for calculating the most recent daily amount going into the grant pool.
# We start at the end of the list to get the most recent values.
daily_fct_to_grant_pool = float(data[-2][1]) - float(data[-3][1])

print(daily_fct_to_grant_pool)

# Parse end date supplied by user and assume UTC
end_time = utils.default_tzinfo(parser.parse(sys.argv[1]),
                                default_tz).timestamp()
current_time = datetime.now(pytz.utc).timestamp()

days = (end_time - current_time) / 86400.0
future_fct_amount = current_grant_fcts + daily_fct_to_grant_pool * days

print(future_fct_amount)
