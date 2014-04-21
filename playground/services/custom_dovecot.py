# Run dovecot

import os

this_dir = os.path.dirname(os.path.abspath(__file__))
playground_dir = os.path.dirname(this_dir)

def main():
    with open('../services/dovecot.conf.template', encoding='utf-8') as f:
        conf = f.read()
    conf = conf.replace('USER', 'brandon')  # TODO: compute username
    conf = conf.replace('PLAYGROUND', playground_dir)
    conf_path = os.path.join(playground_dir, 'var/dovecot.conf')
    with open(conf_path, 'w', encoding='utf-8') as f:
        f.write(conf)
    os.execlp('dovecot', 'dovecot', '-F', '-c', conf_path)

if __name__ == '__main__':
    main()
