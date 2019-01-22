import json
import sys
from base64 import b64encode

OUTPUT_FILE = 'docker-config.json'
JSON_TEMPLATE = 'docker-config.json.template'


def load_config(template):
    with open(template, 'r') as f:
        return json.load(f)


def save_config(config, filename):
    with open(filename, 'w') as f:
        json.dump(config, f)


if __name__ == '__main__':
    username = raw_input('DockerHub Username:')
    password = raw_input('DockerHub Password:')

    config = load_config(JSON_TEMPLATE)

    base64_auth = b64encode(username + ':' + password)
    config["auths"]["https://index.docker.io/v1/"]["auth"] = base64_auth

    save_config(config, OUTPUT_FILE)
