vcl 4.0;
import var;

backend default {
  .host = "apache";
  .port = "80";
}

sub vcl_recv {
    set req.http.xxx = "yyy";
    var.global_set("conn_string", req.http.connection);
}

sub vcl_backend_fetch {
    set bereq.http.connection = var.global_get("conn_string");
}
