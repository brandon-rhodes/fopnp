#
# Build SSL certificates for our example.com
#

BITS=3072

all: ca.crt


ca.crt: ca.cnf ca.key
	openssl req -new -x509 -days 36500 -config ca.cnf \
		-extensions v3_ca -key ca.key -out $@

ca.key:
	openssl genrsa -out $@ $(BITS)

    # openssl genrsa -out server.key $(BITS)
    # openssl req -new -key server.key -config server.cnf -out server.csr
    # openssl ca -batch -config ca.cnf -days 36500 \
    #     -keyfile ca.key -cert ca.crt \
    #     -in server.csr -outdir . -out server.crt

    # openssl genrsa -out client.key $(BITS)
    # openssl req -new -key client.key -config client.cnf -out client.csr
    # openssl ca -batch -config ca.cnf -days 36500 \
    #     -keyfile ca.key -cert ca.crt \
    #     -in client.csr -outdir . -out client.crt
