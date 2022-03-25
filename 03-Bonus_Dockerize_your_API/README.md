# Dockerize your API

Check the `Dockerfile` in the current folder.

In order to build your image you should start Docker then:

```shell
$ docker build . -t salary_api:latest
```

Then, to launch the Docker:

```shell
$ docker run -p 80:5000 -it salary_api
```

We used `-p 80:5000` in order to map HTTP port (which is 80 by defautl) to our Flask port 5000 (which is the default port Flask has chosen). So you can access your documentation to `http://0.0.0.0/` and the prediction endpoint to `http://0.0.0.0/predict`.

You can check that with `curl`:

```shell
$ curl -i -H "Content-Type: application/json" -X POST -d '{"year": 1}' http://0.0.0.0/predict
```
