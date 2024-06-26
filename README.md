# Description

This starter configuration for a modern Flask application is based off of the following guide from [Test Driven IO](https://testdriven.io) with my own additions:

[Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)

This is an excellent (free) resource that I urge you to work through if the building blocks of this template aren't totally familiar. They have many courses, free tutorials, and blog posts to explore to get up to speed.

### Components

 - Flask - lightweight framework for small and complex Web apps
 - PostgreSQL - open source SQL database
 - Docker - popular container runtime for container management
 - Gunicorn - WSGI HTTP application server
 - Nginx - Reverse proxy, load balancer, and static Web server

### Included PyPI packages

 - [requirements.txt](https://github.com/sedexdev/flask-stack-template/blob/main/services/web/requirements.txt)

# Usage

### .env

 - The provided <code>.env</code> files contain test placeholder values and should be updated for your deployments.
 - They should be uncommented in [.gitignore](https://github.com/sedexdev/flask-stack-template/blob/main/.gitignore) so they are kept out of any public repos.

### Docker Compose

### Building the DB

### Inspecting the DB

# Contributing

# License

[MIT](https://github.com/sedexdev/flask-stack-template/blob/main/LICENSE)
