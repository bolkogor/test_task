from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Car

# Create your tests here.


class TransportTestCase(TestCase):

    def setUp(self):
        model = get_user_model().objects.create_superuser(username='admin', password='admin')
        self.client = Client()
        self.transport_data = {
            'make': 'tesla',
            'model': 's3',
            'year': 2000,
            'service_interval': 100,
            'next_service': '2024-08-14',
        }

    def transport_crud_test(self, path, data):
        # empty
        resp = self.client.get(path)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 0)

        # create
        resp = self.client.post(path, data=data)
        self.assertEqual(resp.status_code, 201)
        resp = self.client.get(f'{path}{resp.data["id"]}/')
        del resp.data.serializer
        data['id'] = resp.data['id']
        self.assertDictEqual(dict(resp.data), data)

        # update
        data['model'] = 'new model'
        resp = self.client.put(f'{path}{resp.data["id"]}/', data=data, content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['model'], 'new model')

        # delete
        resp = self.client.delete(f'{path}{resp.data["id"]}/')
        self.assertEqual(resp.status_code, 204)
        resp = self.client.get(path)
        self.assertEqual(len(resp.data), 0)

    def test_cars(self):
        car_data = {
            **self.transport_data,
            'seats': 5,
            'current_mileage': '25600.80',
            'VIN': 'W87FEKGR-G34',
            'color': 'red'
        }
        self.transport_crud_test('/cars/', car_data)

    def test_trucks(self):
        truck_data = {
            **self.transport_data,
            'seats': 2,
            'current_mileage': '25600.80',
            'VIN': 'WRWF546KJ',
            'color': 'orange',
            'bed_length': '11.50'
        }
        self.transport_crud_test('/trucks/', truck_data)

    def test_boats(self):
        boat_data = {
            **self.transport_data,
            'length': '11.04',
            'width': '3.10',
            'NIH': 'WRWF546KJ',
            'current_hours': '18.87'
        }
        self.transport_crud_test('/boats/', boat_data)



