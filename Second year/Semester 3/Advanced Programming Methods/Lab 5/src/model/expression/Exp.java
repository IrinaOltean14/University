package model.expression;

import model.ADT.IMyDictionary;
import model.ADT.IMyHeap;
import model.exception.ExprException;
import model.value.Value;

public interface Exp {
    Value eval(IMyDictionary<String, Value> table, IMyHeap heap) throws ExprException;

    Exp deepCopy();
}
