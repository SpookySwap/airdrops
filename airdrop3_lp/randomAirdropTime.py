import random
import pytz
from datetime import datetime, timedelta, timezone

# 19 April 2021 18:00:01 UTC
startUnixTimestamp = 1618855201
startTime = datetime.fromtimestamp(startUnixTimestamp)
print("Start time UTC: {}".format(startTime.astimezone(pytz.utc).isoformat()))

# Starting unix timestamp used for seed
random.seed(startUnixTimestamp)

# Get a random number in seconds in a 3 day time delta
timeWindowInSeconds = timedelta(days=3).total_seconds()
randomTime = random.randrange(1, timeWindowInSeconds)

# Find the end time
endTime = startTime + timedelta(seconds=randomTime)
print("  End time UTC: {}".format(endTime.astimezone(pytz.utc).isoformat()))
