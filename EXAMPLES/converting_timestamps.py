from datetime import datetime

raw_ts = 239285298509

ts = raw_ts / 1000

dt = datetime.fromtimestamp(ts)

print(dt.strftime("%Y/%M"))

df['timestamp'] = df['timestamp'].astype('float', errors = 'raise')
df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('datetime', inplace=True) 