# Run all scripts to make sure they still work

set -e

cd python3
cd 12
python3 trad_gen_simple.py
python3 trad_gen_newhdrs.py
python3 trad_parse.py
python3 mime_gen_basic.py test.txt test.txt.gz
python3 mime_gen_alt.py
python3 mime_headers.py > message2.txt
python3 mime_gen_both.py test.txt test.txt.gz > message3.txt
python3 mime_structure.py message3.txt
echo q | python3 mime_decode.py message3.txt
python3 mime_parse_headers.py message2.txt
cd ..
cd ..
echo
echo Success!
echo
