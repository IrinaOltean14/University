package model.statement;

import model.ADT.IMyDictionary;
import model.ADT.IMyHeap;
import model.ADT.IMyStack;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.expression.Exp;
import model.type.BoolType;
import model.type.Type;
import model.value.BoolValue;
import model.value.Value;

public class WhileStmt implements IStmt{
    private IStmt stmt;
    private Exp exp;

    public WhileStmt(IStmt s, Exp e){
        stmt = s;
        exp = e;
    }

    @Override
    public PrgState execute(PrgState state) throws ADTException, ExprException, StmtException {
        IMyHeap heap = state.getHeap();
        IMyStack<IStmt> stack = state.getStack();
        IMyDictionary<String, Value> symTable = state.getDictionary();

        Value expValue = exp.eval(symTable, heap);
        if (!((expValue.getType()) instanceof BoolType)){
            throw new StmtException("Expression does not evaluate to bool");
        }
        BoolValue boolValue = (BoolValue) expValue;
        if (boolValue.getVal()){
            stack.push(this);
            stack.push(stmt);
        }
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new WhileStmt(stmt.deepCopy(), exp.deepCopy());
    }

    @Override
    public IMyDictionary<String, Type> typecheck(IMyDictionary<String, Type> typeEnv) throws StmtException, ExprException, ADTException {
        Type typ = exp.typecheck(typeEnv);
        if (typ.equals(new BoolType())){
            /// In this case we also use a copy of the typeEnv because we can have the case
            /// while(...)
            ///{ int a; }
            /// bool a;
            /// And here for example, if the condition of while is not true, we would still declare "a" as an int in the typeEnv through the typeChecking even though we shouldn't
            /// And when we will try to declare "a" as a BOOL it will crash, reason why we use a copy of the typeEnv when we check the whileBody with the typeChecker
            stmt.typecheck(typeEnv.deepCopy());
            return typeEnv;
        }
        else
            throw new StmtException("WhileStatement: the expression does not evaluate to bool");
    }

    @Override
    public String toString(){
        return "while("+exp.toString()+")"+stmt.toString();
    }
}
