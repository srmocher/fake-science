## Real/Fake Science

### Steps
1. Task: Download Common Crawl Index Client tool from https://github.com/ikreymer/cdx-index-client

Run queries for url patterns like "*.com/climate*/","*.com/science*/" etc to get the matching URLs which
will be stored in a file

2. Task: Get the HTML from the URLs and store in Solr

Run the script `cc_solr.py` with parameters modified accordingly.

3. TODO - compare existing fake training data to data pushed to Solr from CC to extract larger fake training set.

4. Task: Added code to train LSTM model on Climate data using Google News word2vec model. Download Google News word2vec model from below model
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing

TODO - add code for training CNN model.