from django.http import HttpResponse


class StripWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__:
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
