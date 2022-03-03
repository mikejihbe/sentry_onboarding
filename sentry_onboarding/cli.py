"""Console script for sentry_onboarding."""
import sentry_sdk
import sys
import click
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://a8bfbc1e05ed497492c6eb25349209ec@o1158395.ingest.sentry.io/6241517",
    integrations=[FlaskIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

"""The main flask application"""
app = Flask(__name__)

@app.route("/")
def root():
    return "<p>Try /bad to trigger a bug!!</p>"

@app.route("/bad")
def bad():
    100 / 0 # Oopsies
    return ""


@click.command()
def main(args=None):
    """Console script for sentry_onboarding."""
    app.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
