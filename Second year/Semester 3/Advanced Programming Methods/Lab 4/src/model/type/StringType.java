package model.type;

import model.value.StringValue;
import model.value.Value;

public class StringType implements Type{
    @Override
    public Type deepCopy() {
        return new StringType();
    }

    @Override
    public Value defaultValue() {
        return new StringValue("");
    }

    @Override
    public String toString(){
        return "string";
    }

    @Override
    public boolean equals(Object o){
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        return true;
    }
}
