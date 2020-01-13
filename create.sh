#!/bin/bash

# To create a new role using this skeleton fill variables and run this script. Remove this file after role creation.

# This variable ideally should contain the name of an application which will be deployed with ansible role.
# Do not use whitespaces.
APPLICATION="alertmanager-irc-relay"

# Port on which your application is listening
PORT="8000"

# Your name. Preferably your full name.
AUTHOR="Goutham Veeramachaneni"

rm -rf .git
rm README.md
mv ROLE_README.md README.md
mv "templates/application.service.j2" "templates/${APPLICATION}.service.j2"

find ./ -type f -exec sed -i "s/Goutham Veeramachaneni/$AUTHOR/g" {} \;
find ./ -type f -exec sed -i "s/alertmanager-irc-relay/$APPLICATION/g" {} \;
find ./ -type f -exec sed -i "s/8000/$PORT/g" {} \;
