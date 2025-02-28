from rest_framework import permissions, viewsets

from airport.models import Airplane, AirplaneType, Airport, Crew, Flight, Order, Route
from airport.serializers import (
    AirplaneSerializer,
    AirplaneTypeSerializer,
    AirportSerializer,
    CrewSerializer,
    FlightSerializer,
    OrderSerializer,
    RouteSerializer,
)


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [permissions.IsAuthenticated]


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.select_related("departure_airport", "arrival_airport")
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.select_related("airplane_type")
    serializer_class = AirplaneSerializer
    permission_classes = [permissions.IsAuthenticated]


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticated]


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.select_related(
        "route",
        "airplane",
        "crew",
    )
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related(
        "flight",
        "passenger",
    )
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
