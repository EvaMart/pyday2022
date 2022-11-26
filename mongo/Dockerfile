FROM mongo

COPY snippets.json /tmp/snippets.json
CMD mongoimport --host mongodb --db PyDayBCN --collection snippets --type json --file /tmp/snippets.json --jsonArray
