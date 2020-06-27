###############################################################################
#
# Makefile
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Unpublished Copyright 2020 some_author. All Rights Reserved.
#
###############################################################################

########################################
# Build variables

PROJECT_NAME=some_package_name
PACKAGE_NAME=some_package_name

INDEX_SERVER=testpypi

# See https://www.python.org/dev/peps/pep-0440/ for more information on pre-
# and post-release tag formats.
TAG_BUILD=dev

EGG_INFO=egg_info --tag-build=$(TAG_BUILD)
EGG_DIR=.eggs
EGG_INFO_DIR=$(PACKAGE_NAME).egg-info

DIST_DIR=dist
DIST_TARGETS=sdist bdist_wheel

BUILD_DIR=build

PYTEST_CACHE_DIR=.pytest_cache

DIST_PACKAGE_DIR=$(PACKAGE_NAME)_install_package
ARCHIVE_ZIP=$(PACKAGE_NAME)_project_source.zip

########################################
# Make targets

.PHONY: \
	all \
	check \
	clean \
	dist \
	dist-clean \
	dist-upload \
	init \
	init-dev \
	init-clean \
	install \
	maintainer-clean \
	uninstall

all: check install

check:
	python setup.py pytest

check-clean:
	rm -rf $(PYTEST_CACHE_DIR)

clean:
	rm -f *.log

dist:
	python setup.py $(EGG_INFO) $(DIST_TARGETS)

dist-clean:
	rm -rf $(EGG_INFO_DIR) $(DIST_DIR) $(BUILD_DIR)

dist-upload: dist
	twine upload --repository $(INDEX_SERVER) dist/*

init:
	pipenv install

init-dev:
	pipenv install --dev

init-clean:
	pip freeze | xargs pip uninstall -y

install:
	pipenv uninstall --dev

maintainer-clean: archive-clean clean check-clean deploy-package-clean dist-clean
	rm -rf $(EGG_DIR)

uninstall:
	pip uninstall -y $(PROJECT_NAME)
