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
`app_test.rb` contains a basic test, which may help in
understanding how to interact with the API. Tests can
be run using `docker-compose run web ruby app_test.rb`.
