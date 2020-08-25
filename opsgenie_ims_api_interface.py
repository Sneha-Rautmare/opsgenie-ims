import opsgenie_sdk
from pprint import pprint


class InterfaceAPIClass:
    def __init__(self):
        self.configuration = opsgenie_sdk.Configuration()
        self.integration_api_key = "aaf5388b-d485-4b2a-8d45-fff84c9d0b08"
        # Configure API key authorization: GenieKey
        self.configuration.api_key["Authorization"] = self.integration_api_key
        # for EU instance of Opsgenie , else https://api.opsgenie.com
        self.configuration.host = "https://api.eu.opsgenie.com"

    def create_alert_exception(self):
        # create an instance of the API class
        alert_api = opsgenie_sdk.AlertApi(opsgenie_sdk.ApiClient(self.configuration))
        # CreateAlertPayload | Request payload of created alert
        create_alert_payload = opsgenie_sdk.CreateAlertPayload(
            message="test-alert-exception", description="Zero Division exception occured in the division operation"
        )
        # create alert
        api_response = alert_api.create_alert(create_alert_payload)
        pprint(api_response)


# create object
myobj = InterfaceAPIClass()

# Example code
try:
    print("Result of division:", 1 / 0)
except ZeroDivisionError:
    print("Exeption occured and alert created........")
    myobj.create_alert_exception()

