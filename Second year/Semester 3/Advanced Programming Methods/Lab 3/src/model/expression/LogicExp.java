package model.expression;

import model.ADT.IMyDictionary;
import model.exception.ExprException;
import model.exception.MyException;
import model.type.BoolType;
import model.value.BoolValue;
import model.value.Value;

public class LogicExp implements Exp{
    Exp e1;
    Exp e2;
    int op; // 1 - and, 2 - or

    public LogicExp(Exp e1, Exp e2, int op){
        this.e1 = e1;
        this.e2 = e2;
        this.op = op;
    }
    @Override
    public Value eval(IMyDictionary<String, Value> table) throws ExprException {
        Value v1, v2;
        v1 = e1.eval(table);
        if (v1.getType().equals(new BoolType())){
            v2 = e2.eval(table);
            if (v2.getType().equals(new BoolType())){
                BoolValue i1 = (BoolValue) v1;
                BoolValue i2 = (BoolValue) v2;
                boolean n1, n2;
                n1 = i1.getVal();
                n2 = i2.getVal();
                if (op == 1)
                    return new BoolValue(n1 && n2);
                if (op == 2)
                    return new BoolValue(n1 || n2);
            }
            else{
                throw new ExprException("Second operand is not a boolean");
            }
        }
        else{
            throw new ExprException("First operand is not a boolean");
        }
        throw new ExprException("Incorrect operand");
    }

    @Override
    public Exp deepCopy() {
        return new LogicExp(e1.deepCopy(), e2.deepCopy(), op);
    }

    @Override
    public String toString(){
        return switch (op) {
            case 1 -> e1.toString() + "&&" + e2.toString();
            case 2 -> e1.toString() + "||" + e2.toString();
            default -> "";
        };
    }
}
