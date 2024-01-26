package model.exception;

public class IException extends Exception{
    public IException(String message){
        super(message);
    }

    @Override
    public String getMessage(){
        return super.getMessage();
    }
}
