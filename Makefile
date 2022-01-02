###############################################################################
#
# Makefile
#
# Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.
#
###############################################################################

########################################
# Build variables

PROJECT_NAME=inception-tools
PACKAGE_NAME=inception_tools

# See https://www.python.org/dev/peps/pep-0440/ for more information on pre-
# and post-release tag formats.
EGG_INFO_OPTIONS=--tag-build=dev
EGG_INFO=egg_info $(EGG_INFO_OPTIONS)
EGG_DIR=.eggs
EGG_INFO_DIR=$(PACKAGE_NAME).egg-info

BUILD_DIR=build

BUMP_VERSION_PART=patch
BUMP_VERSION_OPTIONS=--verbose

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
	bump-version\
	check \
	check-clean \
	check-style \
	check-tests \
	clean \
	dist \
	dist-clean \
	dist-upload \
	docs \
	docs-clean \
	docs-rst \
	docs-rst-clean \
	git-branches-clean \
	init \
	init-clean \
	init-dev \
	init-dev-35 \
	init-dev-36 \
	init-dev-37 \
	init-dev-38 \
	init-dev-39 \
	install \
	lib-bump2version \
	lib-flake8 \
	lib-sphinx \
	lib-twine \
	maintainer-clean \
	pretty \
	uninstall

all: check install

bump-version: lib-bump2version
	bumpversion $(BUMP_VERSION_OPTIONS) $(BUMP_VERSION_PART)

check: check-style check-tests

check-clean:
	rm -rf $(PYTEST_CACHE_DIR)

# 88 characters is black's default line length
check-style: lib-flake8
	flake8 . --count --show-source --statistics  --max-line-length=88 \
	--extend-ignore=E203

check-tests:
	python setup.py test

clean:
	rm -f *.log

dist:
	python setup.py $(EGG_INFO) $(DIST_TARGETS)

dist-clean:
	rm -rf $(EGG_INFO_DIR) $(DIST_DIR) $(BUILD_DIR)

dist-upload: dist lib-twine
	twine upload $(DIST_UPLOAD_OPTIONS) $(DIST_DIR)/*

docs: docs-rst
	@$(MAKE) -C docs html

docs-clean: docs-rst-clean
	rm -rf ./docs/_build/*

docs-rst: lib-sphinx
	sphinx-apidoc -o ./docs/_modules ./inception_tools

docs-rst-clean:
	rm -rf ./docs/_modules/*

git-branches-clean:
	git branch | xargs git branch -D

init:
	pipenv install -d

init-clean:
	pipenv uninstall --all

init-dev:
	pipenv install --dev

init-dev-35:
	pipenv install --dev --skip-lock --python 3.5

init-dev-36:
	pipenv install --dev --skip-lock --python 3.6

init-dev-37:
	pipenv install --dev --skip-lock --python 3.7

init-dev-38:
	pipenv install --dev --skip-lock --python 3.8

init-dev-39:
	pipenv install --dev --skip-lock --python 3.9

install:
	python setup.py $(EGG_INFO) install

lib-black:
	pip install --upgrade black

lib-bump2version:
	pip install --upgrade bump2version

lib-flake8:
	pip install --upgrade flake8

lib-sphinx:
	pip install --upgrade sphinx

lib-twine:
	pip install --upgrade twine

maintainer-clean: clean check-clean dist-clean docs-clean
	rm -rf $(EGG_DIR)

pretty: lib-black
	black --exclude='.*/data/' inception_tools tests

uninstall:
	pip uninstall -y $(PROJECT_NAME)
