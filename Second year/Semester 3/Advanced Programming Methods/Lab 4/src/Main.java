import controller.Controller;
import model.ADT.*;
import model.exception.ADTException;
import model.exception.MyException;
import model.expression.ArithExp;
import model.expression.RelationalExp;
import model.expression.ValueExp;
import model.expression.VarExp;
import model.statement.*;
import model.test.FileTest;
import model.type.BoolType;
import model.type.IntType;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;
import repository.*;
import model.*;
import view.ExitCommand;
import view.RunExample;
import view.TextMenu;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.List;
import java.util.Map;


public class Main {
    public static void main(String[] args) {
        FileTest test = new FileTest();
        test.testExecute();

        IMyStack<IStmt> stack1 = new MyStack<>();

        IStmt example_1 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ValueExp(new IntValue(17))),
                        new PrintStmt(new VarExp("x"))
                )
        );
        stack1.push(example_1);
        PrgState prg1 = new PrgState(stack1, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>());
        IRepository repo1 = new Repository(prg1, "log1.txt");
        Controller ctr1 = new Controller(repo1);

        IMyStack<IStmt> stack2 = new MyStack<>();
        IStmt example2 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ArithExp('+', new ValueExp(new IntValue(5)), new ValueExp(new IntValue(7)))),
                        new PrintStmt(new VarExp("x"))
                )
        );
        stack2.push(example2);
        PrgState prg2 = new PrgState(stack2, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>());
        IRepository repo2 = new Repository(prg2, "log2.txt");
        Controller ctr2 = new Controller(repo2);

        IMyStack<IStmt> stack3 = new MyStack<>();
        IStmt example_3 = new CompStmt(
                new VarDeclStmt("a", new IntType()),
                new CompStmt(
                        new VarDeclStmt("b", new IntType()),
                        new CompStmt(
                                new AssignStmt("a", new ValueExp(new IntValue(10))),
                                new CompStmt(
                                        new AssignStmt("b", new ValueExp(new IntValue(9))),
                                        new IfStmt(new RelationalExp(1,new VarExp("a"), new VarExp("b")), new PrintStmt(new ValueExp(new StringValue("a is smaller"))), new PrintStmt(new ValueExp(new StringValue("b is smaller"))))
                                )
                        )
                )
        );
        stack3.push(example_3);
        PrgState prg3 = new PrgState(stack3,new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>());
        IRepository repo3 = new Repository(prg3, "log3.txt");
        Controller ctr3 = new Controller(repo3);

        IMyStack<IStmt> stack4 = new MyStack<>();
        IStmt example_4 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ValueExp(new BoolValue(false))),
                        new PrintStmt(new VarExp("x"))
                )
        );
        stack4.push(example_4);
        PrgState prg4 = new PrgState(stack4,new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>());
        IRepository repo4 = new Repository(prg4, "log4.txt");
        Controller ctr4 = new Controller(repo4);


        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "Exit"));
        menu.addCommand(new RunExample("1", example_1.toString(), ctr1));
        menu.addCommand(new RunExample("2", example2.toString(), ctr2));
        menu.addCommand(new RunExample("3", example_3.toString(), ctr3));
        menu.addCommand(new RunExample("4", example_4.toString(), ctr4));
        menu.show();;
    }
}

