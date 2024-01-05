package model.expression;

import model.ADT.IMyDictionary;
import model.ADT.IMyHeap;
import model.exception.ExprException;
import model.type.RefType;
import model.value.RefValue;
import model.value.Value;

public class HeapReadingExp implements Exp{
    Exp expression;

    public HeapReadingExp(Exp e){
        this.expression = e;
    }

    @Override
    public Value eval(IMyDictionary<String, Value> table, IMyHeap heap) throws ExprException {
        Value expValue = expression.eval(table, heap);
        if (!(expValue.getType() instanceof RefType)){
            throw new ExprException("Expression not evaluated to RefType");
        }
        RefValue val = (RefValue) expValue;
        int address = val.getAddr();
        if (!heap.containsKey(address)){
            throw new ExprException("The address is not a key in the heap");
        }
        return heap.lookup(address);
    }

    @Override
    public Exp deepCopy() {
        return null;
    }

    @Override
    public String toString(){
        return "rH(" + expression + ")";
    }
}
