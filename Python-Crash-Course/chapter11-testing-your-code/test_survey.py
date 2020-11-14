import unittest
from survey import AnnoymousSurvey


class TestAnnoymousSurvey(unittest.TestCase):
    """Tests for the class AnnoymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnnoymousSurvey(question)
        self.respones = ['english', 'spanish', 'mandarin']

    def test_store_single_response(self):
        """test that a single response is stored properly."""
        self.my_survey.store_response(self.respones[0])
        self.assertIn(self.respones[0], self.my_survey.responses)


    def test_store_three_response(self):
        """test that three individual responses are stored properly."""
        for response in self.respones:
            self.my_survey.store_response(response)

        for response in self.respones:
            self.assertIn(response, self.my_survey.responses)

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
