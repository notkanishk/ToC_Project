
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEleftPOWERrightNEGATIVEBRACKETCL BRACKETOP DIVIDE FLOAT INT MINUS MULTIPLY PLUS POWER\n    calc : expression\n         | empty\n    \n    expression : expression POWER expression\n                | expression PLUS expression\n                | expression MINUS expression\n                | expression MULTIPLY expression\n                | expression DIVIDE expression\n    \n    expression : BRACKETOP expression BRACKETCL\n    \n    expression : MINUS expression %prec NEGATIVE\n    \n    expression : INT\n                | FLOAT\n    empty : '
    
_lr_action_items = {'BRACKETOP':([0,4,5,8,9,10,11,12,],[5,5,5,5,5,5,5,5,]),'MINUS':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[4,10,4,4,-10,-11,4,4,4,4,4,-9,10,-3,-4,-5,-6,-7,-8,]),'INT':([0,4,5,8,9,10,11,12,],[6,6,6,6,6,6,6,6,]),'FLOAT':([0,4,5,8,9,10,11,12,],[7,7,7,7,7,7,7,7,]),'$end':([0,1,2,3,6,7,13,15,16,17,18,19,20,],[-12,0,-1,-2,-10,-11,-9,-3,-4,-5,-6,-7,-8,]),'POWER':([2,6,7,13,14,15,16,17,18,19,20,],[8,-10,-11,-9,8,-3,8,8,8,8,-8,]),'PLUS':([2,6,7,13,14,15,16,17,18,19,20,],[9,-10,-11,-9,9,-3,-4,-5,-6,-7,-8,]),'MULTIPLY':([2,6,7,13,14,15,16,17,18,19,20,],[11,-10,-11,-9,11,-3,11,11,-6,-7,-8,]),'DIVIDE':([2,6,7,13,14,15,16,17,18,19,20,],[12,-10,-11,-9,12,-3,12,12,-6,-7,-8,]),'BRACKETCL':([6,7,13,14,15,16,17,18,19,20,],[-10,-11,-9,20,-3,-4,-5,-6,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,4,5,8,9,10,11,12,],[2,13,14,15,16,17,18,19,]),'empty':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calculate','Gui.py',66),
  ('calc -> empty','calc',1,'p_calculate','Gui.py',67),
  ('expression -> expression POWER expression','expression',3,'p_exp','Gui.py',78),
  ('expression -> expression PLUS expression','expression',3,'p_exp','Gui.py',79),
  ('expression -> expression MINUS expression','expression',3,'p_exp','Gui.py',80),
  ('expression -> expression MULTIPLY expression','expression',3,'p_exp','Gui.py',81),
  ('expression -> expression DIVIDE expression','expression',3,'p_exp','Gui.py',82),
  ('expression -> BRACKETOP expression BRACKETCL','expression',3,'p_group','Gui.py',89),
  ('expression -> MINUS expression','expression',2,'p_negative','Gui.py',96),
  ('expression -> INT','expression',1,'p_terminal','Gui.py',103),
  ('expression -> FLOAT','expression',1,'p_terminal','Gui.py',104),
  ('empty -> <empty>','empty',0,'p_empty','Gui.py',119),
]
