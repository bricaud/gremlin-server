# A Docker container for Gremlin 3.2.4

This docker file create a container running Gremlin Tinkerpop 3.2.4, with a tinkergraph and configured for use with Python.
To build it run the following command:
```
docker build -t gremlin-container . 
```
This will create a docker image with name "gremlin-container".
The graph database is configured using the files in the "files/" folder.
Gremlin server will serve resquests on port 8182. The graph will be saved into a graphson file, each time the server is shut down.
It will also try to load the graph from this file (if it exists) each time the server is started.


You can then start the container using:
```
docker run -p 8182:8182 -v ~/:/graph_file -it --name gremlin gremlin-container
```
The server can be accessed on port 8182 and the graphson file will be saved in the home directory "~/".