
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from .models import Airport, Order
from .serializers import AirportSerializer, OrderSerializer, RouteSerializer


User = get_user_model()

class SerializerTests(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(
      password="testpass123",
      email="test@admin.com"
    )

    self.airport_data = {
      "name": "JFK Airport",
      "closest_big_city": "New York"
    }

    self.route_data = {
      "source": Airport.objects.create(name="LAX", closest_big_city="Los Angeles"),
      "destination": Airport.objects.create(name="ORD", closest_big_city="Chicago"),
      "distance": 1500
    }

  def test_airport_serializer_valid(self):
    serializer = AirportSerializer(data=self.airport_data)
    self.assertTrue(serializer.is_valid())
    airport = serializer.save()
    self.assertEqual(airport.name, "JFK Airport")

  def test_airport_serializer_invalid(self):
    invalid_data = {"closest_big_city": "New York"}
    serializer = AirportSerializer(data=invalid_data)
    self.assertFalse(serializer.is_valid())

  def test_airport_serializer_empty(self):
    serializer = AirportSerializer(data={})
    self.assertFalse(serializer.is_valid())

  def test_route_serializer_valid(self):
    serializer = RouteSerializer(data={
      "source": self.route_data["source"].id,
      "destination": self.route_data["destination"].id,
      "distance": self.route_data["distance"]
    })
    self.assertTrue(serializer.is_valid())

  def test_route_serializer_same_airports(self):
    invalid_route = {
      "source": self.route_data["source"].id,
      "destination": self.route_data["source"].id,
      "distance": 0
    }
    serializer = RouteSerializer(data=invalid_route)
    self.assertTrue(serializer.is_valid())

  def test_order_serializer_create(self):
    order_data = {"user": self.user.id}
    serializer = OrderSerializer(data=order_data)
    self.assertTrue(serializer.is_valid())
    order = serializer.save()
    self.assertEqual(order.user, self.user)

  def test_order_serializer_update(self):
    order = Order.objects.create(user=self.user)
    new_user = User.objects.create_user(email="admin@test.com", password="pass123")

    serializer = OrderSerializer(order, data={"user": new_user.id}, partial=True)
    self.assertTrue(serializer.is_valid())
    updated_order = serializer.save()
    self.assertEqual(updated_order.user, new_user)

  def test_order_serializer_no_user(self):
    order_data = {}
    serializer = OrderSerializer(data=order_data)
    with self.assertRaises(ValidationError):
      serializer.is_valid(raise_exception=True)

  def test_order_serializer_read_only_fields(self):
    order = Order.objects.create(user=self.user)
    serializer = OrderSerializer(order)
    self.assertIn("created_at", serializer.data)
    self.assertIn("id", serializer.data)
