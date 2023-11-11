package model.statement;

import model.ADT.IMyDictionary;
import model.ADT.IMyStack;
import model.PrgState;
import model.exception.ExprException;
import model.exception.MyException;
import model.exception.StmtException;
import model.expression.Exp;
import model.type.BoolType;
import model.value.BoolValue;
import model.value.Value;

public class IfStmt implements IStmt {
    Exp exp;
    IStmt thenS;
    IStmt elseS;

    public IfStmt(Exp e, IStmt s1, IStmt s2) {
        this.exp = e;
        this.thenS = s1;
        this.elseS = s2;
    }

    @Override
    public String toString() {
        return "(IF(" + exp.toString() + ")THEN(" + thenS.toString()
                + ")ELSE(" + elseS.toString() + "))";
    }

    @Override
    public PrgState execute(PrgState state) throws StmtException, ExprException {
        IMyStack<IStmt> stack = state.getStack();
        IMyDictionary<String, Value> table = state.getDictionary();
        Value c = this.exp.eval(table);
        if (!c.getType().equals(new BoolType())) {
            throw new StmtException("Condition is not of boolean");
        }
        BoolValue cond = (BoolValue) c;
        boolean ok = cond.getVal();
        if (ok) {
            stack.push(thenS);
        }
        else {
            stack.push(elseS);
        }
        state.setExecutionStack(stack);
        return state;
    }

    @Override
    public IStmt deepCopy() {
        return new IfStmt(exp.deepCopy(), thenS.deepCopy(), elseS.deepCopy());
    }
}