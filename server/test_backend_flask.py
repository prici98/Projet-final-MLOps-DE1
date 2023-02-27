import json
import unittest
from server import app

class FlaskTest(unittest.TestCase):

    # S'assurer que le backend renvoie une réponse HTTP 200 OK pour une requête valide
    def test_prediction_api(self):
        with app.test_client() as client:
            data = {
                "title": "Attack on Titan",
                "genre": "Action,Drama,Fantasy",
                "description": "Several hundred years ago, humans were nearly exterminated by Titans. Titans are typically several stories tall, seem to have no intelligence, devour human beings and, worst of all, seem to do it for the pleasure rather than as a food source. A small percentage of humanity survived by walling themselves in a city protected by extremely high walls, even taller than the biggest Titans. Flash forward to the present and the city has not seen a Titan in over 100 years. Teenage boy Eren and his foster sister Mikasa witness something horrific as the city walls are destroyed by a Colossal Titan that appears out of thin air. As the smaller Titans flood the city, the two kids watch in horror as their mother is eaten alive. Eren vows that he will murder every single Titan and take revenge for all of mankind.",
                "type": "TV,Finished Airing",
                "producer": "Production I.G,Mainichi Broadcasting System,Pony Canyon,Shingeki no Kyojin Team,Production Committee",
                "studio": "Wit Studio"
            }
            response = client.post('/', json=data)
            self.assertEqual(response.status_code, 200)

    # S'assurer que le backend renvoie la prédiction correcte pour une entrée donnée
    def test_prediction_output(self):
        with app.test_client() as client:
            data = {
                "title": "Attack on Titan",
                "genre": "Action,Drama,Fantasy",
                "description": "Several hundred years ago, humans were nearly exterminated by Titans. Titans are typically several stories tall, seem to have no intelligence, devour human beings and, worst of all, seem to do it for the pleasure rather than as a food source. A small percentage of humanity survived by walling themselves in a city protected by extremely high walls, even taller than the biggest Titans. Flash forward to the present and the city has not seen a Titan in over 100 years. Teenage boy Eren and his foster sister Mikasa witness something horrific as the city walls are destroyed by a Colossal Titan that appears out of thin air. As the smaller Titans flood the city, the two kids watch in horror as their mother is eaten alive. Eren vows that he will murder every single Titan and take revenge for all of mankind.",
                "type": "TV,Finished Airing",
                "producer": "Production I.G,Mainichi Broadcasting System,Pony Canyon,Shingeki no Kyojin Team,Production Committee",
                "studio": "Wit Studio"
            }
            response = client.post('/', json=data)
            prediction = json.loads(response.data)["prediction"]
            # Convertir la prédiction en un nombre à virgule flottante
            prediction_float = float(prediction)

            # Vérifier si la prédiction est dans la plage requise
            self.assertGreaterEqual(prediction_float, 0)
            self.assertLessEqual(prediction_float, 10)


if __name__ == '__main__':
    unittest.main()
