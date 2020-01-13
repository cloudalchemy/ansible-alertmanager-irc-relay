import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:7000"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
