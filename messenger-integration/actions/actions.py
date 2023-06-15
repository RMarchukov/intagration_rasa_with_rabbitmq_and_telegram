from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import asyncio
from rasa.core.brokers.pika import PikaEventBroker


class ActionBotResponse(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # last = json.dumps(tracker.latest_message)
        dispatcher.utter_message('Your message is in processing')

        pika_broker = PikaEventBroker('localhost',
                                      'guest',
                                      'guest',
                                      queues=['for_default'],
                                      )
        loop = asyncio.get_event_loop()
        loop.run_until_complete(pika_broker.connect())
        mes = tracker.latest_message
        pika_broker.publish(event=mes)
        pika_broker.close()

        return []

# class ActionWarnDry(Action):
#
#     def name(self) -> Text:
#         return "action_send_message"
#
#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#
#         message = next(tracker.get_latest_entity_values("message"), "someone")
#         dispatcher.utter_message(f"Your {message} is sent!")
#
#         return []
