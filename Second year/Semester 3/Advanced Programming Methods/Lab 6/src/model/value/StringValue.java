package model.value;

import model.type.StringType;
import model.type.Type;

import java.util.Objects;

public class StringValue implements Value{
    String val;

    public StringValue(String val){
        this.val = val;
    }

    public StringValue(){
        this.val = "";
    }

    public String getValue(){
        return this.val;
    }


    @Override
    public Type getType() {
        return new StringType();
    }

    @Override
    public Value deepCopy() {
        return new StringValue(val);
    }

    @Override
    public boolean equals(Object another) {
        return (another instanceof StringValue && Objects.equals(((StringValue) another).getValue(), this.val));
    }

    @Override
    public String toString(){
        return val;
    }

}
