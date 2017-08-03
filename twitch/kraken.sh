#!/bin/sh

curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: sg06i4hedwd5uqfw0gb57gu0sn09l7' \
-X GET https://api.twitch.tv/kraken/users?login=$1
