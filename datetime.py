from datetime import datetime, timezone, timedelta
dt = datetime.now(timezone.utc)
print(dt)

pdx = timezone(timedelta(hours=7))
ldn = timezone(timedelta(hours=1))
nyc = timezone(timedelta(hours=-4))

pdxdt = datetime.pdx
print(pdxdt)

