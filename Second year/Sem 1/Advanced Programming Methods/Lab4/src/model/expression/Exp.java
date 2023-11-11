package model.expression;

import model.ADT.IMyDictionary;
import model.exception.ExprException;
import model.exception.MyException;
import model.value.Value;

public interface Exp {
    Value eval(IMyDictionary<String, Value> table) throws ExprException;

    Exp deepCopy();
}
