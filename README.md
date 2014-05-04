apcs
====

Data and information on article processing and other charges paid for scholarly publication services

For corrections and contribution please make changes at the version at:
https://docs.google.com/spreadsheets/d/1RXMhqzOZDqygWzyE4HXi9DnJnxjdp0NOhlHcB5SrSZo/edit?usp=sharing

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

The somewhat cleaned dataset is available at wellcome/Wellcome-APCs.tsv in the repository. 

In the short term please make corrections and changes at the following Google spreadsheet and I will aim
to fold them into this version as soon as I can. If you prefer making a pull request then feel free to do
so but I can't currently commit to keeping the various versions in synch.

Obvious enhancements would be to obtain DOIs for the papers from 
Crossref search API and then to use that to clean up the bibliographic information. We could also check the
licenses and/or availability of papers in this dataset.

If you wish to correct financial details please give some information on the provenance of your data. As this
data is potentially sensitive
