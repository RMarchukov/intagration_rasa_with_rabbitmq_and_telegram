import asyncio
import aiohttp
import requests


def main():
    # url = "http://localhost:5005/webhooks/callback/webhook"
    url = 'http://localhost:5005/webhooks/rest/webhook'
    payload = {"sender": "Smoove", "message": "are you bot?"}
    resp = requests.post(url, json=payload)
    res = resp.json()
    result = res[0]['text']
    all = f'my message - {payload["message"]}\nrasa message - {result}'
    return all


print(main())

# async def main():
#     text = input("Some message: ")
#     url = 'https://8509-178-158-195-53.ngrok-free.app/webhooks/telegram/webhook'
#     payload = {'message': {'text': text, 'chat': {'id': '911780768'}}}
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=payload) as resp:
#             print(await resp.text())


# loop = asyncio.new_event_loop()
# loop.run_until_complete(main())
# loop.run_until_complete(asyncio.sleep(1))
# loop.close()


# async def fetch(session: aiohttp.ClientSession) -> None:
#     payload1 = {
#         "text": "New message for you",
#         "sender": "user",
#         "parse_data": {
#             "entities": [
#                 {
#                     "start": 0,
#                     "end": 0,
#                     "value": "",
#                     "entity": "",
#                     "confidence": 0
#                 }
#             ],
#             "intent": {
#                 "confidence": 0.8323,
#                 "name": "send_message"
#             },
#             "intent_ranking": [
#                 {
#                     "confidence": 0.8323,
#                     "name": "send_message"
#                 }
#             ],
#             "text": "New message for you"
#         }
#     }
#
#     payload2 = {
#         "scores": [
#             {
#                 "action": "utter_API",
#                 "score": 1
#             }
#         ],
#         "policy": "policy_2_TEDPolicy",
#         "tracker": {
#             "conversation_id": "911780768",
#             "slots": [
#                 {
#                     "slot_name": ""
#                 }
#             ],
#             "latest_message": {
#                 "entities": [
#                     {
#                         "start": 0,
#                         "end": 0,
#                         "value": "",
#                         "entity": "",
#                         "confidence": 0
#                     }
#                 ],
#                 "intent": {
#                     "confidence": 0.8323,
#                     "name": "send_message"
#                 },
#                 "intent_ranking": [
#                     {
#                         "confidence": 0.8323,
#                         "name": "send_message"
#                     }
#                 ],
#                 "text": "New message for you"
#             },
#             "latest_event_time": 1537645578.314389,
#             "followup_action": "",
#             "paused": False,
#             "events": [
#                 {
#                     "event": "bot",
#                     "timestamp": None,
#                     "metadata": {},
#                     "text": "New message for you",
#                     "input_channel": "telegram",
#                     "message_id": "",
#                     "parse_data": {
#                         "entities": [
#                             {
#                                 "start": 0,
#                                 "end": 0,
#                                 "value": "",
#                                 "entity": "",
#                                 "confidence": 0
#                             }
#                         ],
#                         "intent": {
#                             "confidence": 0.8323,
#                             "name": "send_message"
#                         },
#                         "intent_ranking": [
#                             {
#                                 "confidence": 0.8323,
#                                 "name": "send_message"
#                             }
#                         ],
#                         "text": "New message for you"
#                     }
#                 }
#             ],
#             "latest_input_channel": "telegram",
#             "latest_action_name": "action_listen",
#             "latest_action": {
#                 "action_name": "utter_API",
#                 "action_text": "Some text {text}"
#             },
#             "active_loop": {
#                 "name": ""
#             }
#         }
#     }
#
#     async with session.get("https://8509-178-158-195-53.ngrok-free.app/conversations/911780768/tracker") as resp:
#         print(resp.status)
#         body = await resp.text()
#         print(body)
#
#     async with session.post("https://8509-178-158-195-53.ngrok-free.app/conversations/911780768/messages",
#                             json=payload1) as resp:
#         print(resp.status)
#         body = await resp.text()
#         print(body)
#
#     async with session.post("https://8509-178-158-195-53.ngrok-free.app/conversations/911780768/predict",
#                             json=payload2) as resp:
#         print(resp.status)
#         body = await resp.text()
#         print(body)
#
#
# async def go() -> None:
#     async with aiohttp.ClientSession() as session:
#         await fetch(session)
#
#
# loop = asyncio.new_event_loop()
# loop.run_until_complete(go())
# loop.run_until_complete(asyncio.sleep(0))
# loop.close()


# async def trigger_intent():
#     url = "http://localhost:5005/conversations/911780768/trigger_intent?output_channel=telegram"
#     payload = {"name": "EXTERNAL_dry_plant", "entities": {"plant": "romashka"}}
#
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=payload) as response:
#             result = await response.json()
#             print(result)
#
#
# async def main():
#     await trigger_intent()
#
#
# asyncio.run(main())
