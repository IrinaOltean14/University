package model.expression;

import model.ADT.IMyDictionary;
import model.exception.ExprException;
import model.exception.MyException;
import model.value.Value;

public class ValueExp implements Exp{

    private Value e;

    public ValueExp(Value e){
        this.e = e;
    }
    @Override
    public Value eval(IMyDictionary<String, Value> table) throws ExprException {
        return e;
    }

    @Override
    public Exp deepCopy() {
        return new ValueExp(e.deepCopy());
    }

    @Override
    public String toString(){
        return e.toString();
    }
}
