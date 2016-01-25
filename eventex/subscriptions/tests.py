from django.test import TestCase
class SubscribeTest(TestCase):
    def test_get(self):
        response=self.client.get('/inscricao/')
        self.assertEqual(200,response.status_code)

class SubscribePostTest(TestCase):

    def setUp(self):
        data = dict(
            name='Regis da Silva',
            cpf='71124336656',
            email='rafa@example.com',
            phone='21-9999-9999',
        )
        self.resp= self.client.post('/inscricao/',data)
    def test_post(self):

        self.assertEqual(302,self.resp.status_code)