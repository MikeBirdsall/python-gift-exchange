# Model thoughts

Contains thoughts for model.  Broken down into various 'Lists'; Wish list, Shopping List, Purchased List and Personal Information.  Wish List is a listing of those items desired by individuals or those suggested by others.  Shopping List is a list of items a person is using to buy gifts off the wish list for others for a given event.  Purchased List is those items bought by a person for others for a given event.

Events may be Christmas-year, birthday-year, Anniversary-year, ??.  Reason for specifying is either early buying or buying for more than one event at a time.  Say Christmas and a December birthday as an example.  Another example; buying for Christmas in May since you saw just the gift for someone while on a trip and they either had it on the list or you added the suggestion.  (?)Wishlists don't need events since they are not targeted for a specific event normally(?).

## WishList
### Attributes
1. Owner  
1. Suggestor  
1. Description  
1. Amount Desired  
1. Expiration  
1. Status  

### Methods
* getWishlist(target userid)

* addWish(userid,target UserId, item description, number desired, expiration)  
      add an item to target user's wish list
          
* editWish(userid, targetuserid,itemid, item description, number desired, expiration, notes)  
     change wish info to new values
          
* removeWish(userid, itemid)  
     mark an item as hidden? for userid? all users?  
     
* buyWish(userid,targetUserId, itemId, amount, purchased)  

* reserveWish(userid,targetUserId, itemId, amount, reserved)  

* purgeWishList(userid, target userid, date)  
     date used to hide items purchased and have no value remaining (any will always have value remaining)
     
* clear Wish list(userid,  target userid, date)  
     date used to mark items expired and hidden

## Shopping List
### Attibutes
1. Date  
1. Event  
1. Owner  
1. Target User  
1. Link to Wish of Target User   
1. Status  
1. Number  

### Methods
getShoppingList

addToShoppingList(userid,targetUserid,itemid)
     add an item for targetUser to Shopping List
     
updateShoppingList(userid,targetUserid,itemid,action)
     either mark an item either bought or cancelled
     
purgeShoppingList(userid,date)
     sets date before which items in Shopping list will not be shown

## Purchased List
### Attributes
1. Date Purchased  
1. Event  
1. Owner  
1. For Whom  
1. Item Description  
1. Number Purchased  
1. Notes  

### Methods
purgePurchasedList(userid,date)

getPurchasedList(userid)

## PersonalInformation
### Attributes
* userID
* DisplayName
* FullName
* EmailAddresses
* birthday
* spouse
* wedding day
* children

### Methods
updatePassword

addEmail(userid,email)

removeEmail(userid,email)

setPrimaryEmail(userid,email)

getBirthday(userid)

updateBirthday(userid,birthday)

AddSpouse()

AddChildren()

getMessageIds(userid)

getMessage(userid,messageid)

messageReply()


sendMessage

editMessage

## Group Information
### Attributes
* GroupID
* GroupName
* GroupAdministrator(s)
* GroupMembers
* SecretSanta

### Methods
generateSecretSanta

getSecretSantaPerson

## Site Information
### Attributes
* Site Owner
* Site Administrators


### Methods
setupGroup

## other

