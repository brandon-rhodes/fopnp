#
# Build SSL certificates for our example.com
#

BITS=3072

all: ../base/ca.crt client.crt ftp.crt ../mail/service.pem ../www/service.pem

../base/ca.crt: ca.crt
	cp $< $@

../mail/service.pem: mail.pem
	cp $< $@

../www/service.pem: www.pem
	cp $< $@

mail.pem www.pem: %.pem: %.crt %.key
	cat $*.crt $*.key > $*.pem

client.crt ftp.crt mail.crt www.crt: %.crt: ca.cnf ca.key ca.crt %.csr
	openssl ca -batch -config ca.cnf -days 36500 \
		-keyfile ca.key -cert ca.crt \
		-in $*.csr -outdir . -out $*.crt

client.csr ftp.csr mail.csr www.csr: %.csr: %.key %.cnf
	openssl req -new -key $*.key -config $*.cnf -out $*.csr

ca.crt: ca.cnf ca.key
	openssl req -new -x509 -days 36500 -config ca.cnf \
		-extensions v3_ca -key ca.key -out $@

ca.key client.key ftp.key mail.key www.key:
	openssl genrsa -out $@ $(BITS)
