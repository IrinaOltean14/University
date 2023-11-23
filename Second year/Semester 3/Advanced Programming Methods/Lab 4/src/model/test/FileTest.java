package model.test;

import controller.Controller;
import model.ADT.*;
import model.PrgState;
import model.exception.MyException;
import model.expression.ValueExp;
import model.expression.VarExp;
import model.statement.*;
import model.type.IntType;
import model.type.StringType;
import model.value.StringValue;
import model.value.Value;
import repository.IRepository;
import repository.Repository;

import java.io.BufferedReader;
import java.io.IOException;

public class FileTest {
    public void testExecute() {
        IMyStack<IStmt> exeStack = new MyStack<>();
        IMyDictionary<String, Value> symTable= new MyDictionary<String, Value>();
        IMyList<Value> out = new MyList<>();
        IFileTable<StringValue, BufferedReader> fileTable = new FileTable<StringValue, BufferedReader>();

        IStmt ex = new CompStmt(
                new VarDeclStmt("varf", new StringType()),
                new CompStmt(
                        new AssignStmt("varf", new ValueExp(new StringValue("test.in"))),
                        new CompStmt(
                                new openRFileStmt(new VarExp("varf")),
                                new CompStmt(
                                        new VarDeclStmt("varc", new IntType()),
                                        new CompStmt(
                                                new readRFileStmt(new VarExp("varf"), "varc"),
                                                new CompStmt(
                                                        new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(
                                                                new readRFileStmt(new VarExp("varf"), "varc"),
                                                                new CompStmt(
                                                                        new PrintStmt(new VarExp("varc")),
                                                                        new closeRFileStmt(new VarExp("varf"))
                                                                )
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );
        exeStack.push(ex);
        PrgState prgState = new PrgState(exeStack, symTable, out, fileTable);

        IRepository repository = new Repository("log-test.txt");
        Controller controller = new Controller(repository);
        repository.addState(prgState);
        try{
            controller.allStep();
        }
        catch (IOException | MyException e){
            System.out.println(e.getMessage());
        }
    }
}
