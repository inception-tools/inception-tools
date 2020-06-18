###############################################################################
#
# Makefile
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
#
###############################################################################

########################################
# Build variables

PROJECT_NAME=pyincept
PACKAGE_NAME=pyincept

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
	archive \
	archive-clean \
	check \
	clean \
	deploy-package \
	deploy-package-clean \
	dist \
	dist-clean \
	init \
	init-dev \
	init-clean \
	install \
	maintainer-clean \
	uninstall

all: check install

archive:
	git archive --format zip --output $(ARCHIVE_ZIP) master

archive-clean:
	rm -f $(ARCHIVE_ZIP)

check:
	python setup.py pytest

clean:
	rm -f *.log

check-clean:
	rm -rf $(PYTEST_CACHE_DIR)

deploy-package: archive dist
	rm -rf $(DIST_PACKAGE_DIR) \
	&& mkdir $(DIST_PACKAGE_DIR) \
	&& cp ecg_monitor.cfg $(DIST_PACKAGE_DIR) \
	&& cp log.cfg $(DIST_PACKAGE_DIR) \
	&& cp $(DIST_DIR)/* $(DIST_PACKAGE_DIR) \
	&& cp $(ARCHIVE_ZIP) $(DIST_PACKAGE_DIR) \
	&& zip -r $(DIST_PACKAGE_DIR).zip $(DIST_PACKAGE_DIR)

deploy-package-clean:
	rm -rf $(DIST_PACKAGE_DIR) $(DIST_PACKAGE_DIR).zip

dist:
	python setup.py $(EGG_INFO) $(DIST_TARGETS)

dist-clean:
	rm -rf $(EGG_INFO_DIR) $(DIST_DIR) $(BUILD_DIR)

init:
	pipenv install

init-dev:
	pipenv install --dev

init-clean:
	pip freeze | xargs pip uninstall -y

install:
	python setup.py $(EGG_INFO) install

maintainer-clean: archive-clean clean check-clean deploy-package-clean dist-clean
	rm -rf $(EGG_DIR)

uninstall:
	pip uninstall -y $(PROJECT_NAME)
