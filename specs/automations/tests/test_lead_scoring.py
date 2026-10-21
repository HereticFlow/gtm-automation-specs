import unittest
import sys
import os

# Permet d'importer le script depuis le dossier automations
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'automations')))
from lead_scoring import score_lead, route_lead

class TestLeadScoring(unittest.TestCase):

    def test_perfect_lead(self):
        # Un lead parfait (grande boîte, CEO, a visité les prix, en France)
        lead = {
            "company_size": 300,
            "role": "CEO",
            "intent_signal": "pricing_page_visit",
            "country": "FR"
        }
        self.assertEqual(score_lead(lead), 100)

    def test_low_quality_lead(self):
        # Un lead froid (petite boîte, rôle basique, pas de signal, hors zone)
        lead = {
            "company_size": 10,
            "role": "Intern",
            "intent_signal": "",
            "country": "US"
        }
        self.assertEqual(score_lead(lead), 0)

    def test_mid_level_lead(self):
        # Un lead moyen (taille moyenne, manager, en Belgique)
        lead = {
            "company_size": 100, # +15
            "role": "Sales Manager", # +15
            "intent_signal": "", # 0
            "country": "BE" # +15
        }
        self.assertEqual(score_lead(lead), 45)

    def test_routing_logic(self):
        # Test du routage
        self.assertEqual(route_lead({}, 85), "Senior AE (Fast Track)")
        self.assertEqual(route_lead({}, 55), "Junior AE (Standard Track)")
        self.assertEqual(route_lead({}, 20), "Nurture Sequence (Marketing)")

if __name__ == '__main__':
    unittest.main()
