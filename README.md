# Ansible Role: alertmanager-irc-relay

[![Build Status](https://travis-ci.com/cloudalchemy/ansible-alertmanager-irc-relay.svg?branch=master)](https://travis-ci.com/cloudalchemy/ansible-alertmanager-irc-relay)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.alertmanager_irc_relay-blue.svg)](https://galaxy.ansible.com/cloudalchemy/alertmanager_irc_relay/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-alertmanager-irc-relay.svg)](https://github.com/cloudalchemy/ansible-alertmanager-irc-relay/tags)

## Description

Deploy [alertmanager-irc-relay](https://github.com/gouthamve/alertmanager-irc-relay) using ansible.

## Requirements

- Ansible >= 2.7 (It might work on previous versions, but we cannot guarantee it)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `alertmanager_irc_relay_version` | "0.1.0" | The version to download (from https://github.com/gouthamve/alertmanager-irc-relay/releases) |
| `alertmanager_irc_relay_system_group` | "ircrelay" | System group used to run alertmanager-irc-relay |
| `alertmanager_irc_relay_system_user` | "ircrelay" | System user used to run alertmanager-irc-relay |
| `alertmanager_irc_relay_http_host` | "0.0.0.0" | The ip/interface to listen on. |
| `alertmanager_irc_relay_http_port` | 8000 | The port to listen on. Note that the post and host combination has to be specified while configuring Alertmanager. |
| `alertmanager_irc_relay_irc_host` | "chat.freenode.net" | The IRC host to connect to. |
| `alertmanager_irc_relay_irc_port` | 6697 | The IRC port to connect to. |
| `alertmanager_irc_relay_irc_nickname` | "" | The IRC nickname to connect with. |
| `alertmanager_irc_relay_irc_nickname_password` | "" | The password if the nick requires a password. |
| `alertmanager_irc_relay_irc_realname` | "" | The realname to connect with. |
| `alertmanager_irc_relay_notice_once_per_alert_group` | "yes" | Send only one notice when webhook data is received. |
| `alertmanager_irc_relay_notice_template` | "Alert {{ .Labels.alertname }} on {{ .Labels.instance }} is {{ .Status }}" | The formatting is based on golang's text/template. |
| `alertmanager_irc_relay_channels` | "[]" | A list of channels to join at startup.  |

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - cloudalchemy.alertmanager_irc_relay
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on [DigitalOcean](https://digitalocean.com).

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip3 install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py35-ansible28 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## Troubleshooting

See [troubleshooting](TROUBLESHOOTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
