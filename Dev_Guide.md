# Developer Guide

This guide is intended to help developers update, test, and package the classes in the hsvai module.

## Environment Setup

```
?>pip install -r requirements
```

## Testing

```
?>python -m unittest tests/test_doc2vec.py
```

## Packaging

```
?>python setup.py sdist bdist_wheel
```

## Installation

```
?>python setup.py install
```

## Github Release

Tag the master branch with a release tag and attach the dist/hsvai-#.#.#.tar.gz to the release in Github.