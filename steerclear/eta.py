import requests, urllib

DISTANCEMATRIX_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'

def build_url(query):
    return DISTANCEMATRIX_BASE_URL + '?' + urllib.urlencode(query)

def build_distancematrix_url(start, end):
    query = {
        'origins': "%f,%f" % start,
        'destinations': "%f,%f" % end
    }
    return build_url(query)

def calculate_eta(start, end):
    url = build_distancematrix_url(start, end)
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        return None
    data = response.json()
    rows = data.get(u'rows', None)
    if rows is None:
        return None
    elements = rows[0].get(u'elements', None)
    if elements is None:
        return None
    ride = elements[0]
    if ride.get(u'status', u'') != u'OK':
        return None
    duration = ride.get(u'duration', None)
    if duration is None:
        return None
    return duration.get(u'value', None)