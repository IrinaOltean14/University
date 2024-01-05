package model.statement;

import model.ADT.IFileTable;
import model.ADT.IMyDictionary;
import model.ADT.IMyHeap;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.expression.Exp;
import model.type.StringType;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class closeRFileStmt implements IStmt{
    Exp exp;

    public closeRFileStmt(Exp exp){
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws ADTException, ExprException, StmtException {
        IMyDictionary<String, Value> symTable = state.getDictionary();
        IMyHeap heap = state.getHeap();
        Value val = exp.eval(symTable, heap);
        if (val.getType().equals(new StringType())){
            StringValue stringVal = (StringValue) val;
            IFileTable<StringValue, BufferedReader> fileTable = state.getFileTable();
            if (fileTable.isDefined(stringVal)){
                BufferedReader bufferedReader = fileTable.lookup(stringVal);
                try{
                    bufferedReader.close();
                }
                catch (IOException e){
                    throw new StmtException(e.getMessage());
                }
                fileTable.remove(stringVal);
            }
            else{
                throw new StmtException("The file is not in the file table");
            }
        }
        else{
            throw new StmtException("Expression could not be evaluated to a string");
        }
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new closeRFileStmt(exp.deepCopy());
    }

    @Override
    public String toString(){
        return "close(" + exp + ")";
    }
}
