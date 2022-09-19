print("Welcome to treasure island")
print('''
       ,,,        _,_        _@_        _(_        _?_        >*<
     _/. .\_    _/- -\_    _/, ,\_    _/' '\_    _/a a\_    _/. .\_
    (.\_o_/.)  (.\_-_/.)  (,\_e_/')  (.\_^_/.)  (.\_~_/')  (.\_c_/.)
    (.`,.`'.') (.`,.'.'.) (.`'.,'.') ('.,'.`'.) (.'.,'.`.) (.,'.,'',)
     ('.`,'`,)  ('.`,'',)  ('.','.`)  ('.,'.',)  ('.,'.`.)  (',.'`.,)
      ('.`,'`)   ('.','`)   (.'.,'.)   ('.`.,')   ('.','')   (.'.'.')
 Takshu`--'"`     `--'"`     `--'"`     `--'"'     `--'"'     `--'"'
 *********************WELCOME TO THE TREASURE ISLAND*****************
''')
print('''
 *************************************WELCOME TO THE TREASURE ISLAND************************************
 :"""""""""""""""":"""""""""""""""":"""""""""""""""":"""""""""""""""":"""""""""""""""":"""""""""""""""":
    i"""""""""""""""i"""""""""""""""i"""""""""""""""i"""""""""""""""i"""""""""""""""i"""""""""""""""i
       i""""""""""""""i""""""""""""""i""""""""""""""i""""""""""""""i""""""""""""""i""""""""""""""i
          i"""""""""""""i"""""""""""""i"""""""""""""i"""""""""""""i"""""""""""""i"""""""""""""i
X""""""""""""X""""""""""""X""""""""""""X""""""""""""X""""""""""""X""""""""""""X""""""""""""X""""""""""""X
   ]X["""""""""]X["""""""""]X["""""""""]X["""""""""]X["""""""""]X["""""""""]X["""""""""]X["""""""""]X[
       XXX""""""""XXX""""""""XXX""""""""XXX""""""""XXX""""""""XXX""""""""XXX""""""""XXX""""""""XXX
 XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX
      XXX[""""]XXX[""""]XXX[""""]XXX[""""]XXX[""""]XXX[""""]XXX[""""]XXX[""""]XXX[""""]XXX[""""]XXX      
  XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX
      ""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""
       -XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-
      __XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__XXXXX__
  XXXXX___XXXXX___XXXXX___XXXXX___XXXXX___XXXXX___XXXXX___XXXXX___XXXXX___XXXXX___XXXXX___XXXXX___XXXXX
      XXX[____]XXX[____]XXX[____]XXX[____]XXX[____]XXX[____]XXX[____]XXX[____]XXX[____]XXX[____]XXX
 XXX_______XXX_______XXX_______XXX_______XXX_______XXX_______XXX_______XXX_______XXX_______XXX_______XXX
       XXX________XXX________XXX________XXX________XXX________XXX________XXX________XXX________XXX
   ]X[_________]X[_________]X[_________]X[_________]X[_________]X[_________]X[_________]X[_________]X[
X____________X____________X____________X____________X____________X____________X____________X____________X
          i_____________i_____________i_____________i_____________i_____________i_____________i
       i______________i______________i______________i______________i______________i______________i
    i_______________i_______________i_______________i_______________i_______________i_______________i
 :________________:________________:________________:________________:________________:________________:
''')
choise = input('Where you want to go , "left" or "right" ? \n').lower()

if "left" != choise:
    print("You fell into a hole. Game over!!!")
else:
    choise = input('You\'ve come to a lake having an island in the middle. Would you like to "swim" to the island or "wait" for a boat? \n').lower()
    if "wait" != choise:
        print("You got attacked by angry trout. Game over!!!")
    else:
        choise = input('You arrived the island on a boat unharmed, There is a house with 3 doors, One "Red", one "Yellow" and one "Green", which one will you chose ? \n').lower()
        if "yellow" != choise:
            print("Monster came out and eats you. Game over!!!")
        else:
            print("Congratulations you found the treasure, You win!!!\n")
