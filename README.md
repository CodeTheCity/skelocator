# Skelocator Project
Run by Team Skelocator, CTC14

## Background
This project was part of [Code The City 14 - Archaeology](https://github.com/CodeTheCity/ctc14) hack weekend, run in Aberdeen on 15th - 16th September 2018.

## Purpose
To identfy and extract data from miscellaneous sources arising from the excavation of the Mither Kirk in 2006.

This addressed two specific challenges 
- converting data from a [Microsoft Access2 Database](Levels.mdb)
- identifying co-ordinate information for skeletons and other remains from scanned plans

The former was a 2006 database of transcribed data from the levels notebooks created at the dig and which recorded the various levels of the excavation. 

## Progress
The appropriate folders from the suplied data were identified and are documented in [folders.txt](folders.txt).

### The Levels Database
The [Levels database](Levels.mdb) was processed and two CSV files produced: [Tables Export](Levels_Table_export.csv) and [Queries Export](Levels_query_export.csv). 

The file [Tables Export](Levels_Table_export.csv) was of most interest, but we noted some issues with the contents. 
The "Reduced Value" column is height above sea level for the object being recorded. This file is possibly incomplete: heighest SK# is 641, but have 1004 in other lists, and number of rows seems small even for 641 skeletons. 

A member of another team carried our a futher test of the Levels Database - but we do not have access to the outputs of that at present. 

### The Scanned Plans
The scanned plans were in a mixture of TIFs and JPGs. 

We identified that the [Sloth Application](https://github.com/cvhciKIT/sloth) would allow us to manually capture co-ordinates from plans and export these as a json file per scan of a level.

## To do

Still to be done

## Skeleton Traces

Corel Photo Paint files: http://argh.technology/foo/skelator/cpt-converted/

Skeleton Plan: http://argh.technology/foo/skelator/plan%20of%20skeletons.dxf

Scanned plans: http://argh.technology/foo/skelator/scanned%20plans/
