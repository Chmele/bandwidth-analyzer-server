from influxdb import InfluxDBClient
import json


client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('bandwidth')


def insert_data(data):
    print(data)\
    # if data['error']:
    if data.error:
        print('error')
        return
    body = [{
        'measurement': 'bandwidth',
        'tags': {
            'client': data.remote_host,
        },
        'time': data.time,
        'fields': {
            'bandwidth': data.received_Mbps
        }
    }]
    client.write_points(body)
    print(body)