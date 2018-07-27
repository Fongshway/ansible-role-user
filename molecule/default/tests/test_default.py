import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    username = host.user("user").name
    home_dir = host.user("user").home
    ssh_key = host.file(home_dir + "/.ssh/id_rsa")

    assert username == "user"
    assert home_dir == "/home/user"
    assert ssh_key.exists
