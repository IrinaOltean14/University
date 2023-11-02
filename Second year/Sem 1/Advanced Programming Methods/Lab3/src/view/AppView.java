package view;
import controller.Controller;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.MyException;
import model.exception.StmtException;
import model.expression.ArithExp;
import model.expression.ValueExp;
import model.expression.VarExp;
import model.statement.*;
import model.type.BoolType;
import model.type.IntType;
import model.value.BoolValue;
import model.value.IntValue;
import repository.*;

import java.util.Scanner;

public class AppView {
    Controller controller;

    public AppView(){
        IRepository repository = new Repository();
        this.controller = new Controller(repository);
        printMenu();
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        //try {
         //   controller.example(number);
        //}
        //catch (MyException | StmtException | ADTException | ExprException e){
          //  System.out.println(e.getMessage());
        //}
        this.example(number);
    }

    public void printMenu(){
        System.out.println("Choose your option");
        System.out.println("Example 1: int v; v=2;Print(v) ");
        System.out.println("Example 2: int a;int b; a=2+3*5;b=a+1;Print(b) ");
        System.out.println("Example 3: bool a; int v; a=true;(If a Then v=2 Else v=3);Print(v) ");
        System.out.println("Enter: ");
    }
    
    public void example(int nb){
        IStmt example_1 = new CompStmt(
                new VarDeclStmt("v", new IntType()),
                new CompStmt(
                        new AssignStmt("v", new ValueExp(new IntValue(2))),
                        new PrintStmt(new VarExp("v"))
                )
        );

        // example 2
        IStmt example_2 = new CompStmt(
                new VarDeclStmt("a", new IntType()),
                new CompStmt(
                        new VarDeclStmt("b", new IntType()),
                        new CompStmt(
                                new AssignStmt("a", new ArithExp('+', new ValueExp(new IntValue(2)), new ArithExp('*', new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                                new CompStmt(
                                        new AssignStmt("b", new ArithExp('+', new VarExp("a"), new ValueExp(new IntValue(1)))),
                                        new PrintStmt(new VarExp("b"))
                                )

                        )
                )
        );

        // example 3
        IStmt example_3 = new CompStmt(
                new VarDeclStmt("a", new BoolType()),
                new CompStmt(
                        new VarDeclStmt("v", new IntType()),
                        new CompStmt(
                                new AssignStmt("a", new ValueExp(new BoolValue(true))),
                                new CompStmt(
                                        new IfStmt(new VarExp("a"), new AssignStmt("v", new ValueExp(new IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))),
                                        new PrintStmt(new VarExp("v"))

                                )
                        )
                )
        );
        IStmt e = null;
        if (nb ==1)
            e = example_1;
        else if (nb == 2)
            e = example_2;
        else if (nb == 3)
            e = example_3;
        try{
            controller.example(e);
        }
        catch (ExprException | MyException | StmtException | ADTException exc){
            System.out.println(exc.getMessage());
        }
    }


}
