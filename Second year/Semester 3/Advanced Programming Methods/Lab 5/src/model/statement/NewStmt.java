package model.statement;

import model.ADT.IMyDictionary;
import model.ADT.IMyHeap;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.expression.Exp;
import model.type.RefType;
import model.type.Type;
import model.value.RefValue;
import model.value.Value;


public class NewStmt implements IStmt{
    private String varName;
    private Exp expression;

    public NewStmt(String name, Exp e){
        varName = name;
        expression = e;
    }
    @Override
    public PrgState execute(PrgState state) throws ADTException, ExprException, StmtException {
        IMyDictionary<String, Value> symTable = state.getDictionary();
        IMyHeap heap = state.getHeap();
        // check if the name is a valid name in the symtable
        if (!symTable.isDefined(varName)){
            throw new StmtException("Variable is not defined!");
        }
        // check if it is of RefType
        Value val = symTable.lookup(varName);
        if (!(val.getType() instanceof RefType)){
            throw new StmtException("The type of the variable is not RefType");
        }

        // Evaluate the expression to a value
        Value expValue = expression.eval(symTable, heap);
        Type locationType =((RefType) val.getType()).getInner();

        if (!(expValue.getType().equals(locationType))) {
            throw new StmtException("Reference location type does not match expression type!");
        }
        int heapAddr = heap.getFreeAddress();
        heap.put(heapAddr, expValue);
        RefValue refV = (RefValue) val;
        RefValue newRef = new RefValue(heapAddr, ((RefType) refV.getType()).getInner());
        symTable.update(varName, newRef);
        return state;

    }

    @Override
    public IStmt deepCopy() {
        return new NewStmt(varName, expression.deepCopy());
    }

    @Override
    public String toString(){
        return "new(" + varName + "," + expression.toString() + ")";
    }
}
