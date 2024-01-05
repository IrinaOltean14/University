package model.expression;

import model.ADT.IMyDictionary;
import model.ADT.IMyHeap;
import model.ADT.MyDictionary;
import model.exception.ExprException;
import model.exception.MyException;
import model.type.Type;
import model.value.Value;

public interface Exp {
    Value eval(IMyDictionary<String, Value> table, IMyHeap heap) throws ExprException;

    Exp deepCopy();

    Type typecheck(IMyDictionary<String, Type> typeEnv) throws ExprException;
}
