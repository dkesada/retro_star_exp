import logging


def setup_logger(fname=None, silent=False):
	logger = logging.getLogger('retro_star')
	if silent:
		logger.setLevel(logging.CRITICAL)
