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
import java.io.FileNotFoundException;
import java.io.FileReader;

public class openRFileStmt implements IStmt {
    private Exp exp;

    public openRFileStmt(Exp exp){
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws ADTException, ExprException, StmtException {
        IMyDictionary<String, Value> symTable = state.getDictionary();
        IMyHeap heap = state.getHeap();
        Value val = exp.eval(symTable, heap);
        if (val.getType().equals(new StringType())){
            IFileTable<StringValue, BufferedReader> fileTable = state.getFileTable();
            StringValue stringVal = (StringValue) val;
            if (!fileTable.isDefined(stringVal)){
                try{
                    BufferedReader fileBuffer = new BufferedReader(new FileReader(stringVal.getValue()));
                    fileTable.add(stringVal, fileBuffer);
                }
                catch (FileNotFoundException e){
                    throw new StmtException(e.getMessage());
                }
            }
            else {
                throw new StmtException("The file is already in use");
            }
        }
        else{
            throw new StmtException("Expression can not be evaluated to a string");
        }
        return null;
    }

    @Override
    public String toString(){
        return "Open(" + exp + ")";
    }

    @Override
    public IStmt deepCopy() {
        return new openRFileStmt(exp.deepCopy());
    }
}
