from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from trips.consumers import TaxiConsumer


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('taxi/', TaxiConsumer.as_asgi())
    ])
})