from unittest import TestCase
from leetcode.assessment.unique_email import UniqueEmail


class TestUniqueEmail(TestCase):
    def setUp(self):
        self.uniqueEmail = UniqueEmail()

    def test_handle_dot(self):
        actual = self.uniqueEmail.handleDot("alice.z@leetcode.com")
        self.assertEqual(actual, "alicez@leetcode.com")

    def test_handle_first_plus(self):
        actual = self.uniqueEmail.handleFirstPlus("m.y+name@email.com")
        self.assertEqual(actual, "m.y@email.com")

    def test_actual_email(self):
        actual = self.uniqueEmail.actualEmail("m.y+name@email.com")
        self.assertEqual(actual, "my@email.com")

    def test_num_unique_emails(self):
        input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        actual = self.uniqueEmail.numUniqueEmails(input)
        self.assertEqual(actual, 2)

    def test_num_unique_emails2(self):
        input = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
        actual = self.uniqueEmail.numUniqueEmails(input)
        self.assertEqual(actual, 3)
