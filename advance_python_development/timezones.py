from datetime import datetime,timezone

print(datetime.now()) # naive

print(datetime.now(timezone.utc)) #aware