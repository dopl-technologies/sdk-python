## Setup
```shell
$ GITHUB_TOKEN=<github_token> bash download_libsdk

# Python 3.7.1
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Testing
```shell
$ pytest
```

## Updating libsdk asset
```shell
$ curl -s -u dopl-builder:<githubtoken> https://api.github.com/repos/dopl-technologies/libsdk/releases/tags/v1.0.0

# Update download_libsdk
```