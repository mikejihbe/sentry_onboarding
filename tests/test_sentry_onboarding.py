#!/usr/bin/env python

"""Tests for `sentry_onboarding` package."""


import unittest
from click.testing import CliRunner

from sentry_onboarding import sentry_onboarding
from sentry_onboarding import cli


class TestSentry_onboarding(unittest.TestCase):
    """Tests for `sentry_onboarding` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'sentry_onboarding.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
