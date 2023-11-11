package model.statement;

import model.ADT.IFileTable;
import model.ADT.IMyDictionary;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.expression.Exp;
import model.type.IntType;
import model.type.StringType;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class readRFileStmt implements IStmt{
    Exp exp;
    private String varName;

    public readRFileStmt(Exp exp, String varName){
        this.exp = exp;
        this.varName = varName;
    }

    @Override
    public PrgState execute(PrgState state) throws ADTException, ExprException, StmtException {
        IMyDictionary<String, Value> symTable = state.getDictionary();
        IFileTable<StringValue, BufferedReader> fileTable = state.getFileTable();

        if (symTable.isDefined(varName)){
            if (symTable.lookup(varName).getType().equals(new IntType())){
                Value val = exp.eval(symTable);
                if (val.getType().equals(new StringType())){
                    StringValue stringVal = (StringValue) val;
                    if (fileTable.isDefined(stringVal)){
                        BufferedReader bufferedReader = fileTable.lookup(stringVal);
                        try{
                            String line = bufferedReader.readLine();
                            Value intVal;
                            IntType type = new IntType();
                            if (line == null){
                                intVal = type.defaultValue();
                            }
                            else{
                                intVal = new IntValue(Integer.parseInt(line));
                            }
                            symTable.update(varName, intVal);
                        }
                        catch (IOException e) {
                            throw new StmtException(e.getMessage());
                        }
                    }
                    else{
                        throw new StmtException("The file " + stringVal.getValue()+ " is not in the file table");
                    }
                }
                else {
                    throw new StmtException("The value could not be evaluated to a string value");
                }
            }
            else{
                throw new StmtException(varName + " is not of type int");
            }
        }
        else{
            throw new StmtException(varName + " is not defined in the Sym Table");
        }
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new readRFileStmt(exp.deepCopy(), new String(varName));
    }

    @Override
    public String toString(){
        return "Read from " + exp + " into " + varName;
    }
}
