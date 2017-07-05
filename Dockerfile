FROM openjdk:8-alpine
MAINTAINER Benjamin Ricaud <benjamin.ricaud@eviacybernetics.com>


# Install tools
RUN apk update && \
	apk add wget unzip git bash

# Install the server
RUN wget --no-check-certificate -O /gremlin.zip http://apache.mirrors.ovh.net/ftp.apache.org/dist/tinkerpop/3.2.5/apache-tinkerpop-gremlin-server-3.2.5-bin.zip && \
	unzip /gremlin.zip -d /gremlin && \
	rm /gremlin.zip
WORKDIR /gremlin/apache-tinkerpop-gremlin-server-3.2.5

# Place where the graph is saved, see gremlin-graph.properties
RUN mkdir /graph_file

# Configure gremlin for python
RUN bin/gremlin-server.sh -i org.apache.tinkerpop gremlin-python 3.2.5

EXPOSE 8182

# Copy the configuration files and launch
COPY files .
RUN chmod 700 startup_commands.sh
CMD ["./startup_commands.sh"]
