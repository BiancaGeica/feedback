import unittest
from unittest.mock import patch
import main
import templates

class TestFeedbackGenerator(unittest.TestCase):

    def test_schema_length_is_25(self):
        """a) Valideaza ca schema contine fix 25 de intrebari"""
        data = main.generate_feedback_data(101, "Curs Test", "Profesor Test", 1)
        responses = data["anonattempts"][0]["responses"]
        self.assertEqual(len(responses), 25, "Eroare: Nu sunt 25 de intrebari in JSON!")

    @patch('main.random.random')
    @patch('main.get_random_response')
    def test_text_consistency_nemultumit(self, mock_get_random, mock_random):
        """b) Forteaza nota mica si verifica textul generat pentru 'nemultumit'"""
        # Fortam will_leave_text = True
        mock_random.return_value = 1.0 
        
        def forced_responses(q_type):
            if q_type == "grade": return "3", "3"
            elif q_type == "hours": return "5", "5"
            return "Test", "Test"
            
        mock_get_random.side_effect = forced_responses
        
        curs = "Analiza"
        prof = "Ion Ionescu"
        data = main.generate_feedback_data(102, curs, prof, 1)
        responses = data["anonattempts"][0]["responses"]
        
        # cautam textul generat
        text_generat = next(r["rawval"] for r in responses if r["name"] == "What are the positive ...")
        
        texte_asteptate = [
            t.format(curs=curs, prof=prof) 
            for t in templates.FEEDBACK_TEMPLATES["nemultumit"]["text_positive"]
        ]
        
        # verif ca generatorul a extras fraza corecta
        self.assertIn(text_generat, texte_asteptate, "Textul nu se potriveste cu profilul!")

if __name__ == '_main_':
    unittest.main()