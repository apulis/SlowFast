#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

"""Logging."""

import builtins
import decimal
import logging
import sys, os
import simplejson
import time
import slowfast.utils.distributed as du


def _suppress_print():
    """
    Suppresses printing from the current process.
    """

    def print_pass(*objects, sep=" ", end="\n", file=sys.stdout, flush=False):
        pass

    builtins.print = print_pass

def _get_time_str():
    return time.strftime('%Y%m%d_%H%M%S', time.localtime())

def _add_file_handler(filename=None,
                      mode='w',
                      level=logging.INFO):
    logger = get_logger(__name__)
    file_handler = logging.FileHandler(filename, mode)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    file_handler.setLevel(level)
    logger.addHandler(file_handler)
    return logger
    
def setup_logging(workdir='.'):
    """
    Sets up the logging for multiple processes. Only enable the logging for the
    master process, and suppress logging for the non-master processes.
    """
    # Set up logging format.
    _FORMAT = "[%(levelname)s: %(filename)s: %(lineno)4d]: %(message)s"

    if du.is_master_proc():
        # Enable logging for the master process.
        logging.root.handlers = []
        logging.basicConfig(
            level=logging.INFO, format=_FORMAT, stream=sys.stdout
        )

        log_dir = ''
        filename = '{}.log'.format(_get_time_str())
        log_file = os.path.join(log_dir, filename)
        _add_file_handler(log_file, level=logging.INFO)
    else:
        # Suppress logging for non-master processes.
        _suppress_print()


def get_logger(name):
    """
    Retrieve the logger with the specified name or, if name is None, return a
    logger which is the root logger of the hierarchy.
    Args:
        name (string): name of the logger.
    """
    return logging.getLogger(name)


def log_json_stats(stats):
    """
    Logs json stats.
    Args:
        stats (dict): a dictionary of statistical information to log.
    """
    stats = {
        k: decimal.Decimal("{:.6f}".format(v)) if isinstance(v, float) else v
        for k, v in stats.items()
    }
    json_stats = simplejson.dumps(stats, sort_keys=True, use_decimal=True)
    logger = get_logger(__name__)
    logger.info("json_stats: {:s}".format(json_stats))
    ## TODO: write log to disk
