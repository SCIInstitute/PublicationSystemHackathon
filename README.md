# PublicationSystemHackathon
A Collaborative effort to build a better publication tracking and recording system

## Overview
How do we compile lists of publications that reflect the impact of a given piece of work?  This can be the list of the publications produced by yourself, your team, individual projects, and software products that you need to compile for reports or grant applications.  Or, even better, these would be stored in a sharable database that can be easily and regularly updated.
Some tools, like ORCID, MyNCBI, Google Scholar, among others, can help track the publications of individuals fairly easily, yet it can be difficult to extend these tools to other uses.  Any manual or automatic sorting or tagging of these publications cannot be shared on these same platforms, if they allow tagging or sorting.  Other tools, such as Mendeley and Zotero allow for sorting, tagging, and grouping of publications, and can even be shared with others, yet nearly all these functions, including adding new publications, need to be done manually and they cannot interface with other tracking services.  

For project based publication tracking the options are fewer and more frustrating.  Most of these publications need to be manually vetted and/or added, and these records need to be updated regularly.  Google scholar’s limited tagging system does not allow for binary combination of tags, limiting its utility in tracking a publication database for multiple uses, and these annotations and tags cannot be shared.  Mendelay and Zotero can manually collect and share these publications, but the tagging system is similar to google scholar, and sharing with groups causes duplicate incidences of the publication record.  Additionally, these tools do not interface with other tools, such as Google Scholar, ORCID, and MyNCBI.  These are also difficult to use with version control systems.

The goal of this hackathon is to develop a publication collection, tracking, and sharing system that can be easily updated from publication databases (Google Scholar, PubMed, NCBI, ORCID, etc.) and provide lists of publications for specific and varied reporting purposes.  Possible solutions include: software tools to process publication records, interfaces between existing services, UI tools for web embedding and deployment, and/or an internal database system. 


## Preliminary Schedule
 - 11:00 -12:00 — Description of problem. Existing technologies. Brainstorm requirements
 - 12:00 - 1:00 — Lunch (provided). Requirements discussion.  
 - 1:00 - 1:30 — Identify key pieces, form working groups
 - 1:30 - 3:30 — Report progress and plans


## Previous Work
 - VDL's tracking system : <https://github.com/visdesignlab/visdesignlab.github.io>
 - MedVIC's tracking sytem : <https://github.com/MedVIC-Lab/medvic-lab.github.io>
 - Eric's system: <https://github.com/SCIInstitute/SCIIT-joomla>
 - NASA's SciX: <https://github.com/adsabs>

## Outcomes
During the hackathon, we discuss multiple existing tools, including some that were new to most, outlined a pipeline to work with existing public database to create and maintain private collections, indefied key points to test and prototype, and developed prototype tools for local database management and scapping tools.  

The key descisions were:
 - To pursue [Academic Tracker](https://github.com/MoseleyBioinformaticsLab/academic_tracker) as an option to interface with public databases.  See [PublicationScrapping](https://github.com/SCIInstitute/PublicationSystemHackathon/tree/main/PublicationScraping) folder.  
 - Tabular format will likely be too limiting for expected use cases.  These experiments are found in this repo in [orcid+polars](https://github.com/SCIInstitute/PublicationSystemHackathon/tree/main/orcid%2Bpolars).  PR#2.
 - Use MongoDB for data storage with data validation.  The schema will be a modification of [ORCiD's](https://github.com/ORCID/orcid-model/tree/master).  We have a script with a prototype in place (see [notes_jakew.md](https://github.com/SCIInstitute/PublicationSystemHackathon/blob/main/notes_jakew.md)).  PR#1
 - Build on  these prototypes and test cases using these tools to find areas for future improvement.
 
 The use cases we identified:
  - Shared database of publications for SCI members
  - Ability to make a private database with custom organization
 
 ## next steps:
  - Work with IT to find location for shared database and UI
  - expand prototypes and uses cases to meet existing needs
  - build interface with bibtex, github pages, and others
  
  
## More Notes

Additional notes are found in the other READMEs, [google drive](https://docs.google.com/document/d/1L2mKG3f87lNohPMsirCJHXGM91JM3Ezzx5qxXGxjMok/edit?tab=t.0)) (with recording and AI summary), and on the [slack channel](https://join.slack.com/share/enQtODMxMDE2NzI3ODAzNi01OTk2ZDFlOTFiYmU4NDdmMmI5NTc4NTY5NzM1ZmRhNDQyZmVkMDFiODIyMjliNDIwZDIzYjNjNDJkMjk0YTJi)



  

 

 

