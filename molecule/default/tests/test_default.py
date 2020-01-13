import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/etc/alertmanager-irc-relay"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_files(host):
    files = [
        "/etc/systemd/system/alertmanager-irc-relay.service",
        "/usr/local/bin/alertmanager-irc-relay"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_user(host):
    assert host.group("ircrelay").exists
    assert "ircrelay" in host.user("ircrelay").groups
    assert host.user("ircrelay").shell == "/usr/sbin/nologin"
    assert host.user("ircrelay").home == "/"


def test_service(host):
    s = host.service("alertmanager-irc-relay")
#    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:8080"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
