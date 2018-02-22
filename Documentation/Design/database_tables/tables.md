# Database Tables used in the Christmas Exchange Application

## List of Tables


|Table|Phase|Description|
|-----|-----|-----------|
|[person](#person-table)|conversion|Information defining a person| 
|[clan](#clan-table)|1|Clan name|
|[clanmember](#clanmember-table)|1|Membership for each clan|
|[message](#message-table)|3|messages between users|
|[santalist](#santalist-table)|conversion|group who draw for gift exchange|
|[santalistmember](#santalistmember-table)|conversion|membership for santalists|
|[santalistexclude](#santalistexclude-table)|conversion|excluded links for santalist|
|[santalistdrawing](#santalistdrawing-table)|conversion|instance a drawing|
|[drawingresult](#wish-table)|conversion||
|[wish](#wish-table)|conversion|gift suggestions for users|
|[gift](#gift-table)|conversion|gifts purchaged for users|
|[relationship](#relationship-table)|3|Spouses, children, parents|
|[proxy](#proxy-table)|3|People who can act for other people|

## Table Definitions and Examples

In general, I'm leaving the id (rowid) off of the table description, with the understanding that there will be such an id for pretty much every table; certainly every table that is the object of a foreign key. A datatype of key indicates a link to the rowid for that table.


### person Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|userid|text|id the user uses to log in; may allow email as well, if we implement our own login|
| fullname | text | Unique (at least in all clans) name string which is supposed to identify a human for other users.  Have to figure out how to deal with humans with same name.  Perhaps it should be further broken into first, middle and last names|
| nickname | text | (display name) shorter name used by the user. On further reflection, this needs to be extended to alllow a different nickname by clan, but this one will be left in for the moment.|
| birthday | date ||
| email | text ||
|status|enum|(active,hold,left)|
||||

#### Example Rows

|userid|fullname|nickname|birthday|email|status|
|------|--------|--------|---------|-----|------|
|mbirdsall|Michael G. Birdsall|mike|1953-08-16|fakeone@gmail.com|active|
|ntdgn|Edward A. Birdsall|ed|1952-04-23|anothermail@gmail.com|active|

### clan Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|clanname|text||
|description|text|
|admin|person key|
||||


#### Examples

|name|Description|
|----|-----------|
|CanyonBirdsalls|Ted and Helen's kids and close family|
|Kirkups|Redford Kirkups|
|Eatonites|Group that lived together in Eaton House|

### clanmember Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|clan|key||
|person|key||
|status|enum|(active,hold,status)|
||||

#### Example Rows

|clan|person|status|
|----|------|------|
|1|1|active|active|
|1|2|active|active|
|2|1|active|active|
|2|3|active|active|

### message Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|sender|person key||
|sent|datetime||
|subject|text|
|body|text|
|status|enum|
||||

#### Examples

|sender|sent|subject|body|status|
|------|----|-------|----|------|
|4|2018-03-22|Give Bike Together?|Would you like to join me in buying a bike for Billy for his birthday?|sent|


### santalist Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|listname|text||
|clan|key|
||||

#### Examples

|listname|clan|
|----|----|
|BirdsallChristmas|1|
|OlderEatonites|3|

### santalistmember Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|santalist|key||
|user|key|
||||

#### Examples

|santalist|user|
|---------|----|
|1|1|
|2|1|

### santalistexclude Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|santalist|santalist key|Which list excludes|
|membera|person key|member who cannot draw|
|memberb|person key|member who cannot be drawn|

#### Examples

|santalist|membera|memberb|
|---------|-------|-------|
|4|12|18
|4|18|12

### santalistdrawing Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|listid|key||
|title|text||
|comment|text|Comment about drawing|
|drawdate|datetime||
|giftdate|date|
|status|enum|active, over|

#### Examples

|listid|title|comment|drawdate|giftdate|status|
|---------|------------|-------|-----------|--------|------|
|3|BirdsallChristmas2000|Limit $25|2000-11-13:00:00:00|2000-12-25|over|
|||||||

### drawingresult table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|drawing|santalistdrawing key|which drawing instance|
|giver|person key|giver|
|giftee|person key|receiver|
||||

#### Examples

|drawing|giver|giftee|
|-------|-----|------|
|27|8|14|
|27|14|12|
|27|12|8|

### wish Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|created|datetime|Date and time wish first created|
|by|person key| Person who created/suggested it|
|giftee|person key|Person this gift is a wish for|
|description|description of the item|
|numberwanted|integer+|how many of this item are desired. Some Nonnumeric values, like "any" will be used as well.|
|expires|date|Date at which it is no longer desired. May have non-date value, like "never".|
||||

#### Examples

|Created|by|giftee|description|numberwanted|expires|
|-------|--|---|-----------|------------|-------|
|2017-08-05 10:30:29.000|85|85| A Rogue Steel stage rapier (for use, not collection): http://www.roguesteel.com/store/p1/Rapier_-_Swept_Hilt.html - Opposing Curve Quillions, Right-handed, black leather grip, tapered pommel. (Also happy to share the cost of this :) )| 1 | 2017-12-04|
|2002-10-28 21:04:35|2|2|Frangelico, B&B, Irish Mist|Any|Never|


### gift table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|when_bought|datetime|When item was bought|
|wishid|wish key|Which wish was bought
|giver|person key|Who bought it|
|giftee|person key|Who did they buy it for|
|note|text|Information to help others|
|numberbought|integer|how many were bought|
|givedate|date|Date of occasion when it will be given|
|status|enum|(reserved,bought,given,removed)|
||||

#### Example

|when_bought|wishid|giver|giftee|note|numberbought|givedate|status|
|------|------|--|---|----|------------|--------|------|
|2017-12-06|243|14|7|Purchased on Amazon.com|1|2017-12-25|given|

### relationship table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|from|person key|The one having the relationship|
|relation|enum|Relationship, like parent, child, sibling, spouse|
|to|person key|The one related to| 
||||

#### Examples

|relation|from|to|
|--------|----|--|
|spouse|14|43|
|spouse|43|14|
|sibling|14|95|
|sibling|95|14|

### proxy Table

#### Definition

|Column|Type|Description|
|------|----|-----------|
|clan|clan key|Proxy in which clan|
|principal|person key|The one being proxied|
|proxy|person key|The proxy|
||||

#### Example Rows

|clan|principal|proxy|
|----|---------|-----|
|1|4832|1232|

