package model.expression;

import model.ADT.IMyDictionary;
import model.exception.ExprException;
import model.exception.MyException;
import model.type.IntType;
import model.value.IntValue;
import model.value.Value;

public class ArithExp implements Exp{
    private Exp e1, e2;
    private int op; // 1 - plus, 2 - minus, 3 - star, 4 - divide
    public ArithExp(char op, Exp e1, Exp e2){
        this.e1 = e1;
        this.e2 = e2;
        if (op == '+')
            this.op = 1;
        else if (op == '-')
            this.op = 2;
        else if (op == '*')
            this.op = 3;
        else if (op == '/')
            this.op = 4;
    }
    @Override
    public Value eval(IMyDictionary<String, Value> table) throws ExprException {
        Value v1, v2;
        v1 = e1.eval(table);
        if (v1.getType().equals(new IntType())){
            v2 = e2.eval(table);
            if (v2.getType().equals(new IntType())){
                IntValue i1 = (IntValue) v1;
                IntValue i2 = (IntValue) v2;
                int n1, n2;
                n1 = i1.getVal();
                n2 = i2.getVal();
                if (op == 1)
                    return new IntValue(n1+n2);
                if (op == 2)
                    return new IntValue(n1-n2);
                if (op == 3)
                    return new IntValue(n1*n2);
                if (op == 4){
                    if (n2 == 0)
                        throw new ExprException("Division by zero");
                    return new IntValue(n1/n2);
                }

            }
            else{
                throw new ExprException("Second operand is not an integer");
            }
        }
        else{
            throw new ExprException("First operand is not an integer");
        }
        throw new ExprException("Incorrect operation");
    }

    @Override
    public Exp deepCopy() {
        return switch (this.op) {
            case 1 -> new ArithExp('+', e1.deepCopy(), e2.deepCopy());
            case 2 -> new ArithExp('-', e1.deepCopy(), e2.deepCopy());
            case 3 -> new ArithExp('*', e1.deepCopy(), e2.deepCopy());
            case 4 -> new ArithExp('/', e1.deepCopy(), e2.deepCopy());
            default -> new ArithExp('+', e1.deepCopy(), e2.deepCopy());
        };
    }

    @Override
    public String toString(){
        return switch (op) {
            case 1 -> e1.toString() + "+" + e2.toString();
            case 2 -> e1.toString() + "-" + e2.toString();
            case 3 -> e1.toString() + "*" + e2.toString();
            case 4 -> e1.toString() + "/" + e2.toString();
            default -> "";
        };
    }


}
