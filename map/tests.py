from django.test import TestCase, Client

# Create your tests here.
class MapCase(TestCase):
    def test_map_display(self):
        c = Client()
        response = c.get("/map/")
        self.assertEqual(response.status_code, 200, "unexpected return code")

    def test_get_position(self):
        c = Client()
        response = c.post("/map/positions")
        self.assertEqual(response.status_code, 200, "unexpected return code")