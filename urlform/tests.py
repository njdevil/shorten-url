from django.test import TestCase
from ****.urlform.forms import ShortLinksForm


class ShortLinksFormTest(TestCase):
    """
    Test the ShortLinksForm.
    """

    def good_form_test(self):
        """
        Test a good form.
        """

        test_data = {'long_url': 'www.google.com'}
        form = ShortLinksForm(data = test_data)
        self.assertEqual(form.is_valid(), True)

    def bad_form_test(self):
        """
        Test a bad form.
        """

        test_data = {'long_url': ''}
        form = ShortLinksForm(data = test_data)
        self.assertEqual(form.is_valid(), False)
