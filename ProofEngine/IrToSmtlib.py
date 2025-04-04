import sys
sys.path.insert(0, "../ChironCore/ChironAST/")
from ChironCore.Infix_To_Prefix import Infix_To_Prefix
from ChironAST import ChironAST

def IrToSmtlib(irList):
    for item in irList:
        if(type(item[0]) != ChironAST.AssignmentCommand):
            print("Only Assignment commands are supported")
            return
        else:
            # print(type(item[0].__str__()))
            print(f"assert {Infix_To_Prefix(item[0].__str__())}")

# def IfElseToSmtlib(cond, if_stat, else_stat):
#     cond = Infix_To_Prefix(cond)
#     if_stat = 