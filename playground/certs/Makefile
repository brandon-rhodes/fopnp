#
# Build SSL certificates for our example.com
#

BITS=3072

all: ca.pem client.pem localhost.pem \
     ../base/ca.crt ../ftp/ftp.crt ../ftp/ftp.key \
     ../mail/service.pem ../www/service.pem \
     ../../py3/chapter06/ca.crt ../../py3/chapter06/localhost.pem

../base/ca.crt: ca.crt
	cp $^ $@

../ftp/ftp.crt: ftp.crt
	cp $^ $@

../ftp/ftp.key: ftp.key
	cp $^ $@

../mail/service.pem: mail.pem
	cp $^ $@

../www/service.pem: www.pem
	cp $^ $@

../../py3/chapter06/ca.crt: ca.crt
	cp $^ $@

../../py3/chapter06/localhost.pem: localhost.pem
	cp $^ $@

ca.pem client.pem localhost.pem mail.pem www.pem: %.pem: %.crt %.key
	cat $*.crt $*.key > $*.pem

client.crt ftp.crt localhost.crt mail.crt www.crt: %.crt: ca.cnf ca.key ca.crt %.csr
	openssl ca -batch -config ca.cnf -days 36500 \
		-keyfile ca.key -cert ca.crt \
		-in $*.csr -outdir . -out $*.crt

client.csr ftp.csr localhost.csr mail.csr www.csr: %.csr: %.key %.cnf
	openssl req -new -key $*.key -config $*.cnf -out $*.csr

ca.crt: ca.cnf ca.key
	openssl req -new -x509 -days 36500 -config ca.cnf \
		-extensions v3_ca -key ca.key -out $@

ca.key client.key ftp.key localhost.key mail.key www.key:
	openssl genrsa -out $@ $(BITS)
