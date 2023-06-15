from rasa.core.channels import InputChannel
from sanic import response
from sanic.request import Request
from sanic.response import HTTPResponse
from sanic import Sanic
import requests


# def create_app() -> Sanic:
#     bot_app = Sanic("rest_server", configure_logging=False)
#
#     @bot_app.post("/bot")
#     async def send_response(request: Request) -> HTTPResponse:
#         bot_response = request.json.get("text")
#         r = request.load_json()
#         print(r)
#         response_id = requests.get('https://api.telegram.org/bot6121312355:AAEe-mdQTDNFmVw4MfQeCnNkz-kGRfhCKgg/getMe')
#         print(bot_response)
#         # res = response_id.json()
#         # chat_id = res['result']['id']
#         # # close = requests.post('https://api.telegram.org/bot6121312355:AAEe-mdQTDNFmVw4MfQeCnNkz-kGRfhCKgg/close')
#         # # print(close.json())
#         # rp = requests.post('https://api.telegram.org/bot6121312355:AAEe-mdQTDNFmVw4MfQeCnNkz-kGRfhCKgg/sendMessage',
#         #                    params={'chat_id': chat_id, 'text': bot_response})
#         # print(rp.json())
#         #
#         body = {"status": "message sent"}
#         return response.json(body, status=200)
#
#     return bot_app
#
#
# if __name__ == "__main__":
#     app = create_app()
#     port = 5034
#
#     print(f"Starting callback server on port {port}.")
#     app.run("0.0.0.0", port)
