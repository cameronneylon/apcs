apcs
====

Data and information on article processing and other charges paid for scholarly publication services

Introduction
------------

The Wellcome Trust released a dataset via figshare in March 2014 giving information on their funding of 
Article Processing Charges in 2012/13. This was a concatenation of information from those institutions
that have Wellcome Trust funds. It includes all papers that the Trust is aware of paying money for and
gives paper titles, in some cases Pubmed IDs and Pubmed Central IDs, and the amount paid according to 
the institution.

Data Issues
-----------

The original dataset had inconsistent names for publishers and for journals. This was cleaned up to a 
certain extent using Open Refine. The data also contain significant errors in the amounts apparently
charged. Several of the figures for PLOS papers are different to those in our internal accounting system. 
At the moment these have not been corrected.

Contributions
-------------

The somewhat cleaned dataset is available as Wellcome-APCs.tsv in the repository. Further contributions to the
dataset are welcome via a pull request. Obvious enhancements would be to obtain DOIs for the papers from 
Crossref search API and then to use that to clean up the bibliographic information. We could also check the
licenses and/or availability of papers in this dataset.

If you wish to correct financial details please give some information on the provenance of your data. As this
data is potentially sensitive
