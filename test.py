from datetime import datetime, timezone
from pydantic import BaseModel


class Test(BaseModel):
    data: datetime

now = datetime.now(timezone.utc)

# d = Test(data="2025-09-18T04:46:42.822+00:00")
d = Test(data="2025-06-08 18:26:17")

print(now)
print(d.data.replace(tzinfo=timezone.utc) < now)