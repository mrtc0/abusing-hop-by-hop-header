FROM varnish:6.3

RUN apt-get update -y && \
	    apt-get install -y build-essential automake libtool curl git python-docutils && \
	    curl -s https://packagecloud.io/install/repositories/varnishcache/varnish60/script.deb.sh | bash && \
	    apt-get install -y varnish-dev && \
	    git clone https://github.com/varnish/varnish-modules.git /tmp/vm && \
	    cd /tmp/vm && \
	    ./bootstrap && \
	    ./configure && \
	    make && \
	    make check && \
	    make install

COPY varnish/default.vcl /etc/varnish/default.vcl
CMD ["varnishd", "-F", "-f", "/etc/varnish/default.vcl"]
