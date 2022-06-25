# Docker-MongoDB

#### Manage MongoDB container with Docker Compose

```bash
$ docker-compose up -d

Creating network "docker-mongodb_default" with the default driver
Pulling database (mongo:)...
latest: Pulling from library/mongo
d7bfe07ed847: Pull complete
97ef66a8492a: Pull complete
20cec14c8f9e: Pull complete
38c3018eb09a: Pull complete
ccc9e1c2556b: Pull complete
593c62d03532: Pull complete
1a103a446c3f: Pull complete
be887b845d3f: Pull complete
e5543880b183: Pull complete
Digest: sha256:37e84d3dd30cdfb5472ec42b8a6b4dc6ca7cacd91ebcfa0410a54528bbc5fa6d
Status: Downloaded newer image for mongo:latest
Creating mongo-container ... done
```

#### Access to container WEB_API

```bash
docker exec -ti web_api sh
```

#### Import XML to MongoDB

Execute with Docker. 

```bash
docker exec -ti web_api python import-mongo.py
```

#### Queries API

```bash
curl ...
```