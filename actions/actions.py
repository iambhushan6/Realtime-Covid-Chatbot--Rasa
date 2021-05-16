# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import EventType, SlotSet
from . import api

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


class ValidateUserForm(Action):

    def name(self) -> Text:
        return "user_details_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:
        required_slots = ["name", "pincode","service"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # this slot will be filled by user after request
                return [SlotSet("requested_slot", slot_name)]
        # after slots are filled
        return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        pin = tracker.get_slot("pincode")
        city = tracker.get_slot("name")
        service = tracker.get_slot("service")
        info = api.pininfo(pin)
        service_info = api.service_detail(city, service)
        dispatcher.utter_message(response="utter_return_name_pincode", name=tracker.get_slot("name"), pincode=tracker.get_slot("pincode"), pininfo=info, serviceinfo=service_info)

        # return []