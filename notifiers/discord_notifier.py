"""
Runtime Notifier
"""

import requests

DISCORD_ALERT_MENTION = "<@1280351163304251412>"

class Notifier:

    def __init__(self, webhook, mention):

        self.webhook = webhook
        self.mention = mention

    def notify(self, event):

        try:

            if event.field == "running":

                if event.new:

                    content = (
                        "🖥️ **Runtime Monitor**\n\n"
                        f"🟢 **{event.component}** started"
                    )

                else:

                    content = (
                        f"{self.mention}\n\n"
                        "🖥️ **Runtime Monitor**\n\n"
                        f"🔴 **{event.component}** stopped"
                    )

            else:

                content = (
                    "🖥️ **Runtime Monitor**\n\n"
                    f"{event.component}: {event.field} {event.old} → {event.new}"
                )

            requests.post(
                self.webhook,
                json={
                    "content": content
                },
                timeout=10
            )

        except requests.RequestException:
            pass