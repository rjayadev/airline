from django.test import Client, TestCase

from .models import Airport, Flight
# Create your tests here.
class ModelsTest(TestCase):
    def setUp(self):
        a1=Airport.objects.create(code="AAA",city="City A1")
        a2=Airport.objects.create(code="BBB",city="City A2")

        Flight.objects.create(origin=a1,destination=a2,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=200)
        Flight.objects.create(origin=a1,destination=a2,duration=0)

    def test_departures_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(),3)

    def test_arrivals_count(self):
        a=Airport.objects.get(code="BBB")
        self.assertEqual(a.arrivals.count(),2)

    def test_is_valid_flight1(self):
        a1=Airport.objects.get(code="AAA")
        a2=a=Airport.objects.get(code="BBB")
        f=Flight.objects.get(origin=a1,destination=a2,duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_is_valid_flight2(self):
        a1=Airport.objects.get(code="AAA")
        a2=a=Airport.objects.get(code="AAA")
        f=Flight.objects.get(origin=a1,destination=a1,duration=200)
        self.assertFalse(f.is_valid_flight())

    def test_is_valid_flight3(self):
        a1=Airport.objects.get(code="AAA")
        a2=a=Airport.objects.get(code="BBB")
        f=Flight.objects.get(origin=a1,destination=a2,duration=0)
        self.assertFalse(f.is_valid_flight())

    def test_index(self):

        c=Client()
        response=c.get("/flight")
        #self.assertEqual(response.status_code,200)
        #self.assertEqual(response.context["flights"].count(),2)

    def test_flight_page(self):
        a1=Airport.objects.get(code="AAA")
        f1=Flight.objects.get(origin=a1,destination=a1)
        c=Client()
        response=c.get(f"/flight/{f1.id}")
        self.assertEqual(response.status_code,200)
        #self.assertEqual(response.context["flights"].code,"AAA")
