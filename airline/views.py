from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from sqlalchemy.orm import sessionmaker, aliased
from airline.models import *
from pprint import pprint
f = aliased(Flight)
j = aliased(Journey)
ji = aliased(JourneyInventory)
i = aliased(Item)
from_ap = aliased(Airport)
to_ap = aliased(Airport)

eng = None
con = None
session = None

url = 'postgresql+psycopg2://postgres:Welcome@1234@35.223.143.8:5432/th20_donair'
def get_connection():
    global con
    global eng
    if eng is None:
        eng = create_engine(url)
        con = eng.connect()
    return con

def get_session():
    global session
    global eng
    global con
    if eng is None:
        eng = create_engine(url)
        con = eng.connect()
        Session = sessionmaker(bind=eng)
        session = Session()
    return session


def index(request):
    # todo: Make request to AA-Mock flight data API, add additional fields as necessary
    return HttpResponse("Below are the airline info")


def get_flights(request):
    print(request.body)
    body = json.loads(request.body)
    date = body['date']
    origin = body['source']
    dest = body['dest']
    url = 'http://localhost:3030/flights'

    payload = {'date': date, 'origin': origin, 'dest': dest}
    resp = requests.get(url, params=payload)
    return JsonResponse(resp.text, safe=False)


def get_donations(request):
    date = request.POST.get('date')
    flight_number = request.POST.get('flight_number')
    session = get_session()
    conn = get_connection()
    print(conn)
    print(session)

    q = session.query(f.name.label('flight_name'), from_ap.name.label('from'), to_ap.name.label('to'), j.start_time,
                      j.remaining_space) \
        .join(j, and_(j.flight_id == f.id)) \
        .join(from_ap, and_(from_ap.id == j.src)) \
        .join(to_ap, and_(to_ap.id == j.dest)).filter(f.id==flight_number).all()

    resp = []
    for rec in q:
        tmp = {}
        tmp['flight_name'] = rec[0]
        tmp['from'] = rec[1]
        tmp['to'] = rec[2]
        tmp['start_time'] = str(rec[3])
        tmp['remaining_space'] = str(rec[4])
        resp.append(tmp)
    return JsonResponse(json.dumps(resp), safe=False)
