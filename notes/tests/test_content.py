from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from notes.forms import NoteForm
from notes.models import Note

User = get_user_model()


class TestDetailPage(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор')
        cls.note = Note.objects.create(text='Текст', author=cls.author)
        cls.add_url = reverse('notes:add')
        cls.edit_url = reverse('notes:edit', args=(cls.note.slug,))

    def test_authorized_client_has_form(self):
        self.client.force_login(self.author)
        for page in (self.add_url, self.edit_url):
            response = self.client.get(page)
            self.assertIn('form', response.context)
            self.assertIsInstance(response.context['form'], NoteForm)
