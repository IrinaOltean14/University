package model.value;

import model.type.IntType;
import model.type.Type;

public class IntValue implements Value{
    private int val;

    public IntValue(int v){
        this.val = v;
    }
    public IntValue(){
        this.val = 0;
    }

    public int getVal(){
        return this.val;
    }

    @Override
    public String toString(){
        return Integer.toString(this.val);
    }
    @Override
    public Type getType() {
        return new IntType();
    }

    @Override
    public Value deepCopy() {
        return new IntValue(val);
    }

    @Override
    public boolean equals(Object another) {
        return (another instanceof IntValue && ((IntValue)another).getVal() == this.val);
    }
}
