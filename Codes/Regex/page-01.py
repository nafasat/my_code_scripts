#!/usr/bin/python3

content = """# Kibana is served by a back end server. This setting specifies the port to use.
#server.port: 5601

# Specifies the address to which the Kibana server will bind. IP addresses and host names are both valid values.
# The default is 'localhost', which usually means remote machines will not be able to connect.
# To allow connections from remote users, set this parameter to a non-loopback address.
server.host: "localhost"

# Specifies whether Kibana should rewrite requests that are prefixed with
# `server.basePath` or require that they are rewritten by your reverse proxy.
# This setting was effectively always `false` before Kibana 6.3 and will
# default to `true` starting in Kibana 7.0.
#server.rewriteBasePath: false

# The maximum payload size in bytes for incoming server requests.
#server.maxPayloadBytes: 1048576

# The Kibana server's name.  This is used for display purposes.
server.name: "mbrksapp3221"

# The URLs of the Elasticsearch instances to use for all your queries.
elasticsearch.hosts: ["http://172.29.32.24:9200", "http://172.29.32.23:9200", "http://172.29.32.22:9200"]

# When this setting's value is true Kibana uses the hostname specified in the server.host
# setting. When the value of this setting is false, Kibana uses the hostname of the host
# that connects to this Kibana instance.
#elasticsearch.preserveHost: true

<H1>Hello</H1>

heyyyyy
heyyyyyyy
heyy

data50text
datatext

# Kibana uses an index in Elasticsearch to store saved searches, visualizations and
# dashboards. Kibana creates a new index if the index doesn't already exist.
kibana.index: ".kibana"

# The default application to load"""

creditCards = input()


import re

pattern = re.compile(r'[4-6]\d{3}(-|)\d{4}(-|)\d{4}(-|)\d{4}$')


for match in pattern.finditer(creditCards):
    print(match)