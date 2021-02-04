from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('bandwidth')
q = client.query('SELECT "bandwidth" FROM "bandwidth"."autogen"."bandwidth"')
print((q.raw['series'][0]['values']))
