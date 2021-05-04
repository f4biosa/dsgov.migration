# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from dsgov.migration.testing import DSGOV_MIGRATION_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that dsgov.migration is properly installed."""

    layer = DSGOV_MIGRATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dsgov.migration is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'dsgov.migration'))

    def test_browserlayer(self):
        """Test that IDsgovMigrationLayer is registered."""
        from dsgov.migration.interfaces import (
            IDsgovMigrationLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IDsgovMigrationLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DSGOV_MIGRATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['dsgov.migration'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if dsgov.migration is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'dsgov.migration'))

    def test_browserlayer_removed(self):
        """Test that IDsgovMigrationLayer is removed."""
        from dsgov.migration.interfaces import \
            IDsgovMigrationLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IDsgovMigrationLayer,
            utils.registered_layers())
