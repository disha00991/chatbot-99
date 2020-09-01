# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


timezones = {
 "delhi": "GMT+5:30",
 "london": "GMT:00:00"
}

class ActionFindTZ(Action):

    def name(self) -> Text:
        return "action_find_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('city').lower()
        tz = timezones.get(city)
        output = "Time zone for {} is: {}".format(city, tz) if tz else "{} City not found".format(city)
        dispatcher.utter_message(text=output)

        return []
