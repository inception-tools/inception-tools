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
EGG_INFO_OPTIONS=--tag-build=dev$$(date -u "+%Y%m%d%H%M%S")
EGG_INFO=egg_info $(EGG_INFO_OPTIONS)
EGG_DIR=.eggs
EGG_INFO_DIR=$(PACKAGE_NAME).egg-info

BUILD_DIR=build

DIST_DIR=dist
DIST_TARGETS=sdist bdist_wheel
DIST_UPLOAD_OPTIONS=-r testpypi

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
	dist-upload \
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

check-clean:
	rm -rf $(PYTEST_CACHE_DIR)

clean:
	rm -f *.log

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

dist-upload: dist
	twine upload $(DIST_UPLOAD_OPTIONS) $(DIST_DIR)/*

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
