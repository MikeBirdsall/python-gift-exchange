# Model thoughts

## WishList
getPersonalWishlist(userid)

addWish(userid,item description, number desired, expiration)
:    add an item to user wish list
     
suggestWish(userid,target UserId, item description, number desired, expiration)
>     add an item to anothers wish list
     
editWish(userid,itemid,iteminfo...)
     change wish info to new values
     
editSuggestedWish(userid,targetUserId,itemid,iteminfo...)
     change suggested information for another
     
removeWish(userid,itemid)
     mark an item as hidden? for userid
     
buyWish(userid,targetUserId, itemId, amount, purchased)

reserveWish(userid,targetUserId, itemId, reserved)

purgeWishList(userid,date)
     date used to hide items purchased
     
clear Wish list(userid,date)
     date used to mark items expired and hidden

## Shopping List
getShoppingList

addToShoppingList(userid,targetUserid,itemid)
     add an item for targetUser to Shopping List
     
updateShoppingList(userid,targetUserid,itemid,action)
     either mark an item either bought or cancelled
     
purgeShoppingList(userid,date)
     sets date before which items in Shopping list will not be shown

## Purchased List
purgePurchasedList(userid,date)

getPurchasedList(userid)

## PersonalInformation
updatePassword

addEmail(userid,email)

removeEmail(userid,email)

SetPrimaryEmail(userid,email)

getBirthday(userid)

updateBirthday(userid,birthday)

getMessageIds(userid)

getMessage(userid,messageid)

sendMessage

editMessage



## other
getSecretSantaPerson
