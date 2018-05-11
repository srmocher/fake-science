## Real/Fake Science

### Steps
1. Download Common Crawl Index Client tool from https://github.com/ikreymer/cdx-index-client

Run queries for url patterns like "*.com/climate*/","*.com/science*/" etc to get the matching URLs which
will be stored in a file

2. Get the HTML from the URLs and store in Solr

Run the script `cc_solr.py` with parameters modified accordingly.

3. TODO - compare existing fake training data to data pushed to Solr from CC to extract larger fake training set.

4. TODO - add the Keras code for CNN/LSTM classifiers using Google News word2vec model for classifying real/fake articles.