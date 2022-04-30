import os
import json
import requests

def api_online(url):
    try:
        requests.get(url)
        return True
    except:
        return False

def initialise_modules():
    modules = os.listdir('./modules/')
    for module in modules:
        module_files = os.listdir(f'./modules/{module}')
        if 'config.json' in module_files:
            with open(f'./modules/{module}/config.json', 'r') as f:
                module_config = json.loads(f.read())
                if not api_online(module_config['base_url']):
                    # TODO: check if service is already up before running command below
                    os.system(f"cd ./modules/{module}/ && gnome-terminal --geometry=116x24+800+0 -e \'{module_config['scripts']['start']}\'")

def initialise_client():
    os.system('python client/client.py')

if __name__ == '__main__':
    initialise_modules()
    # TODO: check that all module apis are online before initialising client
    initialise_client()
