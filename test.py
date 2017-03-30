#! /usr/bin/env python

import logging
import sys
import os

import pytest

logger = logging.getLogger(__name__)

logging.basicConfig(format="%(asctime)s.%(msecs)03d %(levelname)s %(name)s %(threadName)s: %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S",
                    level=logging.INFO,
                    stream=sys.stdout)


def test_page_title(driver):
    driver.get(os.environ['APP_URL'])
    logger.info('Test page title')
    assert 'Example' in driver.title
    logger.info('Test Pass')
