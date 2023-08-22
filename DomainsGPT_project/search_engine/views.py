from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import httpx

import asyncio
from time import sleep
import json


#Helper functions
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


# Create your views here.
async def index(request):
    return render(request,"DomainsGPT/DomainsGPT.html")


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    
    return HttpResponse("Non-blocking HTTP request")

#suggestions


#Sample List of dictionaries
tennisPlayers = [
    {
        'sponsor': 'Nike',
        'net worth': 1000000,
        'name': 'Iga Swiatek',
        'nationality': 'USA'
    },
    {
        'sponsor': 'Adidas',
        'net worth': 800000,
        'name': 'Ashleigh Barty',
        'nationality': 'Germany'
    },
    {
        'sponsor': 'Wilson',
        'net worth': 1200000,
        'name': 'Aryna Sabalenka',
        'nationality': 'USA'
    },
    {
        'sponsor': 'Head',
        'net worth': 900000,
        'name': 'Naomi Osaka',
        'nationality': 'Austria'
    }
]




async def suggestions(request):
    req_sample = request.GET.get("sponsor")
    
    await asyncio.sleep(1)
    
    data_json=json.dumps(tennisPlayers)

 
    return HttpResponse(data_json)