"""Console script for sentry_onboarding."""
import sys
import click
from flask import Flask

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
