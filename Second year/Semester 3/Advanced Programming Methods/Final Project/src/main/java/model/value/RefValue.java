package model.value;

import model.type.RefType;
import model.type.Type;

public class RefValue implements Value{
    private int address;
    private Type locationType;

    public RefValue(int address, Type t){
        this.address = address;
        this.locationType = t;
    }
    public int getAddr(){
        return this.address;
    }

    @Override
    public Type getType() {
        return new RefType(locationType);
    }

    @Override
    public Value deepCopy() {
        return new RefValue(this.address, locationType.deepCopy());
    }

    @Override
    public String toString(){
        return "(" + address + ", " + locationType + ")";
    }
}
