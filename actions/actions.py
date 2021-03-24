# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import requests
import json

from typing import Any, Text, Dict, List, Union, Optional

from rasa.shared.core.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.types import DomainDict

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
"""
re.sub(pattern, repl, string, count=0, flags=0)
"""


class ValidateRecuperationDuForm(FormValidationAction):
    """ Exemple of validation action."""

    def name(self) -> Text:
        return "validate_recuperation_du_form"

    @staticmethod
    def required_slot() -> List[Text]:
        """Mes données obligatoires"""
        return ["nom_personne"]

    def validate_nom_personne(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate nom_prenom value."""

        username = ""
        prediction = tracker.latest_message
        entities = prediction['entities']

        print(str(tracker.get_latest_entity_values('username')))

        if entities is not None and len(entities) > 0:
            if (tracker.get_latest_entity_values('username') is not None):
                print(entities[0])
                print("-----11111111---- " + entities[0]["value"])
                username = entities[0]["value"]  # "Kabore"
        elif username == "":
            # get one entity value
            username = tracker.get_latest_entity_values('username')
            print(username)

        myintent = prediction["intent"].get("name")
        if(myintent == "salutations"):
            return {"nom_personne": None}

        slot_value_nom_personne = tracker.get_slot("nom_personne")
        print("user_name  : ", slot_value_nom_personne)

        # prediction['entities'][0]['entity']
        # return [SlotSet("entity", entity_type)]
        if username is not None and username != "":
            return {"nom_personne": username}

        elif slot_value is not None:
            # Le nom_prenom est valid, tu peux donc faire la suite de tes action
            print("La valeur de mon slot. ----   " + str(slot_value))
            dispatcher.utter_message("Bonjour .....1111.")
            return {"nom_personne": slot_value}

        else:
            # La validation à echouer
            # Comme tu as mis un loop l'utilisateur sera demander de nouveau
            dispatcher.utter_message("Bonjour ......")
            return {"nom_personne": None}
