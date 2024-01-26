package model.expression;

import model.ADT.IMyDictionary;
import model.ADT.IMyHeap;
import model.exception.ExprException;
import model.type.BoolType;
import model.type.IntType;
import model.type.Type;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.Value;

public class RelationalExp implements Exp{
    private Exp exp1;
    private Exp exp2;
    private int op; // 1 <, 2 <=, 3 ==, 4 !=, 5 >, 6 >=

    public RelationalExp(int op, Exp e1, Exp e2){
        this.exp1 = e1;
        this.exp2 = e2;
        this.op = op;
    }

    @Override
    public Value eval(IMyDictionary<String, Value> table, IMyHeap heap) throws ExprException {
        Value val1, val2;
        val1 = exp1.eval(table, heap);
        val2 = exp2.eval(table, heap);
        if (val1.getType().equals(new IntType()) && val2.getType().equals(new IntType())){
            int x = ((IntValue) val1).getVal();
            int y = ((IntValue) val2).getVal();
            switch (op) {
                case 1:
                    return new BoolValue(x < y);
                case 2:
                    return new BoolValue(x <= y);
                case 3:
                    return new BoolValue(x == y);
                case 4:
                    return new BoolValue(x != y);
                case 5:
                    return new BoolValue(x > y);
                case 6:
                    return new BoolValue(x >= y);
            }
        }
        else{
            throw new ExprException("At least one operand is not an integer");
        }
        return new BoolValue(false);
    }

    @Override
    public Exp deepCopy() {
        return new RelationalExp(op, exp1.deepCopy(), exp2.deepCopy());
    }

    @Override
    public Type typecheck(IMyDictionary<String, Type> typeEnv) throws ExprException {
        Type typ1, typ2;
        typ1 = exp1.typecheck(typeEnv);
        typ2 = exp2.typecheck(typeEnv);
        if (typ1.equals(new IntType())){
            if (typ2.equals(new IntType())){
                return new BoolType();
            }
            else
                throw new ExprException("Second operand is not an integer");
        }
        else throw new ExprException("First operand is not an integer");
    }

    @Override
    public String toString(){
        String s = switch (op) {
            case 1 -> "<";
            case 2 -> "<=";
            case 3 -> "==";
            case 4 -> "!=";
            case 5 -> ">";
            default -> ">=";
        };
        return exp1 + s + exp2;
    }
}
