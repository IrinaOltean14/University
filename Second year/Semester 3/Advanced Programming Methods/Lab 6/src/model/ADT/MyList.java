package model.ADT;

import model.exception.ADTException;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
public class MyList<T> implements IMyList<T> {

    private List<T> list;
    public MyList(){
        this.list = new ArrayList<T>();
    }

    @Override
    public void add(T item) {
        this.list.add(item);
    }

    @Override
    public void remove(T item) throws ADTException {
        try{
            this.list.remove(item);
        }
        catch (NoSuchElementException e){
            throw new ADTException("No such element");
        }
    }

    @Override
    public String toString() {
        String representation = "";
        for(T elem: list){
            representation += (elem.toString() + "\n");
        }

        return representation;
    }
}
