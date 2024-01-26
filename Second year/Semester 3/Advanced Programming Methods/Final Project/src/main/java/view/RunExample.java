package view;
import controller.Controller;
import model.exception.MyException;

import java.io.IOException;

public class RunExample extends Command{
    private Controller ctr;

    public RunExample(String key, String desc, Controller ctr){
        super(key, desc);
        this.ctr = ctr;
    }

    public Controller getCrt(){
        return ctr;
    }

    @Override
    public void execute() {
        try{
            ctr.allStep();
        }
        catch (MyException | IOException e){
            System.out.println(e.toString());
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
