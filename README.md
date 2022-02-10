# Aptible Deploy Software Engineer Work Sample

Provided is a tiny RESTful API that generates SSH certificates
with specific limitations. See the work sample instructions for
more details.

### Running the application

The application is pre-bundled for usage with
[docker-compose](https://docs.docker.com/compose/gettingstarted/)
to make running the application easier.

To start the application, run `docker-compose up`.

### Running tests
`test_app.py` contains a basic test, which may help in
understanding how to interact with the API. Tests can
be run using `docker-compose run web pytest -rA --disable-warnings`.


# Fulvio Casali's Work Sample

The included Makefile contains most of the commands needed to set up the
local and remote environments, and deploy the docker containers (locally
and remotely).

### Preparation

1. In the `hosts` file, either replace the value of `ansible_ssh_host` with
a real hostname, IP address, or a name that is registered in your `.ssh/config`
file.  Ideally, you should add a `aptible-work-sample` entry to `.ssh/config`.

2. Also, replace the path to the ssh key you want to use in `hosts` file.

3. In `docker-compose`, replace the `TODO` placeholders with real domain names
and email addresses.

4. Run `make playbook-setup`.

5. Run `make docker-context`.

6. Run `make compose-pull`.

7. Run `make compose-up`.

Your remote host will now run an nginx proxy with letsencrypt certificates,
proxying all traffic to flask on port 3000.
