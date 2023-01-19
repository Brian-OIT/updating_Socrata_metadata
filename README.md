# NCHS-Socrata-Metadata-Updates

**Point of Contact** - Anthony Lipphardt (<hku4@cdc.gov>)

**Organizational Unit** - CDC/NCHS/OIS

**Related Projects** - N/A

**Related Governance Status** - N/A

**Program Official** - Travis Hoppe (<qrd5@cdc.gov>)

## Sample Notebooks

- [Create-Public-NCHS-Datasets-CSV](Create-Public-NCHS-Datasets-CSV.ipynb) - Read latests data.json file from data.cdc.gov and write a list of NCHS datasets to CSV.
- [Sample-Metadata-Update](Sample-Metadata-Update.ipynb) - Example of metadata update for required fields on a private NCHS test dataset.
- [Suggested-Citation-Update](Suggested-Citation-Update.ipynb) - Checks each NCHS dataset against recommended citation format. Applies updates to those datasets not in compliance.
- [Remove-Legacy-Fields](Remove-Legacy-Fields.ipynb) - Flags NCHS datasets with the legacy field 'Data Quality: Updated Frequency' and removes or nullifies it.
- [Draft-Datasets-Using-Discovery-API](Draft-Datasets-Using-Discovery-API.ipynb) - Find all **draft** NCHS datasets using Socrata's Discovery API.
- [Excel-to-Socrata-Metadata](Excel_to_Socrata_clean.ipynb) - Push metadata for multiple datasets into the correct fields in Socrata in one script.

## Sample Scripts

- [update_common_core.py](update_common_core.py) - Explictly change some elements of the Common Core for a fixed number of datasets on Socrata. Script provided by Brian Salant (<pev9@cdc.gov>).

## Related Publications [sample]

- Spencer MR, Ahmad F. Timeliness of death certificate data for mortality surveillance and provisional estimates. National Center for Health Statistics. 2016. Available from: [https://www.cdc.gov/nchs/data/vsrr/report001.pdf](https://www.cdc.gov/nchs/data/vsrr/report001.pdf)
- Hedegaard H, Miniño AM, Warner M. Drug overdose deaths in the United States, 1999–2018. NCHS Data Brief, no 356. Hyattsville, MD: National Center for Health Statistics. 2020. Available from: [https://www.cdc.gov/nchs/products/databriefs/db356.htm](https://www.cdc.gov/nchs/products/databriefs/db356.htm)

## Notes

Developer API tokens and secrets have been removed from the notebooks and scripts. Please to [https://support.socrata.com/hc/en-us/articles/360015776014-API-Keys](https://support.socrata.com/hc/en-us/articles/360015776014-API-Keys) for instructions on how to create a developer token and secret.

Metadata API:

- _Read-only_ access does not require authentication
- _Write_ access requires authentication by an administrator or publisher designated as an asset owner

Discovery API:

- Authentication is **not required** for read-only access to anonymously visible (i.e. published, public, approved) assets
- Authentication **is required** to search across private, unpublished, unapproved, or hidden data. Once authenticated you will be able to search over any assets from domains that have granted you a right to view those assets (e.g. datasets you own, datasets shared with you).
