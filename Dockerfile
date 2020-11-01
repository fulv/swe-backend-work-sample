FROM ruby:2.7

RUN gem install bundler -v 1.17.3

RUN mkdir /app
WORKDIR /app

ADD Gemfile /app
ADD Gemfile.lock /app
RUN bundle install

ADD app.rb /app
ADD config.ru /app
ADD ssh_certificate_generator.rb /app
ADD generate_ca_key.rb /app
ADD app_test.rb /app

RUN ruby generate_ca_key.rb
RUN chmod 600 ca.key

EXPOSE 3000

CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "3000"]
