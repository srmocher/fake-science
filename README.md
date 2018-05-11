## Real/Fake Science

### Steps
1. Download Common Crawl Index Client tool from https://github.com/ikreymer/cdx-index-client

Run queries for url patterns like "*.com/climate*/","*.com/science*/" etc to get the matching URLs which
will be stored in a file

2. Get the HTML from the URLs and store in Solr

Run the script `cc_solr.py` with parameters modified accordingly.

3. TODO - 