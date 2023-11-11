package model.expression;

import model.ADT.IMyDictionary;
import model.exception.ExprException;
import model.exception.MyException;
import model.value.Value;

public class VarExp implements Exp{
    private String id;

    public VarExp(String id){
        this.id = id;
    }
    @Override
    public Value eval(IMyDictionary<String, Value> table) throws ExprException {
        return table.lookup(id);
    }

    @Override
    public Exp deepCopy() {
        return new VarExp(new String(id));
    }

    @Override
    public String toString() {
        return id;
    }
}
