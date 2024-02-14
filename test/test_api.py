import unittest
import json
from app.api import app, comments

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        comments.clear()

    def test_api_comment_new(self):
        # Dados de exemplo para o novo comentário
        data = {
            'email': 'example@example.com',
            'comment': 'This is a test comment',
            'content_id': '123'
        }

        # Fazendo uma solicitação POST para /api/comment/new
        response = self.app.post('/api/comment/new', json=data)
        self.assertEqual(response.status_code, 200)

        # Verificando se o comentário foi adicionado
        self.assertTrue('123' in comments)
        self.assertEqual(len(comments['123']), 1)
        self.assertEqual(comments['123'][0]['email'], 'example@example.com')
        self.assertEqual(comments['123'][0]['comment'], 'This is a test comment')

    def test_api_comment_list(self):
        # Adicionando um comentário para teste
        comments['123'] = [{'email': 'test@example.com', 'comment': 'Test comment'}]

        # Fazendo uma solicitação GET para /api/comment/list/<content_id>
        response = self.app.get('/api/comment/list/123')
        self.assertEqual(response.status_code, 200)

        # Verificando se o comentário é retornado corretamente
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['email'], 'test@example.com')
        self.assertEqual(data[0]['comment'], 'Test comment')

    def test_api_comment_list_not_found(self):
        # Fazendo uma solicitação GET para /api/comment/list/<content_id> para um content_id não existente
        response = self.app.get('/api/comment/list/456')
        self.assertEqual(response.status_code, 404)

        # Verificando se a resposta contém a mensagem adequada
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], 'NOT-FOUND')
        self.assertEqual(data['message'], 'content_id 456 not found')

if __name__ == '__main__':
    unittest.main()
