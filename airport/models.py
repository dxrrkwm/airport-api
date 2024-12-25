from django.db import models

from core import settings


class Airport(models.Model):
    name = models.CharField(max_length=64)
    closest_big_city = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="source")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination")
    distance = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.source} to {self.destination}"


class AirplaneType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Airplane(models.Model):
    name = models.CharField(max_length=64)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Crew(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="route")
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="airplane")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.route} on {self.departure_time}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} for {self.user}"


class Ticket(models.Model):
    row = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    @staticmethod
    def validate_ticket(row, seat, flight, error):
        if row < 1:
            error["row"] = "Row number must be positive"
        if seat < 1:
            error["seat"] = "Seat number must be positive"
        if row > flight.airplane.rows:
            error["row"] = "Row number is too big"
        if seat > flight.airplane.seats_in_row:
            error["seat"] = "Seat number is too big"

    def __str__(self):
        return f"Ticket {self.id} for {self.flight} in row {self.row}, seat {self.seat}"
