package model.value;

import model.type.BoolType;
import model.type.Type;

public class BoolValue implements Value{
    boolean val;

    public BoolValue(boolean v){
        this.val = v;
    }
    public BoolValue(){
        this.val = false;
    }
    public boolean getVal(){
        return this.val;
    }

    @Override
    public String toString(){
        return Boolean.toString(this.val);
    }
    @Override
    public Type getType() {
        return new BoolType();
    }

    @Override
    public Value deepCopy() {
        return new BoolValue(val);
    }

    @Override
    public boolean equals(Object another){
        return (another instanceof BoolValue && ((BoolValue)another).getVal() == this.val);
    }
}
