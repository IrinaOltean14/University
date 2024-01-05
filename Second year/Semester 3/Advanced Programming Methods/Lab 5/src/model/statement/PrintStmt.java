package model.statement;

import model.ADT.IMyHeap;
import model.ADT.IMyList;
import model.ADT.IMyStack;
import model.PrgState;
import model.exception.ExprException;
import model.exception.StmtException;
import model.expression.Exp;
import model.value.Value;

public class PrintStmt implements IStmt{
    Exp exp;

    public PrintStmt(Exp e){
        this.exp = e;
    }
    @Override
    public PrgState execute(PrgState state) throws StmtException, ExprException {
        IMyStack<IStmt> stack = state.getStack();
        IMyList<Value> out = state.getList();
        IMyHeap heap = state.getHeap();
        out.add(exp.eval(state.getDictionary(), heap));
        state.setExecutionStack(stack);
        state.setOut(out);
        return state;
    }

    @Override
    public IStmt deepCopy() {
        return new PrintStmt(exp.deepCopy());
    }

    @Override
    public String toString(){
        return "print(" + exp.toString() + ")";
    }
}
