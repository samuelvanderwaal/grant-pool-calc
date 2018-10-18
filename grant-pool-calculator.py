import sys
import pytz
from dateutil import parser, tz, utils
from datetime import datetime

# Create default UTC tzone object
default_tz = pytz.utc

current_grant_fcts = float(sys.argv[1])
daily_fct_to_grant_pool = float(sys.argv[2])

# Parse end date supplied by user and assume UTC if no timzeone is provided
end_date = utils.default_tzinfo(parser.parse(sys.argv[3]), default_tz)

current_time = datetime.now(pytz.utc)

# Factoshi updates the grant pool size once a day at 00:00 UTC, so create today's date to start then
today_date = datetime(current_time.year, current_time.month, current_time.day, tzinfo=pytz.utc)

date_diff = end_date - today_date
days = float(date_diff.days) + float(date_diff.seconds)/86400
future_fct_amount = current_grant_fcts + daily_fct_to_grant_pool * days

print(future_fct_amount)
