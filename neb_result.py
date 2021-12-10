import aiohttp
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
import time

SYMBOL = '25561787'
sdate = '01-05-2058'
edate = '12-30-2060'
dates = pd.date_range(start=sdate, end=edate)
dates = [str(d).replace('-','/')[:10] for d in dates]

url = 'https://neb.ntc.net.np/results.php'
start_time = time.time()

async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(len(dates)):
          data = {
              'symbol':SYMBOL,
              'dob':str(dates[i]),
              'submit':'Submit'
          }
          url = 'https://neb.ntc.net.np/results.php'

          async with session.post(url, data = data) as resp:
            res = await resp.text()

            soup = BeautifulSoup(res, 'html.parser')
            if soup.find(class_='subhead'): #forchecking if result was extracted
              with open('result.html','w') as f:
                f.write(res)
              print(res)
              break

    time.sleep(0.1)       
asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))
