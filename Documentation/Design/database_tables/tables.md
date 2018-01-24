# Database Tables

## Tables Names

Table | Description
---|---
 | **In conversion**
person | Information defining a person
wish | gift suggestions for users
gift | gifts purchaged for users
santalist | group who draw for gift exchange
santalistmember | membership for santalists
santalistexclude | excluded links for santalist
 | **First Implementation**
group | Group names
groupmembers | Membership for each group
message | messages between users
relationships | Spouses, children, parents
proxy | People who can act for other people
 | **Proposed?**
reserved? |
clan |
clanmember |

## Table Definitions

Table | Column | Type | Description
person | | |
 | userid | text | id used to log in 
 | fullname | text | Unique (at least in all groups) name string which is supposed to identify a human for other users.  Have to figure out how to deal with humans with same name.  Perhaps it should be further broken into first, middle and last names
 | nickname | text | (display name) shorter name used by the user. On further reflection, this needs to be extended to alllow a different nickname by group, but this one will be left in for the moment.
 | birthdate | date | 
 | email | text | 
    

group
    id
    name

groupmemmbers
   group id
   person id

message
   sender personid
   sent datetime
   subject
   body
   status

santalist
santalistmember
clan
clanmember
wish
gift
reserved?
relationships - spouses, children, parents
proxy

## Table examples
