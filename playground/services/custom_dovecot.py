# Run dovecot

import os

services_dir = os.path.dirname(os.path.abspath(__file__))
playground_dir = os.path.dirname(services_dir)

def main():
    os.chdir(playground_dir)
    var_dir = os.path.join(playground_dir, 'var')
    if not os.path.isdir(var_dir):
        os.mkdir(var_dir)
    with open('./services/dovecot.conf.template', encoding='utf-8') as f:
        template = f.read()
    conf = template.replace('PLAYGROUND', playground_dir)
    conf_path = os.path.join(playground_dir, 'var/dovecot.conf')
    with open(conf_path, 'w', encoding='utf-8') as f:
        f.write(conf)
    os.execlp('dovecot', 'dovecot', '-F', '-c', conf_path)

if __name__ == '__main__':
    main()
